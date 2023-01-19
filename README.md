# Weather Alerts
This project allows users to request weather information for a specific city via SMTP. Users can send an email to a designated email address with the body of the email containing the desired city, and they will receive an email response with the current weather information for that city.

## Requirements
- A valid email address for sending and receiving the weather alerts
- An SMTP server for sending the weather information
- A valid API key from OpenWeatherMap for accessing current weather data

## Usage
1. Clone or download the repository to your local machine
2. Install the required packages by running pip install -r requirements.txt in the project directory
3. Add your email address, SMTP server, and OpenWeatherMap API key to the env.sample file
4. Start the server with uvicorn main:app --reload
5. Send an email to the designated email address with the body containing the desired city (e.g. "Paris")
6. You will receive an email with the current weather information for that city

## Notes
- You need to execute the function using the FastAPI swagger after sending the email
- Make sure to add the email address and script to your email's whitelist to ensure the script is not blocked
- Keep your API key secret and do not share it with anyone

## Contribution
If you find any bug or have any suggestions, please open an issue or feel free to make a pull request.
