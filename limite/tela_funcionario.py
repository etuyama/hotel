

class TelaFuncionario:
    def tela_opcoes(self):
        escolhas = [1,2,3,4,5,0]
        print("-------- FUNCIONARIOS ----------")
        print("Escolha a opção")
        print("1 - Incluir Funcionário")
        print("2 - Alterar Funcionário")
        print("3 - Listar Funcionários")
        print("4 - Excluir Funcionário")
        print("5 - Listar Funcionários por cargo")
        print("0 - Retornar")

        escolha = int(input("Escolha: "))
        if escolha in escolhas:
            return escolha
        else:
            print("Escolha inválida")
            self.tela_opcoes()

    def pega_dados_funcionario(self):
        print("-------- DADOS FUNCIONÁRIO --------")

        nome = input("Nome: ")
        cpf = input("CPF: ")
        cargo = input("Cargo: ")
        data_admissao = input("Data de admissão: ")
        salario = int(input("Salario: "))
        if isinstance(nome, str) and isinstance(cpf, str) and \
            isinstance(cargo, str) and isinstance(data_admissao, str) and \
            isinstance(salario, int):
            return {"nome": nome, "cpf": cpf, "cargo": cargo,
                    "data_admissao": data_admissao, "salario": salario}
        else:
            print("Dados inválidos")
            self.pega_dados_funcionario()

    def mostra_funcionario(self, dados_funcionario):
        print("Nome do funcionario: ", dados_funcionario["nome"])
        print("CPF: ", dados_funcionario["cpf"])
        print("Cargo: ", dados_funcionario["cargo"])
        print("Data de admissão: ", dados_funcionario["data_admissao"])
        print("Salario: ", dados_funcionario["salario"])
        print("\n")

    def seleciona_funcionario(self):
        cpf = str(input("CPF do funcionário que deseja funcionar: "))
        return cpf

    def seleciona_por_cargo(self):
        cargo = input("Digite o cargo que deseja buscar: ")
        return cargo

    def mostra_mensagem(self, mensagem):
        print(mensagem)