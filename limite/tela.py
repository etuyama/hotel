from abc import ABC, abstractmethod
from datetime import date
from exceptions.data_futura_exception import DataFuturaException
from exceptions.data_invalida_exception import DataInvalidaException
from exceptions.entrada_vazia_exception import EntradaVaziaException
from exceptions.cpf_invalido_exception import CPFInvalidoException
from exceptions.menor_que_zero_exception import MenorQueZeroException
from exceptions.nao_eh_string_exception import NaoEhStringException
from exceptions.valor_invalido_exception import ValorInvalidoException


class Tela(ABC):

    def mostra_mensagem(self, mensagem):
        print(mensagem)

    def le_num_inteiro(self, mensagem="", inteiros_validos = None):
        while True:
            valor_lido = input(mensagem)
            try:
                valor_inteiro = int(valor_lido)
                if inteiros_validos and valor_inteiro not in inteiros_validos:
                    raise ValorInvalidoException

                if inteiros_validos and valor_inteiro in inteiros_validos:
                    return valor_inteiro

                if valor_inteiro <= 0:
                    raise MenorQueZeroException

                return valor_inteiro

            except ValorInvalidoException as e:
                print(e)
            except MenorQueZeroException as e:
                print(e)

    def le_string(self, mensagem=""):
        while True:
            entrada = input(mensagem)
            try:
                #Checa se a entrada é vazia
                if entrada == "":
                    raise EntradaVaziaException
                #Checa se pelo menos começa com uma letra
                if not entrada[0].isalpha():
                    raise NaoEhStringException
                return entrada

            except EntradaVaziaException as e:
                print(e)
            except NaoEhStringException as x:
                print(x)

    def le_cpf(self, mensagem=""):
        while True:
            cpf = input(mensagem)
            try:
                if len(cpf) != 11 or not cpf.isdigit():
                    raise CPFInvalidoException
                elif int(cpf) <= 0:
                    raise CPFInvalidoException
                return cpf

            except CPFInvalidoException as e:
                print(e)

    def le_telefone(self, mensagem=""):
        pass
    def le_data(self, mensagem=""):
        while True:
            data = input(mensagem)
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
                print(e)
            except DataFuturaException as x:
                print(x)

    @abstractmethod
    def tela_opcoes(self):
        pass