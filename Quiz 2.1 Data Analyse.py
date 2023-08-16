#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip3 install seaborn')


# In[3]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[41]:


dataall=pd.read_csv('DataQuiz clan.csv')


# In[42]:


print(dataall)


# In[43]:


type(dataall['Pc'][1])


# In[44]:


import re
dataall['Pc'] = dataall['Pc'].apply(lambda x: re.sub(",", "", x))
dataall['Pc'] = dataall['Pc'].apply(lambda x: int(x))


# In[45]:


type(dataall['Pc'][1])


# In[46]:


filthreecom = dataall[['Customer_id', 'Saleorder', 'Pc']]


# In[47]:


print(filthreecom)


# In[48]:


#ลูกค้าซื้อจากเซลล์คนไหนบ้าง จำนวนกี่เครื่อง
chatklum = filthreecom.groupby(['Customer_id','Saleorder'])['Pc'].sum()


# In[49]:


print(chatklum)


# In[50]:


tablegroup = chatklum.reset_index()


# In[51]:


tablegroup


# In[52]:


#ยอดลูกค้าแต่ละคนซื้อ Pc จากเซลล์มากสุดในปี 2013-2018
phonruam = tablegroup.groupby(['Customer_id']).agg({'Pc':'max'})


# In[53]:


phonruam = phonruam.reset_index()


# In[54]:


phonruam


# In[55]:


#ลูกค้าแต่ละคน ซื้อ Pc กับเซลล์แต่ละคนทั้งหมดกี่เครื่อง
costom= tablegroup.merge(df2, how='left', left_on=['Customer_id','Pc','Saleorder'], right_on = ['Customer_id','Pc','Saleorder'])
popsale = costom.groupby(['Customer_id','Saleorder']).agg({'Pc':'sum'})
popsale


# In[30]:


#ยอดขายรวมของเซลล์แต่ละคน ในแต่ละปี
sale_per_year = dataall.groupby(['year','Saleorder'])['Pc'].sum()
sale_per_year = sale_per_year.reset_index()
sale_per_year


# In[31]:


# 2.เซล์คนไหนยอดขายมากสุดในแต่ละปี และขายได้เท่าไร
max_pc_per_year = sale_per_year.groupby(['year']).agg({'Pc':'max'})
max_pc_per_year.merge(sale_per_year, how='left', left_on=['year','Pc'], right_on = ['year','Pc'])


# In[32]:


# 3.ยอดขายรายปี (total sales(Pc) per year)
tspy = dataall.groupby(['year'])['Pc'].sum()
tspy = tspy.reset_index()
tspy


# In[33]:


# line chart of total sales(Pc) per year.
sns.lineplot(x='year', y='Pc', data=tspy)


# In[ ]:




