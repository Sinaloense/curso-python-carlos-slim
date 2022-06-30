import sqlite3

def insertar():
    db1 = sqlite3.connect('novelas.db')
    print('\nEstas en la función insertar')

    nombre1 = input('Escribe el titulo de la novela: ')
    autor1 = input('\nEscribe el autor de la novela: ')
    year1 = str(input('\nDigita el año de la novela: '))

    consulta = db1.cursor()

    strConsulta = 'INSERT INTO tabla(nombre, autor, year) '\
        'VALUES("' + nombre1 + '", "' + autor1 + '", "' + year1 + '")'
    print('\n' + strConsulta)

    consulta.execute(strConsulta)
    consulta.close()
    db1.commit()
    db1.close()

def consultar():
    db2 = sqlite3.connect('novelas.db')
    print('\nEstas en la función consultar')

    db2.row_factory = sqlite3.Row
    consulta = db2.cursor()
    consulta.execute('SELECT * FROM tabla')

    filas = consulta.fetchall()
    lista = []

    for fila in filas:
        s = {}
        s['nombre'] = fila['nombre']
        s['autor'] = fila['autor']
        s['year'] = str(fila['year'])
        lista.append(s)
    
    consulta.close()
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