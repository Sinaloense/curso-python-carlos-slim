x = 9
y = 0

try:
    z = x / y
except ZeroDivisionError:
    print('No se permite la division entre cero')
except ValueError:
    print('Algun valor es erroneo')
except:
    print('No se realizo la operacion')
else:
    print('La operacion se realizo')