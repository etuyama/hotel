class CPFInvalidoException(Exception):
    def __init__(self):
        self.mensagem = "CPF Inválido"
        super().__init__(self.mensagem)