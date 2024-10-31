class TelefoneInvalidoException(Exception):
    def __init__(self):
        self.mensagem = (
            "Telefone inválido. Exemplo de formato válido: 048123456789"
        )
        super().__init__(self.mensagem)