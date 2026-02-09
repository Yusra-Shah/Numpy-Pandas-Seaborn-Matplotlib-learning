# numpy = numerical python
import numpy as np

# numpy arrays are faster than lists
# they are also more efficient in terms of memory
# they are also more convenient to use
# we can create numpy arrays from lists
# we can perform vectorized operations on numpy arrays
# [1,2,3] *2 = [2,4,6]
#norammlly list just duplicates
# [1,2,3] *2 = [1,2,3,1,2,3]
# we can also perform matrix operations on numpy arrays

print(np.__version__)
array = np.array([1, 2, 3])
print(array)
print(type(array))

array = np.array('A')
print(array.ndim)
array = np.array([1,2,2])
print(array.ndim)
array = np.array([[1,2,3],[4,5,6]])
print(array.ndim)
array = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(array.ndim)
print(array.shape) # layers, rows, columns
#slicing is the same as lists
print(array[0]) # first layer
