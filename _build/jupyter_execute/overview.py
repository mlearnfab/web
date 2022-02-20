#!/usr/bin/env python
# coding: utf-8

# # Preview
# 
# We will study five topics: **simple objects**, **collections**, **iteration**, **branching**, and **functions**

# ## Simple Objects
# 
# Our initial Python world consists of four types of atoms or objects: `int`, `float`, `bool`, and `str`. 
# We can perform various operations on the objects. The operations are shown in the videos and in a separate notebook.

# In[1]:


# let's create a variable and assign a float
f = 2.71828


# In[2]:


# print the value of f and then check its data type
print(f)
print(type(f))


# ## Collections
# 
# We expand our Python world by forming collections. Think of collections as molecules. There are four basic types of collections in Python: `sets`, `lists`, `tuples`, and `dictionaries`. In this notebook we will only look at lists to give you a flavor of some properties of collections.

# In[3]:


# from our atoms let's create a list taking a sample of each simple object

NoahsArk = [3.14159, False, -15, 'So far beyond the causal solitudes']


# In[4]:


# we check the number of elements in a list with the len() function


# In[5]:


len(NoahsArk)


# In[6]:


print(NoahsArk)


# In[7]:


# lists are mutable, meaning we can add and remove elements from it
NoahsArk.append('Re-statement of Romance')


# In[8]:


len(NoahsArk)


# In[9]:


print(NoahsArk)


# # Iteration

# In[10]:


# let's define a list containing colors
colors = ['Mauve', 'Ochre', 'Damask', 'Cattleya']


# In[11]:


# go through our list one at a time, print the item in the list and its length
for color in colors:
    print(color, len(color))


# # Branching, Conditions

# In[12]:


# Let's print out again the list NoahsAk
NoahsArk


# In[13]:


# Go through the list and print the item only if it is a string; also print the index value
for idx, item in enumerate(NoahsArk):
    if type(item)==str:
        print(idx, item)


# # Functions 

# In[14]:


# let's define a function for calculating tips

def tip_calculator(bill, percentage):
    tip = bill * percentage
    return tip


# In[15]:


tip_calculator(27.35,.15)


# In[16]:


from math import ceil

def tip_calculator(bill, percentage):
    tip = ceil(bill * percentage)
    return tip


# In[17]:


tip_calculator(27.35,.15)

