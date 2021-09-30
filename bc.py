#!/usr/bin/env python
# coding: utf-8

# In[6]:


import time
import sys
import subprocess
import os,timeit
import dis
import marshal
    
from tempfile import NamedTemporaryFile
import py_compile

def get_bytecode(arg):
    return dis.Bytecode(arg)

def expand_bytecode(bytecode):
        result = []
        for instruction in bytecode:
            if str(type(instruction.argval)) == "<class 'code'>":
                result += expand_bytecode(dis.Bytecode(instruction.argval))
            else:
                result.append(instruction)
            
        return result


def compile():
    for i in sys.argv[3:]:
        if sys.argv[2]=="-py":
            try:
                py_compile.compile(i, cfile= i + "c")
            except Exception as e:
                print(f"We skipping {i}")
                
        elif sys.argv[2] == "-pyc":
            pass
        elif sys.argv[2] == "-s":
            with NamedTemporaryFile("w",delete = True) as tmp:
                tmp.write(i)
                tmp.seek(0)
                py_compile.compile(tmp.name, cfile="out.pyc")
        else:
            print("Error")
            return
    
def print_bc(arg):
    for i in sys.argv[3:]:
        source = None
        
        if sys.argv[2]=="-py":
            with open(i,'r') as f:
                source = f.read()
                
        elif sys.argv[2] == "-pyc":
            header_size = 12
            if sys.version_info >= (3,7):
                header_size = 16
            with open(i,'r') as f:
                f.seek(header_size)
                source = marshal.load(f)
        elif sys.argv[2] == "-s":
            source = i
        else:
            print("Error")
            return
                
            
        bc = get_bytecode(source)
        res = expand_bytecode(bc)
        for instruction in res:
            print(f"{instruction.opname}\t{instruction.argrepr}")  
            
         
        
#if name == '__main__':
if len(sys.argv) == 1:
    print("Error")
else:
    if sys.argv[1] == "print":
        print_bc(None)
    elif sys.argv[1] == "compile":
        compile()
    elif sys.argv[1] == "compare":
        pass
    else: print("Error")


# In[ ]:




