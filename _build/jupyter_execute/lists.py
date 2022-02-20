#!/usr/bin/env python
# coding: utf-8

# # Lists
# 

# Lists are ordered collections. Lists are mutable. Lists can have heterogeneous data elements.

# In[1]:


# Lists are ordered collections. We create lists with square brackets, []
physicists = ["Curie","Gell Man","Feynman","Born","Einstein"]
mathematicians =[]


# In[2]:


# list are indexed, just like strings
physicists[1]


# In[3]:


# we can add to lists with append
mathematicians.append('Gauss')
print(mathematicians)


# In[4]:


# we can replace an element of the list via the index
physicists[2] = "Schwinger"
physicists


# In[5]:


# we can add multiple values to a list with extend
mathematicians.extend(['Noether','Fermat','Tao'])
mathematicians


# In[6]:


# the same item can appear multiple times in a list
mathematicians.append('Noether')
mathematicians


# In[7]:


# you can have heterogeneous datatypes in lists
mathematicians.extend([5,True, ['Jabberwocky','Nonsense']])
mathematicians


# In[8]:


# the last element in the list is another list
mathematicians[7]


# In[9]:


mathematicians


# In[10]:


# what is happening here?

mathematicians[7][0]
# mathematicians[7]


# In[11]:


del mathematicians[5:8]
mathematicians


# In[12]:


mathematicians.extend(['Ramanujan','Lipshutz'])


# In[13]:


# slicing with lists
physicists[2:4]

