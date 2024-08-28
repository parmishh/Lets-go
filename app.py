from flask import Flask, render_template, request, redirect, url_for, session, flash
import requests
import datetime
import bard,os
from dotenv import load_dotenv

# Load the environment variables
load_dotenv()
api_key = os.environ.get("WEATHER_API_KEY")
app = Flask(__name__)




def get_weather_data(api_key: str, location: str, start_date: str, end_date: str) -> dict:
    # Date Formatting as per API "YYYY-MM-DD"

    base_url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/{start_date}/{end_date}?unitGroup=metric&include=days&key={api_key}&contentType=json"

    try:
        response = requests.get(base_url)
        response.raise_for_status()
        data = response.json()
        # print(json.dumps(data, indent=4, sort_keys=True))
        return data
    except requests.exceptions.RequestException as e:
        print("Error:", e.__str__)
        



@app.route('/', methods=["GET", "POST"])
def index():
    """
    Renders the index.html template.

    Returns:
        The rendered index.html template.
    """
    if request.method == "POST":
        global source, destination, start_date, end_date, budget, Travel_theme
        source = request.form.get("source")
        destination = request.form.get("destination")
        start_date = request.form.get("date")
        end_date = request.form.get("return")
        budget = request.form.get("budget")
        Travel_theme=request.form.get("Travel_theme")
        
        # Calculating the number of days
        no_of_day = (datetime.datetime.strptime(end_date, "%Y-%m-%d") - datetime.datetime.strptime(start_date, "%Y-%m-%d")).days
        # Process the route input here
        if no_of_day < 0:
            flash("Return date should be greater than the Travel date (Start date).", "danger")
            return redirect(url_for("index"))
        else:
            try:
                weather_data = get_weather_data(api_key, destination, start_date, end_date)
            except requests.exceptions.RequestException as e:
                flash("Error in retrieving weather data.{e.Error}", "danger")
                return redirect(url_for("index"))
        
        """Debugging"""
        # Json data format printing
        # print(json.dumps(weather_data, indent=4, sort_keys=True))
        try:
            plan = bard.generate_itinerary(source, destination, start_date, end_date, no_of_day,budget, Travel_theme)
        except Exception as e:
            flash("Error in generating the plan. Please try again later.", "danger")
            return redirect(url_for("index"))
        if weather_data:
            # Render the weather information in the template
            return render_template("dashboard.html", weather_data=weather_data, plan=plan)
    
    return render_template('index.html')



# Injecting current time into all templates for copyright year automatically updation
@app.context_processor
def inject_now():
    return {'now': datetime.datetime.now()}


