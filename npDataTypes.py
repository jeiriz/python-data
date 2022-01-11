import numpy as np

""" 
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
"""

arr = np.array([1,2,3,4,5])
print(arr.dtype) #int 32

arr = np.array(["2","4"])
print(arr.dtype) # <U1 unicode

arr = np.array([2,"s"])
print(arr.dtype) # <U11

arr = np.array([2,"s"],ndmin=3)
print(arr)
print(arr.dtype) # <U11
print(arr.ndim) # 3

#dtype para crear tipo de dato
arr = np.array([2,"s"], dtype='S')
print(arr.dtype)

# para INTS se puede especificar el tamaño
arr = np.array([1,2,3],dtype='i4',ndmin=4)
print(arr, arr.dtype, arr.ndim)
