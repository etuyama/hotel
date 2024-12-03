from DAOs.dao import DAO
from entidade.quarto import Quarto


class QuartoDAO(DAO):
    def __init__(self):
        super().__init__('quarto.pkl')

    def add(self, quarto: Quarto):
        if quarto is not None and isinstance(quarto, Quarto):
            super().add(quarto.numero, quarto)

    def update(self, quarto: Quarto):
        super().update(quarto.numero, quarto)

    def get(self, key):
        key = super().get(key)
        return key

    def remove(self, key):
        if super().get(key) is None:
            return None
        return super().remove(key)
