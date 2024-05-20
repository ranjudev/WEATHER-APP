import requests

api_key = '7ca0ec132e4b28e51adef6bcb7891b7d'

city = input('Enter city name: ')

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius=kelvin-237.15
    fahrenheit=celsius*(9/5)+32
    return celsius,fahrenheit

weather_data=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}")

if weather_data.json()['cod']==404:
    print("No city found")
else:
    weather=weather_data.json()['weather'][0]['main']
    temp=weather_data.json()['main']['temp']
    temp_celsius,temp_fahrenheit=kelvin_to_celsius_fahrenheit(temp)

print(f"The weather in {city} is: {weather}")
print(f"The temparature in {city} is: {temp_celsius}\u2103 or {temp_fahrenheit}\u2109")

