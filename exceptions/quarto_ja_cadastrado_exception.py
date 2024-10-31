class QuartoJaCadastradoException(Exception):
    def __init__(self, numero):
        self.mensagem = "Quarto com o número {} já existe"
        super().__init__(self.mensagem.format(numero))