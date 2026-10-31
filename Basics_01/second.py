# from means is first file chai method import karwao 
# __pychache__  ->  source change and python version
#                   first.cpython-313.pyc
#               ->  works only for imported files
#               ->  not for top level files 
  

from first import chai

chai("ginger tea")

# > python first .py
# 
# [File] ---> Byte Code ---> Python VM (Virtual Machine)
#              ^
#        mostly hidden
#
# 1. Compile to Byte Code
#              ^
#     low level & Platform Independent
#
# -> Byte Code runs faster
# .pyc -> Compiled python (frozen Binaries)


# Python virtual machine (PVM)  - basically software hai  
# code loop to iterate byte code 
# Run time engine
# Also known as python interpreter

# ---> BYTE CODE IS NOTE MACHINE CODE
# python specific interpretation
#cpython(standard implementation) , jpython, iron python , stackless , pypy


# MODULE -> dusre ki likhi hua code hai,jisko hum direclty use kar shakte hai or modification kar shakte hai aapne code mai 
#   import os
#   >>> os.getcwd()
#   'E:\\OneDrive\\Desktop\\Python\\Basics_01'
#   >>> 

#  1. NameError
#  What is it?
#  A NameError happens when Python tries to look up a variable or function name that does not exist or has not been defined yet.

#  2. IndentationError
#  What is it?
#  Python uses whitespace (spaces or tabs) to define code blocks (like inside loops, functions, or if statements) instead of curly braces {}. An IndentationError happens when your spacing is inconsistent or incorrect.

# >>> import sys 
# >>> sys.platform
# 'win32'
#  >>> 

# WHAT WE USE IT FOR:
# reload() updates a previously imported module during runtime. 
# If you change a module's code file, you use reload() to test 
# your changes immediately without restarting your Python shell/program.

# HOW TO USE IT:
import my_module                  # 1. Import your module normally
from importlib import reload     # 2. Import the reload function

# (Imagine you changed and saved code inside 'my_module.py')

reload(my_module)                # 3. Call reload() passing the module name


