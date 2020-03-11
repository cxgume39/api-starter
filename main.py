import requests

URL = "//restcountries.eu/rest/v2/name/{name}"

res = requests.get(URL) # get the data
res = res.json() # convert data to Python format

print(res)