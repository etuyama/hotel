class ServicoNomeException(Exception):
    def __init__(self, nome):
        self.mensagem = "Serviço com o nome {} já existe."
        super().__init__(self.mensagem.format(nome))