def divisors(num):
  divisors = [i for i in range(1, num+1) if num % i == 0]
  return divisors

def run():
    while True:
        try:
            num = input("Inserta un número: ")
            assert num.isnumeric(), "Debes ingresar un numero"
            print(divisors(num))
            print("Terminó el programa")
            break
        except AssertionError:
            print("incerte un nuiemro. Intentelo de nuevo")


if __name__ == '__main__':
  run()