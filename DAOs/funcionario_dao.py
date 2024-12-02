from DAOs.dao import DAO
from entidade.funcionario import Funcionario

class FuncionarioDAO(DAO):
    def __init__(self):
        super().__init__('funcionario.pkl')


    def add(self, funcionario: Funcionario):
        if funcionario is not None and isinstance(funcionario, Funcionario) and isinstance(funcionario.cpf, str):
            super().add(funcionario.cpf, funcionario)

    def update(self, funcionario: Funcionario):
        if funcionario is not None and isinstance(funcionario, Funcionario) and isinstance(funcionario.cpf, str):
            super().update(funcionario.cpf, funcionario)

    def get(selfself, key):
        key = super().get(key)
        return key

    def remove(self, key):
        if super().get(key) is None:
            return None
        return super().remove(key)