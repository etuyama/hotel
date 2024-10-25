from entidade.cliente import Cliente
from entidade.quarto import Quarto

class Reserva:

    def __init__(self, quarto: Quarto, tempo_estadia: int, cliente: Cliente, id: int):

        self.__quarto = quarto
        self.__tempo_estadia = tempo_estadia
        self.__cliente = cliente
        self.__id = id
        self.__valor_total = quarto.valor_diaria * tempo_estadia

    @property
    def tempo_estadia(self):
        return self.__tempo_estadia

    @tempo_estadia.setter
    def tempo_estadia(self, tempo_estadia: int):

        if isinstance(tempo_estadia, int):
            self.__tempo_estadia = tempo_estadia

    @property
    def valor_total(self):
        return self.__valor_total
    
    @property
    def quarto(self):
        return self.__quarto

    @property
    def cliente(self):
        return self.__cliente

    @property
    def id(self):
        return self.__id

    def extender_estadia(self, dias: int):

        if isinstance(dias, int):
            self.__valor_total = self.__valor_total + self.__quarto.valor_diaria * dias

    def adicionar_valor_extra(self, valor: int):

        if isinstance(valor, int):
            self.__valor_total = self.__valor_total + valor

    def mostra_quarto(self):
        return f" quarto {self.__quarto.numero}: {self.__quarto.descricao}"

    def mostra_cliente(self):
        return f" cliente: {self.__cliente.nome}, telefone: {self.__cliente.telefone}"
    
    def detalhes_reserva(self):
        return f"Reserva do {self.mostra_quarto} feita pelo {self.mostra_cliente}"
