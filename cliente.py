from pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, cpf: str, nome: str, idade: int, telefone: str, endereco: str):
        if isinstance(idade, int) and isinstance(telefone, str) and \
            isinstance(endereco, str):
            super().__init__(cpf, nome)
            self.__idade = idade
            self.__telefone = telefone
            self.__endereco = endereco

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        if isinstance(idade, int):
            self.__idade = idade

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

    def validar_maioridade(self):  # essa função poderia ser na classe hotel dentro do método de efetuar a reserva
        if self.__idade >= 18:
            return True
        return False
