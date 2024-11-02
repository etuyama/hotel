from entidade.funcionario import Funcionario
from limite.tela_funcionario import TelaFuncionario
from exceptions.cadastro_repetido_exception import CadastroRepetidoException


class ControladorFuncionarios:

    def __init__(self, controlador_sistema):
        self.__funcionarios = []
        self.__tela_funcionario = TelaFuncionario()
        self.__controlador_sistema = controlador_sistema

    def lista_funcionarios_por_cargo(self):
        cargo  = self.__tela_funcionario.seleciona_por_cargo()

        lista_vazia = True
        for funcionario in self.__funcionarios:
            if cargo.lower() == funcionario.cargo.lower():
                lista_vazia = False
                self.__tela_funcionario.mostra_funcionario({"cpf": funcionario.cpf,
                                                            "nome": funcionario.nome,
                                                            "cargo": funcionario.cargo,
                                                            "data_admissao": funcionario.data_admissao,
                                                            "salario": funcionario.salario})
        if lista_vazia:
            self.__tela_funcionario.mostra_mensagem("Não existe nenhum funcionário com esse cargo.")


    def pega_funcionario_por_cpf(self, cpf: str):
        if isinstance(cpf, str):
            for funcionario in self.__funcionarios:
                if funcionario.cpf == cpf:
                    return funcionario
        return None

    def incluir_funcionario(self):
        dados_funcionario = self.__tela_funcionario.pega_dados_funcionario()
        cpf = dados_funcionario["cpf"]
        funcionario = self.pega_funcionario_por_cpf(cpf)
        try:
            if funcionario is None:
                funcionario = Funcionario(dados_funcionario["nome"],
                                          dados_funcionario["cpf"],
                                          dados_funcionario["cargo"],
                                          dados_funcionario["data_admissao"],
                                          dados_funcionario["salario"])
                self.__funcionarios.append(funcionario)
                self.__tela_funcionario.mostra_mensagem(
                    f"Funcionário {funcionario.nome} cadastrado com sucesso"
                )
            else:
                raise CadastroRepetidoException(cpf, funcionario)
        except CadastroRepetidoException as e:
            self.__tela_funcionario.mostra_mensagem(e)

    def alterar_funcionario(self):
        lista = self.lista_funcionarios()
        if not lista:
            return False

        cpf_funcionario = self.__tela_funcionario.seleciona_funcionario()
        funcionario = self.pega_funcionario_por_cpf(cpf_funcionario)

        if funcionario:
            self.__tela_funcionario.mostra_mensagem("**ALTERANDO DADOS DO FUNCIONARIO**")
            novos_dados_funcionario = self.__tela_funcionario.pega_dados_funcionario()
            try:
                if (self.pega_funcionario_por_cpf(novos_dados_funcionario["cpf"]) and
                    cpf_funcionario != novos_dados_funcionario["cpf"]):

                    raise CadastroRepetidoException(novos_dados_funcionario["cpf"], funcionario)
                else:
                    funcionario.nome = novos_dados_funcionario["nome"]
                    funcionario.cpf = novos_dados_funcionario["cpf"]
                    funcionario.cargo = novos_dados_funcionario["cargo"]
                    funcionario.data_admissao= novos_dados_funcionario["data_admissao"]
                    funcionario.salario = novos_dados_funcionario["salario"]
                    self.__tela_funcionario.mostra_mensagem("Dados alterados com sucesso")
            except CadastroRepetidoException as e:
                self.__tela_funcionario.mostra_mensagem(e)
        else:
            self.__tela_funcionario.mostra_mensagem("Funcionario não encontrado")

    def lista_funcionarios(self):
        
        if len(self.__funcionarios) > 0:
            for funcionario in self.__funcionarios:
                self.__tela_funcionario.mostra_funcionario({"nome": funcionario.nome,
                                                            "cpf": funcionario.cpf,
                                                            "cargo": funcionario.cargo,
                                                            "data_admissao": funcionario.data_admissao,
                                                            "salario": funcionario.salario})
            return True

        self.__tela_funcionario.mostra_mensagem("Não há funcionários cadastrados")
        return None

    def excluir_funcionario(self):
        lista = self.lista_funcionarios()
        if not lista:
            return False

        cpf_funcionario = self.__tela_funcionario.seleciona_funcionario()
        funcionario = self.pega_funcionario_por_cpf(cpf_funcionario)

        if isinstance(funcionario, Funcionario):
            self.__tela_funcionario.mostra_mensagem(f"Funcionário {funcionario.nome} removido com sucesso.")
            self.__funcionarios.remove(funcionario)
        else:
            self.__tela_funcionario.mostra_mensagem("Funcionário não encontrado")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_funcionario,
                        2: self.alterar_funcionario,
                        3: self.lista_funcionarios,
                        4: self.excluir_funcionario,
                        5: self.lista_funcionarios_por_cargo,
                        0: self.retornar}
        
        while True:
            opcao_escolhida = self.__tela_funcionario.tela_opcoes()
            self.__tela_funcionario.mostra_mensagem(f"Opção escolhida: {opcao_escolhida}")
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()