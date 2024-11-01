from limite.tela import Tela


class TelaFuncionario(Tela):
    def tela_opcoes(self):
        escolhas = [1,2,3,4,5,0]
        print("-------- FUNCIONARIOS ----------")
        print("Escolha uma opção")
        print("1 - Incluir Funcionário")
        print("2 - Alterar Funcionário")
        print("3 - Listar Funcionários")
        print("4 - Excluir Funcionário")
        print("5 - Listar Funcionários por cargo")
        print("0 - Retornar")

        escolha = super().le_num_inteiro("Escolha: ", escolhas)
        return escolha

    def pega_dados_funcionario(self):
        print("-------- DADOS FUNCIONÁRIO --------")
        nome = super().le_string("Nome: ")
        cpf = super().le_cpf("CPF: ")
        cargo = super().le_string("Cargo: ")
        data_admissao = super().le_data(
            "Data de admissão (DD/MM/AAAA): "
        )
        salario = super().le_num_inteiro("Salário: ")

        return {"nome": nome, "cpf": cpf, "cargo": cargo,
                "data_admissao": data_admissao, "salario": salario}

    def mostra_funcionario(self, dados_funcionario):
        print("Nome do funcionario: ", dados_funcionario["nome"])
        print("CPF: ", dados_funcionario["cpf"])
        print("Cargo: ", dados_funcionario["cargo"])
        print("Data de admissão: ", dados_funcionario["data_admissao"])
        print(f"Salario: R${dados_funcionario['salario']},00")
        print("\n")

    def seleciona_funcionario(self):
        #Aqui é melhor não usar le_cpf()
        cpf = input("CPF do funcionário que deseja selecionar: ")
        return cpf

    def seleciona_por_cargo(self):
        cargo = input("Digite o cargo que deseja buscar: ")
        return cargo
