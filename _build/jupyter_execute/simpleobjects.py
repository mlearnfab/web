#!/usr/bin/env python
# coding: utf-8

# # Simple Objects
# 

# ## Built-in Data Types and Operations

# Python's building blocks are four basic data types and corresponding operations. 
# 
# 
# - *integer* (whole numbers such as -25 and 10300)
# - *float* (numbers with decimal points such as 3.14159; sometimes expressed as exponents 1.0e8)
# - *boolean* (which have the value True or False)
# - *string* (sequence of characters)
# 

# The following basic arithmetic operations can be performed on ``int`` and ``float``
# 
# | Operator | Description      | Example | Result |
# |----------|------------------|---------|--------|
# | +        | addition         | 5 + 8   | 24     |
# | -        | subtraction      | 9 - 3   | 6      |
# | /        | division         | 7/2     | 3.5    |
# | //       | integer division | 7//2    | 3      |
# | %        | modulus          | 7%3     | 1      |
# | **       | exponentiation   | 3**4    | 81     |
# | *        | multiplication   | 2 * 3.1 | 6.2    |

# Python also has logical operators: ``and``, ``or``, ``not``
# 
# And comparison operators: ``>``, ``<``, ``>=``, ``<=``, ``==``, ``!=``
# 
# And more....

# ### Arithmetic Operations

# In[1]:


# multiplication with *
3.14159 * 50


# In[2]:


# note order of operations
3 + 5.1 * 2


# In[3]:


# use parentheses to enforce your own sense of order
(3 + 5.1) * 2


# In[4]:


# exponentiation requires double asterisks
3 ** 4


# In[5]:


# division is done with a slash
32 / 11


# In[6]:


# modulus operator gives remainder
32 % 11


# In[7]:


# double // is called 'floor' division, rounds down to the nearest whole number
32 // 5


# In[8]:


### Comparisons


# ## boolean data type typically arise in the context of comparison statements
# 

# In[9]:


# == is used to make comparison, the result (boolean) is assigned to a variable
answer = (3 == 3.145)


# In[10]:


type(answer)


# In[11]:


2 <= 5


# In[12]:


(5 < 3) or (2>1)


# In[13]:


(5<3) and (2>1)


# In[14]:


not(5<3) and (2>1)


# ### Variable Assignment

# In[15]:


# we can use a variable to assign the result of an operation 
radius = 5
A = 3.14159 * radius**2 
A


# In[16]:


from math import pi


# In[17]:


A = pi * radius**2
round(A,2)


# In[18]:


# python supports multiple assignments in a single line
x,y, name = 15,24, 'Al'


# In[19]:


print(x)
print(y)
print(name)


# In[20]:


# note that integer 5 and string "5" are not of the same type; making this mistake in life can be tragic
5 == "5"


# In[21]:


# we can check the type of any object 
type(5)


# In[22]:


type(int("5"))


# In[23]:


type(name)


# In[24]:


# however, in python it's easily corrected with type casting
# here we are changing an object of type string to type integer
int("5")

