###################################################################
###################################################################
#                 Data Manipulation with Numpy                    #
###################################################################
###################################################################

# Pandas provides an efficient implementation of a DataFrame. DataFrames are essentially multidimensional
# arrays with attached row and column labels, and often with heterogeneous types and/or missing data. As well
# as offering a convenient storage interface for labeled data, Pandas implements a number of powerful data operations
# familiar to users of both database frameworks and spreadsheet programs.

################################## 
#  Installing and Using Pandas   #
##################################

# As a VSC, to install Pandas
# 1. open cmd.
# 2. type python -m pip install pandas.
# 3. restart your visual studio code.

# Also, think about upgrade your pip:  python -m pip install --upgrade pip

# 1. open cmd.
# 2. type python -m pip install --upgrade pip
# 3. restart your visual studio code.

# Sometimes, Installation of Pandas on your system requires NumPy to be installed, and if building the library from source, 
# requires the appropriate tools to compile the C and Cython sources on which Pandas is built.


import pandas as pd
pd.__version__

# As a Reminder, to display all the contents of the pandas namespace, you can type

# pd.<TAB>

# And to display Pandas's built-in documentation, you can use this:

# pd?

################################## 
#         Pandas Objects         #
##################################

import numpy as np
import pandas as pd

# Pandas objects can be thought of as enhanced versions of NumPy structured arrays in which the rows and columns are identified
# with labels rather than simple integer indices. Pandas provides a host of useful tools, methods, and functionality on top of the 
# basic data structures, but nearly everything that follows will require an understanding of what these structures are. 
# 3 fundamentals data Structures: the Series, DataFrame, and Index

# 1. Pandas Series Objetct

# A Pandas Series is a one-dimensional array of indexed data. It can be created from a list or array as follows:

data = pd.Series([34,45, 57, 67])
data

# the Series wraps both a sequence of values and a sequence of indices, which we can access with the values and index attributes.

data.values
data.index

# Like with a NumPy array, data can be accessed by the associated index via the familiar Python square-bracket notation:

data[1]
data[1:3]

# 1.1 Series as generalized NumPy array

# This explicit index definition gives the Series object additional capabilities. For example, the index need not be an integer, 
# but can consist of values of any desired type. For example, if we wish, we can use strings as an index:

data = pd.Series([0.25, 0.5, 0.75, 1.0],
                 index=['a', 'b', 'c', 'd'])
data

data['b']

# We can even use non-contiguous or non-sequential indices:

data = pd.Series([0.25, 0.5, 0.75, 1.0],
                 index=[2, 5, 3, 7])
data

# 1.2 Series as specialized dictionary

# The Series-as-dictionary analogy can be made even more clear by constructing a Series object directly from a Python dictionary

population_dict = {'California': 38332521,
                   'Texas': 26448193,
                   'New York': 19651127,
                   'Florida': 19552860,
                   'Illinois': 12882135}
population = pd.Series(population_dict)
population

# By default, a Series will be created where the index is drawn from the sorted keys. From here, typical dictionary-style 
# item access can be performed:

population['California']

# Unlike a dictionary, though, the Series also supports array-style operations such as slicing:

population['California':'Illinois']

# 1.3 Constructing Series objects

# We've already seen a few ways of constructing a Pandas Series from scratch; all of them are some version of the following:

## pd.Series(data, index=index)

# Some examples 

pd.Series([2, 4, 6])

pd.Series(5, index=[100, 200, 300])

pd.Series({2:'a', 1:'b', 3:'c'})

pd.Series({2:'a', 1:'b', 3:'c'}, index=[3, 2])


# 2. The Pandas DataFrame Object
# DataFrame can be thought of either as a generalization of a NumPy array, or as a specialization of a Python dictionary. We'll now 
# take a look at each of these perspectives.

# 2.1 DataFrame as a generalized NumPy array

# DataFrame is an analog of a two-dimensional array with both flexible row indices and flexible column names. Just as you might
# think of a two-dimensional array as an ordered sequence of aligned one-dimensional columns, you can think of a DataFrame as a
# sequence of aligned Series objects.

# To demonstrate this, let's first construct a new Series listing the area of each of the five states discussed in the previous section:

area_dict = {'California': 423967, 'Texas': 695662, 'New York': 141297,
             'Florida': 170312, 'Illinois': 149995}
area = pd.Series(area_dict)
area

print(type(area))

# we can use a dictionary to construct a single two-dimensional object containing this information:

states = pd.DataFrame({'Variable pop': population,
                       'Variable area': area})
states

print(type(states))

# Like the Series object, the DataFrame has an index attribute that gives access to the index labels:

states.index

# Additionally, the DataFrame has a columns attribute

states.columns

# 2.1 DataFrame as specialized dictionary 

states['Variable area']

# 2.2 Constructing DataFrame objects

### 2.2.1  From a single Series object

pd.DataFrame(population, columns=['population'])

### 2.2.2 From a list of dicts

data = [{'a': i, 'b': 2 * i}
        for i in range(3)]
pd.DataFrame(data)

pd.DataFrame([{'a': 1, 'b': 2}, {'b': 3, 'c': 4}])

### 2.2.3 From a dictionary of Series objects

pd.DataFrame({'Me ': population,
              'en ': area})

### 2.2.4 From a NumPy structured array

A = np.zeros(3, dtype=[('A', 'i8'), ('B', 'f8')])
A

data1 = pd.DataFrame(A)
data1

# 3. Pandas Index Object

ind = pd.Index([2, 3, 5, 7, 11])
ind

## 3.1 Index as immutable array

ind[1]

ind[::2]

print(ind.size, ind.shape, ind.ndim, ind.dtype)

## 3.2 Index as ordered set

# Pandas objects are designed to facilitate operations such as joins across datasets, which depend on many aspects
# of set arithmetic. The Index object follows many of the conventions used by Python's built-in set data structure,
# so that unions, intersections, differences, and other combinations can be computed in a familiar way:

indA = pd.Index([1, 3, 5, 7, 9])
indB = pd.Index([2, 3, 5, 7, 11])

indA & indB  # intersection
indA | indB  # union
indA ^ indB

##################################
#  Data Indexing and Selection   #
##################################

# methods and tools to access, set, and modify values in NumPy arrays. 

# Data Selection in Series
## Series as dictionary

import pandas as pd
data = pd.Series([0.25, 0.5, 0.75, 1.0],
                 index=['a', 'b', 'c', 'd'])
data

data['b']

'a' in data

data.keys()

list(data.items())

########################################
#   Series as one-dimensional array    #
########################################

data['a':'c'] # slicing by explicit index
data[0:3] # slicing by implicit integer index
data[(data > 0.3) & (data < 0.8)] # masking

# 2. Data Selection in DataFrame

area = pd.Series({'California': 423967, 'Texas': 695662,
                  'New York': 141297, 'Florida': 170312,
                  'Illinois': 149995})
pop = pd.Series({'California': 38332521, 'Texas': 26448193,
                 'New York': 19651127, 'Florida': 19552860,
                 'Illinois': 12882135})
data = pd.DataFrame({'area':area, 'pop':pop})
data

data['area']

data.area

# Create a variable 

data['density'] = data['pop'] / data['area']
data

data['good'] = 'Good'

data

# Transpose # data.


data.T   
data.values[0]

data['area']

data.iloc[:3,:2]


data.loc[:'Illinois', :'pop']


data.loc[data.density > 100, ['pop', 'density']]

# 3. Additional indexing conventions

data['Florida':'Illinois']

data[1:3]

data[data.density > 100]

data2 = data[data.good == 'Good']
data2


# import module
import pandas as pd
  
# assign data
dataFrame = pd.DataFrame({'Name': [' RACHEL  ', ' MONICA  ', ' PHOEBE  ',
                                   '  ROSS    ', 'CHANDLER', ' JOEY    '],
                            
                          'Age': [30, 35, 37, 33, 34, 30],
                            
                          'Salary': [100000, 93000, 88000, 120000, 94000, 95000],
                            
                          'JOB': ['DESIGNER', 'CHEF', 'MASUS', 'PALENTOLOGY',
                                  'IT', 'ARTIST']})
  
# filter dataframe 
dataFrame[dataFrame.eval("Salary <=100000 & (Age <40) & JOB.str.startswith('A').values")]

#####################
# Operating on Data Pandas 