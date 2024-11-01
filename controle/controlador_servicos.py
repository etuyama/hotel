from entidade.servico import Servico
from exceptions.servico_id_exception import ServicoIdException
from exceptions.servico_nome_exception import ServicoNomeException
from limite.tela_servico import TelaServico


class ControladorServicos:

    def __init__(self, controlador_sistema):
        self.__servicos = []
        self.__tela_servico = TelaServico()
        self.__controlador_sistema = controlador_sistema

    def pega_servico_por_nome(self, nome):
        if isinstance(nome, str):
            for servico in self.__servicos:
                if servico.nome == nome:
                    return servico
            return False

    def pega_servico_por_id(self, id):
        if isinstance(id, int):
            for servico in self.__servicos:
                if servico.id == id:
                    return servico
            return False

    def incluir_servico(self):
        dados_servico = self.__tela_servico.pega_dados_servico()
        id = dados_servico["id"]
        nome = dados_servico["nome"]
        try:
            if self.pega_servico_por_id(id):
                raise ServicoIdException(id)
            elif self.pega_servico_por_nome(nome):
                raise ServicoNomeException(nome)

            servico = Servico(dados_servico["nome"],
                              dados_servico["descricao"],
                              dados_servico["preco"],
                              dados_servico["id"])

            self.__servicos.append(servico)
            self.__tela_servico.mostra_mensagem(
                f"Serviço {servico.nome} cadastrado com sucesso!"
                )

        except ServicoIdException as e:
            print(e)
        except ServicoNomeException as x:
            print(x)

    def alterar_servico(self):
        lista = self.lista_servicos()
        if not lista:
            return False

        id_servico = self.__tela_servico.seleciona_servico()
        servico = self.pega_servico_por_id(id_servico)

        if servico:
            self.__tela_servico.mostra_mensagem(
                "**ALTERANDO DADOS DO SERVIÇO**"
            )
            novos_dados_servico = self.__tela_servico.pega_dados_servico()
            id = novos_dados_servico["id"]
            nome = novos_dados_servico["nome"]

            try:
                if self.pega_servico_por_id(id) and id != id_servico:
                    raise ServicoIdException(id)
                if self.pega_servico_por_nome(nome) and nome != servico.nome:
                    raise ServicoNomeException(nome)

                servico.id = novos_dados_servico["id"]
                servico.nome = novos_dados_servico["nome"]
                servico.descricao = novos_dados_servico["descricao"]
                servico.preco = novos_dados_servico["preco"]

                self.__tela_servico.mostra_mensagem(
                    "Dados alterados com sucesso"
                )
            except ServicoIdException as e:
                print(e)
            except ServicoNomeException as x:
                print(x)

        else:
            self.__tela_servico.mostra_mensagem("Serviço não encontrado")

    def lista_servicos(self):

        if len(self.__servicos) > 0:
            self.__tela_servico.mostra_mensagem("\n**LISTANDO SERVIÇOS**\n")  #NÃO tem essa mensagem nos outros controladores,da pra apagar aqui ou mudar nos outros
            for servico in self.__servicos:
                self.__tela_servico.mostra_servico(
                    {
                    "nome": servico.nome,
                    "id": servico.id,
                    "descricao": servico.descricao,
                    "preco": servico.preco
                     }
                )
            return True

        self.__tela_servico.mostra_mensagem("Lista de serviços vazia.")
        return None

    def excluir_servico(self):
        lista = self.lista_servicos()
        if not lista:
            return False

        id_servico = self.__tela_servico.seleciona_servico()
        servico = self.pega_servico_por_id(id_servico)

        if isinstance(servico, Servico):
            self.__tela_servico.mostra_mensagem(
                f"Serviço {servico.nome} com ID {servico.id}"
                f" removido com sucesso"
            )
            self.__servicos.remove(servico)
        else:
            self.__tela_servico.mostra_mensagem("Serviço não encontrado")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_servico,
            2: self.alterar_servico,
            3: self.lista_servicos,
            4: self.excluir_servico,
            0: self.retornar
        }

        while True:
            opcao_escolhida = self.__tela_servico.tela_opcoes()
            print("Opção escolhida: ", opcao_escolhida)
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()