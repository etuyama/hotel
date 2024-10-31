from entidade.funcionario import Funcionario
from entidade.cliente import Cliente

class CadastroRepetidoException(Exception):
    def __init__(self, cpf, classe):
        if isinstance(classe, Funcionario):
            self.mensagem = "Funcionário com CPF {} já existe"
        elif isinstance(classe, Cliente):
            self.mensagem = "Cliente com CPF {} já existe"
        super().__init__(self.mensagem.format(cpf))