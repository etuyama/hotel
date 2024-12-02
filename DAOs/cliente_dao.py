from DAOs.dao import DAO
from entidade.cliente import Cliente


class ClienteDAO(DAO):
    def __init__(self):
        super().__init__('cliente.pkl')

    def add(self, cliente: Cliente):
        if cliente is not None and isinstance(cliente, Cliente) and isinstance(cliente.cpf, str):
            super().add(cliente.cpf, cliente)

    def update(self, cliente: Cliente):
        if cliente is not None and isinstance(cliente, Cliente) and isinstance(cliente.cpf, str):
            super().update(cliente.cpf, cliente)

    def get(selfself, key):
        key = super().get(key)
        return key

    def remove(self, key):
        if super().get(key) is None:
            return None
        return super().remove(key)
