#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
import sys
import subprocess
import os,timeit
import dis

def task1():
    print(sys.argv[1:])
    l = sys.argv[1:]
    #python_executor(l)
    result = dict()
    for i in sys.argv[1:]:
        if os.path.exists(i):
            timer = timeit.timeit(lambda : subprocess.run(["python3",i],stdout = subprocess.PIPE),number = 1)
            result[i] = timer
    print(result)


            
if len(sys.argv) == 1:
    print("Error")
else:
    task1()
    

