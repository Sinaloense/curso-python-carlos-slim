def escritura(datoa, datob, datoc):
    f = open('08-archivos\\datos.txt', 'w')
    f.write(datoa)
    f.write(datob)
    f.write(datoc)
    print('Escritura')
    f.close()

escritura('Hola', 'Mundo', 'Bonito')

def lectura():
    f = open('08-archivos\\datos.txt', 'r')
    print(f.read())
    f.close()

lectura()