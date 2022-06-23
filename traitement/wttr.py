import requests
import json
from bs4 import BeautifulSoup as bs
import os
import re 
from datetime import datetime

import sys
sys.path.insert(0, '/var/www/2022-meteo-it/input/vocal')
from vocal_recognition import text as city

today = datetime.today().strftime('%Y-%m-%d')

test = city
print(test)

