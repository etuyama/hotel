from hotel import Hotel
from cliente import Cliente
from funcionario import Funcionario
from servico import Servico
from realiza_servico import RealizaServico

hotel = Hotel("Panorama")
hotel.adicionar_quarto(600, 100, "Quarto luxo com vista para o mar, banheira de hidromassagem e cama de casal", "Luxo")

gean = Cliente("134", "Gean", 18, "123" , "Campeche")

funcionario1 = Funcionario("123", "Rodrigo", "faz tudo" , "27/09/2024", 900)
hotel.adicionar_funcionario(funcionario1)

massagem = Servico("massagem" , "massagem relaxante", 70)
hotel.adicionar_servico(massagem)

hotel.reservar_quarto(600, 5, gean, funcionario1)

massagemGean = RealizaServico(gean, funcionario1, massagem, hotel)

hotel.extender_estadia(gean, 5)

print(hotel.check_out(gean, funcionario1))
print(hotel.saldo)

hotel.pagar_funcionario(funcionario1)
print(hotel.saldo)