###################################################################
###################################################################
#                 Data Manipulation summary statistics            #
###################################################################
###################################################################

# https://pandas.pydata.org/pandas-docs/stable/getting_started/intro_tutorials/06_calculate_statistics.html
# https://datagy.io/pandas-exploratory-data-analysis/
# https://www.geeksforgeeks.org/pandas-groupby-summarising-aggregating-and-grouping-data-in-python/
# https://www.nbshare.io/notebook/17251835/Summarising-Aggregating-and-Grouping-data-in-Python-Pandas/



# Let's check the main summary statistics  in a DataFrame

# Returns : GroupBy object

# Let's see some examples 

import os
import pandas as pd

cwd = os.getcwd()
cwd

path = 'C:\\Users\\oscar\\Desktop\\GitHub\\Python\\Data-Manipulation\Pandas'

# Change the current working directory
os.chdir(path)

print("Current working directory: {0}".format(os.getcwd()))
  
# Creating the dataframe 
titanic  = pd.read_csv("titanic.csv")


titanic.head()

###########################
# Aggregating statistics  #
###########################

titanic["Age"].mean()

titanic[["Age", "Fare"]].median()

titanic[["Age", "Fare"]].describe() # give everything

# Instead of the predefined statistics, specific combinations of aggregating statistics for given columns can be defined using the DataFrame.agg() method:

titanic.agg(
    {
        "Age": ["min", "max", "median", "skew"],
        "Fare": ["min", "max", "median", "mean"],
    }
)

###############################################
# Aggregating statistics grouped by category  #
###############################################

titanic[["Sex", "Age"]].groupby("Sex").mean()

# Calculating a given statistic (e.g. mean age) for each category in a column (e.g. male/female in the Sex column) is a common pattern. The groupby method is used to support this type of operations. This fits in the more general split-apply-combine pattern:

# Split the data into groups

# Apply a function to each group independently

# Combine the results into a data structure

# The apply and combine steps are typically done together in pandas.

# In the previous example, we explicitly selected the 2 columns first. If not, the mean method is applied to each column containing numerical columns by passing numeric_only=True:

titanic.groupby("Sex").mean(numeric_only=True)   # ---> All columns

# It does not make much sense to get the average value of the Pclass. If we are only interested in the average age for each gender, 
# the selection of columns (rectangular brackets [] as usual) is supported on the grouped data as well:

titanic.groupby("Sex")["Age"].mean()

titanic.groupby(["Sex", "Pclass"])["Fare"].mean()

###############################################
#     Count number of records by category     #
###############################################

titanic["Pclass"].value_counts()
titanic.groupby("Pclass")["Pclass"].count()


###############################################
#                  Aggregation                #
###############################################

# Aggregation is used to get the mean, average, variance and standard deviation of all column in a dataframe or particular column in a data frame.

# sum(): It returns the sum of the data frame
# Syntax:

# dataframe[‘column].sum()

# mean(): It returns the mean of the particular column in a data frame
# Syntax:

# dataframe[‘column].mean()

# std(): It returns the standard deviation of that column.
# Syntax:

# dataframe[‘column].std()

# var(): It returns the variance of that column
# dataframe[‘column’].var()

# min(): It returns the minimum value in column
# Syntax:

# dataframe[‘column’].min()

# max(): It returns maximum value in column
# Syntax:

# dataframe[‘column’].max()

#### Examples 


# importing pandas as pd for using data frame
import pandas as pd
 
# creating dataframe with student details
dataframe = pd.DataFrame({'id': [7058, 4511, 7014, 7033],
                          'name': ['sravan', 'manoj', 'aditya', 'bhanu'],
                          'Maths_marks': [99, 97, 88, 90],
                          'Chemistry_marks': [89, 99, 99, 90],
                          'telugu_marks': [99, 97, 88, 80],
                          'hindi_marks': [99, 97, 56, 67],
                          'social_marks': [79, 97, 78, 90], })
 
# display dataframe
dataframe

# getting all minimum values from
# all columns in a dataframe
print(dataframe.min())
print("-----------------------------------------")
 
# minimum value from a particular
# column in a data frame
print(dataframe['Maths_marks'].min())
print("-----------------------------------------")
 
# computing maximum values
print(dataframe.max())
print("-----------------------------------------")
 
# computing sum
print(dataframe.sum())
print("-----------------------------------------")
 
# finding count
print(dataframe.count())
print("-----------------------------------------")
 
 
# computing standard deviation
print(dataframe.std())
print("-----------------------------------------")
 
# computing variance
print(dataframe.var())

###############################################
#                  Grouping                   #
###############################################

# It is used to group one or more columns in a dataframe by using the groupby() method. Groupby mainly refers to a process involving one or more of the following steps they are:

# Splitting: It is a process in which we split data into group by applying some conditions on datasets.
# Applying: It is a process in which we apply a function to each group independently
# Combining: It is a process in which we combine different datasets after applying groupby and results in a data structure

# Example 1

# importing pandas as pd for using data frame
import pandas as pd
 

# creating dataframe with student details
dataframe = pd.DataFrame({'id': [7058, 4511, 7014, 7033],
                          'name': ['sravan', 'manoj', 'aditya', 'bhanu'],
                          'Maths_marks': [99, 97, 88, 90],
                          'Chemistry_marks': [89, 99, 99, 90],
                          'telugu_marks': [99, 97, 88, 80],
                          'hindi_marks': [99, 97, 56, 67],
                          'social_marks': [79, 97, 78, 90], })
 
 
# group by name
print(dataframe.groupby('name').first())
 
print("---------------------------------")
# group by name with social_marks sum
print(dataframe.groupby('name')['social_marks'].sum())
print("---------------------------------")
 
# group by name with maths_marks count
print(dataframe.groupby('name')['Maths_marks'].count())
print("---------------------------------")
 
# group by name with maths_marks
print(dataframe.groupby('name')['Maths_marks'])

# Example 2

# importing pandas as pd for using data frame
import pandas as pd
 
# creating dataframe with student details
dataframe = pd.DataFrame({'id': [7058, 4511, 7014, 7033],
                          'name': ['sravan', 'manoj', 'aditya', 'bhanu'],
                          'Maths_marks': [99, 97, 88, 90],
                          'Chemistry_marks': [89, 99, 99, 90],
                          'telugu_marks': [99, 97, 88, 80],
                          'hindi_marks': [99, 97, 56, 67],
                          'social_marks': [79, 97, 78, 90], })
 
# group by name
print(dataframe.groupby('name').first())
 
print("------------------------")
# group by name with social_marks sum
print(dataframe.groupby('name')['social_marks'].sum())
print("------------------------")
# group by name with maths_marks count
print(dataframe.groupby('name')['Maths_marks'].count())