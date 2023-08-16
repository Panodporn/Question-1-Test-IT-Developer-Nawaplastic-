#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


dataall=pd.read_csv('DataQuiz clan.csv')


# In[3]:


print(dataall)


# In[4]:


r44 = dataall[dataall.Customer == "R44"]


# In[5]:


r44


# In[8]:


import re
r44['Pc'] = r44['Pc'].apply(lambda x: re.sub(",", "", x))
r44['Pc'] = r44['Pc'].apply(lambda x: int(x))


# In[9]:


#1. ลูกค้าทั้งหมดซื้อสินค้าR44กี่ชิ้นต่อปี
pc_per_year = r44.groupby(['year'])['Pc'].sum()
pc_per_year = pc_per_year.reset_index()


# In[10]:


pc_per_year


# In[13]:


# 2. เขาซื้อสินค้าตัวไหนมากที่สุด ต่อปี กี่ชิ้น
mat_per_year = r44.groupby(['year','material'])['Pc'].sum()
mat_per_year = mat_per_year.reset_index()
max_mat_per_year = mat_per_year.groupby(['year']).agg({'Pc':'max'})
max_mat_per_year = max_mat_per_year.reset_index()
mat_per_year = max_mat_per_year.merge(mat_per_year, how='left', left_on=['year','Pc'], right_on = ['year','Pc'])
mat_per_year


# In[14]:


#3. เขาซื้อผลิตภัณฑ์กับเซลล์คนไหน น้อยที่สุด
Saleorder_pc = r44.groupby(['Saleorder'])['Pc'].sum()
Saleorder_pc = Saleorder_pc.reset_index()
min_pc_per_sale = Saleorder_pc[Saleorder_pc.Pc == min(Saleorder_pc.Pc)]
min_pc_per_sale


# In[ ]:




