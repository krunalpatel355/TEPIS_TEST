from flask import Flask, render_template, request
from datetime import datetime
import json

app = Flask(__name__)

# Mock data with diverse international events
events_data = [
    {
        "_id": "68433ba8abdc1a99e3304d07",
        "event_title": "Summer Music Festival",
        "summary": "Experience the best of electronic and indie music",
        "image_url": "music-festival.jpg",
        "language": "English",
        "event_type": "Festival",
        "event_host": "City Events Inc.",
        "ticket_price": "From $49",
        "booking_url": "http://example.com/summer-fest",
        "start_date": "2025-06-15",
        "end_date": "2025-06-16",
        "start_time": "2:00 PM",
        "end_time": "11:00 PM",
        "event_place": "Central Park",
        "full_address": "123 Park Avenue",
        "country_name": "United States",
        "state_name": "New York",
        "city_name": "New York City",
        "postal_code": "10022",
        "category": "music",
        "price_tier": "moderate",
        "duration": "2 days"
    },
    {
        "_id": "68433ba8abdc1a99e3304d08",
        "event_title": "Tech Innovation Summit",
        "summary": "Join industry leaders in technology and innovation",
        "image_url": "tech-summit.jpg",
        "language": "English",
        "event_type": "Conference",
        "event_host": "Tech Forums",
        "ticket_price": "From $199",
        "booking_url": "http://example.com/tech-summit",
        "start_date": "2025-06-18",
        "end_date": "2025-06-19",
        "start_time": "9:00 AM",
        "end_time": "6:00 PM",
        "event_place": "Convention Center",
        "full_address": "456 Tech Street",
        "country_name": "United States",
        "state_name": "California",
        "city_name": "San Francisco",
        "postal_code": "94103",
        "category": "culture",
        "price_tier": "luxury",
        "duration": "2 days"
    },
    {
        "_id": "68433ba8abdc1a99e3304d09",
        "event_title": "Art & Culture Exhibition",
        "summary": "Discover contemporary art from around the world",
        "image_url": "art-exhibition.jpg",
        "language": "English",
        "event_type": "Exhibition",
        "event_host": "City Gallery",
        "ticket_price": "From $25",
        "booking_url": "http://example.com/art-expo",
        "start_date": "2025-06-11",
        "end_date": "2025-06-21",
        "start_time": "10:00 AM",
        "end_time": "8:00 PM",
        "event_place": "City Gallery",
        "full_address": "789 Art Avenue",
        "country_name": "United States",
        "state_name": "Illinois",
        "city_name": "Chicago",
        "postal_code": "60601",
        "category": "culture",
        "price_tier": "moderate",
        "duration": "10 days"
    },
    {
        "_id": "68433ba8abdc1a99e3304d10",
        "event_title": "Oktoberfest Munich",
        "summary": "The world's largest beer festival and traveling funfair",
        "image_url": "oktoberfest.jpg",
        "language": "English",
        "event_type": "Festival",
        "event_host": "Munich Events",
        "ticket_price": "From $299",
        "booking_url": "http://example.com/oktoberfest",
        "start_date": "2025-09-15",
        "end_date": "2025-09-18",
        "start_time": "10:00 AM",
        "end_time": "11:00 PM",
        "event_place": "Theresienwiese",
        "full_address": "Theresienwiese, Munich",
        "country_name": "Germany",
        "state_name": "Bavaria",
        "city_name": "Munich",
        "postal_code": "80336",
        "category": "culture",
        "price_tier": "moderate",
        "duration": "4 days"
    },
    {
        "_id": "68433ba8abdc1a99e3304d11",
        "event_title": "Wimbledon Championships",
        "summary": "The oldest tennis tournament in the world",
        "image_url": "wimbledon.jpg",
        "language": "English",
        "event_type": "Sports",
        "event_host": "All England Club",
        "ticket_price": "From $799",
        "booking_url": "http://example.com/wimbledon",
        "start_date": "2025-06-30",
        "end_date": "2025-07-06",
        "start_time": "11:00 AM",
        "end_time": "8:00 PM",
        "event_place": "All England Club",
        "full_address": "Church Road, Wimbledon",
        "country_name": "United Kingdom",
        "state_name": "England",
        "city_name": "London",
        "postal_code": "SW19 5AE",
        "category": "sports",
        "price_tier": "luxury",
        "duration": "6 days"
    },
    {
        "_id": "68433ba8abdc1a99e3304d12",
        "event_title": "Coachella Valley Music and Arts Festival",
        "summary": "Annual music and arts festival in the Colorado Desert",
        "image_url": "coachella.jpg",
        "language": "English",
        "event_type": "Festival",
        "event_host": "Goldenvoice",
        "ticket_price": "From $499",
        "booking_url": "http://example.com/coachella",
        "start_date": "2025-04-11",
        "end_date": "2025-04-15",
        "start_time": "12:00 PM",
        "end_time": "2:00 AM",
        "event_place": "Empire Polo Club",
        "full_address": "81800 Avenue 51, Indio",
        "country_name": "United States",
        "state_name": "California",
        "city_name": "Indio",
        "postal_code": "92201",
        "category": "music",
        "price_tier": "premium",
        "duration": "5 days"
    },
    # Adding more international events
    {
        "_id": "68433ba8abdc1a99e3304d13",
        "event_title": "Tomorrowland Belgium",
        "summary": "The world's biggest electronic music festival",
        "image_url": "tomorrowland.jpg",
        "language": "English",
        "event_type": "Festival",
        "event_host": "Tomorrowland",
        "ticket_price": "From $350",
        "booking_url": "http://example.com/tomorrowland",
        "start_date": "2025-07-18",
        "end_date": "2025-07-27",
        "start_time": "2:00 PM",
        "end_time": "2:00 AM",
        "event_place": "De Schorre",
        "full_address": "De Schorre, Boom",
        "country_name": "Belgium",
        "state_name": "Antwerp",
        "city_name": "Boom",
        "postal_code": "2850",
        "category": "music",
        "price_tier": "luxury",
        "duration": "10 days"
    },
    {
        "_id": "68433ba8abdc1a99e3304d14",
        "event_title": "Tokyo Olympics 2025",
        "summary": "Global sporting event bringing nations together",
        "image_url": "tokyo-olympics.jpg",
        "language": "English",
        "event_type": "Sports",
        "event_host": "IOC",
        "ticket_price": "From $150",
        "booking_url": "http://example.com/tokyo-olympics",
        "start_date": "2025-07-23",
        "end_date": "2025-08-08",
        "start_time": "9:00 AM",
        "end_time": "11:00 PM",
        "event_place": "Olympic Stadium",
        "full_address": "Olympic Stadium, Tokyo",
        "country_name": "Japan",
        "state_name": "Tokyo",
        "city_name": "Tokyo",
        "postal_code": "160-0013",
        "category": "sports",
        "price_tier": "moderate",
        "duration": "17 days"
    },
    {
        "_id": "68433ba8abdc1a99e3304d15",
        "event_title": "Cannes Film Festival",
        "summary": "Premier film festival showcasing global cinema",
        "image_url": "cannes.jpg",
        "language": "French",
        "event_type": "Festival",
        "event_host": "Festival de Cannes",
        "ticket_price": "From $500",
        "booking_url": "http://example.com/cannes",
        "start_date": "2025-05-13",
        "end_date": "2025-05-24",
        "start_time": "6:00 PM",
        "end_time": "11:00 PM",
        "event_place": "Palais des Festivals",
        "full_address": "Palais des Festivals, Cannes",
        "country_name": "France",
        "state_name": "Provence-Alpes-Cote d'Azur",
        "city_name": "Cannes",
        "postal_code": "06400",
        "category": "culture",
        "price_tier": "luxury",
        "duration": "12 days"
    },
    {
        "_id": "68433ba8abdc1a99e3304d16",
        "event_title": "Carnival Rio de Janeiro",
        "summary": "World's largest carnival celebration",
        "image_url": "rio-carnival.jpg",
        "language": "Portuguese",
        "event_type": "Festival",
        "event_host": "Rio Tourism",
        "ticket_price": "From $120",
        "booking_url": "http://example.com/rio-carnival",
        "start_date": "2025-03-01",
        "end_date": "2025-03-09",
        "start_time": "7:00 PM",
        "end_time": "6:00 AM",
        "event_place": "Sambadrome",
        "full_address": "Sambadrome, Rio de Janeiro",
        "country_name": "Brazil",
        "state_name": "Rio de Janeiro",
        "city_name": "Rio de Janeiro",
        "postal_code": "20271-130",
        "category": "culture",
        "price_tier": "moderate",
        "duration": "9 days"
    },
    {
        "_id": "68433ba8abdc1a99e3304d17",
        "event_title": "Australian Open Tennis",
        "summary": "Premier tennis tournament in the Southern Hemisphere",
        "image_url": "australian-open.jpg",
        "language": "English",
        "event_type": "Sports",
        "event_host": "Tennis Australia",
        "ticket_price": "From $85",
        "booking_url": "http://example.com/australian-open",
        "start_date": "2025-01-13",
        "end_date": "2025-01-26",
        "start_time": "11:00 AM",
        "end_time": "11:00 PM",
        "event_place": "Melbourne Park",
        "full_address": "Melbourne Park, Melbourne",
        "country_name": "Australia",
        "state_name": "Victoria",
        "city_name": "Melbourne",
        "postal_code": "3000",
        "category": "sports",
        "price_tier": "moderate",
        "duration": "14 days"
    },
    {
        "_id": "68433ba8abdc1a99e3304d18",
        "event_title": "Diwali Festival India",
        "summary": "Festival of lights celebrating Hindu traditions",
        "image_url": "diwali.jpg",
        "language": "Hindi",
        "event_type": "Festival",
        "event_host": "India Tourism",
        "ticket_price": "From $75",
        "booking_url": "http://example.com/diwali",
        "start_date": "2025-11-01",
        "end_date": "2025-11-05",
        "start_time": "6:00 PM",
        "end_time": "11:00 PM",
        "event_place": "Golden Temple",
        "full_address": "Golden Temple, Amritsar",
        "country_name": "India",
        "state_name": "Punjab",
        "city_name": "Amritsar",
        "postal_code": "143001",
        "category": "culture",
        "price_tier": "moderate",
        "duration": "5 days"
    },
    {
        "_id": "68433ba8abdc1a99e3304d19",
        "event_title": "FIFA World Cup Qatar",
        "summary": "The world's most prestigious football tournament",
        "image_url": "world-cup.jpg",
        "language": "Arabic",
        "event_type": "Sports",
        "event_host": "FIFA",
        "ticket_price": "From $200",
        "booking_url": "http://example.com/world-cup",
        "start_date": "2025-11-18",
        "end_date": "2025-12-18",
        "start_time": "4:00 PM",
        "end_time": "10:00 PM",
        "event_place": "Lusail Stadium",
        "full_address": "Lusail Stadium, Doha",
        "country_name": "Qatar",
        "state_name": "Doha",
        "city_name": "Doha",
        "postal_code": "23456",
        "category": "sports",
        "price_tier": "luxury",
        "duration": "30 days"
    },
    {
        "_id": "68433ba8abdc1a99e3304d20",
        "event_title": "Reggae Sumfest Jamaica",
        "summary": "Caribbean's premier reggae and dancehall festival",
        "image_url": "reggae-sumfest.jpg",
        "language": "English",
        "event_type": "Festival",
        "event_host": "Summerfest Productions",
        "ticket_price": "From $95",
        "booking_url": "http://example.com/reggae-sumfest",
        "start_date": "2025-07-14",
        "end_date": "2025-07-20",
        "start_time": "8:00 PM",
        "end_time": "4:00 AM",
        "event_place": "Catherine Hall",
        "full_address": "Catherine Hall, Montego Bay",
        "country_name": "Jamaica",
        "state_name": "Saint James",
        "city_name": "Montego Bay",
        "postal_code": "JMCAS17",
        "category": "music",
        "price_tier": "moderate",
        "duration": "7 days"
    },
    {
        "_id": "68433ba8abdc1a99e3304d21",
        "event_title": "Cherry Blossom Festival",
        "summary": "Traditional Japanese spring celebration",
        "image_url": "cherry-blossom.jpg",
        "language": "Japanese",
        "event_type": "Festival",
        "event_host": "Japan Tourism",
        "ticket_price": "From $60",
        "booking_url": "http://example.com/cherry-blossom",
        "start_date": "2025-04-01",
        "end_date": "2025-04-30",
        "start_time": "9:00 AM",
        "end_time": "8:00 PM",
        "event_place": "Ueno Park",
        "full_address": "Ueno Park, Tokyo",
        "country_name": "Japan",
        "state_name": "Tokyo",
        "city_name": "Tokyo",
        "postal_code": "110-0007",
        "category": "culture",
        "price_tier": "moderate",
        "duration": "30 days"
    },
    {
        "_id": "68433ba8abdc1a99e3304d22",
        "event_title": "Formula 1 Monaco Grand Prix",
        "summary": "The most prestigious Formula 1 race in the world",
        "image_url": "monaco-gp.jpg",
        "language": "French",
        "event_type": "Sports",
        "event_host": "Formula 1",
        "ticket_price": "From $1200",
        "booking_url": "http://example.com/monaco-gp",
        "start_date": "2025-05-23",
        "end_date": "2025-05-25",
        "start_time": "1:00 PM",
        "end_time": "4:00 PM",
        "event_place": "Circuit de Monaco",
        "full_address": "Circuit de Monaco, Monte Carlo",
        "country_name": "Monaco",
        "state_name": "Monaco",
        "city_name": "Monte Carlo",
        "postal_code": "98000",
        "category": "sports",
        "price_tier": "premium",
        "duration": "3 days"
    }
]

# Mock itinerary data based on the provided structure
itinerary_data = {
    "68433ba8abdc1a99e3304d10": {  # Oktoberfest Munich
        "itinerary": [
            {
                "day": 1,
                "location": "Munich Airport",
                "activities": [
                    {
                        "time": "9:00 AM",
                        "description": "Airport transfer to hotel"
                    },
                    {
                        "time": "2:00 PM",
                        "description": "Historic Munich walking tour"
                    },
                    {
                        "time": "6:00 PM",
                        "description": "Traditional Bavarian dinner"
                    }
                ]
            },
            {
                "day": 2,
                "location": "Oktoberfest Grounds",
                "activities": [
                    {
                        "time": "10:00 AM",
                        "description": "Enter the festival grounds and explore beer halls"
                    },
                    {
                        "time": "12:00 PM",
                        "description": "Traditional Bavarian lunch and beer tasting"
                    },
                    {
                        "time": "3:00 PM",
                        "description": "Enjoy rides and traditional games"
                    }
                ]
            },
            {
                "day": 3,
                "location": "Neuschwanstein Castle",
                "activities": [
                    {
                        "time": "9:00 AM",
                        "description": "Begin your day with a hearty breakfast at a nearby café"
                    },
                    {
                        "time": "10:00 AM",
                        "description": "Explore the magnificent Neuschwanstein Castle and its surroundings"
                    },
                    {
                        "time": "1:00 PM",
                        "description": "Enjoy lunch with panoramic views of the Bavarian Alps"
                    },
                    {
                        "time": "3:30 PM",
                        "description": "Visit the nearby Hohenschwangau Castle"
                    },
                    {
                        "time": "5:30 PM",
                        "description": "Return to Munich for your final evening celebration"
                    }
                ]
            }
        ],
        "highlights": [
            "Traditional Bavarian beer halls",
            "Authentic German cuisine",
            "Folk music and dancing",
            "Historic Munich city tour",
            "Neuschwanstein Castle day trip"
        ],
        "trip_info": {
            "duration": "4 days",
            "category": "culture",
            "price_range": "Moderate",
            "end_date": "Oct 2, 2024"
        }
    }
}

# Helper function to get statistics
def get_stats():
    total_events = len(events_data)
    unique_countries = len(set(event['country_name'] for event in events_data))
    # Calculate estimated happy travelers (based on events)
    happy_travelers = min(total_events * 125, 10000)  # Cap at 10k
    
    return {
        'total_events': total_events,
        'countries': unique_countries,
        'happy_travelers': happy_travelers
    }

# Helper function to get filter counts
def get_filter_counts():
    # Count by category
    category_counts = {}
    for event in events_data:
        category = event['category']
        category_counts[category] = category_counts.get(category, 0) + 1
    
    # Count by price tier
    price_counts = {}
    for event in events_data:
        price_tier = event['price_tier']
        price_counts[price_tier] = price_counts.get(price_tier, 0) + 1
    
    # Count by country
    country_counts = {}
    for event in events_data:
        country = event['country_name']
        country_counts[country] = country_counts.get(country, 0) + 1
    
    return {
        'categories': category_counts,
        'price_tiers': price_counts,
        'countries': country_counts
    }

@app.route('/')
def home():
    featured_events = events_data[:3]  # Show first 3 events as featured
    stats = get_stats()
    return render_template('home.html', featured_events=featured_events, stats=stats)

@app.route('/events')
def events():
    category = request.args.get('category', 'All Categories')
    price_range = request.args.get('price_range', 'All Prices')
    country = request.args.get('country', 'All Countries')
    search = request.args.get('search', '')
    
    filtered_events = events_data
    
    # Filter by category
    if category and category != 'All Categories':
        filtered_events = [e for e in filtered_events if e['category'] == category.lower()]
    
    # Filter by price range
    if price_range and price_range != 'All Prices':
        filtered_events = [e for e in filtered_events if e['price_tier'] == price_range.lower()]
    
    # Filter by country
    if country and country != 'All Countries':
        filtered_events = [e for e in filtered_events if e['country_name'] == country]
    
    # Search filter
    if search:
        filtered_events = [e for e in filtered_events if search.lower() in e['event_title'].lower() or search.lower() in e['city_name'].lower()]
    
    # Get filter counts for display
    filter_counts = get_filter_counts()
    
    return render_template('events.html', 
                         events=filtered_events, 
                         total_events=len(filtered_events),
                         current_category=category,
                         current_price_range=price_range,
                         current_country=country,
                         current_search=search,
                         filter_counts=filter_counts)

@app.route('/event/<event_id>')
def event_detail(event_id):
    event = next((e for e in events_data if e['_id'] == event_id), None)
    if not event:
        return "Event not found", 404
    
    itinerary = itinerary_data.get(event_id, {"itinerary": [], "highlights": [], "trip_info": {}})
    
    return render_template('event_detail.html', event=event, itinerary=itinerary)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
