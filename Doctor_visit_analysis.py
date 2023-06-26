#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pandas')


# In[3]:


get_ipython().system('pip install seaborn')


# In[4]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns


# In[45]:


df=pd.read_csv("doctors_visit.csv")


# In[ ]:


df.head(15)


# In[22]:


df.info()


# In[30]:


df['illness'].value_counts()


# In[24]:


df['gender'].value_counts()


# ### Visualize and analyse maximum, minimum and median salary

# In[37]:


y=list(df.salary)
plt.boxplot(y)
plt.ylabel("Income in thousands")


# ### Visualize and analyse reduced activity of male and female separately due to illness

# In[38]:


df.groupby(['gender','reduced']).mean()


# ### visiualize if any missing values in dataset based on heatmap

# In[92]:


sns.heatmap(df.isnull())
#sns.heatmap(df.isnull(),cbar=False,cmap='cividis')


# ### findout corelation b/w each of the attribute with other attributes
# 
# #illness and health are highly corelated---2.7
# #illness and age are corelated---2.1
# #visits and salary are corelated---0.65

# In[47]:


plt.figure(figsize=(10,10))
sns.heatmap(df.corr(),cbar=True,annot=True,cmap='Blues')


# ### analysing how income of patients effect number of visits

# In[48]:


plt.figure(figsize=(10,10))
plt.scatter(x='salary',y='visits',data=df)
plt.xlabel('salary')
plt.ylabel('visits')


# ###count of male and female effected by illness 

# In[49]:


sns.histplot(df.gender,bins=2)


# ###  visulize % od=f people getting govt health insurance due to income and old age and also %of people having private insurance

# In[53]:


label=['yes','no']
Y=df[df['freepoor']=='yes']
N=df[df['freepoor']=='no']

x=[Y.shape[0],N.shape[0]]
plt.figure(figsize=(5,5))
plt.pie(x,labels=label)
plt.title("% getting gvt health insurance")
plt.show()


# In[54]:


#% of ppl having private insurnace
Y=df[df['private']=='yes']
N=df[df['private']=='no']

x=[Y.shape[0],N.shape[0]]
plt.figure(figsize=(5,5))
plt.pie(x,labels=label)
plt.title("% having private insurance")
plt.show()


# In[56]:


#% getting insurance due to old age

Y=df[df['freepat']=='yes']
N=df[df['freepat']=='no']

x=[Y.shape[0],N.shape[0]]
plt.figure(figsize=(5,5))
plt.pie(x,labels=label)
plt.title("% getting insurance due to old age")
plt.show()


# ### horizontal bar chart to analyse reduced days of activity due to illness based on  gender

# In[82]:


db=df.groupby('gender')['reduced'].sum().to_frame().reset_index()
db


# In[93]:


plt.barh(db['gender'],db['reduced'])
plt.title("gender vs reduced acitivity")
plt.ylabel("gender")
plt.xlabel("reduced activity")
plt.show()

