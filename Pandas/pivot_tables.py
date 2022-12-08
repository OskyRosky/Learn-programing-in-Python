###################################################################
###################################################################
#                         Pivot table                             #
###################################################################
###################################################################

# https://analyticsindiamag.com/how-to-create-a-pivot-table-in-python-from-scratch/#:~:text=A%20Pivot%20table%20is%20an,variables%20based%20on%20categorical%20variables.
# https://jakevdp.github.io/PythonDataScienceHandbook/03.09-pivot-tables.html
# https://pandas.pydata.org/docs/reference/api/pandas.pivot_table.html
# https://www.machinelearningplus.com/pandas/pandas-pivot-table-in-python/
# https://datagy.io/python-pivot-tables/    ---> very cool 
# https://www.analyticsvidhya.com/blog/2020/03/pivot-table-pandas-python/
# https://www.youtube.com/watch?v=hA4l2ePFjfM&ab_channel=FrankAndrade
# https://www.youtube.com/watch?v=OJDBUXNySWI&ab_channel=ShwetaLodha
# https://builtin.com/data-science/pandas-pivot-tables


# To create a spreadsheet-style pivot table as a data frame in python, we use pandas.pivot_table() function. 

# pandas.pivot_table(data, 
#                    values=None, 
#                      index=None, 
#                      columns=None, 
#                      aggfunc='mean',
#                      fill_value=None, 
#                       margins=False, 
#                       dropna=True, 
#                       margins_name='All', 
#                       observed=False,
#                         sort=True)

# data: data frame ( Defining the dataset that is to be used for the pivot table.) 
#values: column to aggregate ( Feature that is to be seen in its statistical summary.)
#index: column ( Indexes the value passed in the value argument )
#columns: column ( For aggregating values based on certain features )
#aggfunc: function or list of functions ( Aggregating functions like sum, mean, etc )
#fill_value: scalar ( Value to replace missing values in the table )
#margins: bool ( Add all row / columns ( e.g. for subtotal / grand totals ) )

# Creating a pivot table: By specifying the index and columns parameters in the pd.pivot_table() function, 
# you can determine which features should appear in the columns and rows. In the values parameter, you should 
# specify which feature should be used to fill in the cell values.

import pandas as pd
import numpy as np

# data

df = pd.DataFrame({'Name': ['Minecraft', 'Grand Theft Auto V', 'Tetris (EA)', 'Wii Sports', 'PUBG: Battlegrounds', ],
                   'Genre': ['Survival,Sandbox', 'Action-adventure', 'Puzzle', 'Sports simulation', 'Battle royale'],
                   'Platform': ['Multi-platform', 'Multi-platform', 'Multi-platform', 
                            'Wii', 'PC'],
                   'Publishers': ['Xbox Game Studios', 'Rockstar Games', 'Electronic Arts', 
                                  'Nintendo', 'PUBG Corporation'],
                   'Total_Year': [9, 7, 14, 10, 5],
                   'Sales': [238, 160, 100, 82, 75]})
df

# Create pivot table using pandas

table = pd.pivot_table( data=df, 
                        index=['Platform'], 
                        columns=['Publishers'], 
                        values='Sales',
                        aggfunc='mean')
table

# Using multiple aggregation functions

# if the column parameter is not specified, it will aggregate based on the index. So, let’s not specify the column parameter and see what changes happen in our pivot table.

table2 = pd.pivot_table(data=df, 
                        index=['Platform'],
                        values='Sales',
                        aggfunc=['sum', 'mean', 'count'])
table2

# ! As discussed above, if the column parameter is not specified, the function itself aggregates on the index parameter.


# Aggregating for multiple features and specific features

## Additionally, we can perform different aggregations based on different features. The result is that multiple pivot tables need not be created to apply appropriate operations to different features.

table3 = pd.pivot_table(data=df, 
                        index='Platform', 
                        values=['Sales', 'Total_Year'],
                        columns=['Publishers'],
                        aggfunc={'Sales': np.sum, 'Total_Year': np.mean})
table3

# Replacing missing values
## In the data frame, there are a lot of missing values that can be handled by filling those by specifying the value in the fill_value parameter.

table4 = pd.pivot_table(data=df, 
                        index='Platform', 
                        values=['Sales', 'Total_Year'],
                        columns=['Publishers'],
                        aggfunc={'Sales': np.sum, 'Total_Year': np.mean},
                        fill_value='MISSING')
table4

# Calculate row and column total
## Next, let’s examine the sales totals of each category of the platform. To do this, we will use the margins and margins_name parameters.

table5 = pd.pivot_table(data=df, 
                        index=['Platform'],
                        values='Sales',
                        aggfunc=['sum', 'mean', 'count'],
                        margins=True,
                        margins_name='Grand Total')
table5

# We can observe in that output that a new index is added as a total which contains the total sales for different aggregation functions applied on the sales column.

# Multi-level index pivot table
## Based on the above pivot tables, only one feature was used in the index, i.e., a single level index.
# We can, however, create pivot tables using multiple indices. Whenever data is organized hierarchically,
# a pivot table with multi-level indexes can provide very useful and detailed summary information.

table6 = pd.pivot_table(data=df,
                        index=['Platform', 'Genre'],
                        values='Sales',
                        aggfunc=['sum', 'mean', 'count'],
                        margins=True,
                        margins_name='Grand Total')
table6

###############
###############
###############

import pandas as pd
import numpy as np
from sklearn.datasets import fetch_openml

X,y = fetch_openml("autos", version=1, as_frame=True, return_X_y=True)
data = X
data['target'] = y

pivot = np.round(pd.pivot_table(data, values='price', 
                                index='num-of-doors', 
                                columns='fuel-type', 
                                aggfunc=np.mean),2)
pivot