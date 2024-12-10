from limite.tela import Tela
import PySimpleGUI as sg

# Falta implementar os tratamentos de entrada no Funcionário, Quarto e Cliente.
# 

class TelaQuarto(Tela):

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
            [sg.Text('Quartos', font=('Helvetica', 25))],
            [sg.Text('Escolha sua opção', font=('Helvetica', 15))],
            [sg.Radio('Incluir Quarto', 'Q01', key='1')],
            [sg.Radio('Alterar Quarto', 'Q01', key='2')],
            [sg.Radio('Listar Quartos', 'Q01', key='3')],
            [sg.Radio('Excluir Quarto', 'Q01', key='4')],
            [sg.Radio('Retornar', 'Q01', key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Quartos').Layout(layout)

    def pega_dados_quarto(self):
        while True:
            sg.ChangeLookAndFeel('Dark')
            layout = [
                [sg.Text('Qual tipo de quarto deseja?', font=("Helvica", 25))],
                [sg.Radio('Standard', 'T01', key='1')],
                [sg.Radio('Suíte', 'T01', key='2')],
                [sg.Radio('Luxo', 'T01', key='3')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
            self.__window = sg.Window('Quartos').Layout(layout)
            button, values = self.open()
            if values['1']:
                tipo = 1
            if values['2']:
                tipo = 2
            if values['3']:
                tipo = 3
            if button in (None, 'Cancelar'):
                tipo = 0
                return None

            self.close()

            sg.ChangeLookAndFeel('Dark')
            layout = [
                [sg.Text('Dados do Quarto', font=("Helvica", 25))],
                [sg.Text('Número:', size=(15, 1)), sg.InputText('', key='numero')],
                [sg.Text('Valor da Diária:', size=(15, 1)), sg.InputText('', key='valor_diaria')],
                [sg.Text('Descrição:', size=(15, 1)), sg.InputText('', key='descricao')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
            self.__window = sg.Window('Quartos').Layout(layout)
            button, values = self.open()

            if button in (None, 'Cancelar'):
                return None

            numero = super().le_num_inteiro(values['numero'])
            valor_diaria = super().le_num_inteiro(values['valor_diaria'])
            descricao = super().le_string(values['descricao'])

            self.close()
            if numero and valor_diaria and descricao:
                return {"numero": numero, "valor_diaria": valor_diaria,
                        "descricao": descricao, "tipo": tipo}

    #Não será possível alterar o tipo do quarto, e será possível alterar o status,
    #logo foi necessária uma nova função mais específica
    def pega_dados_alteracao_quarto(self):
        while True:
            sg.ChangeLookAndFeel('Dark')
            layout = [
                [sg.Text('Dados do Quarto', font=("Helvica", 25))],
                [sg.Text('Número:', size=(15, 1)), sg.InputText('', key='numero')],
                [sg.Text('Valor da Diária:', size=(15, 1)), sg.InputText('', key='valor_diaria')],
                [sg.Text('Descrição:', size=(15, 1)), sg.InputText('', key='descricao')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
            self.__window = sg.Window('Quartos').Layout(layout)
            button, values = self.open()

            if button in (None, 'Cancelar'):
                return None
            self.close()

            numero = super().le_num_inteiro(values['numero'])
            valor_diaria = super().le_num_inteiro(values['valor_diaria'])
            descricao = super().le_string(values['descricao'])
            if numero and valor_diaria and descricao:
                return {"numero": numero, "valor_diaria": valor_diaria,
                        "descricao": descricao}

    def mostra_quarto(self, dados):
        string_todos_quartos = ""
        for dado in dados:
            string_todos_quartos = string_todos_quartos + "Tipo do Quarto: " + dado["tipo"] + '\n'
            string_todos_quartos = string_todos_quartos + "Número do Quarto:  " + str(dado["numero"]) + '\n'
            string_todos_quartos = string_todos_quartos + f"Valor da diária: R${dado['valor_diaria']},00" + '\n'
            string_todos_quartos = string_todos_quartos + "Descrição: " + dado["descricao"] + '\n'
            string_todos_quartos = string_todos_quartos + "Status: " + dado["status"] + '\n\n'

        sg.Popup('Lista de Quartos', string_todos_quartos)

    def seleciona_quarto(self):
        while True:
            sg.ChangeLookAndFeel('Dark')
            layout = [
                [sg.Text('Selecionar Quarto', font=("Helvica", 25))],
                [sg.Text('Digite o número do Quarto que deseja selecionar:', font=("Helvica", 15))],
                [sg.Text('Número:', size=(15, 1)), sg.InputText('', key='numero')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]

            self.__window = sg.Window('Seleciona Quarto').Layout(layout)

            button, values = self.open()
            self.close()

            numero = super().le_num_inteiro(values['numero'])
            if numero:
                return numero

    def close(self):
        self.__window.close()

    def open(self):
        button, values = self.__window.Read()
        return button, values