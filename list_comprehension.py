def run ():
    cua = []

    # for numero in range(0,101):
    #     if numero % 3 != 0:
    #         cua.append(numero**2)
    # print(cua)

    cuadrados = [numero**2 for numero in range (0,101) if numero % 3 != 0 ]
    print(cuadrados)

    # for numero in cuadrados:
    #     print(numero)

if __name__ == '__main__':
    
    run()

