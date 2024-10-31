from abc import ABC, abstractmethod


class Tela(ABC):

    def mostra_mensagem(self, mensagem):
        print(mensagem)
        print()

    def le_num_inteiro(self, mensagem="", inteiros_validos = None):
        while True:
            valor_lido = input(mensagem)
            try:
                valor_inteiro = int(valor_lido)
                if inteiros_validos and valor_inteiro not in inteiros_validos:
                    raise ValueError #CRIAR ERRO ESPECÍFICO

                if inteiros_validos and valor_inteiro in inteiros_validos:
                    return valor_inteiro

                if valor_inteiro <= 0:
                    raise ValueError #CRIAR ERRO ESPECÍFICO

                return valor_inteiro

            except ValueError:
                print("Valor inserido inválido")
                if inteiros_validos:
                    print("Valores válidos: ", inteiros_validos)
