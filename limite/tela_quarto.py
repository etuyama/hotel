class TelaQuarto():

    def tela_opcoes(self):
        escolhas = [1,2,3,4,0]
        print("-------- QUARTOS ----------")
        print("Escolha a opção")
        print("1- Incluir Quarto")
        print("2- Alterar Quarto")
        print("3- Listar Quartos")
        print("4- Excluir Quarto")
        print("0- Retornar")
        while True:
            try:
                escolha = int(input("Escolha: "))
                if escolha not in escolhas:
                    raise ValueError #CRIAR ERRO ESPECÍFICO
                return escolha
            except ValueError:
                print("Escolha inválida")

    def pega_dados_quarto(self):
        print("-------- DADOS QUARTO --------")
        print("Qual tipo de quarto deseja?")
        print("1- Standard")
        print("2- Suíte")
        print("3- Luxo")
        tipos_validos = [1,2,3]
        while True:
            try:
                tipo = int(input("Tipo: "))
                if tipo not in tipos_validos:
                    raise ValueError #CRIAR ERRO ESPECÍFICO

                numero = int(input("Número: "))
                if numero <= 0:
                    raise ValueError #CRIAR ERRO ESPECÍFICO?

                valor_diaria = int(input("Valor da diária: "))
                if valor_diaria <= 0:
                    raise ValueError #CRIAR ERRO ESPECÍFICO?

                descricao = input("Descrição: ")
                return {"numero": numero, "valor_diaria": valor_diaria,
                        "descricao": descricao, "tipo": tipo}

            except ValueError:
                print("Valores inseridos inválidos")

    #Não será possível alterar o tipo do quarto, logo foi necessária uma nova função mais específica    
    def pega_dados_alteracao_quarto(self, quarto):
        print("-------- DADOS QUARTO --------")
        while True:
            try:
                numero = int(input("Número: "))
                if numero <= 0:
                    raise ValueError #CRIAR ERRO ESPECÍFICO?

                valor_diaria = int(input("Valor da diária: "))
                if valor_diaria <= 0:
                    raise ValueError #CRIAR ERRO ESPECÍFICO?
                descricao = input("Descrição: ")

                return {"numero": numero, "valor_diaria": valor_diaria,
                        "descricao": descricao, "tipo": quarto.tipo}

            except ValueError:
                print("Valores inseridos inválidos")        

    def mostra_quarto(self, dados_quarto):
        print("Quarto tipo ", dados_quarto["tipo"])
        print("Número: ", dados_quarto["numero"])
        print("Valor da diária: ", dados_quarto["valor_diaria"])
        print("Descrição: ", dados_quarto["descricao"])
        print("\n")

    def seleciona_quarto(self):
        while True:
            try:
                numero = int(input("Número do quarto que deseja selecionar: "))
                return numero

            except ValueError:
                print("Valor inserido inválido")

    def mostra_mensagem(self, mensagem):
        print(mensagem)
