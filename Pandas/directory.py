###################################################################
###################################################################
#               Get and Set directory in Python                   #
###################################################################
###################################################################

##################################
#   Get a working dir in python  #
###################################

# Import the os module
import os

# Get the current working directory  : os.getcwd()
cwd = os.getcwd()
cwd

# Print the current working directory
print("Current working directory: {0}".format(cwd))

# Print the type of the returned object
print("os.getcwd() returns an object of type: {0}".format(type(cwd)))

###########################################
#   Changing the Current Working Directory #
###########################################

# To change the current working directory in Python, use the chdir() method.

# os.getcwd(path)

# The method accepts one argument, the path to the directory to which you want to change. 
# The path argument can be absolute or relative.

# Change the current working directory

# Import the os module
import os

# Print the current working directory
print("Current working directory: {0}".format(os.getcwd()))

path = 'C:\\Users\\oscar\\Desktop\\GitHub\\Python\\Data-Manipulation\Pandas'

# Change the current working directory
os.chdir(path)

# Let's check the new directory 

print("Current working directory: {0}".format(os.getcwd()))

# The argument provided to the chdir() method must be a directory; otherwise NotADirectoryError exception
# is raised. If the specified directory doesn’t exist, a FileNotFoundError exception is raised. If the user
# under which the script is running doesn’t have the necessary permissions, a PermissionError exception is raised.

# Import the os module
import os

path = 'C:\\Users\\oscar\\Desktop\\GitHub\\Python\\Data-Manipulation\Pandas'

try:
    os.chdir(path)
    print("Current working directory: {0}".format(os.getcwd()))
except FileNotFoundError:
    print("Directory: {0} does not exist".format(path))
except NotADirectoryError:
    print("{0} is not a directory".format(path))
except PermissionError:
    print("You do not have permissions to change to {0}".format(path))
    
# So, to find the current working directory in Python, use os.getcwd(), and to change the current working directory,
# use os.chdir(path).