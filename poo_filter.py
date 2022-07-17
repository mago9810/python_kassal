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

salarios_altos = filter(lambda empleado: empleado.salario > 15000, lista_empleados)

for empleado_salario in salarios_altos:
    print(empleado_salario)
    