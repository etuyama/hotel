class ValorInvalidoException(Exception):
    def __init__(self):
        self.mensagem = "Valor inválido inserido."
        super().__init__(self.mensagem)