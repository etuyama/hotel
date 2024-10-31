class QuartoNaoEncontradoException(Exception):
    def __init__(self, numero):
        self.mensagem = "Quarto de número {} não encontrado"
        super().__init__(self.mensagem.format(numero))