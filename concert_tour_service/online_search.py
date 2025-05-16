import os
from dotenv import load_dotenv
from serpapi.google_search import GoogleSearch

load_dotenv()

def search_upcoming_concerts(artist_name: str) -> str:
    api_key = os.getenv("SERPAPI_API_KEY")
    if not api_key:
        return "⚠️ SerpAPI key not found. Please set the 'SERPAPI_API_KEY' environment variable."

    
    params = {
        "engine": "google",
        "q": f"{artist_name} tour dates 2025 site:ticketmaster.com OR site:songkick.com OR site:bandsintown.com OR site:www.viagogo.com",
        "api_key": api_key
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    events = results.get("events_results", [])

    
    if not events and "organic_results" in results:
        organic = results["organic_results"]
        top_links = [r for r in organic if "title" in r and any(word in r["title"].lower() for word in ["tour", "concert", "live"])]
        
        if not top_links:
            return f"❌ No concert info found for artist '{artist_name}'."

        output = f"🔎 Some relevant links for **{artist_name}**:\n\n"
        for item in top_links[:5]:
            title = item.get("title", "No title")
            link = item.get("link", "#")
            output += f"- [{title}]({link})\n"
        return output

    elif not events:
        return f"❌ No concert info found for artist '{artist_name}'."

