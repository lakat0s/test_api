import requests

from pprint import pprint

response = requests.get('https://swapi.dev/api/starships/9/')

# response = response.text
# Напечатаем в терминале содержимое ответа сервера...
# print(response)
# ...и его тип
# print(type(response))

# Приведём ответ сервера к типам данных Python...
# response = response.json()
# ... и напечатаем его.
# print(response)
# Напечатаем и тип данных объекта, полученного в результате преобразования:
# print(type(response))

# print(response.json()['name'])

# А если запросить несуществующий ключ словаря?
# print(response.json()['my_name'])

# print(response.json().get('name'))

# А если запросить несуществующий ключ словаря?
# print(response.json().get('my_name'))

pprint(response.json())
