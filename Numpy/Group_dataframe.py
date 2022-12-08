###################################################################
###################################################################
#                 Data Manipulation group by                      #
###################################################################
###################################################################

# https://www.geeksforgeeks.org/python-pandas-dataframe-groupby/#:~:text=Pandas%20groupby%20is%20used%20for,groups%20based%20on%20some%20criteria.
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html
# https://realpython.com/pandas-groupby/
# https://towardsdatascience.com/5-pandas-group-by-tricks-you-should-know-in-python-f53246c92c94


# Pandas groupby is used for grouping the data according to the categories and apply a function to the categories. 
# It also helps to aggregate data efficiently.

# Pandas dataframe.groupby() function is used to split the data into groups based on some criteria. pandas objects can be split
# on any of their axes. The abstract definition of grouping is to provide a mapping of labels to group names.

# Syntax: DataFrame.groupby(by=None, axis=0, level=None, as_index=True, sort=True, group_keys=True, squeeze=False, **kwargs)

# Parameters :
# by : mapping, function, str, or iterable
# axis : int, default 0
# level : If the axis is a MultiIndex (hierarchical), group by a particular level or levels
# as_index : For aggregated output, return object with group labels as the index. Only relevant for DataFrame input. as_index=False is effectively “SQL-style” grouped output
# sort : Sort group keys. Get better performance by turning this off. Note this does not influence the order of observations within each group. groupby preserves the order of rows within each group.
# group_keys : When calling apply, add group keys to index to identify pieces
# squeeze : Reduce the dimensionality of the return type if possible, otherwise return a consistent type

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
df = pd.read_csv("nba.csv")
  

# Example #1: Use groupby() function to group the data based on the “Team”.
 
 # applying groupby() function to
# group the data on team value.
gk = df.groupby('Team')

gk.first()

# Let’s print the value contained any one of group. For that use the name of the team. 
# We use the function get_group() to find the entries contained in any of the groups.

# Finding the values contained in the "Boston Celtics" group
gk.get_group('Boston Celtics')

# Example #2: Use groupby() function to form groups based on more than one category (i.e. Use more than one column to perform the splitting).

# First grouping based on "Team"
# Within each team we are grouping based on "Position"
gkk = df.groupby(['Team', 'Position'])
  
# Print the first value in each group
gkk.first()