#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Exercise 10.2 write a function called cumsum that takes a list of numbers and returns the cumulative sum
# t = [1, 2 ,3]
#cumsum(t)
#[1, 3, 6]


# In[11]:


t = [1, 2 ,3, 4, 5, 6, 7, 8]

def cumsum(t):
    total = 0
    res = []
    for number in t:
        total += number
        res.append(total)
    return res
        


# In[12]:


cumsum(t)


# In[ ]:




