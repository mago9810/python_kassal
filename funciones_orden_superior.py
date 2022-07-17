# def saludo(func):
#     func()
# def hola():
#     print("hola!!!")

# def adios():
#     print("Adios!!!!")

# saludo(hola)
# saludo(adios)   

my_list = [1,4,5,6,9,13,19,21]
odd = list(filter(lambda x: x%2 != 0, my_list))     #filter recibe como parametros, una lambda y un lista o iterable,
print(odd)                                          # es decir recorre el iterable le aplica la lambda funtion y
                                                    # verifica que los elemtos de una secuenciacumplen con una condicion
                                                    # retornando un iterador con los elemetos que cumplen dicha condicion

#esto visto desde otro punto de vista
