from cliente import Cliente
from funcionario import Funcionario
from servico import Servico


class RealizaServico:
    def __init__(self, cliente: Cliente, funcionario: Funcionario,
                 servico: Servico):
        if isinstance(cliente, Cliente) and \
            isinstance(funcionario, Funcionario) and \
            isinstance(servico, Servico):
            self.__cliente = cliente
            self.__funcionario = funcionario
            self.__servico = servico

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