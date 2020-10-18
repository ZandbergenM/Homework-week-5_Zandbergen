#!/usr/bin/env python
# coding: utf-8

# In[2]:


#10.1 Write a function called nested_sum that takes a list of integers and adds up the elements from all of the nested lists


# In[4]:


#Example
#t = [[1, 2], [3], [4, 5, 6]]
#nested_sum(t)
#21


# In[21]:


t = [[1, 2], [3], [4, 5, 6], [7, 8, 9]]

def nested_sum(t):
    total = 0
    for lists in t:
        total += sum(lists)
    return total


# In[22]:


nested_sum(t)


# In[ ]:




