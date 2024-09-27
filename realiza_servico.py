from cliente import Cliente
from funcionario import Funcionario
from servico import Servico
from hotel import Hotel

class RealizaServico:

    def __init__(self, cliente: Cliente, funcionario: Funcionario,
                 servico: Servico, hotel: Hotel):
        if isinstance(cliente, Cliente) and \
            hotel.verificar_funcionario(funcionario) and \
            isinstance(servico, Servico) and \
            isinstance(hotel, Hotel):
            self.__cliente = cliente
            self.__funcionario = funcionario
            self.__servico = servico
            reserva = hotel.consultar_reserva(cliente)
            reserva.adicionar_valor_extra(servico.preco)

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        if isinstance(cliente, Cliente):
            self.__cliente = cliente

    @property
    def funcionario(self):
        return self.__funcionario

    @funcionario.setter
    def funcionario(self, funcionario):
        if isinstance(funcionario, Funcionario):
            self.__funcionario = funcionario

    @property
    def servico(self):
        return self.__servico

    @servico.setter
    def servico(self, servico):
        if isinstance(servico, Servico):
            self.__servico = servico

    def mostra_valor(self):
        return self.servico.preco

    def detalhes_servico(self):
        return f'Serviço: {self.servico.nome}\nCliente: {self.cliente.nome}\nPreço: {self.mostra_valor()}'