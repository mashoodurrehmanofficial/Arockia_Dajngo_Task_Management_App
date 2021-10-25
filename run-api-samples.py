import requests
from django.core.files import File  # you need this somewhere
from dateutil import parser
from datetime import datetime
from django.conf import settings
import django
import os
import sys,json

from django.shortcuts import redirect
sys.path.append(os.path.join(os.path.dirname(__file__), 'PROJECT'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PROJECT.settings")
django.setup()
from root.models import *


 
 


url = 'http://localhost:8000/rest_api/test/'
url_insert_new_chore = 'http://localhost:8000/rest_api/insert_new_chore/'

chore_data = {
    'chore_name': "test",
    'chore_code':     "1",
    'cre_on': "2021-02-14 09:51:46",
    'last_updt_on': "2021-02-14 09:51:46",
    'cre_by': "test",
    'last_updt_by': "test",
    'category': 0,
    'rank': 100000,
     'points': 300,
    'background_color': "",
    'icon': "test.png"  # path to image
}

# res = requests.post(url_insert_new_chore, data=(chore_data))
# print(res.json())
 
 
  
url_insert_new_transaction = 'http://localhost:8000/rest_api/insert_new_transaction/'

transaction_data = {
    'chore': 26,
    'user': 19, 
    'date'    : "2021-02-14 09:51:46",
    'duration':     30,
    'cre_on': "2021-02-14 09:51:46",
    'last_updt_on': "2021-02-14 09:51:46",
    'cre_by': "test",
    'last_updt_by': "test",  
}

   
   
res = requests.post(url_insert_new_transaction, data=(transaction_data))
with open("res.html",'w',encoding='utf-8') as file:
    file.write(str(res.text))
print(res.text)
 