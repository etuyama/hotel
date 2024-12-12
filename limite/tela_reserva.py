from limite.tela import Tela
import PySimpleGUI as sg

class TelaReserva(Tela):

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
        # if values['5']:
        #     opcao = 5
        # if values['6']:
        #     opcao = 6
        # if values['7']:
        #     opcao = 7
        if values['8']:
            opcao = 8
        if values['9']:
            opcao = 9
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def init_opcoes(self):

        sg.ChangeLookAndFeel('Dark')        
        layout = [
            [sg.Text('Reserva', font=('Helvetica', 25))],
            [sg.Text('Escolha sua opção', font=('Helvetica', 15))],
            [sg.Radio('Efetuar Reserva', 'R01', key='1')],
            [sg.Radio('Alterar Reserva', 'R01', key='2')],
            [sg.Radio('Listar Reservas Pendentes', 'R01', key='3')],
            [sg.Radio('Excluir Reserva', 'R01', key='4')],
            # [sg.Radio('Adicionar Serviço Utilizado', 'R01', key='5')],
            # [sg.Radio('Extender Estadia', 'R01', key='6')],
            # [sg.Radio('Adicionar Valor Extra', 'R01', key='7')],
            [sg.Radio('Listar Todas Reservas', 'R01', key='8')],
            [sg.Radio('Gerar Relatórios', 'R01', key='9')],     
            [sg.Radio('Retornar', 'R01', key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]

        self.__window = sg.Window('Reservas').Layout(layout)

    def seleciona_reserva(self):
        sg.ChangeLookAndFeel('Dark')
        layout = [
            [sg.Text('Selecionar Reserva', font=("Helvica", 25))],
            [sg.Text('Digite o ID da Reserva que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('ID:', size=(15, 1)), sg.InputText('', key='id')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona Reserva').Layout(layout)

        button, values = self.open()

        id = super().le_num_inteiro(values['id'])
        self.close()

        return id

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

    def seleciona_quarto(self):
        sg.ChangeLookAndFeel('Dark')
        layout = [
            [sg.Text('Selecionar Quarto', font=("Helvica", 25))],
            [sg.Text('Digite o número do Quarto que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('Número:', size=(15, 1)), sg.InputText('', key='numero')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]

        self.__window = sg.Window('Seleciona Quarto').Layout(layout)

        button, values = self.open()

        numero = super().le_num_inteiro(values['numero'])
        self.close()

        return numero

    # def pega_dias_extensao(self):
    #     qt_dias = super().le_num_inteiro("Quantos dias deseja adicionar à estadia: ")
    #     return qt_dias

    # def pega_valor_extra(self):
    #     valor_extra = super().le_num_inteiro("Valor extra que deseja adicionar à reserva: ")
    #     return valor_extra

    def pega_tempo_estadia(self):
        sg.ChangeLookAndFeel('Dark')
        layout = [
            [sg.Text('Tempo de estadia', font=("Helvica", 25))],
            [sg.Text('Digite o tempo de estadia da reserva:', font=("Helvica", 15))],
            [sg.Text('tempo:', size=(15, 1)), sg.InputText('', key='tempo_estadia')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Tempo de Estadia').Layout(layout)

        button, values = self.open()

        tempo_estadia = super().le_num_inteiro(values['tempo_estadia'])
        self.close()

        return tempo_estadia

    def tela_relatorio(self):
        sg.ChangeLookAndFeel('Dark')
        layout = [
            [sg.Text('Relatórios', font=('Helvetica', 25))],
            [sg.Text('Escolha sua opção', font=('Helvetica', 15))],
            [sg.Radio('Tipos de quarto mais reservados', 'R01', key='1')],
            [sg.Radio('Meses com mais reservas realizadas', 'R01', key='2')],
            [sg.Radio('Clientes que mais fizeram reservas', 'R01', key='3')],
            [sg.Radio('Retornar', 'C01', key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Clientes').Layout(layout)

        button, values = self.open()
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    # def seleciona_servico(self):
    #     id = super().le_num_inteiro("ID do serviço que deseja selecionar: ")
    #     return id

    def seleciona_ano(self):

        sg.ChangeLookAndFeel('Dark')
        layout = [
            [sg.Text('Seleciona Ano', font=("Helvica", 25))],
            [sg.Text('Para qual ano deseja gerar o relatório? (Ex 2024):', font=("Helvica", 15))],
            [sg.Text('ano:', size=(15, 1)), sg.InputText('', key='ano')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona Ano').Layout(layout)

        button, values = self.open()

        ano = super().le_num_inteiro(values['ano'])
        self.close()

        return ano
    
    def mostra_reserva(self, dados):
        string_todas_reservas = ""
        for dado in dados:
            string_todas_reservas = string_todas_reservas + "ID: " + str(dado["id"]) + '\n'
            string_todas_reservas = string_todas_reservas + "Data da Reserva: " + str(dado["data_reserva"]) + '\n'
            string_todas_reservas = string_todas_reservas + "Situação: " + dado["situacao"] + '\n'
            string_todas_reservas = string_todas_reservas + "Nome do Cliente: " + dado["nome_cliente"] + '\n'
            string_todas_reservas = string_todas_reservas + "CPF do Cliente: " + dado["cpf_cliente"] + '\n'
            string_todas_reservas = string_todas_reservas + "Número do Quarto: " + str(dado["numero_quarto"]) + '\n'
            string_todas_reservas = string_todas_reservas + f"Valor da Diária: R${dado['valor_diaria']},00" + '\n'
            string_todas_reservas = string_todas_reservas + "Tempo de Estadia: " + str(dado["tempo_estadia"]) + '\n'
            string_todas_reservas = string_todas_reservas + f"Valor Total: R${dado['valor_total']},00" + '\n\n'

        sg.Popup('Lista de reservas', string_todas_reservas)

        # print("ID: ", dados_reserva["id"])
        # print("Data da reserva: ", dados_reserva["data_reserva"])
        # print("Situação: ", dados_reserva["situacao"])
        # print("Nome do Cliente: ", dados_reserva["nome_cliente"])
        # print("CPF do Cliente: ", dados_reserva["cpf_cliente"])
        # print("Número do Quarto: ", dados_reserva["numero_quarto"])
        # print(f"Valor da Diária: R${dados_reserva['valor_diaria']},00")
        # print("Tempo de Estadia: ", dados_reserva["tempo_estadia"])
        # print("Serviços Utilizados: ", dados_reserva["servicos_utilizados"])
        # print(f"Valor Total: R${dados_reserva['valor_total']},00")
        # print("\n")


    def close(self):
        self.__window.close()

    def open(self):
        button, values = self.__window.Read()
        return button, values