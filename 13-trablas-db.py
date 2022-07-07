import os
import sqlite3

# Si no existe la carpeta, la crea
if not os.path.exists('db'):
    os.mkdir('db')

conexion = sqlite3.connect('db/novelas.db')
consulta = conexion.cursor()
tabla = 'CREATE TABLE tabla('\
    'id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,'\
    'nombre VARCHAR(30) NOT NULL,'\
    'autor VARCHAR(40) NOT NULL,'\
    'year INTEGER(9) NOT NULL);'

print(tabla)

if(consulta.execute(tabla)):
    print('la tabla fue creada')
else:
    print('la tabla no fue creada')

# Cerrar consulta
consulta.close()

# Guardar cambios
conexion.commit()

# Cerrar conexión
conexion.close()