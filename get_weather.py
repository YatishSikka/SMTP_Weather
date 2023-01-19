import requests, json
from send_email import Envs

key = Envs.API_KEY

async def GetCityName(name: str):
    try:
        weather_data=requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={name}&APPID={key}")
        x = json.loads(weather_data.text)
        x = json.dumps(x)
        return x

    except:
        return False