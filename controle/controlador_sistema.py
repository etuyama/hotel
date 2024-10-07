from limite.tela_sistema import TelaSistema
#from controle.controlador_reservas import ControladorReservas
from controle.controlador_clientes import ControladorClientes
#from controle.controlador_servicos import ControladorServicos
#from controle.controlador_quartos import ControladorQuartos

class ControladorSistema:

    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_clientes = ControladorClientes(self)
        #self.__controlador_reservas = ControladorReservas(self)
        #self.__controlador_servicos = ControladorServicos(self)
        #self.__controlador_quartos = ControladorQuartos(self)


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

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1 : self.cadastra_clientes,
                        2 : self.cadastra_reservas,
                        3 : self.cadastra_servicos,
                        4 : self.cadastra_quartos,
                        0 : self.encerra_sistema
                        }

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
