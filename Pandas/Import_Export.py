###################################################################
###################################################################
#                      Import - Export files                      #
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
data.columns


# df = pd.DataFrame(data, columns= ['Product'])

# First 5 rows

first5 = data.head(5)
first5

# Lasts 5 rows

lasts5 = data.tail(5)
lasts5

###################################
#   Import data from csv files    #
###################################

# https://www.w3schools.com/python/pandas/pandas_csv.asp

data2_cvs = pd.read_csv(r'C:\Users\oscar\Desktop\GitHub\Python\Data-Manipulation\Pandas\data_csv.csv')
data2_cvs

print(df.to_string()) 

print(pd.options.display.max_rows) 

# pd.options.display.max_rows = 9999

# print(pd.options.display.max_rows)

######################################
#   Export a .xlsx fiel from python  #
######################################

import os

os.getcwd()

# A new Data Frame 
d_data = pd.DataFrame({'ID': {0: 23, 1: 43, 2: 12,
                                 3: 13, 4: 67, 5: 89,
                                 6: 90, 7: 56, 8: 34},
                          'Name': {0: 'Ram', 1: 'Deep',
                                   2: 'Yash', 3: 'Aman',
                                   4: 'Arjun', 5: 'Aditya',
                                   6: 'Divya', 7: 'Chalsea',
                                   8: 'Akash' },
                          'Marks': {0: 89, 1: 97, 2: 45, 3: 78,
                                    4: 56, 5: 76, 6: 100, 7: 87,
                                    8: 81},
                          'Grade': {0: 'B', 1: 'A', 2: 'F', 3: 'C',
                                    4: 'E', 5: 'C', 6: 'A', 7: 'B',
                                    8: 'B'}})

d_data.index
d_data.Name
d_data
  

  
# determining the name of the file
file_name = 'LetsExport.xlsx'
  
# saving the excel
d_data.to_excel(file_name)