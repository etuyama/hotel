from entidade.quarto import Quarto


class QuartoLuxo(Quarto):

    def __init__(self, numero: int, valor_diaria: int, descricao: str):

        if isinstance(numero, int) and isinstance(valor_diaria, int) and \
            isinstance(descricao, str):
            super().__init__(numero, valor_diaria, descricao)