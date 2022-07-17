from functools import reduce
#filter

my_list = [1,4,5,6,9,13,19,21]
odd = list(filter(lambda x: x%2 != 0, my_list))     
print(odd)        


#map

my_list = [1,2,3,4,5]
square = list(map(lambda x: x**2, my_list))

print(square)



#reduce
my_list = [2,3,2,3,2]
all_multiplied = reduce(lambda a,b: a*b , my_list)

print(all_multiplied)



numeros=[2,1,4,3,5]
#resultado=reduce(suma,numeros)
resultado=reduce(lambda a,b: a if a > b else b,numeros)
print (resultado)


s =('h','o','l','a','-','m','u','n','d','o')

def concatenar(a,b):
    return a+b
sr = reduce(concatenar,s)

print(type(sr))
print(sr)
