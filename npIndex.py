import numpy as np
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

#accede al elemento con index 1,2 y 3 del array con index 1, es decir, el segundo
print(arr[1, 1:4]) # 7 8 9

print(arr[0,0:-1]) # 1 2 3 4

print(arr[0:2,2]) # 3 y 8, agarra de ambos arrays, el index 2

print(arr[0:2,2:4]) # crea un array con 2 arrays, 3 4 del primer array y 8 9 del segundo

#Complex
a = 1.0 + 2.0j
print(type(a))