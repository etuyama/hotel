class QuartoIndisponivelException(Exception):
    def __init__(self):
        self.mensagem = "Quarto indisponível"
        super().__init__(self.mensagem)