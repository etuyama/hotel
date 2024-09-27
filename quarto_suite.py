from quarto import Quarto


class QuartoSuite(Quarto):

    def __init__(self, numero: int, valor_diaria: int, descricao: str):

        if isinstance(numero, int) and isinstance(valor_diaria, int) and \
            isinstance(descricao, str):
            super().__init__(numero, valor_diaria, descricao)
