###################################################################
###################################################################
#                 Data Manipulation with Numpy                    #
###################################################################
###################################################################

# Numpy as Numerical Python, NumPy arrays are like Python's built-in list type
# But, NumPy arrays provide much more efficient storage and data operations as the arrays grow larger in size. 

# Import Numpy

import numpy
numpy.__version__

# Setting alias of Numpy

import numpy as np

# To  display all the contents of the numpy namespace, you can type this:

# --> np.<TAB>

# To display NumPy's built-in documentation

# --> np?

####################
#    Python List   #
####################

# List 1

L = list(range(10))
print(L)
print(type(L))

# A object from the List

print(type(L[0]))

# List 2

L2 = [str(c) for c in L]
print(L2)
print(type(L2))
print(type(L2[0]))

# Because of Python's dynamic typing, we can even create heterogeneous lists:

L3 = [True, "2", 3.0, 4]
[type(item) for item in L3]


#####################################
#    Fixed-Type Arrays in Python    #
#####################################

# Python offers several different options for storing data in efficient, fixed-type data buffers. 
# The built-in array module (available since Python 3.3) can be used to create dense arrays of a uniform type:

import array
L = list(range(10))
A = array.array('i', L)
A

#  Much more useful, however, is the ndarray object of the NumPy package. While Python's array object provides efficient 
# storage of array-based data, NumPy adds to this efficient operations on that data. We will explore these operations in later sections; 
# here we'll demonstrate several ways of creating a NumPy array.

##########################################
#    Creating Arrays from Python Lists   #
##########################################

import numpy as np
np.array([1, 4, 2, 5, 3])

# Remember that unlike Python lists, NumPy is constrained to arrays that all contain the same type. If types do not match,
# NumPy will upcast if possible 

np.array([3.14, 4, 2, 3])

# If we want to explicitly set the data type of the resulting array, we can use the dtype keyword

np.array([1, 2, 3, 4], dtype='float32')

# NumPy arrays can explicitly be multi-dimensional; here's one way of initializing a multidimensional array using a list of lists:

# nested lists result in multi-dimensional arrays
np.array([range(i, i + 3) for i in [2, 4, 6]])

# The inner lists are treated as rows of the resulting two-dimensional array.

##########################################
#      Creating Arrays: fundamentals     #
##########################################

# Especially for larger arrays, it is more efficient to create arrays from scratch using routines built into NumPy. 
# Here are several examples:

# Create a length-10 integer array filled with zeros
np.zeros(10, dtype=int)

# Create a 3x5 floating-point array filled with ones
np.ones((3, 5), dtype=float)

# Create a 3x5 array filled with 3.14
np.full((3, 5), 3.14)

# Create an array of five values evenly spaced between 0 and 1
np.linspace(0, 1, 5)

# Create an array filled with a linear sequence
# Starting at 0, ending at 20, stepping by 2
# (this is similar to the built-in range() function)

np.arange(0, 20, 2)

# Create a 3x3 array of uniformly distributed
# random values between 0 and 1
np.random.random((3, 3))

# Create a 3x3 array of random integers in the interval [0, 10)
np.random.randint(0, 10, (3, 3))

# Create a 3x3 identity matrix
np.eye(3)

#  Standard Data Types in Numpy 

# NumPy arrays contain values of a single type, so it is important to have detailed knowledge of those types and their limitations. 
# Because NumPy is built in C, the types will be familiar to users of C, Fortran, and other related languages.
# The standard NumPy data types are listed in the following table. 

np.zeros(10, dtype=np.int16)

# bool_
# int_
# intp
# int8
# int64
# uint16
# uint64
# float_
# float16
# float32
# float64
# complex_
# complex64
#  complex128
 
 # More advanced type specification is possible, such as specifying big or little endian numbers; for more information, 
 # refer to the NumPy documentation.
 
##########################################
#              NumPy Arrays              #
##########################################

# Attributes of arrays # --> Determining the size, shape, memory consumption, and data types of arrays

import numpy as np
np.random.seed(0) 

x1 = np.random.randint(10, size=6)  # One-dimensional array
x2 = np.random.randint(10, size=(3, 4))  # Two-dimensional array
x3 = np.random.randint(10, size=(3, 4, 5))  # Three-dimensional array

# Each array has attributes ndim (the number of dimensions), shape (the size of each dimension), and size (the total size of the array):


print(x3)

print("x3 ndim: ", x3.ndim)
print("x3 shape:", x3.shape)
print("x3 size: ", x3.size)

# Some attributes

print("dtype:", x3.dtype)
print("itemsize:", x3.itemsize, "bytes")
print("nbytes:", x3.nbytes, "bytes")

# Indexing of arrays # --> can be accessed by specifying the desired index in square brackets

x1
x1[0]
x1[4]
x1[-1]
x1[-2]

x2
x2[0, 0]
x2[2, 0]
x2[2, -1]

# Slicing of arrays  # -->

# Just as we can use square brackets to access individual array elements, we can also use them to access subarrays with the slice notation,
# marked by the colon (:) character. The NumPy slicing syntax follows that of the standard Python list; to access a slice of an array x,
# use this:   ---->    x[start:stop:step] 

## One-dimensional subarrays

x = np.arange(10)
x

x[:5]  # first five elements

x[5:]  # elements after index 5

x[4:7]  # middle sub-array

x[::2]  # every other element

x[1::2]  # every other element, starting at index 1

## Multi-dimensional subarrays: Multi-dimensional slices work in the same way, with multiple slices separated by commas. For example:

x2
x2[:2, :3]

x2[:3, ::2]

x2[::-1, ::-1]

##  Accessing array rows and columns

print(x2[:, 0])

print(x2[:, 0])

print(x2[0])


# Reshaping of arrays # 
# --> Another useful type of operation is reshaping of arrays. The most flexible way of doing this is with the reshape method. 
# For example, if you want to put the numbers 1 through 9 in a 3×3 grid, you can do the following:

grid = np.arange(1, 10).reshape((3, 3))
print(grid)

# Another common reshaping pattern is the conversion of a one-dimensional array into a two-dimensional row or column matrix.
# This can be done with the reshape method, or more easily done by making use of the newaxis keyword within a slice operation:

x = np.array([1, 2, 3])

# row vector via reshape
x.reshape((1, 3))

# row vector via newaxis
x[np.newaxis, :]

# column vector via reshape
x.reshape((3, 1))

# column vector via newaxis
x[:, np.newaxis]

# Joining and splitting of arrays # --> Array Concatenation and Splitting

# All of the preceding routines worked on single arrays. It's also possible to combine multiple arrays into one, and to 
# conversely split a single array into multiple arrays. We'll take a look at those operations here.

## Concatenation of arrays
## Concatenation, or joining of two arrays in NumPy, is primarily accomplished using the routines np.concatenate, np.vstack, and np.hstack.
## np.concatenate takes a tuple or list of arrays as its first argument, as we can see here:

x = np.array([1, 2, 3])
y = np.array([3, 2, 1])
np.concatenate([x, y])

# More than 2 arrays

z = [99, 99, 99]
print(np.concatenate([x, y, z]))

# It can also be used for two-dimensional arrays:

grid = np.array([[1, 2, 3],
                 [4, 5, 6]])


# concatenate along the first axis
np.concatenate([grid, grid])

# concatenate along the second axis (zero-indexed)
np.concatenate([grid, grid], axis=1)

# For working with arrays of mixed dimensions, it can be clearer to use the np.vstack (vertical stack) and np.hstack
# (horizontal stack) functions:

x = np.array([1, 2, 3])
grid = np.array([[9, 8, 7],
                 [6, 5, 4]])

# vertically stack the arrays
np.vstack([x, grid])

## Splitting of arrays:  The opposite of concatenation is splitting, which is implemented by the functions np.split, np.hsplit, 
## and np.vsplit. For each of these, we can pass a list of indices giving the split points:

x = [1, 2, 3, 99, 99, 3, 2, 1]
x1, x2, x3 = np.split(x, [3, 5])
print(x1, x2, x3)

# Notice that N split-points, leads to N + 1 subarrays. The related functions np.hsplit and np.vsplit are similar:

grid = np.arange(16).reshape((4, 4))
grid

upper, lower = np.vsplit(grid, [2])
print(upper)
print(lower)

left, right = np.hsplit(grid, [2])
print(left)
print(right)

# Array arithmetic: NumPy's ufuncs feel very natural to use because they make use of Python's native arithmetic operators. The standard addition,
# subtraction, multiplication, and division can all be used:

x = np.arange(4)
print("x     =", x)
print("x + 5 =", x + 5)
print("x - 5 =", x - 5)
print("x * 2 =", x * 2)
print("x / 2 =", x / 2)
print("x // 2 =", x // 2)  # floor division

# There is also a unary ufunc for negation, and a ** operator for exponentiation, and a % operator for modulus:

print("-x     = ", -x)
print("x ** 2 = ", x ** 2)
print("x % 2  = ", x % 2)

# The following table lists the arithmetic operators implemented in NumPy: 
# Operator	Equivalent ufunc	Description

# +	np.add	Addition (e.g., 1 + 1 = 2)
# -	np.subtract	Subtraction (e.g., 3 - 2 = 1)
# -	np.negative	Unary negation (e.g., -2)
# *	np.multiply	Multiplication (e.g., 2 * 3 = 6)
# /	np.divide	Division (e.g., 3 / 2 = 1.5)
# //	np.floor_divide	Floor division (e.g., 3 // 2 = 1)
# **	np.power	Exponentiation (e.g., 2 ** 3 = 8)
# %	np.mod	Modulus/remainder (e.g., 9 % 4 = 1)

# Absolute value : just as NumPy understands Python's built-in arithmetic operators, it also understands Python's built-in absolute value function:

x = np.array([-2, -1, 0, 1, 2])
abs(x)

# In Numpy

np.absolute(x)
np.abs(x)

# Exponents and logarithms: Another common type of operation available in a NumPy ufunc are the exponentials:

x = [1, 2, 3]
print("x     =", x)
print("e^x   =", np.exp(x))
print("2^x   =", np.exp2(x))
print("3^x   =", np.power(3, x))

# The inverse of the exponentials, the logarithms, are also available. The basic np.log gives the natural logarithm; 
# if you prefer to compute the base-2 logarithm or the base-10 logarithm, these are available as well:

x = [1, 2, 4, 10]
print("x        =", x)
print("ln(x)    =", np.log(x))
print("log2(x)  =", np.log2(x))
print("log10(x) =", np.log10(x))

# Aggregates: for binary ufuncs, there are some interesting aggregates that can be computed directly from the object. For example,
# if we'd like to reduce an array with a particular operation, we can use the reduce method of any ufunc. A reduce repeatedly applies
# a given operation to the elements of an array until only a single result remains.

x = np.arange(1, 6)
np.add.reduce(x)

np.multiply.reduce(x)

np.add.accumulate(x)

##################################################################
#     Aggregations: Min, Max, and Everything In Between          #
##################################################################

# ften when faced with a large amount of data, a first step is to compute summary statistics for the data in question. Perhaps the most 
# common summary statistics are the mean and standard deviation, which allow you to summarize the "typical" values in a dataset, but other aggregates 
# are useful as well (the sum, product, median, minimum and maximum, quantiles, etc.). 
# NumPy has fast built-in aggregation functions for working on arrays; we'll discuss and demonstrate some of them here.

# Summing the Values in an Array

import numpy as np
L = np.random.random(100)
sum(L)

# Let's numpy the results
np.sum(L)

# Minimum and Maximum

# Normal : min(DATA), max(DATA)
# Numpy:  np.min(DATA), np.max(DATA)

# Multi dimensional aggregates
# One common type of aggregation operation is an aggregate along a row or column. Say you have some data stored in a two-dimensional array:

M = np.random.random((3, 4))
print(M)

M.sum()   # M has already np.[TAB]

M.min(axis=0)
M.max(axis=1)

# Other aggregation functions

# np.sum	np.nansum	Compute sum of elements
# np.prod	np.nanprod	Compute product of elements
# np.mean	np.nanmean	Compute mean of elements
# np.std	np.nanstd	Compute standard deviation
# np.var	np.nanvar	Compute variance
# np.min	np.nanmin	Find minimum value
# np.max	np.nanmax	Find maximum value
# np.argmin	np.nanargmin	Find index of minimum value
# np.argmax	np.nanargmax	Find index of maximum value
# np.median	np.nanmedian	Compute median of elements
# np.percentile	np.nanpercentile	Compute rank-based statistics of elements
# np.any	N/A	Evaluate whether any elements are true
# np.all	N/A	Evaluate whether all elements are true

##################################################################
#                          Comparisons                           #
##################################################################

# using +, -, *, /, and others on arrays leads to element-wise operations. NumPy also implements comparison operators such as < (less than)
# and > (greater than) as element-wise ufuncs. The result of these comparison operators is always an array with a Boolean data type. All six of
# the standard comparison operations are available:

x = np.array([1, 2, 3, 4, 5])
x < 3  # less than
x > 3  # greater than
x <= 3  # less than or equal
x >= 3  # greater than or equal
x != 3  # not equal
x == 3  # equal

(2 * x) == (x ** 2)

# Operator	Equivalent ufunc		Operator	Equivalent ufunc

# ==	np.equal		!=	np.not_equal
# <	np.less		<=	np.less_equal
# >	np.greater		>=	np.greater_equal

rng = np.random.RandomState(0)
x = rng.randint(10, size=(3, 4))
x

x < 6

##################################################################
#                 Working with Boolean Arrays                    #
##################################################################

# Given a Boolean array, there are a host of useful operations you can do. We'll work with x, the two-dimensional array we created earlier.

# how many values less than 6?
np.count_nonzero(x < 6)

np.sum(x < 6)

# how many values less than 6 in each row?
np.sum(x < 6, axis=1)

# are there any values greater than 8?
np.any(x > 8)

# are there any values less than zero?
np.any(x < 0)

# are all values less than 10?
np.all(x < 10)

# are all values equal to 6?
np.all(x == 6)

# are all values in each row less than 8?
np.all(x < 8, axis=1)


##################################################################
#                         Sorting Arrays                         #
##################################################################

# Fast Sorting in NumPy: np.sort and np.argsort
# lthough Python has built-in sort and sorted functions to work with lists, we won't discuss them here because NumPy's np.sort function turns out
# to be much more efficient and useful for our purposes

x = np.array([2, 1, 4, 3, 5])
np.sort(x)

x.sort()
print(x)

# A related function is argsort, which instead returns the indices of the sorted elements:

x = np.array([2, 1, 4, 3, 5])
i = np.argsort(x)
print(i)

x[i]

# Sorting along rows or columns

# rand = np.random.RandomState(42)
# X = rand.randint(0, 10, (4, 6))
# print(X)

# sort each column of X
np.sort(X, axis=0)

# sort each row of X
np.sort(X, axis=1)

# Partial Sorts: Partitioning
# Sometimes we're not interested in sorting the entire array, but simply want to find the k smallest values in the array. NumPy provides this in 
# the np.partition function. np.partition takes an array and a number K

x = np.array([7, 2, 3, 1, 6, 5, 4])
np.partition(x, 3)

np.partition(x, 2, axis=1)


##################################################################
#                       Structured Data                          #
##################################################################

# Workwith Dataframes ----> let's use Pandas
# But it's possible with Numpy

import numpy as np

name = ['Alice', 'Bob', 'Cathy', 'Doug']
age = [25, 45, 37, 19]
weight = [55.0, 85.5, 68.0, 61.5]

x = np.zeros(4, dtype=int)

# Use a compound data type for structured arrays
data = np.zeros(4, dtype={'names':('name', 'age', 'weight'),
                          'formats':('U10', 'i4', 'f8')})
print(data.dtype)

data['name'] = name
data['age'] = age
data['weight'] = weight
print(data)

data['name']

data[0]

data[-1]['name']

data[data['age'] < 30]['name']

# Note that if you'd like to do any operations that are any more complicated than these, you should probably consider the Pandas 