import csv
import numpy as np
from Clases import Empleado
from Clases import Contratado
from Clases import Externo
from Clases import Planta
class ManejadorEmpleados:
    __cantidad = 0
    __dimension = 0
    __incremento = 5
    __empleados=None
    def __init__(self, dimension, incremento = 5):
        self.__empleados = np.empty(dimension, dtype=Empleado)
        self.__cantidad = 0
        self.__dimension = dimension  
    def agregarEmpleado(self, unEmpleado):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__empleados.resize(self.__dimension)     
        self.__empleados[self.__cantidad]=unEmpleado
        self.__cantidad += 1
    def getEmpleado(self, indice):
        return self.__empleados[indice]
    def cargarEmpleados(self): 
        archivo = open('contratados.csv', 'r')
        reader = csv.reader(archivo,delimiter=',')
        band = True
        for fila in reader:
            if band == True:
                band = False
            else: 
                emp = Contratado(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], int(fila[6]), float(fila[7]))
                self.agregarEmpleado(emp)
        archivo = open('externos.csv', 'r')
        reader = csv.reader(archivo,delimiter=',')
        band = True
        for fila in reader:
            if band == True:
                band = False
            else: 
                emp = Externo(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], float(fila[7]), float(fila[8]), float(fila[9]))
                self.agregarEmpleado(emp)
        archivo = open('planta.csv', 'r')
        reader = csv.reader(archivo,delimiter=',')
        band = True
        for fila in reader:
            if band == True:
                band = False
            else: 
                emp = Planta(fila[0], fila[1], fila[2], fila[3], float(fila[4]), int(fila[5]))
                self.agregarEmpleado(emp)
    def mostrarEmpleados(self):
        for i in range(self.__cantidad):
            print(self.__empleados[i])
    def registrarHoras(self, dni):
        incremento = int(input("Ingrese el incremento"))
        i = 0
        while i < (self.__cantidad) and self.__empleados[i].getDNI() != dni:
            i = i + 1
        if i < (self.__cantidad):
            self.__empleados[i].getIncremento(incremento)
    def totalTareas(self, tarea):
        for fila in self.__empleados:
            if isinstance(fila, Externo) and fila.getTarea() == tarea:
                if fila.comparaFecha() == True:
                    print(fila.getcostoObra())
    def ayudaEconomica(self):
        for fila in range(self.__cantidad):
            if self.__empleados[fila].getSueldo() < 150000:
                print("EMPLEADOS QUE RECIBIRAN LA  AYUDA ECONOMICA: DNI es: {}, Nombre es: {}, Direccion es: {}".format(self.__empleados[fila].getDNI(), self.__empleados[fila].getNombre(), self.__empleados[fila].getDireccion()))
    def calcularSueldo(self):
        for fila in range(self.__cantidad):
            print("El sueldo es: {} El nombre es: {} El telefono es: {}".format(self.__empleados[fila].getSueldo(), self.__empleados[fila].getNombre(), self.__empleados[fila].getTelefono()))