#Valor absoluto (mismo numero sin importar su signo, para distancia x ejemplo)
#ABS
print (abs(-3) == abs(3))

#ALL -> returns true if all are true / ANY, returns true if any(alguno) is true
lista = [1,2,"s"]
print(all(lista))

#DIR -> devuelve propiedades y metodos del objeto
dir("string")

#ENUMERATE -> takes a colection (tuple, list) and returns a list/tuples of tuples with the index and the value. Como lo transforma en un objeto, hay que parchearlo
lista = [1,2,3]
a = enumerate(lista)
print(tuple(a)) # o list(a)

#MAX -> returns the largest item, number an string
lista = [1,2,3]
listaStrings = ["a","b","c"]
print(max(lista))
print(max(listaStrings))

#MAP -> use a colection and a function to aply it to each item, al igua que enumerate, esto crea una map object, debe ser parcheado
lista = [1,2,3]
def funcion(x):
    return x*2

x = map(funcion,lista) #devuelve 2,4,6
print(list(x))
#lambda
x=map(lambda x:x*2,lista) #devuelve 2,4,6
print(tuple(x))

#ZIP -> similar as ENUMERATE but using 2 colections and returns a list/tuples of tuples with the items from both colections in order
#For example
lista1 = [1,2,3]
lista2 = ['juan','pedro','jose']
x = zip(lista1, lista2)
print(tuple(x)) #1 juan, 2 pedro, 3 jose

