from abc import ABC, abstractmethod
from datetime import date
from exceptions.data_futura_exception import DataFuturaException
from exceptions.data_invalida_exception import DataInvalidaException
from exceptions.entrada_vazia_exception import EntradaVaziaException
from exceptions.cpf_invalido_exception import CPFInvalidoException
from exceptions.menor_que_zero_exception import MenorQueZeroException
from exceptions.nao_eh_string_exception import NaoEhStringException
from exceptions.telefone_invalido_exception import TelefoneInvalidoException
from exceptions.valor_invalido_exception import ValorInvalidoException
import PySimpleGUI as sg


class Tela(ABC):

    def mostra_mensagem(self, mensagem):
        sg.Popup('', mensagem)

    def le_num_inteiro(self, valor_inserido):

        try:
            valor_inteiro = int(valor_inserido)

            if valor_inteiro <= 0:
                raise MenorQueZeroException

            return valor_inteiro

        except MenorQueZeroException as e:
            sg.Popup('', e)
            return False

        except ValueError:
            sg.Popup('', 'Valor inválido inserido')
            return False

    def le_string(self, entrada):

        try:
            #Checa se a entrada é vazia
            if entrada == "":
                raise EntradaVaziaException
            #Checa se pelo menos começa com uma letra
            if not entrada[0].isalpha():
                raise NaoEhStringException
            return entrada

        except EntradaVaziaException as e:
            sg.Popup(e)
            return False
        except NaoEhStringException as x:
            sg.Popup(x)
            return False

    def le_cpf(self, cpf_inserido):
        try:
            if len(cpf_inserido) != 11 or not cpf_inserido.isdigit():
                raise CPFInvalidoException

            elif int(cpf_inserido) <= 0:
                raise CPFInvalidoException

            return cpf_inserido

        except CPFInvalidoException as e:
            sg.Popup(e)
            return False

    def le_telefone(self, telefone=""):

        try:
            if not telefone.isdigit() or len(telefone) != 12:
                raise TelefoneInvalidoException
            if int(telefone) <= 0:
                raise TelefoneInvalidoException
            return telefone

        except TelefoneInvalidoException as e:
            sg.Popup(e)
            return False

    def le_data(self, data=""):

        dia = data[0:2]
        mes = data[3:5]
        ano = data[6:10]
        trinta_um = ['01', '03', '05', '07', '08', '10', '12']
        trinta = ['04', '06', '09', '11']
        ano_atual = date.today().year
        try:
            if not (dia.isdigit() or mes.isdigit() or ano.isdigit()) or \
                len(data) != 10:
                raise DataInvalidaException
            if int(mes) < 1 or int(mes) > 12:
                raise DataInvalidaException
            if mes in trinta_um and int(dia) > 31:
                raise DataInvalidaException
            if mes in trinta and int(dia) > 30:
                raise DataInvalidaException
            if mes == '02' and int(dia) > 28:
                raise DataInvalidaException
            if  int(ano) < 1600 or int(ano) > ano_atual or int(dia) < 1:
                raise DataInvalidaException
            if date(int(ano), int(mes), int(dia)) > date.today():
                raise DataFuturaException

            return data

        except DataInvalidaException as e:
            sg.Popup(e)
            return False
        except DataFuturaException as x:
            sg.Popup(x)
            return False

    @abstractmethod
    def tela_opcoes(self):
        pass
