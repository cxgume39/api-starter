import requests


Name = "https://restcountries.eu/rest/v2/name/united"
res = requests.get(Name) # get the data

res = requests.get(Name) # get the data
res = res.json() # convert data to Python format







print(res)