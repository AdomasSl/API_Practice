# Learning APIs and trying to get data in json format, practice run.
from colorama import Fore, Back, Style
import requests
import json
import random
from datetime import datetime
from pathlib import Path
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
x = random.randint(1,1065)
BaseUrl = 'https://pokeapi.co/api/v2/'
final = BaseUrl + selectedClean
settings = {"limit": 5, "offset":x}
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
    item['region'] = region['name'] if region else None
    print(f'Name: ' + item['name']+' URL: ' + item['url'] + ' Region: '+region['name'])
current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
output_dir = Path("TEST_to_json")
output_dir.mkdir(exist_ok=True)
file_path = output_dir / f"Data_json_{current_datetime}.json"
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data_json, f, ensure_ascii=False, indent=4)

print("file has been closed and saved")
print()






