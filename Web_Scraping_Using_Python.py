#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install beautifulsoup4')


# In[10]:


get_ipython().system('pip install requests')


# In[12]:


import requests
import pandas
from bs4 import BeautifulSoup


# In[19]:


url_base="https://www.sakile.co.ke/"

headers={'user-agent': 'Mozzila/5.0'}


# In[20]:


response = requests.get(url_base,headers=headers)
response


# In[21]:


soup=BeautifulSoup(response.content,'html.parser')


# In[23]:


#soup()


# In[25]:


#Accessing the title
match=soup.title.text
print(match)


# In[27]:


#match=soup.div
#print(match)


# In[31]:


match=soup.find_all("a",class_="listing_title_unit")
match


# In[32]:


html_texts=[element.text for element in match]
for text in html_texts:
    print(text)


# In[34]:





# In[ ]:




