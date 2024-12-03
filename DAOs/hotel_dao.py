from DAOs.dao import DAO
from entidade.hotel import Hotel

class HotelDAO(DAO):
    def __init__(self, datasource='hotel.pkl'):
        super().__init__(datasource)

    def save_hotel(self, hotel: Hotel):
        self.add("hotel", hotel)

    def get_hotel(self) -> Hotel:
        return self.get("hotel")

    def save_transacoes(self, transacoes: list):
        self.add("transacoes", transacoes)

    def get_transacoes(self) -> list:
        return self.get("transacoes") or []

    def save_avaliacoes(self, avaliacoes: list):
        self.add("avaliacoes", avaliacoes)

    def get_avaliacoes(self) -> list:
        return self.get("avaliacoes") or []
