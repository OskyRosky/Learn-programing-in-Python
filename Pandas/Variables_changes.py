###################################################################
###################################################################
#                   DataFrame variables changes                   #
###################################################################
###################################################################

############################################
# Let's check before de current directory  #
############################################

# Import the os module
import os

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

data = pd.read_excel (r'HealthCenter.xlsx') 

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

###################################
#    Changing variables type     #
###################################

data.dtypes

# Identificador                     object  --> string
# Edad                               int64  --> int
# Trabajador                         int64  --> string
# Sexo                               int64  --> strin
# Residencia                        object  -->
# Área                               int64  -->
# Estado Cita                        int64  -->
# % grasa                            int64  -->
# Condición %grasa                   int64  -->
# Principal Padecimiento Crónico     int64  -->
# Diagnóstico Macro                  int64  -->
# Diagnóstico Micro                  int64  -->
# Instancia de Atención              int64  -->
# Laboratorio                        int64  -->
# Rayos "X"                          int64  -->
# Consulta adicional                 int64  -->
# Incapacidad                        int64  -->
# Días                               int64  -->
# Monto de la consulta               int64  -->

# Var types in Pandas: dtype

# object
# int64
# float64
# bool
# datetime64
# timedelta[ds]
# category

data.info()

# Convert Edad to string

# df['DataFrame Column'] = df['DataFrame Column'].apply(str)

data['Edad'] = data['Edad'].apply(str)
data.info()

# Convert the Entire DataFrame to Strings


data = {'Product': ['ABC','DDD','XYZ'],
        'Price': [350,370,410],
        'Original Cost': [200,230,280]
        }

df = pd.DataFrame(data)

print (df)
print (df.dtypes)

# . applymap()

df = df.applymap(str)

df.info()

###############################################
# Strings to Integers in Pandas DataFrame
############################################

# Two approaches 
# 1.  df['DataFrame Column'] = df['DataFrame Column'].astype(int)      --> astype()
# 2. df['DataFrame Column'] = pd.to_numeric(df['DataFrame Column'])    --> to_numeric

# df['DataFrame Column'] = pd.to_numeric(df['DataFrame Column'])



data = {'Product': ['AAA','BBB'],
          'Price': ['210','250']}

df = pd.DataFrame(data)
print (df)
print (df.dtypes)

df['Price'] = pd.to_numeric(df['Price'],errors='coerce')

print (df)
print (df.dtypes)


###############################################
# Strings to Floats  in Pandas DataFrame
############################################

# Two approaches 
# 1.  df['DataFrame Column'] = df['DataFrame Column'].astype(float)      --> astype()
# 2. df['DataFrame Column'] = pd.to_numeric(df['DataFrame Column'],errors='coerce')    --> to_numeric

data = {'Product': ['ABC','XYZ'],
          'Price': ['250','270']
        }

df = pd.DataFrame(data)
print (df)
print (df.dtypes)

df = pd.DataFrame(data)
df['Price'] = df['Price'].astype(float)

print (df)
print (df.dtypes)

# or

data = {'Product': ['AAA','BBB','CCC','DDD'],
          'Price': ['250','ABC260','270','280XYZ']
        }

df = pd.DataFrame(data)

df = pd.DataFrame(data)
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

print (df)
print(df.dtypes)

# Convert Strings to Floats under the Entire DataFrame

data = {'Price_1': ['300','750','600','770','920'],
        'Price_2': ['250','270','950','580','410'],
        'Price_3': ['530','480','420','290','830']
        }

df = pd.DataFrame(data)

df = df.astype(float)

print (df)
print (df.dtypes)

###############################################
#  Integers to Floats in Pandas DataFrame     #
###############################################

# Two approaches 
# 1.  df['DataFrame Column'] = df['DataFrame Column'].astype(float)      --> astype()
# 2. df['DataFrame Column'] = pd.to_numeric(df['DataFrame Column'], downcast='float')   --> to_numeric

data = {'Product': ['AAA','BBB','CCC','DDD'],
          'Price': [300,500,700,900]
        }

df = pd.DataFrame(data)

print (df)
print (df.dtypes)

# 1. astype()

df['Price'] = df['Price'].astype(float)

print (df)
print (df.dtypes)

# 2. pd.to_numeric(df['DataFrame Column'], downcast='float')

import pandas as pd

data = {'Product': ['AAA','BBB','CCC','DDD'],
          'Price': [300,500,700,900]
        }

df = pd.DataFrame(data)
df['Price'] = pd.to_numeric(df['Price'], downcast='float')

print (df)
print (df.dtypes)


# From https://statisticsglobe.com/change-data-type-of-column-pandas-dataframe-python

data = pd.DataFrame({"x1":["10", "9", "8", "7"],  # Create example data
                     "x2":["1.1", "2.1", "3.1", "4.1"],
                     "x3":range(1, 5)})

data.dtypes

# Example 1: Convert pandas DataFrame Column to Integer

data["x1"] = data["x1"].astype(int)

# Example 2: Convert pandas DataFrame Column to Float

data["x2"] = data["x2"].astype(float)

# Example 3: Convert pandas DataFrame Column to String

data["x3"] = data["x3"].astype(str)  

# Exameple 4:  Convert Multiple Columns of pandas DataFrame to Different Data Types

data = data.astype({"x2": int, "x3": complex})  

# Example 5: Convert All Columns of pandas DataFrame to Other Data Type

data = data.astype(str)   

#   Example 6:  Convert pandas DataFrame Column to Other Data Type Using to_numeric Function

data["x1"] = pd.to_numeric(data["x1"])  

# Example 7: Convert All pandas DataFrame Columns to Other Data Type Using infer_objects Function
# The infer_objects command attempts to infer better data types for object columns, so for example it can be used to convert an
# object column to a more explicit class such as a string or an intege

data = data.infer_objects() 

# Example 8: Convert All pandas DataFrame Columns to Other Data Type Using convert_dtypes Function
# Another function that is used to convert columns to the best possible data types is the convert_dtypes function. 
# It can be applied as follows:

data = data.convert_dtypes()  