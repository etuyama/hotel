from abc import ABC, abstractmethod


class Tela(ABC):

    def mostra_mensagem(self, mensagem):
        print(mensagem)

    #TESTE
    def le_num_inteiro(self, mensagem="", inteiros_validos = None):
        while True:
            valor_lido = input(mensagem)
            try:
                valor_inteiro = int(valor_lido)
                if inteiros_validos and valor_inteiro not in inteiros_validos:
                    raise ValueError
                return valor_inteiro

            except ValueError:
                print("Valor incorreto!")
                if inteiros_validos:
                    print("Valores válidos: ", inteiros_validos)

    def tela_opcoes(self):
        print("-------- SisLivros ---------")
        print("Escolha sua opcao")
        print("1 - Livros")
        print("2 - Amigos")
        print("3 - Emprestimos")
        print("0 - Finalizar sistema")
        opcao = self.le_num_inteiro("Escolha a opcao:", [0,1,2,3])
        return opcao