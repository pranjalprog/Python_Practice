# from means is first file chai method import karwao 
# __pychache__  ->  source change and python version
#                   first.cpython-313.pyc
#               ->  works only for imported files
#               ->  not for top level files 
  

from first import chai

chai("ginger tea")

# > python chai.py
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