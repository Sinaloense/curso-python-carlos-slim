# Calculo de areas

PI = 3.141592

# Area del cuadrado
def acuadrado():
    lado = int(input('\n¿Cual es el valor del lado? '))
    x = lado**2
    print('El area del cuadrado es ' + str(x) + ' unidades cuadradas')

# Area del triangulo
def atriangulo():
    base = int(input('\n¿Cual es el valor de la base? '))
    altura = int(input('¿Cual es el valor de la altura? '))
    x = (base * altura) / 2

    print('El area del triangulo es ' + str(x) + ' unidades cuadradas')

# Area del circulo
def acirculo():
    radio = int(input('\n¿Cual es el valor del radio? '))
    x = (PI * radio) ** 2

    print('El area del circulo es ' + str(x) + ' unidades cuadradas')


repetir = True

while repetir == True:
    area = int(input('Elige la figura geometrica para calcular su area:\nCuadrado = 1\nTriangulo = 2\nCirculo = 3\n'))

    if(area == 1):
        acuadrado()
    elif(area == 2):
        atriangulo()
    elif(area == 3):
        acirculo()
    else:
        print('Ingresa una opciòn valida')
    
    respuesta = input('\n¿Quieres calcular el area de otra figura? ')

    if(respuesta.lower() == 'si'):
        repetir = True
    else:
        repetir = False