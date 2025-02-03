import requests

x = requests.get('https://www.ndbc.noaa.gov/data/realtime2/44091.txt')

print(x.text)