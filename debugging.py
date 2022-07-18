def divisors(num):
  divisors = [i for i in range(1, num+1) if num % i == 0]
  return divisors

def run():
    while True:
        try: 
            
            num = int(input("Inserta un número: "))
            if num < 0:
                raise TypeError("No se permiten numeros negativos")
            print(divisors(num))
            print("Terminó el programa")
            break
        except ValueError:
            print("Debes ingresar un numero, intentalo de nuevo")
        except TypeError:
            print("Debes ingresar un nuemero positivo, intentalo de nuevo")

        


if __name__ == '__main__':
  run()