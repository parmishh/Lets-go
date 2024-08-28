import google.generativeai as palm
import os
from dotenv import load_dotenv

# Load the environment variables
load_dotenv()
palm_api_key = os.environ.get("PALM_API_KEY")

# Configure the API key
palm.configure(api_key=palm_api_key)

# Generate some text.
def generate_itinerary(source, destination, start_date, end_date, no_of_day, budget,Travel_theme):
    prompt = f"Generate a personalized trip itinerary for a {no_of_day}-day trip from {source} to {destination} from {start_date} to {end_date}, having a travel theme of {Travel_theme}, with an maximum budget strictly under {budget} INR rupees."
    
    # Use palm's generate_text method instead of loading a model manually
    response = palm.generate_text(prompt=prompt)
    
    return response.result  # Access the generated text

