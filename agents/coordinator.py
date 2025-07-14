"""
Coordinator to manage all AI agents for generating event itineraries
"""

import json
import sys
import os

# Handle both direct execution and module import
if __name__ == "__main__":
    # Direct execution - add parent directory to path
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from agents.hotel_agent import HotelAgent
    from agents.restaurant_agent import RestaurantAgent
    from agents.itinerary_agent import ItineraryAgent
    from agents.weather_agent import WeatherAgent
    from agents.transportation_agent import TransportationAgent
else:
    # Module import - use relative imports
    from .hotel_agent import HotelAgent
    from .restaurant_agent import RestaurantAgent
    from .itinerary_agent import ItineraryAgent
    from .weather_agent import WeatherAgent
    from .transportation_agent import TransportationAgent

class ItineraryCoordinator:
    def __init__(self, event_data):
        self.event_data = event_data
        self.destination = event_data.get('city_name', 'unknown location')
        self.days = (event_data.get('duration') or '').split(' ')[0] or '1'
        self.cost = event_data.get('cost', 'in-between')
        self.hotel_agent = HotelAgent()
        self.restaurant_agent = RestaurantAgent()
        self.itinerary_agent = ItineraryAgent()
        self.weather_agent = WeatherAgent()
        self.transportation_agent = TransportationAgent()

    def generate_itinerary(self):
        # Gather data from each agent
        hotel_data = self.hotel_agent.get_recommendations(self.destination)
        restaurant_data = self.restaurant_agent.get_recommendations(self.destination)
        itinerary_data = self.itinerary_agent.generate_itinerary(self.destination, self.days)
        weather_data = self.weather_agent.get_weather(self.destination)
        transportation_data = self.transportation_agent.get_recommendations(self.destination)

        # Combine data
        itinerary = {
            "destination": self.destination,
            "weather": weather_data,
            "hotels": hotel_data,
            "restaurants": restaurant_data,
            "itinerary": itinerary_data,
            "transportation": transportation_data
        }

        return itinerary

# Example usage:
if __name__ == "__main__":
    example_event = {
        "city_name": "Toronto",
        "duration": "3 days",
        "cost": "in-between"
    }
    coordinator = ItineraryCoordinator(example_event)
    result_itinerary = coordinator.generate_itinerary()
    print(json.dumps(result_itinerary, indent=2))

