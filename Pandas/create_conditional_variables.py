########################################################################
########################################################################
#              Replace Values in Pandas DataFramen                 #####
########################################################################
########################################################################

# https://www.geeksforgeeks.org/python-creating-a-pandas-dataframe-column-based-on-a-given-condition/
# https://medium.com/analytics-vidhya/pandas-how-to-change-value-based-on-condition-fc8ee38ba529
#
# 



# importing pandas as pd
import pandas as pd
 
# Creating the dataframe
df = pd.DataFrame({'Date' : ['11/8/2011', '11/9/2011', '11/10/2011',
                                        '11/11/2011', '11/12/2011'],
                'Event' : ['Music', 'Poetry', 'Music', 'Comedy', 'Poetry'],
                'Salary': [123,3123,34234,34234,234234]
                
                })

df


# Method 1: Using list comprehension
#Now we will add a new column called ‘Price’ to the dataframe. For that purpose, we will use list comprehension technique.
# Set the price to 1500 if the ‘Event’ is ‘Music’ else 800. 

# Add a new column named 'Price'
df['Price'] = [1500 if x =='Music' else 800 for x in df['Event']]
df

df['Status'] = ['Rch' if x>=10000 else 'Poor' for x in df['Salary']]

# Method 2: Using DataFrame.apply() function

# We can use DataFrame.apply() function to achieve the goal. There could be instances when we have more than two values, 
# in that case, we can use a dictionary to map new values onto the keys. This does provide a lot of flexibility when we 
# are having a larger number of categories for which we want to assign different values to the newly added column. 

# add a new column called ‘Price’ to the dataframe. For that purpose we will use DataFrame.apply() function to achieve 
# the goal. Set the price to 1500 if the ‘Event’ is ‘Music’, 1200 if the ‘Event’ is ‘Comedy’ and 800 if the ‘Event’ is ‘Poetry’. 

# Define a function to map the values
def set_value(row_number, assigned_value):
    return assigned_value[row_number]
 
# Create the dictionary
event_dictionary ={'Music' : 1500, 'Poetry' : 800, 'Comedy' : 1200}
 
# Add a new column named 'Price'
df['Price'] = df['Event'].apply(set_value, args =(event_dictionary ,))
 
# Print the DataFrame
print(df)

# Method 3: Using DataFrame.map() function

# We can use DataFrame.map() function to achieve the goal. It is a very straight forward method where we use a dictionary 
# to simply map values to the newly added column based on the key. 
# add a new column called ‘Price’ to the dataframe. For that purpose we will use DataFrame.map() function to achieve the goal. 
# Set the price to 1500 if the ‘Event’ is ‘Music’, 1200 if the ‘Event’ is ‘Comedy’ and 800 if the ‘Event’ is ‘Poetry’. 

# Create the dictionary
event_dictionary ={'Music' : 1500, 'Poetry' : 800, 'Comedy' : 1200}
 
# Add a new column named 'Price'
df['Price'] = df['Event'].map(event_dictionary)
 
# Print the DataFrame
print(df)

# Method 4: Using numpy.where() function
# We can use numpy.where() function to achieve the goal. It is a very straight forward method where we use a where condition to simply map values to the newly added column based on the condition. 
# Now we will add a new column called ‘Price’ to the dataframe. Set the price to 1500 if the ‘Event’ is ‘Music’, 1500 and rest all the events to 800.

df['Price'] = np.where(df['Event']
                       =='Music', 1500,800 )
 
print(df)