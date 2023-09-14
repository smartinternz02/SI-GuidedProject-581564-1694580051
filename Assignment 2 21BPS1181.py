#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Assignment 2
Raghav S
21BPS1181


# In[15]:


pip install seaborn


# In[3]:


import numpy as np
import pandas as pd
import seaborn as sns


# In[5]:


print(sns.get_dataset_names())


# In[6]:


df=sns.load_dataset('car_crashes')


# In[7]:


df


# In[8]:


df.info()


# In[14]:


sns.scatterplot(x="total",y="speeding",data=df)


# In[15]:


# Inference: As speed increases total also increased in car crashes.


# In[16]:


sns.scatterplot(x="total",y="alcohol",data=df)


# In[17]:


# Inference: As alcohol in driver increases total also increased in car crashes.


# In[18]:


sns.scatterplot(x="total",y="not_distracted",data=df)


# In[19]:


# Inference: Distracted drivers cause more crashes


# In[20]:


sns.scatterplot(x="total",y="no_previous",data=df)


# In[21]:


# Inference: Drivers with previous records of crahing cause more crashes


# In[22]:


sns.scatterplot(x="total",y="ins_premium",data=df)


# In[23]:


#Inference: People who pay less premium cause more car crashes


# In[25]:


sns.scatterplot(x="total",y="ins_losses",data=df)


# In[26]:


#Inference: Car crashes are high when insurance losses are between 110 and 160


# In[11]:


sns.barplot(x="total",y="abbrev",data=df)


# In[28]:


#Inference: Plot shows the states where the insurance loss is high


# In[29]:


sns.scatterplot(x="alcohol",y="speeding",data=df)


# In[30]:


#Inference: Speedinng is high when alcohol in driver is low


# In[32]:


sns.barplot(x="abbrev",y="alcohol",data=df)


# In[33]:


#Inference : Drunk driving cases in the states are shown


# In[34]:


sns.scatterplot(x="alcohol",y="not_distracted",data=df)


# In[ ]:


#Inference People who consumed less alcohol were less distracted

