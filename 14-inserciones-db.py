import sqlite3

def insertar():
    print('\nEstas en la función insertar')

    # Obtener datos
    nombre1 = input('Escribe el titulo de la novela: ')
    autor1 = input('\nEscribe el autor de la novela: ')
    year1 = str(input('\nDigita el año de la novela: '))

    # Conectarse a la base de datos
    db1 = sqlite3.connect('db/novelas.db')

    # Abrir conexion a la base de datos
    consulta = db1.cursor()

    # Consulta
    strConsulta = 'INSERT INTO tabla(nombre, autor, year) '\
        'VALUES("' + nombre1 + '", "' + autor1 + '", "' + year1 + '")'
    print('\n' + strConsulta)

    # Ejecutar consulta
    consulta.execute(strConsulta)

    # Cerrar consulta
    consulta.close()

    # Guardar cambios
    db1.commit()
    
    # Cerrar conexión
    db1.close()

def consultar():
    print('\nEstas en la función consultar')

    # Conectarse a la base de datos
    db2 = sqlite3.connect('db/novelas.db')

    # Preparar consulta
    db2.row_factory = sqlite3.Row

    # Abrir conexion a la base de datos
    consulta = db2.cursor()

    # Ejecutar consulta
    consulta.execute('SELECT * FROM tabla')

    # Almacenar resultado de la consulta
    filas = consulta.fetchall()

    # Variable para almacenar resultados de la consulta
    lista = []

    # Ciclo para recorrer las filas
    for fila in filas:
        s = {}
        s['nombre'] = fila['nombre']
        s['autor'] = fila['autor']
        s['year'] = str(fila['year'])
        lista.append(s)
    
    # Cerrar consulta
    consulta.close()

    # Cerrar conexión
    db2.close()

    return(lista)

def menu():
    opcion = int(input('\nIngresa la opción deseada:\n'\
        '1.Insertar un valor en la tabla\n'\
        '2.Consultar los valores de la tabla\n'))
    
    if opcion == 1:
        insertar()
        menu()
    elif opcion == 2:
        listaNovelas = consultar()

        for novela in listaNovelas:
            print(novela['nombre'], novela['autor'], novela['year'])
            
        menu()

menu()