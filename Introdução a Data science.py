#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[5]:


url = 'C:/Users/natal/Documents/Data-science/introducao-a-data-science-aula0/aula0/ml-latest-small/ratings.csv'


# In[7]:


notas = pd.read_csv('C:/Users/natal/Documents/Data-science/introducao-a-data-science-aula0/aula0/ml-latest-small/ratings.csv')


# In[8]:


notas.head()


# In[9]:


notas.shape


# In[11]:


notas.columns = ["usuarioId", "filmeId", "nota", "momento"]


# In[12]:


notas.head()


# In[13]:


notas['nota']


# In[14]:


notas['nota'].unique()


# In[15]:


notas['nota'].value_counts()


# In[18]:


notas.nota.head()


# In[20]:


notas.nota.plot(kind='hist')


# In[22]:


notas.nota.describe()


# In[23]:


import seaborn as sns


# In[24]:


sns.boxplot(notas.nota)


# In[ ]:




