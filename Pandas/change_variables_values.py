########################################################################
########################################################################
#              Replace Values in Pandas DataFramen                 #####
########################################################################
########################################################################


# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.replace.html
# https://python-course.eu/numerical-programming/accessing-and-changing-values-dataframes.php
# https://www.geeksforgeeks.org/python-pandas-dataframe-replace/

# Depending on your needs, you may use either of the following approaches to replace values in Pandas DataFrame:

# (1) Replace a single value with a new value for an individual DataFrame column:

df['column name'] = df['column name'].replace(['old value'],'new value')

# (2) Replace multiple values with a new value for an individual DataFrame column:

df['column name'] = df['column name'].replace(['1st old value','2nd old value',...],'new value')

# (3) Replace multiple values with multiple new values for an individual DataFrame column:

df['column name'] = df['column name'].replace(['1st old value','2nd old value',...],['1st new value','2nd new value',...])

# (4) Replace a single value with a new value for an entire DataFrame:

df = df.replace(['old value'],'new value')

# Let's explore



#Syntax: DataFrame.replace(to_replace=None, value=None, inplace=False, limit=None, regex=False, method=’pad’, axis=None) 

# Parameters:

# to_replace : [str, regex, list, dict, Series, numeric, or None] pattern that we are trying to replace in dataframe. 
# value : Value to use to fill holes (e.g. 0), alternately a dict of values specifying which value to use for each column (columns not in the dict will not be filled). Regular expressions, strings and lists or dicts of such objects are also allowed. 
# inplace : If True, in place. Note: this will modify any other views on this object (e.g. a column from a DataFrame). Returns the caller if this is True. 
# limit : Maximum size gap to forward or backward fill 
# regex : Whether to interpret to_replace and/or value as regular expressions. If this is True then to_replace must be a string. Otherwise, to_replace must be None because this parameter will be interpreted as a regular expression or a list, dict, or array of regular expressions.
# method : Method to use when for replacement, when to_replace is a list. 

# Some examples 

import pandas as pd
  
df = {
  "Array_1": [49.50, 70],
  "Array_2": [65.1, 49.50]
}
  
data = pd.DataFrame(df)
  
data = data.replace(49.50, 60)

data

### The Data: nba ###

import os
import pandas as pd

path = 'C:\\Users\\oscar\\Desktop\\GitHub\\Python\\Data-Manipulation\Pandas'

# Change the current working directory
os.chdir(path)

# Print the current working directory
print("Current working directory: {0}".format(os.getcwd()))

# Making data frame from the csv file
df = pd.read_csv("nba.csv")
df.head


# Case 1: We are going to replace team “Boston Celtics” with “Omega Warrior” in the ‘df’ Dataframe.

df.replace(to_replace="Boston Celtics",
           value="Omega Warrior")

# Case 2: Replacing more than one value at a time. Using python list as an argument We are going to replace team “Boston Celtics” and “Texas”
# with “Omega Warrior” in the ‘df’ Dataframe. 

# this will replace "Boston Celtics" and "Texas" with "Omega Warrior"
df.replace(to_replace=["Boston Celtics", "Texas"],
           value="Omega Warrior")

# Case 3: Replace the Nan value in the data frame with the -99999 value. 

# will replace Nan value in dataframe with value -99999
df.replace(to_replace = np.nan, value =-99999)


##### Others examples 

# A  Scalar `to_replace` and `value`

s = pd.Series([1, 2, 3, 4, 5])
s.replace(1, 5)


df = pd.DataFrame({'A': [0, 1, 2, 3, 4],
                   'B': [5, 6, 7, 8, 9],
                   'C': ['a', 'b', 'c', 'd', 'e']})

df.replace(0, 5)


# B List-like `to_replace`


df.replace([0, 1, 2, 3], 4)

df.replace([0, 1, 2, 3], [4, 3, 2, 1])


s.replace([1, 2], method='bfill')

# C dict-like `to_replace`

df.replace({0: 10, 1: 100})

df.replace({'A': 0, 'B': 5}, 100)

df.replace({'A': {0: 100, 4: 400}})

# Regular expression `to_replace`

df = pd.DataFrame({'A': ['bat', 'foo', 'bait'],
                   'B': ['abc', 'bar', 'xyz']})

df.replace(to_replace=r'^ba.$', value='new', regex=True)

df.replace({'A': r'^ba.$'}, {'A': 'new'}, regex=True)

df.replace(regex=r'^ba.$', value='new')

df.replace(regex={r'^ba.$': 'new', 'foo': 'xyz'})

#

#

#

#


#


#


#


#


#


#

