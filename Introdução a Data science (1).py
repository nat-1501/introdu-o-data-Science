#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
filmes = pd.read_csv('C:/Users/natal/Documents/Data-science/introducao-a-data-science-aula0/aula0/ml-latest-small/movies.csv')
notas = pd.read_csv('C:/Users/natal/Documents/Data-science/introducao-a-data-science-aula0/aula0/ml-latest-small/ratings.csv')


# In[5]:


filmes.columns = ["filmeId", "titulo", "generos"]
filmes.head()


# In[12]:


notas.head()


# In[11]:


notas.columns = ["usuarioId", "filmeId", "nota", "momento"]


# In[16]:


#Analisando as notas em geral

notas.query("filmeId==1").nota.mean()


# In[17]:


notas.query("filmeId==2").nota.mean()


# In[21]:


medias_por_filme = notas.groupby("filmeId").mean()["nota"]
medias_por_filme.head()


# In[23]:


medias_por_filme.plot(kind='hist')


# In[26]:


import seaborn as sns

sns.boxplot(medias_por_filme)


# In[28]:


sns.distplot(medias_por_filme, bins=10)


# In[29]:


import matplotlib.pyplot as plt


# In[30]:


plt.hist(medias_por_filme)


# In[ ]:




