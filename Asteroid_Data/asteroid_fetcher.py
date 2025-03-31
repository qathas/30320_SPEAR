import requests
import pandas as pd
import time
import csv

# ✅ NASA API Key (Replace with your actual key)
NASA_API_KEY = "key"

# ✅ API Endpoint
NEO_WS_URL = "https://api.nasa.gov/neo/rest/v1/neo/browse"
params = {
    "api_key": NASA_API_KEY,
    "size": 100  # Fetches 100 asteroids per request
}

# ✅ CSV file setup (write headers once)
csv_file = "asteroids_full_data.csv"
csv_headers = [
    "id", "name", "diameter", "absolute_magnitude", "is_potentially_hazardous",
    "orbiting_body", "last_observation_date", "eccentricity",
    "inclination", "mean_motion", "semi_major_axis"
]

# ✅ Create the CSV and write the headers if the file does not exist
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=csv_headers)
    writer.writeheader()  # Write headers at the start

page = 1  # Start from page 1

while True:
    print(f"🔍 Fetching page {page} of asteroid data...")
    
    try:
        response = requests.get(NEO_WS_URL, params=params, timeout=30)
        response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
        data = response.json()
        
        if "near_earth_objects" not in data:
            print("❌ Error: No asteroid data found.")
            break

        # ✅ Open CSV in append mode to write rows immediately
        with open(csv_file, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=csv_headers)
            
            # ✅ Process and write each asteroid
            for asteroid in data["near_earth_objects"]:
                # ✅ Diameter check
                diameter = asteroid.get("estimated_diameter", {}).get("meters", {}).get("estimated_diameter_max", None)

                # ✅ Skip asteroids outside the size range
                if diameter is None or not (25 <= diameter <= 250):
                    continue  

                # ✅ Handle missing close_approach_data
                close_approach_data = asteroid.get("close_approach_data", [])
                orbiting_body = close_approach_data[0].get("orbiting_body", "N/A") if close_approach_data else "N/A"

                # ✅ Handle missing orbital_data
                orbital_data = asteroid.get("orbital_data", {})
                last_observation_date = orbital_data.get("last_observation_date", "Unknown")
                eccentricity = orbital_data.get("eccentricity", None)
                inclination = orbital_data.get("inclination", None)
                mean_motion = orbital_data.get("mean_motion", None)
                semi_major_axis = orbital_data.get("semi_major_axis", None)

                # ✅ Write asteroid data immediately
                writer.writerow({
                    "id": asteroid.get("id", "Unknown"),
                    "name": asteroid.get("name", "Unknown"),
                    "diameter": diameter,
                    "absolute_magnitude": asteroid.get("absolute_magnitude_h", None),
                    "is_potentially_hazardous": asteroid.get("is_potentially_hazardous_asteroid", False),
                    "orbiting_body": orbiting_body,
                    "last_observation_date": last_observation_date,
                    "eccentricity": eccentricity,
                    "inclination": inclination,
                    "mean_motion": mean_motion,
                    "semi_major_axis": semi_major_axis
                })

        print(f"✅ Page {page} written to CSV.")

        # ✅ Stop if no more pages exist
        if not data["links"].get("next"):
            print("✅ No more pages available. Finished fetching data.")
            break

        # ✅ Move to the next page
        params["page"] = page
        page += 1

        # ✅ Prevent hitting API rate limits
        time.sleep(1)

    except requests.exceptions.Timeout:
        print("❌ Timeout occurred. Data saved so far. Retrying...")
        time.sleep(5)  # Wait and retry
        continue  # Restart loop

    except requests.exceptions.RequestException as e:
        print(f"❌ Error: {e}. Stopping script.")
        break  # Exit loop on fatal error

print(f"✅ Finished! All asteroid data saved to {csv_file}.")
