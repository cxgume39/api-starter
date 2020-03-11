import requests

URL1 = "https://restcountries.eu/rest/v2/name/{name}"
res = requests.get(URL1) # get the data
res = res.json() # convert data to Python format
print(["region"])



print(res)