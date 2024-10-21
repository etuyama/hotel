class TelaQuarto():
    #NAO ESQUECER DE PEDIR O TIPO DO QUARTO
    def tela_opcoes(self):
        escolhas = [1,2,3,4,0]
        print("-------- QUARTOS ----------")
        print("Escolha a opção")
        print("1- Incluir Quarto")
        print("2- Alterar Quarto")
        print("3- Listar Quartos")
        print("4- Excluir Quarto")
        print("0- Retornar")

        escolha = int(input("Escolha: ")) #FALTA APLICAR TRY EXCEPT
        if escolha in escolhas:
            return escolha
        else:
            print("Escolha inválida")
            self.tela_opcoes()

    def pega_dados_quarto(self):
        print("-------- DADOS QUARTO --------")
        print("Qual tipo de quarto deseja?")
        print("1- Standard")
        print("2- Suíte")
        print("3- Luxo")
        tipos_validos = [1,2,3]
        try:
            tipo = int(input("Tipo: "))
            if tipo not in tipos_validos:
                raise ValueError #CRIAR CLASSE DE ERRO?

            numero = int(input("Número: "))
            valor_diaria = int(input("Valor da diária: "))
            descricao = input("Descrição: ")
            return {"numero": numero, "valor_diaria": valor_diaria,
                    "descricao": descricao, "tipo": tipo}

        except ValueError:
            print("Valores inseridos inválidos")
            self.pega_dados_quarto()

    #Não será possível alterar o tipo do quarto, logo foi necessária uma nova função mais específica    
    def pega_dados_alteracao_quarto(self, quarto):
        print("-------- DADOS QUARTO --------")
        try:
            numero = int(input("Número: "))
            valor_diaria = int(input("Valor da diária: "))
            descricao = input("Descrição: ")
            return {"numero": numero, "valor_diaria": valor_diaria,
                    "descricao": descricao, "tipo": quarto.tipo}

        except ValueError:
            print("Valores inseridos inválidos")
            self.pega_dados_alteracao_quarto(quarto)
        

    def mostra_quarto(self, dados_quarto):
        print("Quarto tipo ", dados_quarto["tipo"])
        print("Número: ", dados_quarto["numero"])
        print("Valor da diária: ", dados_quarto["valor_diaria"])
        print("Descrição: ", dados_quarto["descricao"])
        print("\n")

    def seleciona_quarto(self):
        try:
            print("2")
            numero = int(input("Número do quarto que deseja selecionar: "))
            return numero

        except ValueError:
            print("Valor inserido inválido")
            self.seleciona_quarto()

    def mostra_mensagem(self, mensagem):
        print(mensagem)
