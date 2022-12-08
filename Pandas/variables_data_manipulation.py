###################################################################
###################################################################
#                  Columns data manipulation                      #
###################################################################
###################################################################

##  Some variables or cols manipulation

# Select
# Rename
# Add_colum



############ 
#  Select  #
############

# https://www.geeksforgeeks.org/python-pandas-dataframe/
# https://www.geeksforgeeks.org/how-to-select-multiple-columns-in-a-pandas-dataframe/

# Method #1: Basic Method

# Define a dictionary containing employee data
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
  
# Convert the dictionary into DataFrame 
df = pd.DataFrame(data)
  
# select two columns

df2 = df[['Name', 'Qualification']]
df2

# Select Second to fourth column.

# Define a dictionary containing employee data
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
  
# Convert the dictionary into DataFrame 
df = pd.DataFrame(data)
  
# select all rows 
# and second to fourth column
df[df.columns[1:4]]

# Method #2: Using loc[]

# Define a dictionary containing employee data
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
  
# Convert the dictionary into DataFrame 
df = pd.DataFrame(data)
  
# select three rows and two columns
df.loc[1:3, ['Name', 'Qualification']]

# select two rows and 
# column "name" to "Address"
# Means total three columns
df.loc[0:1, 'Name':'Address']

# Example 3: First filtering rows and selecting columns by label format and then Select all columns.

# Define a dictionary containing employee data
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']
       }
# Convert the dictionary into DataFrame 
df = pd.DataFrame(data)
  
# .loc DataFrame method
# filtering rows and selecting columns by label
# format
# df.loc[rows, columns]
# row 1, all columns
df.loc[0, :]

# Method 3: Using iloc[]

# Define a dictionary containing employee data
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
  
# Convert the dictionary into DataFrame 
df = pd.DataFrame(data)
  
# Remember that Python does not
# slice inclusive of the ending index.
# select all rows 
# select first two column
df.iloc[:, 0:2] 

# Define a dictionary containing employee data
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
  
# Convert the dictionary into DataFrame 
df = pd.DataFrame(data)
  
# iloc[row slicing, column slicing]
df.iloc [0:2, 1:3]

# Method #4: Using .ix

# Define a dictionary containing employee data
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
  
# Convert the dictionary into DataFrame 
df = pd.DataFrame(data)
  
# select all rows and 0 to 2 columns 
print(df.ix[:, 0:2])


############ 
#  Rename   #
############

###################################
#    Changing variables names     #
###################################

data.columns

#  Rename a single column. 

data.rename(columns = {'Edad':'Años'}, inplace = True)

data.columns

data.rename(columns = {'Años':'Edad'}, inplace = True)

data.columns

# Rename multiple columns.

data.rename(columns = {'Id':'Identificador', 
                       'Tipo trabajador':'Trabajador',
                       'Área':'Zona'}, 
            inplace = True)

data.columns

# Rename column names using DataFrame set_axis() function
  
# Define a dictionary containing ICC rankings
rankings = {'test': ['India', 'South Africa', 'England',
                     'New Zealand', 'Australia'],
            'odi': ['England', 'India', 'New Zealand',
                    'South Africa', 'Pakistan'],
            't20': ['Pakistan', 'India', 'Australia',
                    'England', 'New Zealand']}
  
# Convert the dictionary into DataFrame
rankings_pd = pd.DataFrame(rankings)
  
# Before renaming the columns
print(rankings_pd.columns)
  
rankings_pd.set_axis(['A', 'B', 'C'], axis='columns', inplace=True)
  
# After renaming the columns
print(rankings_pd.columns)
rankings_pd.head()

# Rename column names using DataFrame add_prefix() and add_suffix() functions

# Define a dictionary containing ICC rankings
rankings = {'test': ['India', 'South Africa', 'England',
                     'New Zealand', 'Australia'],
            'odi': ['England', 'India', 'New Zealand',
                    'South Africa', 'Pakistan'],
            't20': ['Pakistan', 'India', 'Australia',
                    'England', 'New Zealand']}
  
# Convert the dictionary into DataFrame
rankings_pd = pd.DataFrame(rankings)
  
# Before renaming the columns
print(rankings_pd.columns)
  
rankings_pd = rankings_pd.add_prefix('col_')
rankings_pd = rankings_pd.add_suffix('_1')
  
# After renaming the columns
rankings_pd.head()

# Replace specific texts of column names using Dataframe.columns.str.replace function

# Define a dictionary containing ICC rankings
rankings = {'test': ['India', 'South Africa', 'England',
                     'New Zealand', 'Australia'],
            'odi': ['England', 'India', 'New Zealand',
                    'South Africa', 'Pakistan'],
            't20': ['Pakistan', 'India', 'Australia',
                    'England', 'New Zealand']}
  
# Convert the dictionary into DataFrame
rankings_pd = pd.DataFrame(rankings)
  
# Before renaming the columns
print(rankings_pd.columns)
# df = rankings_pd
  
rankings_pd.columns = rankings_pd.columns.str.replace('test', 'Col_TEST')
rankings_pd.columns = rankings_pd.columns.str.replace('odi', 'Col_ODI')
rankings_pd.columns = rankings_pd.columns.str.replace('t20', 'Col_T20')
  
rankings_pd.head()

################# 
#  Add columns  #
#################

# Method #1: By declaring a new list as a column. 

# Import pandas package
import pandas as pd
  
# Define a dictionary containing Students data
data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Height': [5.1, 6.2, 5.1, 5.2],
        'Qualification': ['Msc', 'MA', 'Msc', 'Msc']}
  
# Convert the dictionary into DataFrame
df = pd.DataFrame(data)
  
# Declare a list that is to be converted into a column
address = ['Delhi', 'Bangalore', 'Chennai', 'Patna']
  
# Using 'Address' as the column name
# and equating it to the list
df['Address'] = address
  
df

# Method #2: By using DataFrame.insert()

# Define a dictionary containing Students data
data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Height': [5.1, 6.2, 5.1, 5.2],
        'Qualification': ['Msc', 'MA', 'Msc', 'Msc']}
  
# Convert the dictionary into DataFrame
df = pd.DataFrame(data)
  
# Using DataFrame.insert() to add a column
df.insert(2, "Age", [21, 23, 24, 21], True)

df

# Method #3: Using Dataframe.assign() method

# Define a dictionary containing Students data
data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Height': [5.1, 6.2, 5.1, 5.2],
        'Qualification': ['Msc', 'MA', 'Msc', 'Msc']}
  
  
# Convert the dictionary into DataFrame
df = pd.DataFrame(data)
  
# Using 'Address' as the column name and equating it to the list
df2 = df.assign(address=['Delhi', 'Bangalore', 'Chennai', 'Patna'])

df2

# Method #4: By using a dictionary

# Define a dictionary containing Students data
data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Height': [5.1, 6.2, 5.1, 5.2],
        'Qualification': ['Msc', 'MA', 'Msc', 'Msc']}
  
# Define a dictionary with key values of
# an existing column and their respective
# value pairs as the # values for our new column.
address = {'Delhi': 'Jai', 'Bangalore': 'Princi',
           'Patna': 'Gaurav', 'Chennai': 'Anuj'}
  
# Convert the dictionary into DataFrame
df = pd.DataFrame(data)
  
# Provide 'Address' as the column name
df['Address'] = address

df