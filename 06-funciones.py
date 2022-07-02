# Calculo de areas

# Constante para almacenar PI
PI: float = 3.141592

# Area del cuadrado
def acuadrado():
    lado: float = float(input('\n¿Cual es el valor del lado? '))
    x: float = lado ** 2 # Multiplicación exponencial, multiplicarse por si mismo, X veces

    print('El area del cuadrado es {:.2f} unidades cuadradas'.format(x))

# Area del triangulo
def atriangulo():
    base: float = float(input('\n¿Cual es el valor de la base? '))
    altura: float = float(input('¿Cual es el valor de la altura? '))
    x: float = (base * altura) / 2

    print('El area del triangulo es {:.2f} unidades cuadradas'.format(x))

# Area del circulo
def acirculo():
    radio: float = float(input('\n¿Cual es el valor del radio? '))
    x: float = PI * (radio ** 2)

    print('El area del circulo es {:.2f} unidades cuadradas'.format(x))


repetir: bool = True

while repetir == True:
    area: int = int(input('Elige la figura geometrica para calcular su area:\nCuadrado = 1\nTriangulo = 2\nCirculo = 3\n'))

    if(area == 1):
        acuadrado()
    elif(area == 2):
        atriangulo()
    elif(area == 3):
        acirculo()
    else:
        print('Ingresa una opción valida')
    
    respuesta: str = input('\n¿Quieres calcular el area de otra figura? ').lower()

    # Si la respuesta es si
    if(respuesta == 'si' or respuesta == 'sí'):
        repetir = True
    else:
        repetir = False