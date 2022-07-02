# Variable para almacenar respuesta de input
libros: int = int(input('¿Cuantos libros lees anualmente? '))

# Si lee 15 o más libros
if libros >= 15:
    print('Eres un buen lector')
else:
    print('Necesitas leer mas')