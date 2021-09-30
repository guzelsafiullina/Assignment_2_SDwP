#!/usr/bin/env python
# coding: utf-8

# In[4]:


def filter_new(list = [1,2,3,4,5],action = lambda i: i+1):
    '''Performs an action on the given list'''
    newList = []
    for item in list:
        newList.append(action(item))
    return newList
filter_new([3224,3415,253,124], lambda i: i**2)


# In[ ]:




