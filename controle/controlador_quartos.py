from entidade.quarto_luxo import QuartoLuxo
from entidade.quarto_standard import QuartoStandard
from entidade.quarto_suite import QuartoSuite
from entidade.quarto import Quarto
from exceptions.quarto_ja_cadastrado_exception import QuartoJaCadastradoException
from limite.tela_quarto import TelaQuarto


class ControladorQuartos():

    def __init__(self, controlador_sistema):
        self.__quartos = []
        self.__tela_quarto = TelaQuarto()
        self.__controlador_sistema = controlador_sistema

    def pega_quarto_por_numero(self, numero: int):

        if isinstance(numero, int):

            for quarto in self.__quartos:

                if quarto.numero == numero:
                    return quarto
            return None

    def incluir_quarto(self):
        dados_quarto = self.__tela_quarto.pega_dados_quarto()
        quarto = self.pega_quarto_por_numero(dados_quarto["numero"])
        try:
            if quarto:
                raise QuartoJaCadastradoException(dados_quarto["numero"])

            if dados_quarto["tipo"] == 1:
                quarto = QuartoStandard(dados_quarto["numero"], dados_quarto["valor_diaria"],
                                        dados_quarto["descricao"])
                self.__quartos.append(quarto)
                self.__tela_quarto.mostra_mensagem(f"Quarto Standard número {dados_quarto["numero"]} adicionado com sucesso")
                return quarto

            if dados_quarto["tipo"] == 2:
                quarto = QuartoSuite(dados_quarto["numero"], dados_quarto["valor_diaria"],
                                        dados_quarto["descricao"])
                self.__quartos.append(quarto)
                self.__tela_quarto.mostra_mensagem(f"Quarto Suíte número {dados_quarto["numero"]} adicionado com sucesso")
                return quarto

            if dados_quarto["tipo"] == 3:
                quarto = QuartoLuxo(dados_quarto["numero"], dados_quarto["valor_diaria"],
                                        dados_quarto["descricao"])
                self.__quartos.append(quarto)
                self.__tela_quarto.mostra_mensagem(f"Quarto Luxo número {dados_quarto["numero"]} adicionado com sucesso")
                return quarto
        except QuartoJaCadastradoException as e:
            self.__tela_quarto.mostra_mensagem(e)

    def alterar_quarto(self):
        lista = self.lista_quartos()
        if not lista:
            return False
        numero_quarto = self.__tela_quarto.seleciona_quarto()
        quarto = self.pega_quarto_por_numero(numero_quarto)

        if quarto:
            self.__tela_quarto.mostra_mensagem("**ALTERANDO DADOS DO QUARTO")
            novos_dados_quarto = self.__tela_quarto.pega_dados_alteracao_quarto()
            try:

                #Verifica se está inserindo número de algum outro quarto já existente
                if (self.pega_quarto_por_numero(novos_dados_quarto["numero"]) and
                    quarto.numero != novos_dados_quarto["numero"]):
                    raise QuartoJaCadastradoException(novos_dados_quarto["numero"])

                quarto.numero = novos_dados_quarto["numero"]
                quarto.valor_diaria = novos_dados_quarto["valor_diaria"]
                quarto.descricao = novos_dados_quarto["descricao"]
                quarto.status = novos_dados_quarto["status"]

                self.__tela_quarto.mostra_mensagem("Dados alterados com sucesso")
            except QuartoJaCadastradoException as e:
                self.__tela_quarto.mostra_mensagem(e)
        else:
            self.__tela_quarto.mostra_mensagem("Quarto não encontrado")  #RAISE QNAOENCONTRADO

    def lista_quartos(self):

        if len(self.__quartos) > 0:
            for quarto in self.__quartos:
                self.__tela_quarto.mostra_quarto({"numero": quarto.numero,
                                                  "valor_diaria": quarto.valor_diaria,
                                                  "descricao": quarto.descricao,
                                                  "tipo": quarto.tipo,
                                                  "status": quarto.status})
            return True

        self.__tela_quarto.mostra_mensagem("Lista de quartos vazia")
        return None

    def excluir_quarto(self):
        lista = self.lista_quartos()
        if not lista:
            return False

        numero_quarto = self.__tela_quarto.seleciona_quarto()
        quarto = self.pega_quarto_por_numero(numero_quarto)

        if isinstance(quarto, Quarto):
            self.__quartos.remove(quarto)
            self.__tela_quarto.mostra_mensagem(f"Quarto número {quarto.numero} removido com sucesso")
        else:
            self.__tela_quarto.mostra_mensagem("Quarto não encontrado") #RAISE QNAOENCONTRADO

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_quarto, 2: self.alterar_quarto, 3: self.lista_quartos,
                        4: self.excluir_quarto, 0: self.retornar}

        while True:
            opcao_escolhida = self.__tela_quarto.tela_opcoes()
            print("Opção escolhida: ", opcao_escolhida)
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
  

