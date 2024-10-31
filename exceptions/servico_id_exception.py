class ServicoIdException(Exception):
    def __init__(self, id):
        self.mensagem = "Serviço com o ID {} já existe."
        super().__init__(self.mensagem.format(id))