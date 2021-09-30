#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def pascal_triangle(n):   
    """This function calculates coefficients for the Pascal Triangle"""
    def next_string(a):    
        b = [0]
        for i in range(len(a)-1):
            b.append(a[i]+a[i+1])
        b.append(0)
        return(b)

    a = [0,1,0]

    for i  in range(n):
        print(a[1:len(a)-1])
        a = next_string(a)

