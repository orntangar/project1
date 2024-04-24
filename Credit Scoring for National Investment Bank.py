#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import date
from datetime import datetime


from scipy import stats as st


# In[28]:


pd.set_option('display.max_row', 100)
pd.set_option('display.max_column',100 )

data = pd.read_excel(r'E:\LENOVODOC\ISMD23\Module Projet\Dataset_scoring13082022.xlsx')


# In[29]:


(data.isna().sum()/data.shape[0]).sort_values(ascending=True)


# In[30]:


data.shape


# In[31]:


df = data[data.columns[data.isna().sum()/data.shape[0] <0.9]]
df.head()


# In[32]:


df.shape


# In[8]:


df1=pd.crosstab(df['NOTE'], df['Professsion'])


# In[9]:


df1.head()


# In[10]:


st_chi2, st_p, st_dof, st_exp = st.chi2_contingency(df1)


# In[11]:


st_chi2, st_p, st_dof


# In[14]:


df2=pd.crosstab(df['NOTE'], df['SECTEUR_ACTIVITE'])


# In[15]:


st_chi2, st_p, st_dof, st_exp = st.chi2_contingency(df2)


# In[17]:


df2.head()


# In[18]:


df3=pd.crosstab(df['NOTE'], df['SITUATIONMATRIMONIALE'])
st_chi2, st_p, st_dof, st_exp = st.chi2_contingency(df3)


# In[19]:


st_chi2, st_p, st_dof


# In[20]:


df3.head()


# In[21]:


df4=pd.crosstab(df['NOTE'], df['COMMUNE_NAISSANCE'])
st_chi2, st_p, st_dof, st_exp = st.chi2_contingency(df4)


# In[20]:


df4.head()


# In[21]:


st_chi2, st_p, st_dof


# In[22]:


df4=pd.crosstab(df['NOTE'], df['TYPEPRÊT'])
st_chi2, st_p, st_dof, st_exp = st.chi2_contingency(df4)


# In[23]:


st_chi2,st_p, st_dof


# In[24]:


df4.head()


# In[25]:


df6=pd.crosstab(df['NOTE'], df['PERIODICITE'])
st_chi2, st_p, st_dof, st_exp = st.chi2_contingency(df6)


# In[26]:


st_chi2, st_p, st_dof


# In[27]:


df6.head()


# In[28]:


df7=pd.crosstab(df['NOTE'], df['NB_ECHEANCE'])
st_chi2, st_p, st_dof, st_exp = st.chi2_contingency(df7)


# In[29]:


st_chi2, st_p, st_dof


# In[30]:


df7.head()


# In[31]:


df.corr()


# In[33]:


from datetime import date
 
def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year -((today.month, today.day) <(birthDate.month, birthDate.day))
 
    return age


# In[34]:


print(calculateAge(date(1962,6,16)), "years")


# In[35]:


df['DATENAISSANCE'] = pd.to_datetime(df.DATENAISSANCE)


# In[14]:


df.head()


# In[36]:


#Création d'une nouvelle colonne age  à partir de la fonction de calcul de l'age 
df['AGE']=df['DATENAISSANCE'].apply(lambda x: calculateAge(x))


# In[18]:


df.head()


# In[39]:


del df['DATENAISSANCE']


# In[40]:


df.head()


# In[69]:


df['AGE_Class'] = pd.cut(df.AGE, range(0,110,25), include_lowest=True)


# In[70]:


df.head()


# In[71]:


df8=pd.crosstab(df['NOTE'], df['AGE_Class'])


# In[72]:


df8.head()


# In[ ]:




