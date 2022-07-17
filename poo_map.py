
class empleado:
    def __init__(self, nombre, cargo, salario) -> None:
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self) -> str:
        return "{} que trabaja como {} tiene un salario de ${}".format(self.nombre, self.cargo, self.salario)

lista_empleados = [
    empleado("Diego", "Director", 75000),
    empleado("Paola", "Gerente", 95000),
    empleado("Jero", "Secretario", 15000),
    empleado("Cristo", "Asistente", 15000)
] 


def  calculo_comision(empleado):
    if empleado.salario <= 30000:
        empleado.salario = empleado.salario * 1.03
    
    return empleado

lista_comision = map(calculo_comision, lista_empleados)



for lista_comosion_empleado in lista_comision:
    print(lista_comosion_empleado)
    
