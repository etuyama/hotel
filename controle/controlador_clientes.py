from entidade.cliente import Cliente
from limite.tela_cliente import TelaCliente
from exceptions.cadastro_repetido_exception import CadastroRepetidoException

class ControladorClientes:

    def __init__(self, controlador_sistema):
        self.__clientes = []
        self.__tela_cliente = TelaCliente()
        self.__controlador_sistema = controlador_sistema

    def pega_cliente_por_cpf(self, cpf: str):
        if isinstance(cpf, str):

            for cliente in self.__clientes:

                if cliente.cpf == cpf:
                    return cliente
            return None

    def incluir_cliente(self):
        dados_cliente = self.__tela_cliente.pega_dados_cliente()
        cpf = dados_cliente["cpf"]
        cliente = self.pega_cliente_por_cpf(cpf)
        try:
            if cliente is None:
                cliente = Cliente(
                    dados_cliente["cpf"],
                    dados_cliente["nome"],
                    dados_cliente["idade"],
                    dados_cliente["telefone"],
                    dados_cliente["endereco"]
                )

                self.__clientes.append(cliente)
                self.__tela_cliente.mostra_mensagem(
                    f"Cliente {cliente.nome} cadastrado com sucesso"
                )
            else:
                raise CadastroRepetidoException(cpf, cliente)
        except CadastroRepetidoException as e:
            self.__tela_cliente.mostra_mensagem(e)

    def alterar_cliente(self):
        lista = self.lista_clientes()
        if not lista:
            return False

        cpf_cliente = self.__tela_cliente.seleciona_cliente()
        cliente = self.pega_cliente_por_cpf(cpf_cliente)

        if cliente:
            self.__tela_cliente.mostra_mensagem(
                "**ALTERANDO DADOS DO CLIENTE**"
            )
            novos_dados_cliente = self.__tela_cliente.pega_dados_cliente()

            try:
                if (self.pega_cliente_por_cpf(novos_dados_cliente["cpf"]) and
                    cpf_cliente != novos_dados_cliente["cpf"]):

                    raise CadastroRepetidoException(cpf_cliente, cliente)
                else:
                    cliente.cpf = novos_dados_cliente["cpf"]
                    cliente.nome = novos_dados_cliente["nome"]
                    cliente.idade = novos_dados_cliente["idade"]
                    cliente.telefone = novos_dados_cliente["telefone"]
                    cliente.endereco = novos_dados_cliente["endereco"]
                    self.__tela_cliente.mostra_mensagem("Dados alterados com sucesso")
            except CadastroRepetidoException as e:
                self.__tela_cliente.mostra_mensagem(e)
        else:
            self.__tela_cliente.mostra_mensagem("Cliente não encontrado")

    def lista_clientes(self):

        if len(self.__clientes) > 0:
            for cliente in self.__clientes:
                self.__tela_cliente.mostra_cliente(
                    {"cpf": cliente.cpf,
                     "nome": cliente.nome,
                     "idade": cliente.idade,
                     "telefone": cliente.telefone,
                     "endereco": cliente.endereco}
                )
            return True

        self.__tela_cliente.mostra_mensagem("Lista de clientes vazia")
        return None

    def excluir_cliente(self):
        lista = self.lista_clientes()
        if not lista:
            return False

        cpf_cliente = self.__tela_cliente.seleciona_cliente()
        cliente = self.pega_cliente_por_cpf(cpf_cliente)

        if isinstance(cliente, Cliente):
            self.__tela_cliente.mostra_mensagem(
                f"Cliente {cliente.nome} com CPF {cliente.cpf}"
                f" removido com sucesso"
            )
            self.__clientes.remove(cliente)
        else:
            self.__tela_cliente.mostra_mensagem("Cliente não encontrado")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_cliente,
            2: self.alterar_cliente,
            3: self.lista_clientes,
            4: self.excluir_cliente,
            0: self.retornar
        }

        while True:
            lista_opcoes[self.__tela_cliente.tela_opcoes()]()