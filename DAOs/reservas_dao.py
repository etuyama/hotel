from DAOs.dao import DAO
from entidade.reserva import Reserva


class ReservaDAO(DAO):
    def __init__(self):
        super().__init__('reserva.pkl')

    def add(self, reserva: Reserva):
        if reserva is not None and isinstance(reserva, Reserva) and isinstance(reserva.id, int):
            super().add(reserva.id, reserva)

    def update(self, reserva: Reserva):
        if reserva is not None and isinstance(reserva, Reserva) and isinstance(reserva.id, int):
            super().update(reserva.id, reserva)

    def get(self, key):
        key = super().get(key)
        return key

    def remove(self, key):
        if super().get(key) is None:
            return None
        return super().remove(key)