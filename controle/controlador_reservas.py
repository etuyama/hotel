from entidade.reserva import Reserva
from exceptions.cliente_menor_de_idade_exception import ClienteMenorDeIdadeException
from exceptions.quarto_indisponivel_exception import QuartoIndisponivelException
from exceptions.quarto_nao_encontrado_exception import QuartoNaoEncontradoException
from exceptions.reserva_finalizada_exception import ReservaFinalizadaException
from limite.tela_reserva import TelaReserva
from datetime import date


class ControladorReservas:

    def __init__(self,
                 controlador_sistema,
                 controlador_clientes,
                 controlador_quartos,
                 controlador_servicos):

        self.__reservas = []
        self.__tela_reserva = TelaReserva()
        self.__controlador_sistema = controlador_sistema
        self.__controlador_clientes = controlador_clientes
        self.__controlador_quartos = controlador_quartos
        self.__controlador_servicos = controlador_servicos
        self.__id = 1

    @property
    def reservas(self):
        return self.__reservas

    def pega_reserva_por_id(self, id: int):
        if isinstance(id, int):

            for reserva in self.__reservas:

                if reserva.id == id:
                    return reserva
            return None

    #Só efetua a reserva se o quarto estiver disponível
    def efetuar_reserva(self):
        self.__tela_reserva.mostra_mensagem("-------- CLIENTES --------\n")
        lista = self.__controlador_clientes.lista_clientes()
        if not lista:
            return False

        cpf_cliente = self.__tela_reserva.seleciona_cliente()
        cliente = self.__controlador_clientes.pega_cliente_por_cpf(cpf_cliente)

        if not cliente:
            self.__tela_reserva.mostra_mensagem("Cliente não encontrado")
            return False

        try:
            if not cliente.validar_maioridade():
                raise ClienteMenorDeIdadeException(cliente.calcular_idade())

            self.__controlador_quartos.lista_quartos()
            numero_quarto = self.__tela_reserva.seleciona_quarto()
            quarto = self.__controlador_quartos.pega_quarto_por_numero(numero_quarto)

            if not quarto:
                raise QuartoNaoEncontradoException(numero_quarto)

            if quarto.status != "Disponível":
                raise QuartoIndisponivelException

            tempo_estadia = self.__tela_reserva.pega_tempo_estadia()

            reserva = Reserva(quarto, tempo_estadia, cliente, self.__id)
            reserva.data_reserva = date.today().strftime("%d/%m/%Y")
            self.__reservas.append(reserva)

            self.__tela_reserva.mostra_mensagem("Reserva efetuada com sucesso")
            quarto.status = "Ocupado"

            self.__id = self.__id + 1

        except ClienteMenorDeIdadeException as e:
            self.__tela_reserva.mostra_mensagem(e)
        except QuartoNaoEncontradoException as x:
            self.__tela_reserva.mostra_mensagem(x)
        except QuartoIndisponivelException as c:
            self.__tela_reserva.mostra_mensagem(c)

    def alterar_reserva(self):
        lista = self.lista_reservas()
        if not lista:
            return False

        id_reserva = self.__tela_reserva.seleciona_reserva()
        reserva = self.pega_reserva_por_id(id_reserva)

        if reserva:

            #Mesmo que sejam mostradas somente as reservas pendentes, ainda é possível selecionar o
            # id de uma reserva finalizada, por isso é necessário o try
            try:
                self.verifica_situacao_reserva(reserva)

                self.__tela_reserva.mostra_mensagem("**ALTERANDO DADOS DA RESERVA**")

                self.__controlador_clientes.lista_clientes()
                cpf_cliente = self.__tela_reserva.seleciona_cliente()
                cliente = self.__controlador_clientes.pega_cliente_por_cpf(cpf_cliente)

                if not cliente:
                    self.__tela_reserva.mostra_mensagem("Cliente não encontrado")
                    return False

                try:
                    reserva.cliente = cliente

                    self.__controlador_quartos.lista_quartos()
                    numero_quarto = self.__tela_reserva.seleciona_quarto()
                    quarto = self.__controlador_quartos.pega_quarto_por_numero(numero_quarto)

                    if not quarto:
                        raise QuartoNaoEncontradoException(numero_quarto)
                    if reserva.quarto != quarto and quarto.status != "Disponível":
                        raise QuartoIndisponivelException

                    reserva.quarto = quarto
                    self.__tela_reserva.mostra_mensagem("Dados alterados com sucesso")

                except QuartoNaoEncontradoException as e:
                    self.__tela_reserva.mostra_mensagem(e)
                except QuartoIndisponivelException as x:
                    self.__tela_reserva.mostra_mensagem(e)

            except ReservaFinalizadaException as e:
                self.__tela_reserva.mostra_mensagem(e)

        else:
            self.__tela_reserva.mostra_mensagem("Reserva não encontrada")

    #Lista as reservas pendentes
    def lista_reservas(self):

        if len(self.__reservas) > 0:

                cont_reservas_finalizadas = 0
                for reserva in self.__reservas:

                        try:
                            self.verifica_situacao_reserva(reserva)

                            self.__tela_reserva.mostra_reserva({"id": reserva.id,
                                                                "data_reserva": reserva.data_reserva,
                                                                "situacao": reserva.situacao,
                                                                "nome_cliente": reserva.cliente.nome,
                                                                "cpf_cliente": reserva.cliente.cpf,
                                                                "numero_quarto": reserva.quarto.numero,
                                                                "tipo_quarto": reserva.quarto.tipo,
                                                                "valor_diaria": reserva.quarto.valor_diaria,
                                                                "tempo_estadia": reserva.tempo_estadia,
                                                                "servicos_utilizados": self.lista_servicos(reserva),
                                                                "valor_total": reserva.valor_total})

                        except ReservaFinalizadaException:
                            cont_reservas_finalizadas = cont_reservas_finalizadas + 1

                if cont_reservas_finalizadas == len(self.__reservas):
                    self.__tela_reserva.mostra_mensagem("Não há reservas pendentes")
                    return None

                return True

        self.__tela_reserva.mostra_mensagem("Ainda não há reservas registradas")
        return None

    def lista_todas_reservas(self):

        if len(self.__reservas) > 0:
            for reserva in self.__reservas:

                self.__tela_reserva.mostra_reserva({
                    "id": reserva.id,
                    "data_reserva": reserva.data_reserva,
                    "situacao": reserva.situacao,
                    "nome_cliente": reserva.cliente.nome,
                    "cpf_cliente": reserva.cliente.cpf,
                    "numero_quarto": reserva.quarto.numero,
                    "tipo_quarto": reserva.quarto.tipo,
                    "valor_diaria": reserva.quarto.valor_diaria,
                    "tempo_estadia": reserva.tempo_estadia,
                    "servicos_utilizados": self.lista_servicos(reserva),
                    "valor_total": reserva.valor_total}
                )
            return True

        self.__tela_reserva.mostra_mensagem("Ainda não há reservas registradas")
        return None

    def excluir_reserva(self):
        lista = self.lista_reservas()
        if not lista:
            return False

        id_reserva = self.__tela_reserva.seleciona_reserva()
        reserva = self.pega_reserva_por_id(id_reserva)

        if reserva:

            try:
                self.verifica_situacao_reserva(reserva)
                self.__reservas.remove(reserva)
                reserva.quarto.status = "Disponível"
                self.__tela_reserva.mostra_mensagem("Reserva removida com sucesso")

            except ReservaFinalizadaException as e:
                self.__tela_reserva.mostra_mensagem(e)

        else:
            self.__tela_reserva.mostra_mensagem("Reserva não encontrada")

    def adiciona_servico(self):
        lista = self.lista_reservas()
        if not lista:
            return False

        id_reserva = self.__tela_reserva.seleciona_reserva()
        reserva = self.pega_reserva_por_id(id_reserva)
        if not isinstance(reserva, Reserva):
            self.__tela_reserva.mostra_mensagem("Reserva não encontrada")
            return False

        try:
            self.verifica_situacao_reserva(reserva)
            self.__controlador_servicos.lista_servicos()
            id_servico = self.__tela_reserva.seleciona_servico()
            servico = self.__controlador_servicos.pega_servico_por_id(id_servico)

            if servico:
                reserva.adiciona_servico(servico)
                self.__tela_reserva.mostra_mensagem(f"Serviço {servico.id}: {servico.nome} adicionado com sucesso")
            else:
                self.__tela_reserva.mostra_mensagem(f"Serviço não encontrado")

        except ReservaFinalizadaException as e:
            self.__tela_reserva.mostra_mensagem(e)


    def lista_servicos(self, reserva: Reserva):
        #CONVERTE LISTA DE SERVIÇOS EM LISTA DE STRINGS CONTENDO O NOME DO SERVIÇO E O PREÇO
        servicos = reserva.servicos_utilizados
        if len(servicos) == 0:
            return "Nenhum serviço utilizado"

        string_servicos = ""
        for servico in servicos:
            string = f"{servico.nome} R${servico.preco},00 | "
            string_servicos = string_servicos + string

        return string_servicos

    def extender_estadia(self):
        lista = self.lista_reservas()
        if not lista:
            return False

        id_reserva = self.__tela_reserva.seleciona_reserva()
        reserva = self.pega_reserva_por_id(id_reserva)

        if reserva:

            try:
                self.verifica_situacao_reserva(reserva)
                qt_dias = self.__tela_reserva.pega_dias_extensao()
                reserva.extender_estadia(qt_dias)
                self.__tela_reserva.mostra_mensagem(f"Foram adicionados {qt_dias} dias na reserva de ID: {reserva.id}")

            except ReservaFinalizadaException as e:
                self.__tela_reserva.mostra_mensagem(e)

        else:
            self.__tela_reserva.mostra_mensagem("Reserva não encontrada")

    def adiciona_valor_extra(self):
        lista = self.lista_reservas()
        if not lista:
            return False

        id_reserva = self.__tela_reserva.seleciona_reserva()
        reserva = self.pega_reserva_por_id(id_reserva)

        if reserva:

            try:
                self.verifica_situacao_reserva(reserva)
                valor_extra = self.__tela_reserva.pega_valor_extra()
                reserva.adiciona_valor_extra(valor_extra)
                self.__tela_reserva.mostra_mensagem(f"R${valor_extra},00 adicionado à reserva de ID: {reserva.id}")

            except ReservaFinalizadaException as e:
                self.__tela_reserva.mostra_mensagem(e)

        else:
            self.__tela_reserva.mostra_mensagem("Reserva não encontrada")

    def verifica_situacao_reserva(self, reserva):

        if reserva.situacao == "Finalizada":
            raise ReservaFinalizadaException(reserva)

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.efetuar_reserva, 2: self.alterar_reserva,
                        3: self.lista_reservas, 4: self.excluir_reserva,
                        5: self.adiciona_servico, 6: self.extender_estadia,
                        7: self.adiciona_valor_extra, 8: self.lista_todas_reservas,
                        0: self.retornar}
        while True:
            opcao_escolhida = self.__tela_reserva.tela_opcoes()
            self.__tela_reserva.mostra_mensagem(f"Opção escolhida: {opcao_escolhida}")
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
