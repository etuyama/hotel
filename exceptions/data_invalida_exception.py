class DataInvalidaException(Exception):
    def __init__(self):
        self.mensagem = (
            "Digite uma data válida."
        )
        super().__init__(self.mensagem)
