import requests

<<<<<<< HEAD
URL1 = "https://restcountries.eu/rest/v2/name/{name}"
res = requests.get(URL1) # get the data
=======
URL = "//restcountries.eu/rest/v2/name/{name}"

res = requests.get(URL) # get the data
>>>>>>> d4dfb9ebd747082112a7278986a1d50bb81c271a
res = res.json() # convert data to Python format
print(["region"])



print(res)