from limite.tela import Tela
import PySimpleGUI as sg

class TelaSistema(Tela):
    def __init__(self):
        super().__init__()
        self.__window = None
        self.init_components()

    def tela_opcoes(self):
        self.init_components()
        button, values = self.__window.Read()
        opcao = 0
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
        if values['0'] or button in (None,'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def close(self):
        self.__window.close()

    def init_components(self):
        sg.ChangeLookAndFeel('Dark')
        layout = [
            [sg.Text('Sistema de Hotel', font=('Helvica', 25))],
            [sg.Text('Escolha sua opção', font=('Helvica', 15))],
            [sg.Radio('Clientes', "S01", key='1')],
            [sg.Radio('Reservas', "S01", key='2')],
            [sg.Radio('Serviços', "S01", key='3')],
            [sg.Radio('Quartos', "S01", key='4')],
            [sg.Radio('Funcionários', "S01", key='5')],
            [sg.Radio('Hotel ', "S01", key='6')],
            sg.Radio('Finalizar Sistema', "S01", key='0')
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Hotel').Layout(layout)
