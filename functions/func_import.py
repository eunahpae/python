import func_kwargs
from func_args import hello_name
from func_kwargs import *

from func_kwargs import name_hello as nh

import numpy as np


func_kwargs.name_hello(a="배",b="김",c="박")
data = hello_name(1,2,3,4,5)
print(data)
name_hello(a="배",b="김",c="박")
nh(a="배",b="김",c="박")

# 상위경로 import
import sys, os
print(os.path.dirname(__file__))
print(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
print(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import hello

file_path= "C:\apps\test"
sys.path.append(file_path)


list_1 = [1,2,3,4,5]
list_2 = [2,5,4,6,3]
a = np.array(list_1)
b = np.array(list_2)
print(list_1+list_2)
print(a+b)


