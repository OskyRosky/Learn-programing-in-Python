###################################################################
###################################################################
#                 Operations with string variables                #
###################################################################
###################################################################

# https://docs.python.org/3/library/stdtypes.html#string-methods
# https://pandas.pydata.org/pandas-docs/stable/user_guide/text.html
# https://www.aboutdatablog.com/post/10-most-useful-string-functions-in-pandas


# Pandas provides a set of string functions which make it easy to operate on string data. Most importantly, these functions ignore (or exclude) missing/NaN values.

# Almost, all of these methods work with Python string functions (refer: https://docs.python.org/3/library/stdtypes.html#string-methods). So, convert the Series Object to String Object and then perform the operation.

# Let us now see how each operation performs.


# 1	 lower() Converts strings in the Series/Index to lower case.

# 2 upper() Converts strings in the Series/Index to upper case.

# 3	len() Computes String length().

# 4	strip() Helps strip whitespace(including newline) from each string in the Series/index from both the sides.

# 5  split(' ') Splits each string with the given pattern.

# 6  cat(sep=' ')  Concatenates the series/index elements with given separator.

# 7	get_dummies() Returns the DataFrame with One-Hot Encoded values.

# 8 contains(pattern)  Returns a Boolean value True for each element if the substring contains in the element, else False.

# 9 replace(a,b) Replaces the value a with the value b.

# 10  repeat(value) Repeats each element with specified number of times.

# 11 count(pattern) Returns count of appearance of pattern in each element.

# 12 startswith(pattern)  Returns true if the element in the Series/Index starts with the pattern.

# 13 endswith(pattern) Returns true if the element in the Series/Index ends with the pattern.

# 14 find(pattern) Returns the first position of the first occurrence of the pattern.

# 15  findall(pattern)  Returns a list of all occurrence of the pattern.

# 16 swapcase Swaps the case lower/upper.

# 17 islower() Checks whether all characters in each string in the Series/Index in lower case or not. Returns Boolean

# 18 isupper() Checks whether all characters in each string in the Series/Index in upper case or not. Returns Boolean.

# 19 isnumeric() Checks whether all characters in each string in the Series/Index are numeric. Returns Boolean.

##########
#  Data  #
##########

import pandas as pd
import numpy as np

s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t', np.nan, '1234','SteveSmith'])

s


# lower()

s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t', np.nan, '1234','SteveSmith'])

s.str.lower()

# upper()

s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t', np.nan, '1234','SteveSmith'])

s.str.upper()

# len()

s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t', np.nan, '1234','SteveSmith'])
s.str.len()

# strip()

s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
s
print ("After Stripping:")
s.str.strip()

# split(pattern)

s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
s
print("Split Pattern:")
s.str.split(' ')

# cat(sep=pattern)

s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])

s.str.cat(sep='_')

# get_dummies()

s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])

s.str.get_dummies()

# contains ()

s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])

s.str.contains(' ')

# replace(a,b)

s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])

print ("After replacing @ with $:")
s.str.replace('@','$')

# repeat(value)

s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])

s.str.repeat(2)

# count(pattern)

s = pd.Series(['Tommmmmmmm', ' William Rick', 'John', 'Alber@t'])

print ("The number of 'm's in each string:")
s.str.count('m')

# startswith(pattern) 

s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])

print("Strings that start with 'T':")
s.str. startswith ('T')

# endswith(pattern)

s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
print("Strings that end with 't':")
s.str.endswith('t')

# find(pattern)

s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])

s.str.find('e')

# findall(pattern)

s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])

s.str.findall('e')

# swapcase()

s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t'])
s.str.swapcase()

# islower()

s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t'])
s.str.islower()

# isupper()

s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t'])

s.str.isupper()

# isnumeric()

s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t'])

s.str.isnumeric()