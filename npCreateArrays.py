# Python library
# Usefull for arrays, math, stadistic, algebra lineal
# Its like a list but faster 
# ndarray
# locality of reference

import numpy as np

print(np.__version__)
# 0 - D Array
arr0d = np.array(32)
print(arr0d)
# 1 - D Arrays
arr1d = np.array([1,2,3,4,5])
arrTuple1d = np.array((1,2,3,4,5)) #same as arr
print(type(arrTuple1d))
print("array tuple 1d", arrTuple1d)
print(type(arr1d))
print("array 1d", arr1d)

#2 - D Arrays
array2d= np.array([[1,2,3],[4,5,6]])
print("array 2d", array2d)

# 3 - D Arrays
array3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9]]])
print("array 3d",array3d)

# Create array with the dimension especified NDMIN
arr5d = np.array([1,2,[3],3,6,7], ndmin=5)
print(arr5d)

#2 4 
print(arr1d[1:5:2])

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[0:8:2]) # 1 3 5 7
# ==
print (arr[::2]) # 1 3 5 7 usa el step para imprimir cada 2 valores, utilizando slicing

