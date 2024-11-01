from limite.tela_hotel import TelaHotel
from entidade.hotel import Hotel
from controle.controlador_reservas import ControladorReservas #TIRAR ISSO

class ControladorHotel:

    def __init__(self, controlador_sistema, controlador_reservas: ControladorReservas, controlador_funcionarios):
        self.__tela_hotel = TelaHotel()
        self.__controlador_sistema = controlador_sistema
        self.__controlador_reservas = controlador_reservas
        self.__controlador_funcionarios = controlador_funcionarios
        self.__hotel = Hotel()

    def efetuar_checkout(self):
        self.__controlador_reservas.lista_reservas()
        id_reserva = self.__tela_hotel.seleciona_reserva()
        reserva = self.__controlador_reservas.pega_reserva_por_id(id_reserva)

        if reserva:

            if reserva.situacao: #USAR A FUNCAO VERIFICA RESERVA
                pass

            valor_reserva = reserva.valor_total
            self.__hotel.saldo = self.__hotel.saldo + valor_reserva

            reserva.quarto.status = "Manutenção"
            self.__tela_hotel.mostra_mensagem(
                f"Check-out da reserva do cliente: 
                {reserva.cliente.nome}(CPF:{reserva.cliente.cpf}) 
                no quarto {reserva.quarto.numero} realizado com sucesso"
                )

            self.__tela_hotel.mostra_mensagem(f"Valor total da reserva: {reserva.valor_total}")
        else:
            self.__tela_hotel.mostra_mensagem("Reserva não encontrada")
