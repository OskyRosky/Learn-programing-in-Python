###################################################################
###################################################################
#              Create new variable with in Data Frame             #
###################################################################
###################################################################

import pandas as pd
import numpy as np
 
#Create a DataFrame
d = {
    'Name':['Alisa','Bobby','Cathrine','Madonna','Rocky','Sebastian','Jaqluine',
   'Rahul','David'],
   'Score1':[62,47,55,74,31,77,85,63,42],
   'Score2':[89,87,67,55,47,72,76,79,44]}
 
df = pd.DataFrame(d)

# 1. Create new column or variable to existing dataframe in python pandas

# assign new column to existing dataframe
df2=df.assign(Score3 = [56,86,77,45,73,62,74,89,71])
df2

# 2. Create a new variable using list converted to column in pandas:
# To the above existing dataframe, lets add new column named “address” using list. 
# As the list is created first and then added as the column to the dataframe as shown below

address = ['Newyork', 'California', 'Chennai', 'Vladivosk','London','Tokyo','Paris','Texas','Mumbai'] 
df['Address'] = address 
 
df

# 3. Create a new variable to the particular position using insert() function in pandas python:
# To the existing dataframe, lets add new column named “Address” to the mentioned position using insert() function.
# insert() function creates new column to the specific position as shown below.

#### Using DataFrame.insert() to add a column at specific position
df.insert(1, "Address", ['Newyork', 'California', 'Chennai', 'Vladivosk','London','Tokyo','Paris','Texas','Mumbai'] , True) 
df  

# 4. Create a new variable through dictionary in pandas python:
# To the existing dataframe, lets add new column named “address” using dictionary. As the dictionary is created as the column
# to the dataframe as shown below

#### add a new column of the dataframe: through dictionary
 
address = {'Newyork':'Alisa','California':'Bobby','Chennai':'Cathrine','Vladivosk':'Madonna','London':'Rocky','Tokyo':'Sebastian','Paris':'Jaqluine','Texas':'Rahul','Mumbai':'David'}
df['Address'] = address 
df

# 4. Add a new column in pandas python using existing column
# 
#### new columns based on existing columns
 
df['Total_Score'] = df.apply(lambda row: row.Score1 + row.Score2, axis = 1) 
df

# 5. Add a new column in pandas python using existing column
# To the existing dataframe, lets add new column named “Total_score” using by adding “Score1” and “Score2”  as shown below

#### new columns based on existing columns
 
df['Total_Score'] = df['Score1'] +  df['Score2']
df
