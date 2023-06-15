from datetime import datetime
class Empleado:
    __dni: int
    __nombre: str
    __direccion: str
    __telefono: str
    def __init__(self, dni, nombre, direccion, telefono):
        self.__dni = dni
        self.__nombre =  nombre
        self.__direccion = direccion
        self.__telefono =  telefono
    def getDNI(self):
        return self.__dni
    def getNombre(self):
        return self.__nombre
    def getDireccion(self):
        return self.__direccion
    def getTelefono(self):
        return self.__telefono
    def __str__(self):
        return "DNI: {} \n Nombre: {} \n Direccion: {} \n Telefono: {}".format(self.__dni, self.__nombre, self.__direccion, self.__telefono)

class Externo(Empleado):
    __tarea: str
    __fInicio: str
    __fFinalizacion: str
    __montoViatico: float
    __costoObra: float
    __seguroVida: float
    def __init__(self, dni, nombre, direccion, telefono, tarea, fInicio, fFinalizacion, montoViatico, costoObra, seguroVida):
        super().__init__(dni, nombre, direccion, telefono)
        self.__tarea = tarea
        self.__fInicio =  fInicio
        self.__fFinalizacion = fFinalizacion
        self.__montoViatico =  montoViatico
        self.__costoObra = costoObra
        self.__seguroVida =  seguroVida
    def getSueldo(self):
        return self.__costoObra - self.__montoViatico - self.__seguroVida
    def getTarea(self):
        return self.__tarea
    def getFInicio(self):
        return self.__fInicio
    def getFFinalizacion(self):
        return self.__fFinalizacion
    def getmontoViatico(self):
        return self.__montoViatico
    def getcostoObra(self):
        return self.__costoObra
    def getseguroVida(self):
        return self.__seguroVida
    def getIncremento(self):
        print("Clase externo no tiene incremento")
    def comparaFecha(self):
        var = False
        now = datetime.now().date()
        fecha_finalizacion = datetime.strptime(self.__fFinalizacion, "%d/%m/%Y").date()
        if fecha_finalizacion >= now:
            var = True
        return (var)
    def __str__(self):
        r =  super().__str__()
        return "{}  \n tarea: {} fecha de inicio: {} \n fecha de finalizacion: {} \n viatico: {} costo de obra: {} seguro vida {}".format(r, self.__tarea, self.__fInicio, self.__fFinalizacion, self.__montoViatico, self.__costoObra, self.__seguroVida)

class Contratado(Empleado):
    __fechaInicio: str
    __fechaFinalizacion: str
    __cantidadHoras: int
    __valorHora: float
    def __init__(self, dni, nombre, direccion, telefono, fechaInicio, fechaFinalizacion, cantidadHoras, valorHora):
        super().__init__(dni, nombre, direccion, telefono)
        self.__fechaInicio = fechaInicio
        self.__fechaFinalizacion =  fechaFinalizacion
        self.__cantidadHoras = cantidadHoras
        self.__valorHora = valorHora
    def getSueldo(self):
        return self.__cantidadHoras * self.__valorHora
    def getfechaInicio(self):
        return self.__fechaInicio
    def getFechaFinalizacion(self):
        return self.__fechaFinalizacion
    def getCantidadHoras(self):
        return self.__cantidadHoras
    def getValorHora(self):
        return self.__valorHora
    def getIncremento(self, incremento):
        self.__cantidadHoras += incremento
        print(self.__cantidadHoras)
    def __str__(self):
        r =  super().__str__()
        return "{}  \n fecha de inicio: {} \n fecha de finalizacion: {} \n cantidad de horas: {} valor de hora: {}".format(r, self.__fechaInicio, self.__fechaFinalizacion, self.__cantidadHoras, self.__valorHora)
    
class Planta(Empleado):
    __sueldoBasico: float
    __antiguedad:int
    def __init__(self, dni, nombre, direccion, telefono, sueldoBasico, antiguedad):
        super().__init__(dni, nombre, direccion, telefono)
        self.__sueldoBasico = sueldoBasico
        self.__antiguedad =  antiguedad
    def getSueldo(self):
        return ((self.__sueldoBasico) + ((self.__sueldoBasico * 1 / 100) * (self.__antiguedad)))
    def getsueldoBasico(self):
        return self.__sueldoBasico
    def getAntiguedad(self):
        return self.__antiguedad
    def getIncremento(self):
        print("Clase Planta no tiene incremento")
    def __str__(self):
        r =  super().__str__()
        return "{} \n sueldo basico: {} \n Antiguedad: {}".format(r, self.__sueldoBasico, self.__antiguedad)