#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install pandas')


# In[3]:


get_ipython().system('pip install seaborn')


# In[21]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns


# In[7]:


df=pd.read_csv("doctors_visit.csv")


# In[12]:


df.info()


# In[8]:


df.head(15)


# In[43]:


df.describe()


# In[42]:


df['illness'].value_counts()


# In[8]:


df['gender'].value_counts()


# ### Visualize and analyse maximum, minimum and median salary

# In[10]:


y=list(df.income)
plt.boxplot(y)
plt.ylabel("Income in thousands")


# ### Visualize and analyse reduced activity of male and female separately due to illness

# In[11]:


df.groupby(['gender','reduced']).mean()


# ### visiualize if any missing values in dataset based on heatmap

# In[12]:


sns.heatmap(df.isnull())
#sns.heatmap(df.isnull(),cbar=False,cmap='cividis')


# ### findout corelation b/w each of the attribute with other attributes
# 

# In[13]:


plt.figure(figsize=(10,10))
sns.heatmap(df.corr(),cbar=True,annot=True,cmap='Blues')


# ### analysing how income of patients effect number of visits

# In[27]:


plt.figure(figsize=(10,10))
plt.scatter(x='income',y='visits',data=df)
plt.xlabel('Income')
plt.ylabel('visits')
plt.legend()


# ## count of male and female effected by illness 

# In[16]:


sns.histplot(df.gender,bins=2)


# ###  visualize % of people getting govt health insurance due to income and old age and also %of people having private insurance

# In[28]:


label=['yes','no']
Y=df[df['freepoor']=='yes']
N=df[df['freepoor']=='no']

x=[Y.shape[0],N.shape[0]]
plt.figure(figsize=(5,5))
plt.pie(x,labels=label)
plt.title("% getting gvt health insurance")
plt.legend()
plt.show()


# In[29]:


#% of ppl having private insurnace
Y=df[df['private']=='yes']
N=df[df['private']=='no']

x=[Y.shape[0],N.shape[0]]
plt.figure(figsize=(5,5))
plt.pie(x,labels=label)
plt.title("% having private insurance")
plt.legend()
plt.show()


# In[31]:


#% getting insurance due to old age

Y=df[df['freerepat']=='yes']
N=df[df['freerepat']=='no']

x=[Y.shape[0],N.shape[0]]
plt.figure(figsize=(5,5))
plt.pie(x,labels=label)
plt.title("% getting insurance due to old age")
plt.legend()
plt.show()


# ### horizontal bar chart to analyse reduced days of activity due to illness based on  gender

# In[21]:


db=df.groupby('gender')['reduced'].sum().to_frame().reset_index()
db


# In[22]:


plt.barh(db['gender'],db['reduced'])
plt.title("gender vs reduced acitivity")
plt.ylabel("gender")
plt.xlabel("reduced activity")
plt.show()


# ## Calculating number of people at each age group

# In[13]:


age_count={}
for i in df['age']:
    if i in age_count.keys():
        age_count[i]+=1
    else:
        age_count[i]=1
age_count


# ## Counting the no.of patients at each age group

# In[15]:


ill=[]
df1=df.groupby('age')
for i in age_count.keys():
    c=df1.get_group(i)
    ill.append(c['illness'].count())
ill


# In[41]:


plt.pie(ill,autopct='%1.1f%%')
plt.show()

