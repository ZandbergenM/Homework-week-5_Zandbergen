#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import os
import matplotlib.pyplot as plot


# In[4]:


pwd


# In[5]:


df1 = pd.read_csv(r"C:/Users/zandb/OneDrive/Documents/Northeastern/Classwork/GIS 6345 Geospatial Programming/Week 5/Assignments/Part 2/Crime.csv")


# In[20]:


df1.head()


# In[28]:


df1.plot.bar(x= 'COUNTY', rot = 45, y = 'DRUG_VIOLATIONS')


# In[ ]:




