###################################################################
###################################################################
#                DataFrame structure un Python                   #
###################################################################
###################################################################

############################################
# Let's check before de current directory  #
############################################

# Import the os module
import os

# Get the current working directory  : os.getcwd()
cwd = os.getcwd()
cwd

# Print the current working directory
print("Current working directory: {0}".format(cwd))

# Let's set the directory 

path = 'C:\\Users\\oscar\\Desktop\\GitHub\\Python\\Data-Manipulation\Pandas'

# Change the current working directory
os.chdir(path)

# Let's check the new directory 

print("Current working directory: {0}".format(os.getcwd()))

###################################
#   Import data from excel file   #
###################################

import pandas as pd

# Step 0: install an additional package openpyxl for .xlsx files

# Step 1: Capture the file path

# C:\Users\oscar\Desktop\GitHub\Python\Data-Manipulation\Pandas\HealthCenter.xlsx

# Step 2: Capture the file path

# Step 3: coding time 

import pandas as pd

data = pd.read_excel (r'C:\Users\oscar\Desktop\GitHub\Python\Data-Manipulation\Pandas\HealthCenter.xlsx') 




##################################
# Dimensions of the DataFrame   #
#################################

# General dimension 

data.shape


# To get the number of rows of a DataFrame or get the length of a Series, use the len function. An integer will be returned.

len(data)

# To get the total number of elements in the DataFrame or Series, use the size attribute. For DataFrames, this is the product of the number 
# of rows and the number of columns. For a Series, this will be equivalent to the len function:

data.size

# The ndim attribute returns the number of dimensions of your DataFrame or Series. It will always be 2 for DataFrames and 1 for Series:

data.ndim

# The count method can be used to return the number of non-missing values for each column/row of the DataFrame. 

data.count()

# Variables or columns

data.columns

# Rows or index

data.index

#  The info method returns the number of non-missing values and data types of each column

data.info()

##################################
#   Names of the DataFrame       #
##################################

# Get the names of variables o a DataFrame 
set
data.head()
data.columns

## Method #1: Simply iterating over columns 

# iterating the columns
for col in data.columns:
    print(col)

##  Method #2: Using columns attribute with dataframe object 

list(data.columns)
 
## Method #3: Using keys() function: It will also give the columns of the dataframe.

 # calling keys() function
print(data.keys())
 
# Method #4:  column.values method returns an array of index. 

list(data.columns.values)


#  Method #5: Using tolist() method with values with given the list of columns. 

list(data.columns.values.tolist())
 
 # Method #6: Using sorted() method : sorted() method will return the list of columns sorted in alphabetical order. 
 
 sorted(data)
 
##################################
#   Data Type of each variable    #
##################################

# apply the dtype attribute
result = data.dtypes

print("Output:")
print(result)

data.info()
 
##################################
# Indexing a    DataFrame   #
#################################

# Pandas Indexing using [ ], .loc[], .iloc[ ], .ix[ ]

# Dataframe.[ ] ; This function also known as indexing operator
# Dataframe.loc[ ] : This function is used for labels.
# Dataframe.iloc[ ] : This function is used for positions or integer based
# Dataframe.ix[] : This function is used for both label and integer based

# An Specif column

data["Id",]

# 2 or more columns

data[["Id","Edad", "Sexo"]]

# A row

data.loc[[1, 2]]

data.loc[[0,1,2,3,4,5]]

# Rows and Columns selections
# Dataframe.loc[["row1", "row2"], ["column1", "column2", "column3"]]

data.loc[[0,1,2,3,4],
                   ["Id","Edad", "Sexo"]]


# Selecting all of the rows and some columns
# Dataframe.loc[:, ["column1", "column2", "column3"]]

data.loc[:, ["Id","Edad", "Sexo"]]
  
  
# iloc

data.iloc[3] 

#  order to select multiple rows, we can pass a list of integer to .iloc[] function.

data.iloc [[3, 5, 7]]

# Rows and Columns selections

data.iloc [[3, 4], [1, 2]]

# Selecting all the rows and a some columns

data.iloc [:, [1, 2]]


# Function         	Description
# Dataframe.head()	Return top n rows of a data frame.
# Dataframe.tail()	Return bottom n rows of a data frame.
# Dataframe.at[]	Access a single value for a row/column label pair.
# Dataframe.iat[]	Access a single value for a row/column pair by integer position.
# Dataframe.tail()	Purely integer-location based indexing for selection by position.
# DataFrame.lookup()	Label-based “fancy indexing” function for DataFrame.
# DataFrame.pop()	Return item and drop from frame.
# DataFrame.xs()	Returns a cross-section (row(s) or column(s)) from the DataFrame.
# DataFrame.get()	Get item from object for given key (DataFrame column, Panel slice, etc.).
# DataFrame.isin()	Return boolean DataFrame showing whether each element in the DataFrame is contained in values.
# DataFrame.where()	Return an object of same shape as self and whose corresponding entries are from self where cond is True and otherwise are from other.
# DataFrame.mask()	Return an object of same shape as self and whose corresponding entries are from self where cond is False and otherwise are from other.
# DataFrame.query()	Query the columns of a frame with a boolean expression.
# DataFrame.insert()	Insert column into DataFrame at specified location.