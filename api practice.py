import json
from pprint import pp
import requests

url = 'https://swapi.dev/api/planets/?page=1'
while url is not None:
    response = requests.get(url)
    planets = json.loads(response.text)
    pp(planets)




    break



# url='https://swapi.dev/api/planets/?page=1'
# lst=[]
# while url is not None:
#     response = requests.get(url)
#     todos=json.loads(response.text)
#     #pprint(todos)
#     for i in todos['results']:
#         lst.append(i['name'])
#     url=todos['next']

# print(lst)