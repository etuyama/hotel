class EntradaVaziaException(Exception):
    def __init__(self):
        self.mensagem = "Entrada não pode ser vazia."
        super().__init__(self.mensagem)