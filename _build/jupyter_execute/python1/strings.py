#!/usr/bin/env python
# coding: utf-8

# # String
# 
# 
# 

#     Here we list some basic string operations.
# 
# | Description    	| Example        	| Result                    	|
# |----------------	|----------------	|---------------------------	|
# | concatenate    	| first + last   	| 'William Shakespeare'     	|
# | extract a char 	| author[4]      	| 'i'                       	|
# | slice          	| author[2:7]    	| 'lliam'                   	|
# | split()        	| author.split() 	| ['William','Shakespeare'] 	|

# In[1]:


# assign a string to a variable called author
author = "Virginia Woolf"


# In[2]:


# check data type of variable
type(author)


# In[3]:


# strings are indexed, in Python the index starts at 0
author[0]


# In[4]:


# slice [start, stop, step]; stop is up to but not including stop
author[3:6]


# In[5]:


# negative index starts from the end
author[-1]


# In[6]:


# we can index backwards, the third item from the item. 
# why doesn't python use zeroth indexing when going backwards?
author[-3]


# In[7]:


# starting at -3 and go to -1; we are not going backwards, just using negative indices
author[-4:-1]


# In[8]:


# start at second index, go all the way to the end, in steps of two
# the first argument is the start index, the second argument is the stop index,
# the third argument is the stride
author[2::2]


# In[9]:


# admittedly this is a bit roccoco; 
# we can go backward if we use negative steps

author[-3:1:-1]


# In[10]:


# we can concatenate two strings using + 
first = "Virginia"
last = "Woolf"


# In[11]:


name = first + last


# In[12]:


name


# In[13]:


sentence = "To be or not to be that is the question"


# In[14]:


# split method (function) returns accepts as input a string and returns a list
words = sentence.split()


# In[15]:


len(words)


# In[16]:


words


# In[ ]:




