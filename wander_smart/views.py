from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import google.generativeai as genai
import os
from .prompts import generate_travel_prompt
import json
import re
from datetime import datetime


def generate_slug(trip_name):
    sanitized = trip_name.lower()
    sanitized = re.sub(
        r"[^\w\s-]", "", sanitized
    )  # Remove non-alphanumeric, spaces, or hyphens
    sanitized = re.sub(
        r"[\s_-]+", "-", sanitized
    )  # Replace spaces and underscores with hyphens
    sanitized.strip("-")  # Remove leading/trailing hyphens
    # return f"{sanitized}-{unique_id}"
    # Add datetime suffix
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")  # Format: YYYYMMDDHHMMSS
    return f"{sanitized}-{timestamp}"


def get_trip_plan_from_ai(travel_prompt):
    GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
    travel_prompt = travel_prompt
    # Load Google Gemini API key
    genai.configure(api_key=GEMINI_API_KEY)

    # Set up Gemini AI model
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(travel_prompt)
    ai_result = response.text
    # Remove code block markers and strip whitespace
    ai_result = ai_result.replace("```json", "").replace("```", "").strip()

    # replace non breaking spaces.
    ai_result = ai_result.replace("\u00a0", " ")
    # Parse AI response
    parsed_ai_result = json.loads(ai_result)
    return parsed_ai_result


class GenerateTripPlan(APIView):

    def post(self, request):
        try:
            data = request.data
            destination = data["destination"]
            trip_duration = data["tripDuration"]
            group_size = data["groupSize"]
            budget = data["budget"]
            if not (destination and trip_duration and group_size and budget):
                return Response(
                    {"message": "Missing required fields"},
                    status.HTTP_400_BAD_REQUEST,
                )
            travel_prompt = generate_travel_prompt(
                destination=destination,
                trip_duration=trip_duration,
                group_size=group_size,
                budget=budget,
            )
            parsed_ai_result = get_trip_plan_from_ai(travel_prompt=travel_prompt)

            trip_plan = {
                "tripName": parsed_ai_result["trip_name"],
                "destination": destination,
                "duration": str(trip_duration),
                "hotelDetails": parsed_ai_result["hotel_details"],
                "itineraryPlan": parsed_ai_result["daily_wise_itinerary_plan"],
                "tripDescription": parsed_ai_result["trip_description"],
                "timeToRead": parsed_ai_result["time_to_read"],
                "averageBudgetPerPerson": parsed_ai_result["average_budget_per_person"],
                "travelTips": parsed_ai_result["travel_tips"],
                "localCuisines": parsed_ai_result["local_cuisines"],
                "emergencyContacts": parsed_ai_result["emergency_contacts"],
                "culturalEtiquette": parsed_ai_result["cultural_etiquette"],
                "photographySpots": parsed_ai_result["photography_spots"],
                "slug": generate_slug(parsed_ai_result["trip_name"]),
            }
            return Response(
                {
                    "message": "Your itinerary is generated from Gemini AI! 🎉 wait we are updating it to database",
                    "data": trip_plan,
                    "status": 200,
                },
                status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        except Exception as e:
            return ({"message": str(e)}, status.HTTP_500_INTERNAL_SERVER_ERROR)
