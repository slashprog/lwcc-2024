from flask import Flask, render_template
from weather import Weather

API_KEY="65bda05da4f075dc2bd5ddc75240316e"

weather = Weather(API_KEY)

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>A Simple Weather Report Application</h1>"

@app.route("/weather/<city>")
def view_weather(city):
    weather.city = city
    temperature, humidity = weather.get_weather()
    return render_template("weather_report.html", place=weather.city, t=temperature, h=humidity)



if __name__ == '__main__':
    app.run()
    