# Learning APIs and trying to get data in json format, practice run.
from colorama import Fore, Back, Style
import requests
print()
print(Fore.GREEN + 'This project retrieves data in JSON format via an API and includes colorful design elements for visual appeal :)' + Style.RESET_ALL)
print()
print(Back.RED + Fore.BLACK + "Working." + Style.RESET_ALL)
print(Back.YELLOW + Fore.BLACK + "Working.." + Style.RESET_ALL)
print(Back.GREEN + Fore.BLACK + "Working..." + Style.RESET_ALL)

url = 'https://official-joke-api.appspot.com/jokes/random'
response = requests.get(url)
print(response.status_code)
print(response.reason)
response = response.json()
print(response)






