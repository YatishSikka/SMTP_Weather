from fastapi import FastAPI, BackgroundTasks
from send_email import send_email_async
from read_email import read_email_message
from get_weather import GetCityName

app = FastAPI()

@app.get("/")
def index():
    return "Hello World"

@app.get("/send_email/asynchronous")
async def send_email_asynchronous():
    city,to = await read_email_message()
    body = await GetCityName(city)
    await send_email_async(f"Weather in {city}",to,body)
    return "Success"


# @app.get("/send_email/backgroundtask")
# async def send_email_backgroundtask(background_tasks: BackgroundTasks):
#    send_email_background(background_tasks,"Test subject background", "yatish.sikka96@gmail.com","{Title:Hello World Background, Name:Yatish Sikka bg}")
#    return 'Success'
