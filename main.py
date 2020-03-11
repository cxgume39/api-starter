import requests

url = "https://privatix-temp-mail-v1.p.rapidapi.com/request/mail/id/%7Bmd5%7D/"

headers = {
    'x-rapidapi-host': "privatix-temp-mail-v1.p.rapidapi.com",
    'x-rapidapi-key': "723a7f4069mshd39cc473ea7d918p1c8cacjsnd38cc7c107c8"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)