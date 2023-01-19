import requests, json

key = "981c95e600e137fb1568801556700177"

async def GetCityName(name: str):
    try:
        weather_data=requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={name}&APPID={key}")
        x = json.loads(weather_data.text)
        x = json.dumps(x)
        return x

    except:
        return False