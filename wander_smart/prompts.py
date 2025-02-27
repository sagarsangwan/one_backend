# trips/prompts.py


def generate_travel_prompt(destination, budget, trip_duration, group_size):
    return f"""Generate a travel plan for {destination} with a {budget} budget for {trip_duration} days for a group size of {group_size}.
The response must be in **valid JSON format** and follow this structure exactly:

{{
  "trip_name": "A descriptive name for the trip based on the destination",
  "trip_description": "A description for the destination place",
  "time_to_read": "calculate time to read this travel plan in minute",
  "average_budget_per_person": "calculated average budget per person",
  "travel_tips": ["Tip 1", "Tip 2", "Tip 3"],
  "local_cuisines": ["Dish 1", "Dish 2", "Dish 3"],
  "emergency_contacts": {{
    "local_police": "string",
    "nearest_hospital": "string",
    "tourist_help_center": "string"
  }},
  "cultural_etiquette": "Any dos and don'ts for tourists visiting the location",
  "photography_spots": ["Spot 1", "Spot 2", "Spot 3"],
  "hotel_details": [
    {{
      "HotelName": "string",
      "Hotel address": "string",
      "Price": "string",
      "Rating": "string or number",
      "hotel booking url": "string",
      "description": "string"
    }}
  ],
  "daily_wise_itinerary_plan": [
    {{
      "day": "integer (1, 2, 3, etc.)",
      "best_time_to_visit": "string (e.g., 'Morning')",
      "places": [
        {{
          "Place name": "string",
          "ticket pricing": "string",
          "rating": "string or number",
          "time travel": "string",
          "must_try_experience": "string (e.g., 'Try the local street food')"
        }}
      ]
    }}
  ]
}}

The response must:
- Begin and end with curly braces .
- add some emojis for better readability in all trip plan.
- Include all fields, even if some fields are empty.
- include nearby maximum hotels available in the {budget} budget.
- Contain no additional explanations or text outside the JSON format.
Strictly adhere to this structure.
"""
