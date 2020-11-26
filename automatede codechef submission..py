#!/usr/bin/env python
# coding: utf-8

# In[255]:


get_ipython().system('pip install selenium')
import time 


# In[256]:


from selenium import webdriver


# In[257]:



browser=webdriver.Chrome(r"C:\Users\tusha\Downloads\chromedriver_win32 (1)\chromedriver.exe")


# In[258]:


browser.get("https://www.codechef.com")


# In[259]:


username=browser.find_element_by_id("edit-name")


# In[260]:


username.send_keys("tushara272")


# In[261]:


password=browser.find_element_by_id("edit-pass")


# In[262]:


from getpass import getpass


# In[263]:


password.send_keys(getpass("Enter password: "))


# In[264]:


browser.find_element_by_id("edit-submit").click()


# In[265]:


browser.get("https://www.codechef.com/submit/TEST")

time.sleep(10)


# In[266]:


browser.find_element_by_id("edit-submit").click()
time.sleep(10)


# In[267]:


browser.find_element_by_id("edit_area_toggle_checkbox_edit-program").click()


# In[ ]:


with open("codechef.cpp",'r') as f:
    code=f.read()


# In[ ]:


code


# In[ ]:


code_element=browser.find_element_by_id("edit-program")


# In[ ]:


code_element.send_keys(code)
time.sleep(10)
#browser.find_element_by_xpath("//*[@id="ember391_chosen"]/a/span").click()


# In[ ]:


browser.find_element_by_id("edit-submit-1").click()


# In[ ]:




