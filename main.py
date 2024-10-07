from entidade.hotel import Hotel
from entidade.cliente import Cliente
from entidade.funcionario import Funcionario
from entidade.servico import Servico
from entidade.realiza_servico import RealizaServico
from controle.controlador_sistema import ControladorSistema

if __name__ == "__main__":
    ControladorSistema().inicializa_sistema()