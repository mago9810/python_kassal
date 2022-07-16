
class Vehiculo ():   #crear la clase
    
    def __init__(self,marca,modelo) -> None:  #constructor
        self.marca = marca
        self.modelo = modelo  #caracteristicas
        # self.emnarcha = False  
        # self.acelera = False   #comportamientos 
        # self.frena = False

    def arrancar (self):   #Definicion de los metodos
        print(f"{self.marca} {self.modelo} Encendido ")
        # self.emnarcha = True
    
    def acelerar (self):
        aceleracion = int(input(f"Hasta que velocidad quiere acelerar?"))
        print(" _ " * aceleracion)
        # self.acelera = True





def main ():
    carro_1 = Vehiculo("mazda" ,  "cx-5")
    carro_2 = Vehiculo("Ford", "Mustang")
    carro_2.arrancar()
    carro_2.acelerar()

main()