import requests  # Import the requests library to make HTTP requests
import sys  # Import sys to handle command-line arguments

# Define the API key and base URL for the Open Weather Geocoding API
API_KEY = 'f897a99d971b5eef57be6fafa0d83239'
BASE_URL = 'http://api.openweathermap.org/geo/1.0/'

def fetch_location_data(location):
    """
    Fetch geographical data for a given location (city/state or zip code).
    
    Args:
        location (str): The location input (either city/state or zip code).
    
    Returns:
        dict or None: A dictionary containing location data (name, state, country, latitude, longitude)
                       or None if no data is found.
    """
    # Check if the input is a zip code (5 digits)
    if location.isdigit() and len(location) == 5:  # Zip code
        # Construct the URL for the zip code endpoint
        url = f"{BASE_URL}zip?zip={location},US&appid={API_KEY}"
    else:  # Assume it's a city/state combination
        # Construct the URL for the city/state endpoint
        url = f"{BASE_URL}direct?q={location}&appid={API_KEY}"

    # Make a GET request to the API
    response = requests.get(url)
    
    # Check if the response status is OK (200)
    if response.status_code == 200:
        data = response.json()  # Parse the JSON response
        if data:  # If data is returned
            return data[0]  # Return the first result
        else:
            return None  # No data found
    else:
        # Print an error message if the request failed
        print(f"Error fetching data for {location}: {response.status_code}")
        return None  # Return None on error

def main(locations):
    """
    Main function to process a list of locations and print their geographical data.
    
    Args:
        locations (list): A list of location strings (city/state or zip code).
    """
    results = []  # Initialize a list to store results
    for location in locations:
        # Fetch location data for each input location
        location_data = fetch_location_data(location)
        if location_data:
            # Append the relevant data to results
            results.append({
                'name': location_data.get('name'),  # Get the name of the place
                'state': location_data.get('state', ''),  # Get the state (if available)
                'country': location_data.get('country'),  # Get the country
                'latitude': location_data.get('lat'),  # Get the latitude
                'longitude': location_data.get('lon')  # Get the longitude
            })
        else:
            # Append an error message if no data was found
            results.append({'error': f'No data found for {location}'})

    # Print the results
    for result in results:
        print(result)

if __name__ == "__main__":
    # Check if at least one location argument is provided
    if len(sys.argv) < 2:
        print("Usage: geoloc-util <location1> <location2> ...")
        sys.exit(1)  # Exit if no locations are provided

    # Get the list of locations from command-line arguments
    locations = sys.argv[1:]
    main(locations)  # Call the main function with the list of locations