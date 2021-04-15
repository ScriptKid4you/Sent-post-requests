import requests

for i in range(1):
  data = {"Email": "makilejin@gmail.com", "password": "mas3421"}
  url = input("type url:")
  response = requests.post(url, data)
  print(response)
