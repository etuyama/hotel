from entidade.quarto_luxo import QuartoLuxo
from entidade.quarto_standard import QuartoStandard
from entidade.quarto_suite import QuartoSuite
from entidade.quarto import Quarto
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
        if isinstance( self.pega_quarto_por_numero(dados_quarto["numero"]) , Quarto):
            self.__tela_quarto.mostra_mensagem("Esse quarto já está cadastrado")
            return False

        if dados_quarto["tipo"] == 1:
            quarto = QuartoStandard(dados_quarto["numero"], dados_quarto["valor_diaria"],
                                    dados_quarto["descricao"])
            self.__quartos.append(quarto)
            self.__tela_quarto.mostra_mensagem(f"Quarto Standard número: {dados_quarto["numero"]} adicionado com sucesso")
            return quarto

        if dados_quarto["tipo"] == 2:
            quarto = QuartoSuite(dados_quarto["numero"], dados_quarto["valor_diaria"],
                                    dados_quarto["descricao"])
            self.__quartos.append(quarto)
            self.__tela_quarto.mostra_mensagem(f"Quarto Suíte número: {dados_quarto["numero"]} adicionado com sucesso")
            return quarto

        if dados_quarto["tipo"] == 3:
            quarto = QuartoLuxo(dados_quarto["numero"], dados_quarto["valor_diaria"],
                                    dados_quarto["descricao"])
            self.__quartos.append(quarto)
            self.__tela_quarto.mostra_mensagem(f"Quarto Luxo número: {dados_quarto["numero"]} adicionado com sucesso")
            return quarto

    def alterar_quarto(self):
        lista = self.lista_quartos()
        if not lista:
            return False
        numero_quarto = self.__tela_quarto.seleciona_quarto()
        quarto = self.pega_quarto_por_numero(numero_quarto)

        if isinstance(quarto, Quarto):
            self.__tela_quarto.mostra_mensagem("**ALTERANDO DADOS DO QUARTO")
            novos_dados_quarto = self.__tela_quarto.pega_dados_alteracao_quarto(quarto)
            quarto.numero = novos_dados_quarto["numero"]
            quarto.valor_diaria = novos_dados_quarto["valor_diaria"]
            quarto.descricao = novos_dados_quarto["descricao"]

            self.__tela_quarto.mostra_quarto({"numero": quarto.numero,
                                              "valor_diaria": quarto.valor_diaria,
                                              "descricao": quarto.descricao,
                                              "tipo": quarto.tipo})
        else:
            self.__tela_quarto.mostra_mensagem("Quarto não encontrado")

    def lista_quartos(self):

        if len(self.__quartos) > 0:
            for quarto in self.__quartos:
                self.__tela_quarto.mostra_quarto({"numero": quarto.numero,
                                           "valor_diaria": quarto.valor_diaria,
                                           "descricao": quarto.descricao,
                                           "tipo": quarto.tipo})
            return True
        else:
            self.__tela_quarto.mostra_mensagem("Lista vazia")
            return None

    def excluir_quarto(self):
        lista = self.lista_quartos()
        if not lista:
            return False
        numero_quarto = self.__tela_quarto.seleciona_quarto()
        quarto = self.pega_quarto_por_numero(numero_quarto)
        if isinstance(quarto, Quarto):
            self.__quartos.remove(quarto)
            self.__tela_quarto.mostra_mensagem(f"Quarto número: {quarto.numero} removido com sucesso")
        else:
            self.__tela_quarto.mostra_mensagem("Quarto não encontrado")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_quarto, 2: self.alterar_quarto, 3: self.lista_quartos,
                        4: self.excluir_quarto, 0: self.retornar}

        while True:
            lista_opcoes[self.__tela_quarto.tela_opcoes()]()
            

