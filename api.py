import requests
import json

url_link = "https://restcountries.com/v3.1/capital/jakarta"
response = requests.get(url_link)

#Data
data = response.json(url_link)