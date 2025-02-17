from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "f795b157f48e57126c53282c111b75d8"  

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    if request.method == "POST":
        city = request.form.get("city")
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_data = {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"].capitalize(),
                "icon": data["weather"][0]["icon"]
            }
        else:
            weather_data = {"error": "City not found!"}
    return render_template("index.html", weather_data=weather_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5032, debug=True)
