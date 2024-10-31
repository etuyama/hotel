class DataFuturaException(Exception):
    def __init__(self):
        self.mensagem = (
            "Data não pode ser no futuro."
        )
        super().__init__(self.mensagem)
