###################################################################
###################################################################
#                    Cases data manipulation                      #
###################################################################
###################################################################

# In cases data manipulation, we works throuhgh rows. 
# Some cases data manipulations :

# Filter
# distinct
# sampling
# arrange
# add_row


#########################
#  Importing libraries  #
#########################

import numpy as np
import pandas as pd

#########################
#       Filter          #
#########################

# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.filter.html
# https://towardsdatascience.com/8-ways-to-filter-pandas-dataframes-d34ba585c1b8

    df = pd.DataFrame({
    'name':['Jane','John','Ashley','Mike','Emily','Jack','Catlin'],
    'ctg':['A','A','C','B','B','C','B'],
    'val':np.random.random(7).round(2),
    'val2':np.random.randint(1,10, size=7)
    })
    
    df.info
    
# 1. Logical operators

df[df.val > 0.5]

# The logical operators also works on strings

df[df.name > 'Jane']

# 2. Multiple logical operators
# Pandas allows for combining multiple logical operators. For instance, we can apply conditions on both val and val2 columns as below.

df[(df.val > 0.5) & (df.val2 == 5)]

# The “&” signs stands for “and” , the “|” stands for “or”.

df[(df.val < 0.5) | (df.val2 == 7)]

# Isin
# The isin method is another way of applying multiple condition for filtering. For instance, we can filter the names that exist in a given list.

names = ['John','Catlin','Mike']
df[df.name.isin(names)]

# 4. Str accessories
# Pandas is a highly efficient library on textual data as well. The functions and methods under the str accessor provide flexible ways to filter rows based on strings.

df[df.name.str.startswith('J')]

# The contains function under the str accessor returns the values that contain a given set of characters.

df[df.name.str.contains('y')]

# 5. Tilde (~)
# The tilde operator is used for “not” logic in filtering. If we add the tilde operator before the filter expression, 
# the rows that do not fit the condition are returned.

df[~df.name.str.startswith('J')]

# 6. Query
# The query function offers a little more flexibility at writing the conditions for filtering. We can pass the conditions as a string.

df.query('ctg == "B" and val > 0.5')

# 7. Nlargest or nsmallest
# In some cases, we do not have a specific range for filtering but just need the largest or smallest values. 
#  The nlargest and nsmallest functions allow for selecting rows that have the largest or smallest values in a column, respectively.

df.nlargest(3, 'val')

df.nsmallest(2, 'val2')

# 8. Loc and iloc

# The loc and iloc methods are used to select rows or columns based on index or label.
# loc: select rows or columns using labels
# iloc: select rows or columns using indices

# Thus, they can be used for filtering. However, we can only select a particular part of the dataframe without specifying a condition.

df.iloc[2:5, :] #rows 3 and 4, all columns

# If the dataframe has integer index, the indices and labels of the rows are the same. Thus, both loc and iloc accomplished the same thing on the rows.

df.loc[2:5, :] #rows 3 and 4, all columns


###########################
#       Distinct          #
###########################

# the unique values ( distinct rows) of a dataframe in python pandas with drop_duplicates() function.  Lets see with an example 
# on how to drop duplicates and get Distinct rows of the dataframe in pandas python.

d = {
    'Name':['Alisa','Bobby','jodha','jack','raghu','Cathrine',
            'Alisa','Bobby','kumar','Alisa','Alex','Cathrine'],
    'Age':[26,24,23,22,23,24,26,24,22,23,24,24]
}
 
df = pd.DataFrame(d,columns=['Name','Age'])
df

# Get the unique values (distinct rows) of the dataframe in python pandas

df.drop_duplicates()

# Get the unique values (rows) of the dataframe in python pandas by retaining last row:

df.drop_duplicates(keep='last')

# Get Distinct values of the dataframe based on a column:

df2  = df.drop_duplicates(subset = ["Age"])
df2

# Select distinct rows across dataframe

df = pd.DataFrame({'col_1':['A','B','A','B','C'], 'col_2':[3,4,3,5,6]})
df

# To get the distinct values in col_1 you can use Series.unique()

df['col_1'].unique()   # ---> But Series.unique() works only for a single column.

#  To simulate the select unique col_1, col_2 of SQL you can use DataFrame.drop_duplicates()

 df.drop_duplicates()
 
 # This will get you all the unique rows in the dataframe. So if
 
df = pd.DataFrame({'col_1':['A','B','A','B','C'], 'col_2':[3,4,3,5,6], 'col_3':[0,0.1,0.2,0.3,0.4]})
df.drop_duplicates()

# To specify the columns to consider when selecting unique records, pass them as arguments

df = pd.DataFrame({'col_1':['A','B','A','B','C'], 'col_2':[3,4,3,5,6], 'col_3':[0,0.1,0.2,0.3,0.4]})
df.drop_duplicates(['col_1','col_2'])


###    More general   ##### 
# pandas.DataFrame().unique() method is used when we deal with a single column of a DataFrame and returns all unique elements of a column. 
# The method returns a DataFrame containing the unique elements of a column, along with their corresponding index labels.


data = {
  "Students": ["Ray", "John", "Mole", "Smith", "Jay", "Milli", "Tom", "Rick"],
  "Subjects": ["Maths", "Economics", "Science", "Maths", "Statistics", "Statistics", "Statistics", "Computers"]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df["Subjects"].unique())                   # variable 
print(type(df["Subjects"].unique()))            # 

#  drop_duplicates() is an in-built function in the panda's library that helps to remove the duplicates from the dataframe. 
# It helps to preserve the type of the dataframe object or its subset and removes the rows with duplicate values.
#  When it comes to dealing with the large set of dataframe, using the drop_duplicate() method is considered to be the faster option to remove the duplicate values.

data = {
  "Students": ["Ray", "John", "Mole", "Smith", "Jay", "Milli", "Tom", "Rick"],
  "Subjects": ["Maths", "Economics", "Science", "Maths", "Statistics", "Statistics", "Statistics", "Computers"]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df.drop_duplicates(subset = "Subjects"))
print(type(df.drop_duplicates(subset = "Subjects")))


# With Strings columns or variables 

# Example #1: Get the unique values of ‘B’ column

# create a dictionary with five fields each
data = {
    'A':['A1', 'A2', 'A3', 'A4', 'A5'], 
    'B':['B1', 'B2', 'B3', 'B4', 'B4'], 
    'C':['C1', 'C2', 'C3', 'C3', 'C3'], 
    'D':['D1', 'D2', 'D2', 'D2', 'D2'], 
    'E':['E1', 'E1', 'E1', 'E1', 'E1'] }
  
# Convert the dictionary into DataFrame 
df = pd.DataFrame(data)
  
# Get the unique values of 'B' column
df.B.unique()

# Example #2: Get the unique values of ‘E’ column

# # create a dictionary with five fields each
data = {
    'A':['A1', 'A2', 'A3', 'A4', 'A5'], 
    'B':['B1', 'B2', 'B3', 'B4', 'B4'], 
    'C':['C1', 'C2', 'C3', 'C3', 'C3'], 
    'D':['D1', 'D2', 'D2', 'D2', 'D2'], 
    'E':['E1', 'E1', 'E1', 'E1', 'E1'] }
  
# Convert the dictionary into DataFrame 
df = pd.DataFrame(data)
  
# Get the unique values of 'E' column
df.E.unique()

# Example #3: Get number of unique values in a column

# create a dictionary with five fields each
data = {
    'A':['A1', 'A2', 'A3', 'A4', 'A5'], 
    'B':['B1', 'B2', 'B3', 'B4', 'B4'], 
    'C':['C1', 'C2', 'C3', 'C3', 'C3'], 
    'D':['D1', 'D2', 'D2', 'D2', 'D2'], 
    'E':['E1', 'E1', 'E1', 'E1', 'E1'] }
  
# Convert the dictionary into DataFrame 
df = pd.DataFrame(data)
  
# Get number of unique values in column 'C'
df.C.nunique(dropna = True)


###########################################
#       Sampling in a Data Frame          #
###########################################

#  in cmd:  pip install -U scikit-learn

# random sampling
# sampling with condition
# sampling at a constant rate

from sklearn.datasets import load_iris
import pandas as pd

data = load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)
df.head(5)
df.shape

## Random Sampling ## 

# Knowning the exact number of samples to return

subset = df.sample(n=100)
subset.shape

# Knowning the percentage of samples to return

subset = df.sample(frac=0.5)
subset.shape

## Sampling with condition ## 

# Return 10 random sample where sepal width (cm) < 3 Firstly count the number of records which satisfy the condition

condition = df['sepal width (cm)'] < 3
condition

true_index = condition[condition == True].index
len(true_index)

subset = df[condition].sample(n = 10)
subset.shape

## Sampling at a Constant Rate ##

rate = 10
subset = df[::rate]
subset.shape

subset.head()

## Getting the remaining part of the dataset

# 1.

remaining = df.drop(labels=subset.index)
remaining.shape

# 2. 2

remaining = df[~df.index.isin(subset.index)]
remaining.shape

remaining.head()

#### More extensive document 

# https://datagy.io/pandas-sample/

# 7 Ways to Sample Data in Pandas

# 1. Using Pandas Sample to Sample your Dataframe

# DataFrame.sample(
 
    
    n=None, 
    frac=None, 
    replace=False, 
    weights=None, 
    random_state=None, 
    axis=None, 
    ignore_index=False
)


# Creating a Reproducible Random Sample in Pandas

#  Pandas Weighted Samples

# Pandas Sample with Replacements

 # Pandas Sampling Every nth Item (Sampling at a constant rate)
 
 # Pandas Sampling Items by Conditions
 
 # Pandas Sampling Random Columns
 
 
###########################
#       Arrange or sort   #
###########################

# DataFrame.sort_values
#                       (by, axis=0, a
#                          scending=True, 
#                            inplace=False, 
#                           kind='quicksort', 
#                           na_position='last', 
#                           ignore_index=False,
#                           key=None)


# In order to sort the data frame in pandas, function sort_values() is used. Pandas sort_values() can 
# sort the data frame in Ascending or Descending order.


# creating and initializing a nested list
age_list = [['Afghanistan', 1952, 8425333, 'Asia'],
            ['Australia', 1957, 9712569, 'Oceania'],
            ['Brazil', 1962, 76039390, 'Americas'],
            ['China', 1957, 637408000, 'Asia'],
            ['France', 1957, 44310863, 'Europe'],
            ['India', 1952, 3.72e+08, 'Asia'],
            ['United States', 1957, 171984000, 'Americas']]
 
# creating a pandas dataframe
df = pd.DataFrame(age_list, columns=['Country', 'Year',
                                     'Population', 'Continent'])



# Example 1: Sorting the Data frame in Ascending order 

# Sorting by column 'Country'

df.sort_values(by=['Country'])

# Example 2: Sorting the Data frame in Descending order 


# Sorting by column "Population"
df.sort_values(by=['Population'], ascending=False)

# Example 3: Sorting Pandas Data frame by putting missing values first

# Sorting by column "Population"
# by putting missing values first
df.sort_values(by=['Population'], na_position='first')

# Example 4: Sorting Data frames by multiple columns

# Sorting by columns "Country" and then "Continent"
df.sort_values(by=['Country', 'Continent'])


# Example 5: Sorting Data frames by multiple columns but different order

# Sorting by columns "Country" in descending
# order and then "Continent" in ascending order
 
df.sort_values(by=['Country', 'Continent'],
               ascending=[False, True])







