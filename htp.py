import requests

# Make a GET request
response = requests.get('https://developer.atlassian.com/server/crowd/json-requests-and-responses/')

# Check if the request was successful (status code 200)
if response.status_code == 200:
    try:
        # Parse the JSON response
        json_data = response.json()
        
        # Print the JSON data
        print(json_data)
    except requests.exceptions.JSONDecodeError as e:
        print("Error decoding JSON:", e)
else:
    print('Error:', response.status_code)
