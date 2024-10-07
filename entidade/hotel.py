from entidade.quarto_standard import QuartoStandard
from entidade.quarto_suite import QuartoSuite
from entidade.quarto_luxo import QuartoLuxo
from entidade.servico import Servico
from cliente import Cliente
from entidade.reserva import Reserva
from funcionario import Funcionario


class Hotel:

    def __init__(self, nome: str):

        if isinstance(nome, str):
            self.__nome = nome
            self.__saldo = 0
            self.__registro = 'Registro' # INSTÂNCIA DE REGISTRO
            self.__quartos = []
            self.__reservas = []
            self.__funcionarios = []
            self.__servicos = []

    @property
    def nome(self):
        return self.__nome
   
    @nome.setter
    def nome(self, nome):

        if isinstance(nome, str):
            self.__nome = nome

    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def registro(self):
        return self.__registro
    
    def adicionar_quarto(self, numero: int, valor_diaria: int, descricao: str, tipo_do_quarto: str):

        if isinstance(numero, int) and isinstance(valor_diaria, int) and \
            isinstance(descricao, str) and isinstance(tipo_do_quarto, str):

            if tipo_do_quarto == 'Standard':
                quarto = QuartoStandard(numero, valor_diaria, descricao)
                self.__quartos.append(quarto)
            
            elif tipo_do_quarto == 'Suite': 
                quarto = QuartoSuite(numero, valor_diaria, descricao)
                self.__quartos.append(quarto)

            elif tipo_do_quarto == 'Luxo':
                quarto = QuartoLuxo(numero, valor_diaria, descricao) 
                self.__quartos.append(quarto)

            else:
                return 'Tipo de quarto inválido'

    def adicionar_funcionario(self, funcionario: Funcionario):

        if isinstance(funcionario, Funcionario) and not self.verificar_funcionario(funcionario):
            self.__funcionarios.append(funcionario)

    def reservar_quarto(self, numero_quarto: int, tempo_estadia: int, cliente: Cliente, funcionario: Funcionario):

        if isinstance(numero_quarto, int) and isinstance(tempo_estadia, int) and \
            isinstance(cliente, Cliente) and self.verificar_funcionario(funcionario):

            quarto = self.consultar_quarto(numero_quarto)
            if quarto != False and quarto.status == 'Disponível':

                reserva = Reserva(quarto, tempo_estadia, cliente)
                self.__reservas.append(reserva)
                funcionario.registrar_check_in(quarto)

    def adicionar_servico(self, servico: Servico):

        if isinstance(servico, Servico):
            self.__servicos.append(servico)

    def consultar_quarto(self, numero_quarto):

        for quarto in self.__quartos:
            if quarto.numero == numero_quarto:
                return quarto
            
        return False

    def consultar_reserva(self, cliente: Cliente):

        if isinstance(cliente, Cliente):

            for reserva in self.__reservas:
                
                if reserva.cliente == cliente:
                    return reserva

            return False
    
    def verificar_funcionario(self, funcionario: Funcionario):

            if funcionario in self.__funcionarios:
                return True
            
            return False

    def extender_estadia(self, cliente: Cliente, dias: int):

        if isinstance(dias, int) and isinstance(cliente, Cliente):

            reserva = self.consultar_reserva(cliente)
            if reserva != False:
                reserva.extender_estadia(dias)

    def pagar_funcionario(self, funcionario: Funcionario):

        if self.verificar_funcionario(funcionario):
            salario = funcionario.salario
            self.__saldo = self.__saldo - salario

    def check_out(self, cliente: Cliente, funcionario: Funcionario):

        if isinstance(cliente, Cliente) and self.verificar_funcionario(funcionario):
            reserva = self.consultar_reserva(cliente)
            if isinstance(reserva, Reserva):

                self.__reservas.remove(reserva)
                self.__saldo = self.__saldo + reserva.valor_total
                funcionario.registrar_check_out(reserva.quarto)
                return f'Preço final: {reserva.valor_total}'

    def finalizar_manutencao(self, numero_quarto: int, funcionario: Funcionario):

        if isinstance(numero_quarto, int) and self.verificar_funcionario(funcionario):
            quarto = self.consultar_quarto(numero_quarto)
            funcionario.atualizar_status_quarto('Disponível', quarto)

    def gerar_relatorio_reservas(registro):
        pass

    def gerar_relatorio_financeiro(registro):
        pass

    def gerar_relatorio_servicos(registro):
        pass
    



