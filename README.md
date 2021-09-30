# Assignment_2_SDwP
In this repo you can find programs that works with execution time of programs, work with bytecode of code snippets, programs in py- files and pyc- files.
Requirements files time, sys, subprocess, os,timeit, dis, marshal, tempfile, py_compile
## compare_time.py
It takes N arbitrary .py files and creates a neat table out of their execution time. 

Example:
``` python
usage: compare.py [files]
input: python3 compare_time.py src1.py src2.py src3.py
```
``` python
output: {'src1.py': 0.10321269999999999, 'src2.py': 0.09951339999999997, 'src3.py': 0.10906860000000002} 
```
## bc.py (Bytecode printer)
Bytecode printer can compile py- files and and code snippets.
But the main function of Bytecode printer is to yield opcodes (and their arguments) for ordinary python programs, code snippets and pyc- files. The opcodes are ”machine” instructions produced out of your program for executing them on Python Virtual Machine. 

Example
```python
usage: bc.py action [-flag value]*
This program ...
compile
    -py file.py compile file into bytecode and store it as file.pyc
    -s "src" compile src into bytecode and store it as out.pyc
print
    -py src.py produce human-readable bytecode from python file
    -pyc src.pyc produce human-readable bytecode from compiled .pyc file
    -s "src" produce human-readable bytecode from normal string
```
Examples
```python
input: python3 bc.py print -s "print(54+4525)"
output:
LOAD_NAME       print
LOAD_CONST      4579
CALL_FUNCTION
RETURN_VALUE
```
```python
input: python3 bc.py print -py src1.py
output:
LOAD_CONST      0
BUILD_LIST
STORE_FAST      b
SETUP_LOOP      to 58
LOAD_GLOBAL     range
...
```
```python
input: python3 bc.py compile -py src1.py
       ls
output:
-a----        30.09.2021     13:16            398 src1.py
-a----        30.09.2021     19:24            602 src1.pyc

```
``` python
input: python3 bc.py print -pyc src1.pyc
LOAD_CONST      0
BUILD_LIST
STORE_FAST      b
SETUP_LOOP      to 58
...
```
## bc_with_compare.py
This program is extended version of bc_printer.py. 
It can compare bytecode among different sources and produce neat table with stats of the used opcodes (and only them).

```python
usage: bc.py action [-flag value]*
This program ...
compile
    -py file.py compile file into bytecode and store it as file.pyc
    -s "src" compile src into bytecode and store it as out.pyc
print
    -py src.py
    -pyc src.pyc produce human-readable bytecode from python file produce human-readable bytecode from compiled .pyc file
    -s "src" produce human-readable bytecode from normal string
compare -format src [-format src]+
    produce bytecode comparison for giving sources 
    (supported formats -py, -pyc, -s)
```
Examples

```python
$ python3 bc.py compare -py src1.py -py src2.py -py src3.py

INSTRUCTION | src1.py | src2.py | src3.py
LOAD_FAST       15         8         3
POP_TOP         0         12         0
CALL_FUNCTION   9          0         0
LOAD_NAME       9          3         9
RETURN_VALUE    3          3         3
```
