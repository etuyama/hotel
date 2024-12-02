from limite.tela import Tela
from exceptions.valor_invalido_exception import ValorInvalidoException
import PySimpleGUI as sg

class TelaHotel(Tela):

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
        if values['6']:
            opcao = 6
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def init_opcoes(self):
        sg.ChangeLookAndFeel('Dark')
        layout = [
            [sg.Text('Hotel', font=('Helvetica', 25))],
            [sg.Text('Escolha sua opção', font=('Helvetica', 15))],
            [sg.Radio('Realizar Check-out', 'H01', key='1')],
            [sg.Radio('Finalizar Manutenção de Quarto', 'H01', key='2')],
            [sg.Radio('Pagar Funcionário', 'H01', key='3')],
            [sg.Radio('Pagar Despesa', 'H01', key='4')],
            [sg.Radio('Mostrar Avaliação', 'H01', key='5')],
            [sg.Radio('Mostrar Saldo', 'H01', key='6')],
            [sg.Radio('Retornar', 'H01', key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Hotel').Layout(layout)

    #Alterar esse método para mostrar usando PySimpleGUI
    def le_avaliacao(self, mensagem, escolhas_validas):
        while True:
            escolha = input(mensagem)
            print()
            try:
                escolha_avaliacao = int(escolha)
                if escolhas_validas and escolha_avaliacao not in escolhas_validas:
                    raise ValorInvalidoException

                return escolha_avaliacao

            #se for inserido qualquer valor não numérico a avaliação é dada como não feita
            except ValueError:
                escolha = "N/A"
                return escolha

            #caso tenha sido inserido algum número inteiro inválido,
            #  o usuário pode tentar novamente
            except ValorInvalidoException as e:
                print(e)

    def pega_avaliacao_hotel(self):
        sg.ChangeLookAndFeel('Dark')
        layout = [
            [sg.Text('Hotel', font=('Helvetica', 25))],
            [sg.Text('Qual avaliação gostaria de dar para o Hotel?', font=('Helvetica', 15))],
            [sg.Radio('Excelente', "H01", key='5', enable_events=True)],
            [sg.Radio('Boa', "H01", key='4', enable_events=True)],
            [sg.Radio('Razoável', "H01", key='3', enable_events=True)],
            [sg.Radio('Ruim', "H01", key='2', enable_events=True)],
            [sg.Radio('Péssima', "H01", key='1', enable_events=True)],
            [sg.Radio('Não avaliar', "H01", key='0', enable_events=True)],
            [sg.Radio('Retornar', 'H01', key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Hotel').Layout(layout)
    def pega_dados_despesa(self):
        sg.ChangeLookAndFeel('Dark')
        layout = [
            [sg.Text('Hotel', font=('Helvetica', 25))],
            [sg.Text('Registrar despesa', font=('Helvetica', 15))],
            [sg.Text('Valor da despesa:', size=(15, 1)), sg.InputText('', key='valor')],
            [sg.Text('Descricao:', size=(15, 1)), sg.InputText('', key='descricao')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de livros').Layout(layout)

        button, values = self.open()
        valor = values['valor']
        descricao = values['descricao']
        return {"valor": valor, "descricao": descricao}

    def seleciona_reserva(self):
        sg.ChangeLookAndFeel('Dark')
        layout = [
            [sg.Text('Hotel', font=('Helvetica', 25))],
            [sg.Text('Digite o ID da reserva que deseja selecionar:', font=('Helvetica', 15))],
            [sg.Text('ID:', size=(15, 1)), sg.InputText('', key='id')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona ID').Layout(layout)

        button, values = self.open()
        id = values['id']
        self.close()
        return id

    def seleciona_quarto(self):
        sg.ChangeLookAndFeel('Dark')
        layout = [
            [sg.Text('Hotel', font=('Helvetica', 25))],
            [sg.Text('Digite o número do quarto que deseja selecionar', font=('Helvetica', 15))],
            [sg.Text('Número:', size=(15, 1)), sg.InputText('', key='numero')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona Número').Layout(layout)

        button, values = self.open()
        numero = values['numero']
        self.close()
        return numero

    def seleciona_funcionario(self):
        sg.ChangeLookAndFeel('Dark')
        layout = [
            [sg.Text('Hotel', font=('Helvetica', 25))],
            [sg.Text('Digite o CPF do funcionario que deseja selecionar', font=('Helvetica', 15))],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona CPF').Layout(layout)

        button, values = self.open()
        cpf = values['cpf']
        self.close()
        return cpf

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
    

