###################################################################
###################################################################
#                       Combine tables                            #
###################################################################
###################################################################

# join
# merge
# concatenate
# append 

# https://realpython.com/pandas-merge-join-and-concat/
# https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html
# https://jakevdp.github.io/PythonDataScienceHandbook/03.07-merge-and-join.html
# https://www.shanelynn.ie/merge-join-dataframes-python-pandas-index-1/
# https://www.geeksforgeeks.org/how-to-combine-two-dataframe-in-python-pandas/
# https://www.w3schools.com/python/python_mysql_join.asp

# Concatenating DataFrames 

# The concat() function in pandas is used to append either columns or rows from one DataFrame to another. 
# The concat() function does all the heavy lifting of performing concatenation operations along an 
# axis while performing optional set logic (union or intersection) of the indexes (if any) on the other axes.


import pandas as pd

# First DataFrame
df1 = pd.DataFrame({'id': ['A01', 'A02', 'A03', 'A04'],
                    'Name': ['ABC', 'PQR', 'DEF', 'GHI']})
  
# Second DataFrame
df2 = pd.DataFrame({'id': ['B05', 'B06', 'B07', 'B08'],
                    'Name': ['XYZ', 'TUV', 'MNO', 'JKL']})
  
  
frames = [df1, df2]
  
result = pd.concat(frames)
result

# Joining Data Frames

# When we concatenated our DataFrames we simply added them to each other i.e. stacked them either vertically or side by side. Another way to
# combine DataFrames is to use columns in each dataset that contain common values (a common unique id). Combining DataFrames using a common field 
# is called “joining”. The columns containing the common values are called “join key(s)”. Joining DataFrames in this way is often useful when one 
# DataFrame is a “lookup table” containing additional data that we want to include in the other.

df1 = pd.DataFrame({'id': ['A01', 'A02', 'A03', 'A04'],
                    'Name': ['ABC', 'PQR', 'DEF', 'GHI']})
  
df3 = pd.DataFrame({'City': ['MUMBAI', 'PUNE', 'MUMBAI', 'DELHI'],
                    'Age': ['12', '13', '14', '12']})
  
# the default behaviour is join='outer'
# inner join
  
result2 = pd.concat([df1, df3], axis=1, join='inner')
result2

# Concatenating using append

# A useful shortcut to concat() is append() instance method on Series and DataFrame. These methods actually predated concat. 

# First DataFrame
df1 = pd.DataFrame({'id': ['A01', 'A02', 'A03', 'A04'],
                    'Name': ['ABC', 'PQR', 'DEF', 'GHI']})
  
# Second DataFrame
df2 = pd.DataFrame({'id': ['B05', 'B06', 'B07', 'B08'],
                    'Name': ['XYZ', 'TUV', 'MNO', 'JKL']})
  
# append method
result3 = df1.append(df2)
result3

# append() may take multiple objects to concatenate.

# First DataFrame
df1 = pd.DataFrame({'id': ['A01', 'A02', 'A03', 'A04'],
                    'Name': ['ABC', 'PQR', 'DEF', 'GHI']})
  
# Second DataFrame
df2 = pd.DataFrame({'id': ['B05', 'B06', 'B07', 'B08'],
                    'Name': ['XYZ', 'TUV', 'MNO', 'JKL']})
  
df3 = pd.DataFrame({'City': ['MUMBAI', 'PUNE', 'MUMBAI', 'DELHI'],
                    'Age': ['12', '13', '14', '12']})
  
  
# appending multiple DataFrame
result4 = df1.append([df2, df3])
result4

# First DataFrame
df1 = pd.DataFrame({'id': ['A01', 'A02', 'A03', 'A04'],
                    'Name': ['ABC', 'PQR', 'DEF', 'GHI']})
  
# Second DataFrame
df2 = pd.DataFrame({'id': ['B05', 'B06', 'B07', 'B08'],
                    'Name': ['XYZ', 'TUV', 'MNO', 'JKL']})
  
df3 = pd.DataFrame({'City': ['MUMBAI', 'PUNE', 'MUMBAI', 'DELHI'],
                    'Age': ['12', '13', '14', '12']})
  
  
# appending multiple DataFrame
result = df1.append([df2, df3])
display(result)


##########################################
#  Merge, join, concatenate and compare  #
##########################################

# pandas provides various facilities for easily combining together Series or DataFrame with various kinds of set logic for the indexes and relational algebra functionality in the case of join / merge-type operations.
# In addition, pandas also provides utilities to compare two Series or DataFrame and summarize their differences.

# The concat() function (in the main pandas namespace) does all of the heavy lifting of performing concatenation operations along an axis
# while performing optional set logic (union or intersection) of the indexes (if any) on the other axes


pd.concat(
    objs,
    axis=0,
    join="outer",
    ignore_index=False,
    keys=None,
    levels=None,
    names=None,
    verify_integrity=False,
    copy=True,
)

import pandas as pd

df1 = pd.DataFrame(
    {
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    },
    index=[0, 1, 2, 3],
)


df2 = pd.DataFrame(
    {
        "A": ["A4", "A5", "A6", "A7"],
        "B": ["B4", "B5", "B6", "B7"],
        "C": ["C4", "C5", "C6", "C7"],
        "D": ["D4", "D5", "D6", "D7"],
    },
    index=[4, 5, 6, 7],
)


df3 = pd.DataFrame(
    {
        "A": ["A8", "A9", "A10", "A11"],
        "B": ["B8", "B9", "B10", "B11"],
        "C": ["C8", "C9", "C10", "C11"],
        "D": ["D8", "D9", "D10", "D11"],
    },
    index=[8, 9, 10, 11],
)

# first frame

frames = [df1, df2, df3]

result = pd.concat(frames)
result

result2 = pd.concat(frames, keys=["x", "y", "z"])
result2

# Set logic on the other axes

#When gluing together multiple DataFrames, you have a choice of how to handle the other axes (other than the one being concatenated). This can be done in the following two ways:
#Take the union of them all, join='outer'. This is the default option as it results in zero information loss.
#Take the intersection, join='inner'.

df4 = pd.DataFrame(
    {
        "B": ["B2", "B3", "B6", "B7"],
        "D": ["D2", "D3", "D6", "D7"],
        "F": ["F2", "F3", "F6", "F7"],
    },
    index=[2, 3, 6, 7],
)


result5 = pd.concat([df1, df4], axis=1)

## Here is the same thing with join='inner'

df1
df4

pd.concat([df1, df4], axis=1, join="inner")

pd.concat([df1, df4], axis=1).reindex(df1.index)

################################################################
# Database-style DataFrame or named Series joining/merging
################################################################

pandas provides a single function, merge(), as the entry point for all standard database join operations between DataFrame or named Series objects:

pd.merge(
    left,
    right,
    how="inner",
    on=None,
    left_on=None,
    right_on=None,
    left_index=False,
    right_index=False,
    sort=True,
    suffixes=("_x", "_y"),
    copy=True,
    indicator=False,
    validate=None,
)



Create the cartesian product of rows of both frames

left = pd.DataFrame(
    {
        "key": ["K0", "K1", "K2", "K3"],
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
    }
)


right = pd.DataFrame(
    {
        "key": ["K0", "K1", "K2", "K3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    }
)


 pd.merge(left, right, on="key")
 
 pd.merge(left, right, how="cross")