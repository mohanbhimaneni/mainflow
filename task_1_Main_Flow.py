#!/usr/bin/env python
# coding: utf-8

# # Python Datatypes

# ## List

# ### Creation

# In[1]:


l=[1,2,3]
print(l)


# ### Insertion

# In[5]:


l.insert(1,3)
print(l)


# In[6]:


l.append(5)
print(l)


# ### Deletion

# In[7]:


l.remove(2)
print(l)


# In[8]:


l.remove(3)
print(l)


# In[32]:


del l[1]
print(l)


# ## Set

# ### Creation

# In[9]:


set={1,2,3}
print(set)


# ### Insertion

# In[11]:


set.add(4)
print(set)


# ### Deletion

# In[12]:


set.remove(2)
print(set)


# ## Dictionary

# ### Creation

# In[25]:


dict1={
    "name":"Lubber",
    "age":25
}
print(dict1)


# ### Insertion and Updation

# In[26]:


dict1["height"]=170
print(dict1)


# In[27]:


dict1["age"]=30
print(dict1)


# In[28]:


dict1.update({"height":182})
print(dict1)


# ### Deletion

# In[29]:


dict1.pop("height")
print(dict1)


# In[30]:


del dict1["age"]
print(dict1)


# In[31]:


del dict1
print(dict1)

