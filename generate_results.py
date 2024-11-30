import requests
import json

# Endpoint and parameters for fetching results
FLIPP_API_URL = "https://cdn-gateflipp.flippback.com/bf/flipp/items/search"
PARAMS = {
    "locale": "en-us",
    "postal_code": "57106",
    "sid": "",
    "q": "Coke 24 Pack"
}

def fetch_results():
    """Fetch results from the Flipp API and save them as results.json."""
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
        }
        response = requests.get(FLIPP_API_URL, params=PARAMS, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        # Save the fetched results to results.json
        with open("results.json", "w") as file:
            json.dump(data, file, indent=4)
        print("results.json has been generated successfully.")
    except requests.RequestException as e:
        print(f"Error fetching data from Flipp API: {e}")
        raise

if __name__ == "__main__":
    fetch_results()
