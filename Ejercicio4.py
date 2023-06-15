from ManejadorEmpleados import ManejadorEmpleados
if __name__ == "__main__":
    empleados = ManejadorEmpleados(dimension = 20)
    empleados.cargarEmpleados()
    empleados.mostrarEmpleados()
    dni = input("Ingrese DNI de un contratado")
    empleados.registrarHoras(dni)
    tarea = input("ingrese la tarea de un externo")
    empleados.totalTareas(tarea)
    empleados.ayudaEconomica()
    empleados.calcularSueldo()