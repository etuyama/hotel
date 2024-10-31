class MenorQueZeroException(Exception):
    def __init__(self):
        self.mensagem = "Valor deve ser maior que zero."
        super().__init__(self.mensagem)