from abc import ABC, abstractmethod


class Quarto(ABC):

    @abstractmethod
    def __init__(self, numero: int, valor_diaria: int, descricao: str):

        if isinstance(numero, int) and isinstance(valor_diaria, int) and \
            isinstance(descricao, str):
            self.__numero = numero
            self.__valor_diaria = valor_diaria
            self.__descricao = descricao
            self.__status = "Disponível"  # poderia ser True/ False, se trocar isso, trocar o isinstance do setter

    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self, numero: int):

        if isinstance(numero, int):
            self.__numero = numero

    @property
    def valor_diaria(self):
        return self.__valor_diaria
    
    @valor_diaria.setter
    def valor_diaria(self, valor_diaria: int):

        if isinstance(valor_diaria, int):
            self.__valor_diaria = valor_diaria

    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, descricao):

        if isinstance(descricao, str):
            self.__descricao = descricao

    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, status: str):

        if isinstance(status, str):
            self.__status = status