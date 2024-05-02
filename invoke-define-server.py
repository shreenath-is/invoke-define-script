import requests

# Define the API endpoint URL with the word to query
url = "https://define-command-middleware.onrender.com/api/definition?word=blunder"

# Send a GET request to the API
response = requests.get(url)

# Check for successful response
if response.status_code == 200:
    # Get the string response
    definition = response.text

    # Print the definition
    print(definition)
else:
    print(f"Error: API request failed with status code {response.status_code}")
