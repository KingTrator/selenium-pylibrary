from booking.booking import Booking

with Booking() as bot:
    bot.land_first_page()
    print('Exiting ...')


# Assim como aprendi com o with open(), usar o
# with aqui faz com que, após a linha de código dentro do with acabar
# o arquivo em questão seja fechado. Para efetivar isso,
# precisei pôr o método "with" dentro da class Booking()