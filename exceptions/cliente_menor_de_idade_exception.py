class ClienteMenorDeIdadeException(Exception):
    def __init__(self, idade):
        self.mensagem = (
            "Idade minima para fazer uma reserva é de 18 anos. "
            "Este cliente tem {} anos."
        )
        super().__init__(self.mensagem.format(idade))