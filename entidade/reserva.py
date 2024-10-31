from entidade.cliente import Cliente
from entidade.quarto import Quarto
from entidade.servico import Servico

class Reserva:

    def __init__(self, quarto: Quarto, tempo_estadia: int, cliente: Cliente, id: int):

        self.__quarto = quarto
        self.__tempo_estadia = tempo_estadia
        self.__cliente = cliente
        self.__id = id
        self.__servicos_utilizados = []
        self.__valor_total = quarto.valor_diaria * tempo_estadia

    @property
    def tempo_estadia(self):
        return self.__tempo_estadia

    @property
    def valor_total(self):
        return self.__valor_total

    @property
    def quarto(self):
        return self.__quarto

    @quarto.setter
    def quarto(self, quarto: Quarto):

        if isinstance(quarto,Quarto):
            self.__quarto = quarto

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente: Cliente):

        if isinstance(cliente, Cliente):
            self.__cliente = cliente

    @property
    def id(self):
        return self.__id

    @property
    def servicos_utilizados(self):
        return self.__servicos_utilizados

    def extender_estadia(self, dias: int):

        if isinstance(dias, int):
            self.__valor_total = self.__valor_total + self.__quarto.valor_diaria * dias
            self.__tempo_estadia = self.__tempo_estadia + dias

    def adiciona_valor_extra(self, valor: int): #Pode ser uma multa, por exemplo.

        if isinstance(valor, int):
            self.__valor_total = self.__valor_total + valor

    def adiciona_servico(self, servico: Servico):

        if isinstance(servico, Servico):
            self.__valor_total = self.__valor_total + servico.preco
            self.__servicos_utilizados.append(servico)
