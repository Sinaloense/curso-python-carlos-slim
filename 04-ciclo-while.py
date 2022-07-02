# Tabla del 7 usando while

# Variable para almacenar multiplicador actual
i: int = 1

while i <= 10:
    tabla: int = 7 * i
    print('7 x {} = {}'.format(i, tabla))
    i += 1