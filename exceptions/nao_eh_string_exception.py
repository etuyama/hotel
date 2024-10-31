class NaoEhStringException(Exception):
    def __init__(self):
        self.mensagem = "Entrada deve começar com uma letra."
        super().__init__(self.mensagem)