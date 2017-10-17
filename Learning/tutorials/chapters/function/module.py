# Modules refer to a file containing Python statements and definitions.

# We use modules to break down large programs into small manageable and organized files.
# Furthermore, modules provide reusability of code.

# Python from...import statement
# We can import specific names form a module without importing the module as a whole. Here is an example.

from arithmetic import mul

print(mul(10,11))

# Import with renaming
# We can import a module by renaming it as follows.

import math as m

print(m.pi)

#Python Module Search Path
#While importing a module, Python looks at several places. Interpreter first looks for a built-in module then
#  (if not found) into a list of directories defined in sys.path. The search is in this order.

#The current directory.
#PYTHONPATH (an environment variable with a list of directory).
#The installation-dependent default directory.


#Reloading a module
#The Python interpreter imports a module only once during a session. This makes things more efficient.
