import requests

response = requests.get('https://developer.atlassian.com/server/crowd/json-requests-and-responses/')

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
