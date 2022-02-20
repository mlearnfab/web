#!/usr/bin/env python
# coding: utf-8

# # Collections

# When we deal with data we have to deal with collections, not just individuals. Collections are either ordered or unordered. If they are ordered, an individual's position in the sequence is marked by it's index. Collections are also mutable or immutable. 
# 
# - **Lists**: ordered collection, mutable
# - **Tuple**: ordered collection, immutable
# - **Sets**: unordered collection of unique elements, mutable
# - **Dictionary**: map of one collection to another, mutable; dictionaries are not ordered.

# ## Lists

# In[1]:


# create a list
authors = ['Stefan Zweig','William Shakespeare','Friedrich Schiller',           'Leila Slimani','Kazuo Ishiguro','Marcel Proust',           'Ernest Hemingway','Miguel Cervantes']


# In[2]:


# create an empty list
lonely = []


# In[3]:


type(authors)


# In[4]:


# add an element to a list. list elements don't have to be of same type.
authors.append(5)


# In[5]:


authors


# In[6]:


len(authors)


# In[7]:


# removes last item from a list
authors.pop()


# In[8]:


authors


# In[9]:


who = authors.pop()


# In[10]:


who


# In[11]:


authors


# In[12]:


authors.sort()


# In[13]:


authors


# In[14]:


authors[2]


# In[15]:


authors.index('Leila Slimani')


# lists can contain lists

# In[16]:


library = [
           ['Stefan Zweig', 'The World of Yesterday'],
           ['William Shakespeare','Hamlet','Othello'],
           ['Friedrich Schiller','Wallenstein','On the Aesthetic Education of Man'],
           ['Leila Slimani','Chanson Douce'],
           ['Kazuo Ishiguro','Unconsoled'],
           ['Virginia Woolf', 'To the Lighthouse']]
            


# In[17]:


# returns the first element (which is in fact the second) of the list which is a list
library[1]


# In[18]:


library[1][1]


# In[19]:


library[0][0]


# In[20]:


library[0:2]


# ## Tuples

# In[21]:


suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace')


# Tuples are immutable. Tuple supports only two methods: count and index. Count gives the number of occurences of a certain object. Index gives the index value of the object's first appearance.

# In[22]:


new = list(suits)


# In[23]:


new


# In[24]:


ranks.index('Jack')


# In[25]:


alpha = {3,5,7,3,3}


# In[26]:


alpha


# ## Sets

# In[27]:


even = {2,4,6,8,10}
odd = {1,3,5,7,9}
prime = {2,3,5,7}
composite = {4,6,8,9,10}


# In[28]:


# union with or operator
even | odd


# In[29]:


even.union(odd)


# In[30]:


even.intersection(odd)


# In[31]:


# intersection with and operator
even & odd


# In[32]:


even & composite


# In[33]:


prime & even


# ## Dictionaries
# 
# Dictions are key, value pairs

# In[34]:


lib = {'Stefan Zweig': ['The World of Yesterday'],
       'William Shakespeare': ['Hamlet','Othello'],
       'Friedrich Schiller': ['Wallenstein','On the Aesthetic Education of Man'],
       'Leila Slimani' : ['Chanson Douce'],
       'Kazuo Ishiguro': ['Unconsoled'],
       'Virginia Woolf': ['To the Lighthouse']}


# In[35]:


lib


# In[36]:


lib['Kazuo Ishiguro']


# In[37]:


lib


# In[38]:


lib['William Shakespeare'].append('Richard III') 


# In[39]:


lib['William Shakespeare']


# In[40]:


lib


# In[41]:


lib


# In[42]:


lib['William Shakespeare'].remove("Othello")


# In[43]:


lib


# In[44]:


lib.keys()


# In[45]:


lib.values()


# In[46]:


my_authors =list(lib.keys())


# In[47]:


my_authors

