def run ():
    cua = []

    # for numero in range(0,10001):
    #     if numero % 4 == 0 and numero % 6 == 0 and numero % 9 == 0 :
    #         cua.append(numero)
    # print(cua)

    comun_multiplo = [numero for numero in range(0,10001) if numero % 4 == 0 and numero % 6 == 0 and numero % 9 == 0]
    print(comun_multiplo)

    # cuadrados = [numero**2 for numero in range (0,101) if numero % 3 != 0 ]
    # print(cuadrados)

    # for numero in cuadrados:
    #     print(numero)

if __name__ == '__main__':
    
    run()
