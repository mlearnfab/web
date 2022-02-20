#!/usr/bin/env python
# coding: utf-8

# # Functions

# ## Definition
# 
# Functions are used to define blocks of reusable code. They are executed only when called. Functions can have inputs. The inputs are also called arguments or parameters. They can return outputs.
# 
# In python functions are defined using the **def** keyword.

# ## Examples

# ### Simple Function

# In[1]:


def greeting():
    print("Hello")


# In[2]:


greeting()


# ###  Function with one argument (input)

# In[3]:


def greeting(name):
    print("Hello", name)


# In[4]:


greeting("Alfred the Great")


# ### Function with one input and one output

# In[5]:


def name_lengths(names):
    """input is a list of names. output is length of each name in names"""
    lengths = []
    for name in names:
        lengths.append(len(name))
    return(lengths)


# In[6]:


physicists = ["Curie","Heisenberg","Feynman","Einstein","Pauli"]


# In[7]:


name_lengths(physicists)


# In[8]:


# the output can be assigned to a variable
my_lengths = name_lengths(physicists)


# In[9]:


my_lengths


# In[10]:


# function which returns the longest and shortest names

def name_lengths(names):
    """input is a list of names. output is the longest name"""
    lengths = []
    for name in names:
        lengths.append(len(name))
    max_name = names[lengths.index(max(lengths))]
    min_name = names[lengths.index(min(lengths))]
    return lengths, max_name, min_name


# In[11]:


name_lengths(physicists)


# In[12]:


result = name_lengths(physicists)


# In[13]:


result


# In[14]:


type(result)


# In[15]:


length_list, longest_name, shortest_name = name_lengths(physicists)


# In[16]:


print(length_list, longest_name, shortest_name)


# In[ ]:





# In[ ]:




