from tkinter import *

class Interfaz:
    def __init__(self, contenedor):
        self.textoE3 = StringVar()

        self.e1 = Label(contenedor, text = 'Convertir Celsius a Farenheit', fg = 'black')
        self.e2 = Label(contenedor, text = 'Celsius', fg = 'black')
        self.e3 = Label(contenedor, text = 'Fahrenheit', fg = 'black')
        self.e4 = Button(contenedor, text = 'Convertir', fg = 'black', command = self.__hacerConversion)
        self.e5 = Entry(contenedor, fg = 'black', bg = 'white')
        self.e6 = Label(contenedor, text = '', fg = 'black', textvariable = self.textoE3)

        self.e1.grid(column = 0, row = 0, columnspan = 2)
        self.e2.grid(column = 0, row = 1)
        self.e3.grid(column = 0, row = 2)
        self.e4.grid(column = 0, row = 3, columnspan = 2)
        self.e5.grid(column = 1, row = 1)
        self.e6.grid(column = 1, row = 2)

    def __hacerConversion(self):
        cel = float(self.e5.get())
        far = (cel * 1.8) + 32
        self.textoE3.set(far)

# Instancia TK (Ventana)
ventana = Tk()

# Agregar contenido a la ventana
miInterfaz = Interfaz(ventana)

# Ciclo infinito que permite al programa monitoriar las acciones en la ventana
ventana.mainloop()

