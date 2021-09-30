#!/usr/bin/env python
# coding: utf-8

# In[2]:


from math import sqrt
def quadratic_equation(a = 1,b = 2,c = 1):
    """This function finds roots of the quadratic equation"""
    D = b*b - 4*a*c
    if a==0 :
        if b!=0: print -c/b
        else: print("No roots")
    else:
        if D>0:
            print("x_1 = ", (-b+sqrt(D))/(2*a), "x_2 = ",(-b-sqrt(D))/(2*a))
        elif D==0: print("x = ",-b/(2*a))
        else: print("No real decision")
            
            
quadratic_equation(1,35,5)


# In[ ]:




