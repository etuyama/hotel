from limite.tela import Tela
import PySimpleGUI as sg


class TelaCliente(Tela):

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
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def init_opcoes(self):
        sg.ChangeLookAndFeel('Dark')
        layout = [
            [sg.Text('Clientes', font=('Helvetica', 25))],
            [sg.Text('Escolha sua opção', font=('Helvetica', 15))],
            [sg.Radio('Incluir Cliente', 'C01', key='1')],
            [sg.Radio('Alterar Cliente', 'C01', key='2')],
            [sg.Radio('Listar Clientes', 'C01', key='3')],
            [sg.Radio('Excluir Cliente', 'C01', key='4')],
            [sg.Radio('Retornar', 'C01', key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Clientes').Layout(layout)

    def pega_dados_cliente(self):
        while True:
            sg.ChangeLookAndFeel('Dark')
            layout = [
                [sg.Text('Dados do Cliente', font=("Helvica", 25))],
                [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
                [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
                [sg.Text('Telefone:', size=(15, 1)), sg.InputText('', key='telefone')],
                [sg.Text('Data de nascimento:', size=(15, 1)), sg.InputText('', key='data_nascimento')],
                [sg.Text('Endereço:', size=(15, 1)), sg.InputText('', key='endereco')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
            self.__window = sg.Window('Sistema do Hotel').Layout(layout)

            button, values = self.open()
            nome = super().le_string(values['nome'])
            cpf = super().le_cpf(values['cpf'])
            telefone = super().le_telefone(values['telefone'])
            data_nascimento = super().le_data(values['data_nascimento'])
            endereco = super().le_string(values['endereco'])

            self.close()
            if nome and cpf and telefone and data_nascimento and endereco:
                return {"nome": nome, "cpf": cpf, "telefone": telefone,
                        "data_nascimento": data_nascimento, "endereco": endereco}


    def mostra_cliente(self, dados):
        string_todos_clientes = ""
        for dado in dados:
            string_todos_clientes = string_todos_clientes + "Nome do Cliente: " + dado["nome"] + '\n'
            string_todos_clientes = string_todos_clientes + "CPF do Cliente: " + dado["cpf"] + '\n'
            string_todos_clientes = string_todos_clientes + "Telefone do Cliente: " + dado["telefone"] + '\n'
            string_todos_clientes = string_todos_clientes + "Data de nascimento do Cliente: " + str(dado["data_nascimento"]) + '\n'
            string_todos_clientes = string_todos_clientes + "Endereço do Cliente: " + dado["endereco"] + '\n\n'

        sg.Popup('Lista de Clientes', string_todos_clientes)

    def seleciona_cliente(self):
        sg.ChangeLookAndFeel('Dark')
        layout = [
            [sg.Text('Selecionar Cliente', font=("Helvica", 25))],
            [sg.Text('Digite o CPF do Cliente que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona Cliente').Layout(layout)

        button, values = self.open()

        cpf = super().le_cpf(values['cpf'])
        self.close()

        return cpf

    def close(self):
        self.__window.close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
