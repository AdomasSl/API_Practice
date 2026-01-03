# Learning APIs and trying to get data in json format, practice run.
from colorama import Fore, Back, Style
import requests
import json
print()
print(Fore.CYAN + "-----Select an option-----" + Style.RESET_ALL)
endpoint = ['Locations']
for i in endpoint:
    print(i)
print()
selected = input('Enter one of the endpoints listed above: ')
selectedClean = None
match selected:
    case 'Locations':
        selectedClean='location'
    case _:
        print('Invalid selection')
        exit()

BaseUrl = 'https://pokeapi.co/api/v2/'
final = BaseUrl + selectedClean
settings = {"limit": 5, "offset":10}
response1 = requests.get(final, params = settings)

print(response1.status_code)
print(response1.reason)
print(response1.elapsed.total_seconds())
print()

data_json = json.loads(response1.text)
dicts = data_json['results']
for item in dicts:
    detail = requests.get(item['url']).json()
    region = detail.get('region')
    print(f'Name: ' + item['name']+' URL: ' + item['url'] + ' Region: '+region['name'])








