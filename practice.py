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

# print(np.__version__)
# array = np.array([1, 2, 3])
# print(array)
# print(type(array))

# array = np.array('A')
# print(array.ndim)
# array = np.array([1,2,2])
# print(array.ndim)
# array = np.array([[1,2,3],[4,5,6]])
# print(array.ndim)
# array = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
# print(array.ndim)
# print(array.shape) # layers, rows, columns
# #slicing is the same as lists
# print(array[0]) # first layer


array = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12]])
#array[start:end:step]
# : this is the slicing operator
#arry(::-1) this will reverse the array
#print(array[:,1]) # select the second column 
#print(array[:,1:3]) # select the second to third column 
#print(array[:,1::2]) # select the second to last column with a step of 2 (1,3)
#print(array[0:2,0:2])
#select the first two rows and the first two columns


#scalar arithmetic
# array = np.array([1,2,3])
# print(array + 1) # add 1 to each element
# print(array - 1) # subtract 1 from each element
# print(array * 2) # multiply each element by 2
# print(array / 2) # divide each element by 2
# print(array ** 2) # square each element

#vectorized operations

#vector = asingle dimension

# array = np.array([1,2,3])
# print(np.sqrt(array)) # square root of each element
# print(np.exp(array)) # exponential of each element
# print(np.log(array)) # natural logarithm of each element
# print(np.sin(array)) # sine of each element
# print(np.cos(array)) # cosine of each element
# print(np.tan(array)) # tangent of each element
# print(np.sort(array)) # sort the array
# print(np.unique(array)) # unique elements in the array


# #exercise
# radii = np.array([1,2,3,4,5])

# print(np.pi * radii ** 2) # area of circles with given radii

#elementwise operations
# array1 = np.array([1,2,3])
# array2 = np.array([4,5,6])

# print(array1 + array2) # add two arrays elementwise
# print(array1 - array2) # subtract two arrays elementwise
# # same for multiplication and division and exponentiation


#comparison operators
# scores = np.array([90, 80, 70, 60, 50])
# print(scores > 75) # boolean array indicating which scores are greater than 75
# # same for <, >=, <=, ==, !=

#broadcasting
# virtually expanding dimensions to perform operations on arrays of different shapes
# the dimensions hvae to be compatible for broadcasting to work
# all same shape or one of the dimensions is 1

# array1 = np.array([[1,2,3,4]])
# array2 = np.array([[1],[2],[3],[4]])

# print(array1.shape)
# print(array2.shape)
# # dimension are not same but one of them is 1
# # if not we get valuse erroe
# print(array1* array2)
# # now 4 by 4

# #multiplication table
# array1 = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
# array2 = np.array([[1,2,3,4,5,6,7,8,9,10]])

# print(array1 * array2)

#aggregate functions
# array = np.array([[1,2,3,4,5],
#                  [6,7,8,9,10]])
# print(np.sum(array)) # sum of all elements
# print(np.mean(array)) # mean of all elements
# print(np.median(array)) # median of all elements
# print(np.std(array)) # standard deviation of all elements
# print(np.var(array)) # variance of all elements
# print(np.min(array)) # minimum of all elements
# print(np.max(array)) # maximum of all elements
# print(np.argmin(array)) # index of minimum element
# print(np.argmax(array)) # index of maximum element

# print(np.sum(array, axis=0)) # sum of each column
# print(np.sum(array, axis=1)) # sum of each row


# filtering
# refers to selecting elements from an array based on a condition
array = np.array([[1,2,3,4,5,6,7],
                  [8,9,10,11,12,13,14],
                  [15,16,17,18,19,20,21]])
# print(array[array > 4]) # select elements greater than 4 
# print(array[array % 2 == 0]) # select even elements
# print(array[array == 10]) # return an empty array since there are no elements equal to 10
# print(array[(array > 4) & (array % 2 == 1)]) 
# select elements greater than 4 and odd

#but to keep original shape we can use np.where

# print(np.where((array > 4) & (array % 2 == 1), array, 0))
#np.where(condition, x, y) returns an array with elements from x where condition is true and elements from y where condition is false   


# genetate random number

random_num_gen = np.random.default_rng() # create a random number generator
# print(random_num_gen.random()) # generate a random number between 0 and 1
# print(random_num_gen.integers(1, 10)) # generate a random integer between 1 and 10
# random_num_gen.integer(low,high,size)
# high is exclusive
# size: no of num to generate

# print(random_num_gen.integers(1, 10, size=5)) # generate 5 random integers between 1 and 10

#print(random_num_gen.integers(1, 10, size=(3,4))) # generate a 3 by 4 array of random integers between 1 and 10

#random_num_gen = np.random.default_rng(seed= 1)
# we always get the same result

# np.random.seed(1) # set the seed for reproducibility

# #uniform means uniform distriution#floationg point numbers between 0 and 1
# print(np.random.uniform(0, 1, size=(3,4))) # generate a 3 by 4 array of random numbers between 0 and 1

#shuffling array

rng = np.random.default_rng()
# array = np.array([1,2,3,4,5])
# rng.shuffle(array) # shuffle the array in place
# print(array)
# rps=["rock","paper","scissors"]
# # select = rng.choice(rps) # randomly select an element from the list]]
# # print(select)
# selects = rng.choice(rps, size=5) # randomly select 5 elements from the list
# print(selects)

emoji = ["😀","😂","😍","🤔","😎","😭","😡","👍"
         ,"👎","🙏"]
selects = rng.choice(emoji, size=(3,4)) # randomly select 5 elements from the list
print(selects)