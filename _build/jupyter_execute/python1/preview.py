#!/usr/bin/env python
# coding: utf-8

# # Preview
# 
# In **Python Module 1** we will study five topics: **simple objects**, **collections**, **iteration**, **branching**, and **functions**.
# 

# ## Takeaways
# 
# 
# - Python contains four **simple objects**: `int`, `float`, `bool`, and `str`. 
# 
# - Python contains four **collections**: `list`, `tuple`, `set`, and `dictionary`.
# 
# - **Iteration** is performed in Python with `for` and `while` loops.
# 
# - **Branching** is performed in Python with `if`, `else`, and `elif`.
# 
# - A Python **function** takes one or more inputs, performs an operation on the inputs, and returns an output. 
# 

# ## Simple Objects Example
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


# In[3]:


# let's create a string object and assign it to a variable
s = "Virginia Woolf"


# In[4]:


# print the value of s and check its data type
print(s)
print(type(s))


# ## Collections Example
# 
# We expand our Python world by forming collections. Think of collections as molecules. 
# 
# There are four basic types of collections in Python: `set`, `list`, `tuple`, and `dict`. 
# 
# In this notebook we will only look at lists. Lists are ordered collections.

# In[5]:


# from our atoms let's create a list taking a sample of each simple object

NoahsArk = [3.14159, False, -15, 'So far beyond the casual solitudes']


# In[6]:


# we check the number of elements in a list with the len() function
len(NoahsArk)


# In[7]:


print(NoahsArk)


# In[8]:


# lists are mutable, meaning we can add and remove elements from it
NoahsArk.append('Re-statement of Romance')


# In[9]:


len(NoahsArk)


# In[10]:


print(NoahsArk)


# In[11]:


# individual elements of a list can be referred to with an index
NoahsArk[4]


# # Iteration Example
# 
# Iteration is the process of repeating a block of code multiple times. 

# In[12]:


# let's define a list containing colors
colors = ['Mauve', 'Ochre', 'Damask', 'Cattleya']


# In[13]:


colors[2]


# In[14]:


# go through our list one at a time, print the item in the list and its length
for color in colors:
    print(color, len(color))


# # Branching Example
# 
# A program is a series of instructions. But a **straight line** series of instructions is very limiting. Branching allows us to deviate from straight line instructions. The simplest form of branching is a conditional. It's structure has three parts:
# 
# - a test, an expression that evaluates to either `True` or `False`
# - a block of code that is executed if the evaluation is `True`
# - an optional block if the evaluation is `False`

# In[15]:


# Let's print the list NoahsAk
NoahsArk


# In[16]:


# Go through the list and print an item only if it is a string; also print the index value
for idx, item in enumerate(NoahsArk):
    if type(item)==str:
        print(idx, item)


# In[17]:


x, y = 500, -22233


# In[18]:


x


# In[19]:


if x<y:
    print(f"{x} is less than {y}.")
elif x>y: 
    print(f"{x} is greater than {y}.")
else:
    print(f"{x} is equal to {y}.")


# # Functions Example
# 
# Functions form the core of any programming language. What is a function in programming? It's a block of code that performs a computation. But it is defined in a way that we call on the function as we need it. A function takes a set of inputs, performs a computation on the inputs, and produces an output.

# In[20]:


def name_of_function(x,y,z):
    return x+y+z


# In[21]:


name_of_function(2,3,5)


# In[22]:


# let's define a function for calculating tips

def tip_calculator(bill, percentage):
    tip = bill * percentage
    return tip


# In[23]:


tip_calculator(33,.25)


# In[24]:


# round up the tip; import the ceil function from the math library in pytho
from math import ceil

def tip_calculator(bill, percentage):
    tip = ceil(bill * percentage)
    return tip


# In[25]:


tip_calculator(27.35,.15)

