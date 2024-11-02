from entidade.quarto_standard import QuartoStandard
from entidade.quarto_suite import QuartoSuite
from entidade.quarto_luxo import QuartoLuxo
from entidade.servico import Servico
from entidade.cliente import Cliente
from entidade.reserva import Reserva
from entidade.funcionario import Funcionario


class Hotel:

    def __init__(self):
        self.__saldo = 0
        self.__avaliacao_hotel = None

    @property
    def saldo(self):
        return self.__saldo

    @property
    def avaliacao_hotel(self):
        return self.__avaliacao_hotel

    @avaliacao_hotel.setter
    def avaliacao_hotel(self, avaliacao: float):
        if isinstance(avaliacao, float):
            self.__avaliacao_hotel = avaliacao

    def incrementar_saldo(self, valor: int):
        if isinstance(valor, int):
            self.__saldo = self.__saldo + valor

    def decrementar_saldo(self, valor: int):
        if isinstance(valor, int):
            self.__saldo = self.__saldo - valor




