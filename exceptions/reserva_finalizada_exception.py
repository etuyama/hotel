class ReservaFinalizadaException(Exception):

    def __init__(self, reserva):
        self.mensagem = "Reserva de ID: {} já foi finalizada"
        super().__init__(self.mensagem.format(reserva.id))