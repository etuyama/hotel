from limite.tela_sistema import TelaSistema
from controle.controlador_reservas import ControladorReservas
from controle.controlador_clientes import ControladorClientes
from controle.controlador_servicos import ControladorServicos
from controle.controlador_quartos import ControladorQuartos
from controle.controlador_funcionarios import ControladorFuncionarios
from controle.controlador_hotel import ControladorHotel

class ControladorSistema:

    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_clientes = ControladorClientes(self)
        self.__controlador_servicos = ControladorServicos(self)
        self.__controlador_funcionarios = ControladorFuncionarios(self)
        self.__controlador_quartos = ControladorQuartos(self)
        self.__controlador_reservas = ControladorReservas(self,
                                                          self.__controlador_clientes,
                                                          self.__controlador_quartos,
                                                          self.__controlador_servicos)

        self.__controlador_hotel = ControladorHotel(self,
                                                    self.__controlador_reservas,
                                                    self.__controlador_funcionarios,
                                                    self.__controlador_quartos)

    @property
    def controlador_clientes(self):
        return self.__controlador_clientes

    @property
    def controlador_reservas(self):
        return self.__controlador_reservas

    @property
    def controlador_servicos(self):
        return self.__controlador_servicos

    @property
    def controlador_quartos(self):
        return self.__controlador_quartos

    @property
    def controlador_funcionarios(self):
        return self.__controlador_funcionarios

    @property
    def controlador_hotel(self):
        return self.__controlador_hotel

    def inicializa_sistema(self):
        self.abre_tela()

    def cadastra_clientes(self):
        self.__controlador_clientes.abre_tela()

    def cadastra_reservas(self):
        self.__controlador_reservas.abre_tela()

    def cadastra_servicos(self):
        self.__controlador_servicos.abre_tela()

    def cadastra_quartos(self):
        self.__controlador_quartos.abre_tela()

    def cadastra_funcionarios(self):
        self.__controlador_funcionarios.abre_tela()

    def sistema_hotel(self):
        self.__controlador_hotel.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1 : self.cadastra_clientes,
                        2 : self.cadastra_reservas,
                        3 : self.cadastra_servicos,
                        4 : self.cadastra_quartos,
                        5 : self.cadastra_funcionarios,
                        6 : self.sistema_hotel,
                        0 : self.encerra_sistema,
                        }

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            self.__tela_sistema.mostra_mensagem(f"Opção escolhida: {opcao_escolhida}")
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
