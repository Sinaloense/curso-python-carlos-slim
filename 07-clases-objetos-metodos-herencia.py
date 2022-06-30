from abc import ABC, abstractmethod

class Persona(ABC):
     def __init__(self, edad, nombre):
          self.edad = edad
          self.nombre = nombre
          print('Se ha creado a ' + self.nombre + " de " + str(self.edad))
     
     # El * es para indicar que recibira una tupla
     # @abstractmethod es para hacer la clase abstracta
     @abstractmethod
     def hablar(self, *palabras):
          pass

     # El ** es para indicar que recibira un diccionario
     def hablar2(self, **palabras):
          for frase in palabras:
               print(self.nombre + ': ' + palabras[frase])

# Deportista hereda de Persona
class Deportista(Persona):
     def __init__(self, edad, nombre, deporte):
          self.edad = edad
          self.nombre = nombre
          self.__deporte = deporte
          print('Se ha creado a ' + self.nombre + " de " + str(self.edad))

     def getDeporte(self):
          return self.__deporte

     def practicarDeporte(self):
          print(self.nombre + ': voy a practicar')
     
     def hablar(self, *palabras):
          for frase in palabras:
               print(self.nombre + ': ' + frase)
     
     
# Esto es para crear una clase virtual o subclsae de persona, pero no lo entiendo bien
#Persona.register(Deportista)

""" juan = Persona(18, 'Juan')
juan.hablar('Hola, estoy hablando', 'Este soy yo')
juan.hablar2(t1 = 'Hola, estoy hablando', t2 = 'Este soy yo') """

luis = Deportista(20, 'Luis', 'Natación')
luis.hablar('Hola estoy hablado', 'Este soy yo')
luis.hablar2(t1 = 'Hola, estoy hablando', t2 = 'Este soy yo')
luis.practicarDeporte()
print('Luis practica: ' + luis.getDeporte())