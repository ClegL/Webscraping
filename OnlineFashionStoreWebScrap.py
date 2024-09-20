#!/usr/bin/env python
# coding: utf-8

# In[6]:


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import json
import time
import requests
from bs4 import BeautifulSoup
import pandas as pd


#Check clés JSON

chrome_driver_path = "C:\\Users\\Ulysse\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

url = "https://www2.hm.com/en_ca/women/shop-by-product/tops.html"
driver.get(url)

time.sleep(5)

html = driver.page_source

driver.quit()

soup = BeautifulSoup(html, 'html.parser')

script = soup.find('script', id="__NEXT_DATA__").string

data = json.loads(script)

print(data.keys()) 

if 'props' in data:
    print(data['props'].keys())

if 'pageProps' in data['props']:
    print(data['props']['pageProps'].keys())


# In[5]:


#Affichage sous-clés + contenu

if 'plpProps' in data['props']['pageProps']:
    print(data['props']['pageProps']['plpProps'].keys())

    print(json.dumps(data['props']['pageProps']['plpProps'], indent=4))  


# In[8]:


chrome_driver_path = "C:\\Users\\Ulysse\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

url = "https://www2.hm.com/en_ca/women/shop-by-product/tops.html"
driver.get(url)

time.sleep(5)

html = driver.page_source

driver.quit()

soup = BeautifulSoup(html, 'html.parser')

script = soup.find('script', id="__NEXT_DATA__").string
data = json.loads(script)

products = data['props']['pageProps']['plpProps']['productListingProps']['hits']

product_data = []

for product in products:
    brand = product['brandName']
    product_name = product['title']
    subcategory = product['category'].replace('_', ' ').title()
    price = product['regularPrice']
    location = "Canada"
    product_link = product['pdpUrl']
    image_link = product['imageProductSrc']
    
    if 'Neck' in product_name:
        neckline = 'Neck'
    else:
        neckline = 'Unknown'
    product_data.append([brand, product_name, subcategory, neckline, price, location, product_link, image_link])

df = pd.DataFrame(product_data, columns=[
    'Brand', 'Product Name', 'Subcategory', 'Neckline', 
    'Price', 'Location', 'Product Link', 'Image Link'])
                           
df.to_csv('C:\\Users\\Ulysse\\Downloads\\hm_products_sample.csv', index=True)

print("Données produits extraites et sauvegardées dans 'hm_products_sample.csv'")


# In[9]:


df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




