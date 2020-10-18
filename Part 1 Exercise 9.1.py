#!/usr/bin/env python
# coding: utf-8

# In[7]:


#9.1Write a program that reads words.txt and prints only the words with more than 20 characters

fin = open('words.txt')

def read(x):
    for line in fin:
        word = line.strip()
        if len(word)>20:
            print(word)
        
read(fin)


# In[6]:


pwd


# In[ ]:





# In[ ]:





# In[ ]:




