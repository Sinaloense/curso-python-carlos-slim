# Variable para almacenar respuesta de input
respuesta = input('Trabajas desde casa? ')

# Si la respuesta es si
if respuesta.lower() == 'si':
    print('Eres afortunado')
else:
    print('Trabajas fuera de casa')

    # Variable para almacenar respuesta de input
    tiempo = int(input('¿Cuantos minutos haces al trabajo? '))

    if tiempo <= 0:
        print('Trabajas desde casa')
    elif tiempo <= 20:
        print('Es poco tiempo')
    elif tiempo >= 21 and tiempo <= 45:
        print('Es un tiempo razonable');
    else:
        print('Busca otras rutas')