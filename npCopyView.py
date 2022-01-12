import numpy as np

arr = np.array([0,1,2], dtype="i")

# Create a copy that doesnt change the original array
arrCopy = arr.copy()
arrCopy[0] = 3
print(arr[0])
print(arrCopy[0])

# If you create a view and change that or change the original, it changes the original|view too
arrView = arr.view()
arrView[0] = 1
arr[0]=3
print(arrView)
print(arr)