from limite.tela import Tela
import PySimpleGUI as sg


class TelaFuncionario(Tela):

    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def tela_opcoes(self):
        self.init_opcoes()
        button, values = self.open()
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        if values['5']:
            opcao = 5
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def init_opcoes(self):
        sg.ChangeLookAndFeel('Dark')
        layout = [
            [sg.Text('Funcionarios', font=('Helvetica', 25))],
            [sg.Text('Escolha sua opção', font=('Helvetica', 15))],
            [sg.Radio('Incluir Funcionario', 'F01', key='1')],
            [sg.Radio('Alterar Funcionario', 'F01', key='2')],
            [sg.Radio('Listar Funcionarios', 'F01', key='3')],
            [sg.Radio('Excluir Funcionario', 'F01', key='4')],
            [sg.Radio('Listar Funcionários por cargo', 'F01', key='5')],
            [sg.Radio('Retornar', 'C01', key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Funcionario').Layout(layout)

    def pega_dados_funcionario(self):
        sg.ChangeLookAndFeel('Dark')
        layout = [
            [sg.Text('Dados do Funcionario', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Text('Cargo:', size=(15, 1)), sg.InputText('', key='cargo')],
            [sg.Text('Data de admissão:', size=(15, 1)), sg.InputText('', key='data_admissao')],
            [sg.Text('Salário:', size=(15, 1)), sg.InputText('', key='salario')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Funcionarios').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        cpf = values['cpf']
        cargo = values['cargo']
        data_admissao = values['data_admissao']
        salario = values['salario']

        self.close()
        return {"nome": nome, "cpf": cpf, "cargo": cargo,
                "data_admissao": data_admissao, "salario": salario}

    def mostra_funcionario(self, dados):
        string_todos_funcionarios = ""
        for dado in dados:
            string_todos_funcionarios = string_todos_funcionarios + "Nome do Funcionario: " + dado["nome"] + '\n'
            string_todos_funcionarios = string_todos_funcionarios + "CPF do Funcionario: " + dado["cpf"] + '\n'
            string_todos_funcionarios = string_todos_funcionarios + "Cargo do Funcionario: " + dado["cargo"] + '\n'
            string_todos_funcionarios = string_todos_funcionarios + "Data de Admissão do Funcionario: " + str(dado["data_admissao"]) + '\n'
            string_todos_funcionarios = string_todos_funcionarios + "Salario do Funcionario: " + dado["salario"] + '\n\n'

        sg.Popup('Lista de Funcionarios', string_todos_funcionarios)

    def seleciona_funcionario(self):
        sg.ChangeLookAndFeel('Dark')
        layout = [
            [sg.Text('Selecionar Funcionario', font=("Helvica", 25))],
            [sg.Text('Digite o CPF do Funcionario que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona Funcionario').Layout(layout)

        button, values = self.open()
        cpf = values['cpf']
        self.close()
        return cpf

    def seleciona_por_cargo(self):
        sg.ChangeLookAndFeel('Dark')
        layout = [
            [sg.Text('Selecionar Funcionario', font=("Helvica", 25))],
            [sg.Text('Digite o Cargo do funcionario que deseja buscar:', font=("Helvica", 15))],
            [sg.Text('Cargo:', size=(15, 1)), sg.InputText('', key='cargo')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona Funcionario').Layout(layout)

        button, values = self.open()
        cargo = values['cargo']
        self.close()
        return cargo
    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
