from datetime import date

from entidade.pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, cpf: str, nome: str, data_nascimento: str, telefone: str, endereco: str):
        if isinstance(data_nascimento, str) and isinstance(telefone, str) and \
            isinstance(endereco, str):
            super().__init__(cpf, nome)
            self.__data_nascimento = data_nascimento
            self.__telefone = telefone
            self.__endereco = endereco

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        if isinstance(data_nascimento, str):
            self.__data_nascimento = data_nascimento

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        if isinstance(telefone, str):
            self.__telefone = telefone

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        if isinstance(endereco, str):
            self.__endereco = endereco

    def calcular_idade(self):
        hoje = date.today()
        data_cliente = date(int(self.__data_nascimento[6:10]), int(self.__data_nascimento[3:5]), int(self.__data_nascimento[0:2]))
        idade = hoje.year - data_cliente.year
        if (hoje.month, hoje.day) < (data_cliente.month, data_cliente.day):
            idade -= 1
        return idade

    def validar_maioridade(self):
        if self.calcular_idade() >= 18:
            return True
        return False
