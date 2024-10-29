

class Servico:
    def __init__(self, nome: str, descricao: str, preco: int, id: int):
        self.__nome = nome
        self.__descricao = descricao
        self.__preco = preco
        self.__id = id

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        if isinstance(descricao, str):
            self.__descricao = descricao

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, preco):
        if isinstance(preco, int):
            self.__preco = preco

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        if isinstance(id, int):
            self.__id = id

