from limite.tela_hotel import TelaHotel
from entidade.hotel import Hotel
from exceptions.reserva_finalizada_exception import ReservaFinalizadaException
from exceptions.quarto_nao_encontrado_exception import QuartoNaoEncontradoException


class ControladorHotel:

    def __init__(self, controlador_sistema, controlador_reservas, controlador_funcionarios, controlador_quartos):
        self.__tela_hotel = TelaHotel()
        self.__controlador_sistema = controlador_sistema
        self.__controlador_reservas = controlador_reservas
        self.__controlador_funcionarios = controlador_funcionarios
        self.__controlador_quartos = controlador_quartos
        self.__avaliacoes = []
        self.__transacoes = []
        self.__hotel = Hotel()

    def avaliar_hotel(self):
        avaliacao = self.__tela_hotel.pega_avaliacao_hotel()

        if avaliacao != "N/A":

            self.__avaliacoes.append(avaliacao)
            media = sum(self.__avaliacoes) / len(self.__avaliacoes)
            media_avaliacao = round(media, 1)

            self.__hotel.avaliacao_hotel = media_avaliacao

    def mostra_avaliacao_hotel(self):

        if len(self.__avaliacoes) > 0:

            avaliacao = self.__hotel.avaliacao_hotel
            self.__tela_hotel.mostra_mensagem(f"Avaliação Média do Hotel: {avaliacao}")
            self.__tela_hotel.mostra_mensagem(f"Avaliações do hotel: {self.__avaliacoes}")

        else:
            self.__tela_hotel.mostra_mensagem("O hotel ainda não foi avaliado")

    def mostra_saldo(self):
        saldo = self.__hotel.saldo
        self.__tela_hotel.mostra_mensagem(f"Saldo do Hotel: R${saldo},00")

        transacoes = self.lista_transacoes()
        self.__tela_hotel.mostra_mensagem(f"Relatório de Transações: {transacoes}")

    def realizar_checkout(self):
        lista = self.__controlador_reservas.lista_reservas()
        if not lista:
            return False

        id_reserva = self.__tela_hotel.seleciona_reserva()
        reserva = self.__controlador_reservas.pega_reserva_por_id(id_reserva)

        if reserva:

            try:            
                self.__controlador_reservas.verifica_situacao_reserva(reserva)
                reserva.situacao = "Finalizada"

                valor_reserva = reserva.valor_total
                self.__hotel.incrementar_saldo(valor_reserva)

                self.__transacoes.append(f" Reserva(+R${reserva.valor_total},00) ")

                reserva.quarto.status = "Manutenção"

                self.avaliar_hotel()

                self.__tela_hotel.mostra_mensagem(
                    f"Check-out da reserva do cliente:"
                    f" {reserva.cliente.nome}(CPF:{reserva.cliente.cpf})"
                    f" no quarto {reserva.quarto.numero} realizado com sucesso"
                    )

                self.__tela_hotel.mostra_mensagem(
                    f"Valor total da reserva: R${reserva.valor_total},00"
                    f" incrementados ao saldo do hotel"
                    )

            except ReservaFinalizadaException as e:
                self.__tela_hotel.mostra_mensagem(e)

        else:
            self.__tela_hotel.mostra_mensagem("Reserva não encontrada")

    def finalizar_manutencao(self):
        lista = self.__controlador_quartos.lista_quartos()
        if not lista:
            return False

        numero_quarto = self.__tela_hotel.seleciona_quarto()
        quarto = self.__controlador_quartos.pega_quarto_por_numero(numero_quarto)

        try:
            if not quarto:
                raise QuartoNaoEncontradoException(numero_quarto)

            if quarto.status != "Manutenção":
                self.__tela_hotel.mostra_mensagem(
                    f"O quarto número {quarto.numero} não"
                    f" está em Manutenção"
                    )
                return False

            quarto.status = "Disponível"
            self.__tela_hotel.mostra_mensagem(
                f"Manutenção do quarto número {quarto.numero}"
                f" foi finalizada, o quarto agora está Disponível"
                )

        except QuartoNaoEncontradoException as e:
            self.__tela_hotel.mostra_mensagem(e)

    def pagar_funcionario(self):
        lista = self.__controlador_funcionarios.lista_funcionarios()
        if not lista:
            return False

        cpf_funcionario = self.__tela_hotel.seleciona_funcionario()
        funcionario = self.__controlador_funcionarios.pega_funcionario_por_cpf(cpf_funcionario)

        if funcionario:
            self.__hotel.decrementar_saldo(funcionario.salario)

            self.__transacoes.append(f" Funcionário(-R${funcionario.salario},00) ")

            self.__tela_hotel.mostra_mensagem(
                f"Salário do funcionário {funcionario.nome}(CPF: {funcionario.cpf})"
                f" pago. Valor do salário: R${funcionario.salario},00"
                )

            if self.__hotel.saldo < 0:
                self.__tela_hotel.mostra_mensagem("***ATENÇÃO: Saldo do Hotel está NEGATIVO")
                self.mostra_saldo()

        else:
            self.__tela_hotel.mostra_mensagem("Funcionário não encontrado")

    def pagar_despesa(self):
        dados_despesa = self.__tela_hotel.pega_dados_despesa()
        valor = dados_despesa["valor"]
        descricao = dados_despesa["descricao"]

        self.__hotel.decrementar_saldo(valor)

        self.__transacoes.append(f" Despesa(-R${valor},00): {descricao} ")

        if self.__hotel.saldo < 0:
            self.__tela_hotel.mostra_mensagem("***ATENÇÃO: Saldo do Hotel está NEGATIVO")
            self.mostra_saldo()

    def lista_transacoes(self):
        transacoes = self.__transacoes
        if len(transacoes) == 0:
            return "Nenhuma transação realizada"

        string_transacoes = ""
        for transacao in transacoes:
            string = f"{transacao} | "
            string_transacoes = string_transacoes + string

        return string_transacoes

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.realizar_checkout,
                        2: self.finalizar_manutencao,
                        3: self.pagar_funcionario,
                        4: self.pagar_despesa,
                        5: self.mostra_avaliacao_hotel,
                        6: self.mostra_saldo,
                        0: self.retornar}

        while True:
            opcao_escolhida = self.__tela_hotel.tela_opcoes()
            self.__tela_hotel.mostra_mensagem(f"Opção escolhida: {opcao_escolhida}")
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()