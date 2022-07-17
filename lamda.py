def run ():
    palindromo = lambda string: string == string[::-1]  
    print(palindromo('ana'))

    area_triangulo = lambda base, altura: (base * altura)/2

    triangulo1 = area_triangulo(5,20)

    print(triangulo1)

    format_sueldo = lambda sueldo: "${}".format(sueldo)
    sueldo_diego = 15000
    print(format_sueldo(sueldo_diego))





if __name__ == '__main__':
    run()