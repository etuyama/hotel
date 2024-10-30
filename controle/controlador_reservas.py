from entidade.reserva import Reserva
from limite.tela_reserva import TelaReserva
from controle.controlador_clientes import ControladorClientes
from controle.controlador_quartos import ControladorQuartos
from controle.controlador_servicos import ControladorServicos
from entidade.cliente import Cliente
from entidade.quarto_luxo import QuartoLuxo
from entidade.quarto_standard import QuartoStandard
from entidade.quarto_suite import QuartoSuite
from entidade.quarto import Quarto
from entidade.reserva import Reserva


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
        self.__servicos_utilizados = [] #FALTA IMPLEMENTAR OS SERVIÇOS UTILIZADOS E INCREMENTAR SEUS PREÇOS NO VALOR TOTAL
        self.__id = 1

    def pega_reserva_por_id(self, id: int):
        if isinstance(id, int):

            for reserva in self.__reservas:

                if reserva.id == id:
                    return reserva
            return None

    #Só efetua caso o quarto esteja disponível
    def efetuar_reserva(self):
        self.__tela_reserva.mostra_mensagem("-------- DADOS CLIENTE --------\n")
        self.__controlador_clientes.lista_clientes()
        cpf_cliente = self.__tela_reserva.seleciona_cliente()
        cliente = self.__controlador_clientes.pega_cliente_por_cpf(cpf_cliente)

        if not isinstance(cliente, Cliente):
            self.__tela_reserva.mostra_mensagem("Cliente não encontrado")
            return False

        self.__controlador_quartos.lista_quartos()
        numero_quarto = self.__tela_reserva.seleciona_quarto()
        quarto = self.__controlador_quartos.pega_quarto_por_numero(numero_quarto)

        if not isinstance(quarto, Quarto):
            self.__tela_reserva.mostra_mensagem("Quarto não encontrado")
            return False

        if quarto.status != "Disponível":
            self.__tela_reserva.mostra_mensagem("Quarto não está disponível")
            return False

        tempo_estadia = self.__tela_reserva.pega_tempo_estadia()

        reserva = Reserva(quarto, tempo_estadia, cliente, self.__id)
        self.__reservas.append(reserva)

        quarto.status = "Ocupado"

        self.__id = self.__id + 1

    def alterar_reserva(self):
        lista = self.lista_reservas()
        if not lista:
            return False

        id_reserva = self.__tela_reserva.seleciona_reserva()
        reserva = self.pega_reserva_por_id(id_reserva)

        if isinstance(reserva, Reserva):
            self.__tela_reserva.mostra_mensagem("**ALTERANDO DADOS DA RESERVA**")

            self.__controlador_clientes.lista_clientes()
            cpf_cliente = self.__tela_reserva.seleciona_cliente()
            cliente = self.__controlador_clientes.pega_cliente_por_cpf(cpf_cliente)

            if not isinstance(cliente, Cliente):
                self.__tela_reserva.mostra_mensagem("Cliente não encontrado")
                return False

            reserva.cliente = cliente

            tempo_estadia = self.__tela_reserva.pega_tempo_estadia()
            reserva.tempo_estadia = tempo_estadia

            self.__controlador_quartos.lista_quartos()
            numero_quarto = self.__tela_reserva.seleciona_quarto()
            quarto = self.__controlador_quartos.pega_quarto_por_numero(numero_quarto)

            if not isinstance(quarto, Quarto):
                self.__tela_reserva.mostra_mensagem("Quarto não encontrado")
                return False

            reserva.quarto = quarto
            self.__tela_reserva.mostra_mensagem("Dados alterados com sucesso")

        else:
            self.__tela_reserva.mostra_mensagem("Reserva não encontrada")

    def lista_reservas(self):

        if len(self.__reservas) > 0:
            for reserva in self.__reservas:
                self.__tela_reserva.mostra_reserva({"id": reserva.id,
                                                    "nome_cliente": reserva.cliente.nome,
                                                    "cpf_cliente": reserva.cliente.cpf,
                                                    "numero_quarto": reserva.quarto.numero,
                                                    "tipo_quarto": reserva.quarto.tipo,
                                                    "valor_diaria": reserva.quarto.valor_diaria,
                                                    "tempo_estadia": reserva.tempo_estadia,
                                                    "servicos_utilizado": self.lista_servicos(),
                                                    "valor_total": reserva.valor_total})
            return True

        self.__tela_reserva.mostra_mensagem("Lista de reservas vazia")
        return None

    def excluir_reserva(self):
        lista = self.lista_reservas()
        if not lista:
            return False

        id_reserva = self.__tela_reserva.seleciona_reserva()
        reserva = self.pega_reserva_por_id(id_reserva)

        if isinstance(reserva, Reserva):
            self.__reservas.remove(reserva)
            self.__tela_reserva.mostra_mensagem("Reserva removida com sucesso")
        else:
            self.__tela_reserva.mostra_mensagem("Reserva não encontrada")

    def adiciona_servico(self):
        #TAMBÉM MOSTRAR OS SERVICOS UTILIZADOS NA FUNÇÃO MOSTRA_RESERVA
        # self.__controlador_servicos.pega_servico_por_nome?
        # self.__tela_reserva.seleciona_servico
        pass

    def lista_servicos(self):
        #CONVERTE LISTA DE SERVIÇOS EM LISTA DE STRINGS CONTENDO O NOME DO SERVIÇO E O PREÇO
        pass

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.efetuar_reserva, 2: self.alterar_reserva,
                        3: self.lista_reservas, 4: self.excluir_reserva,
                        5: self.adiciona_servico, 0: self.retornar}
        while True:
            lista_opcoes[self.__tela_reserva.tela_opcoes()]()