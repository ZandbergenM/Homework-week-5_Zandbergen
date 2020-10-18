#!/usr/bin/env python
# coding: utf-8

# In[1]:


#9.2 Write a function called has_no_e that returns True if the given word doesn't have the letter "e" in it
# Write a program that reads words.txt and prints only the words that have no "e", Compute the percentage of words in the list that have no "e"


# In[67]:


def has_no_e(word):
    if "e" in word:
        return False
    else:
        return True
        
    
print(has_no_e('eel'))
print(has_no_e('cow'))
    


# In[84]:


def only_no_e(f):
    no_e = 0
    yes_e = 0
    with open(f) as fin:
        for line in fin:
            yes_e += 1
            word = line.strip()
            if has_no_e(word):
                print (word)
                no_e += 1
        print (no_e/yes_e)
            
only_no_e('words.txt')


# In[ ]:








# In[64]:





# In[ ]:




