from pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, cpf: str, nome: str, cargo: str, data_admissao: str, salario: int):
        if isinstance(cargo, str) and isinstance(data_admissao, str) and isinstance(salario, int):
            super().__init__(cpf, nome)
            self.__cargo = cargo
            self.__data_admissao = data_admissao
            self.__salario = salario

    @property
    def cargo(self):
        return self.__cargo

    @cargo.setter
    def cargo(self, cargo):
        if isinstance(cargo,str):
            self.__cargo = cargo

    @property
    def data_admissao(self):
        return self.__data_admissao

    @data_admissao.setter
    def data_admissao(self, data_admissao):
        if isinstance(data_admissao, str):
            self.__data_admissao = data_admissao

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, salario: int):

        if isinstance(salario, int):
            self.__salario = salario

    def atualizar_status_quarto(self, quarto, novo_status):

        if isinstance(novo_status, str):
            quarto.status = novo_status

    def registrar_check_in(self, quarto):
        quarto.status = 'Ocupado'

    def registrar_check_out(self, quarto):
        quarto.status = 'Manutenção'
