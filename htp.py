import requests

def send_post_request(url, data):
    try:
        response = requests.post(url, data=data)
        response.raise_for_status()  # Check for errors
        return response.text
    except requests.exceptions.HTTPError as errh:
        print ("HTTP Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print ("An error occurred:", err)

def send_get_request(url, params=None):
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Check for errors
        return response.text
    except requests.exceptions.HTTPError as errh:
        print ("HTTP Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print ("An error occurred:", err)

# Example usage:
post_url = "localhost::3000"
post_data = {"key": "value"}

get_url = "localhost::3000"
get_params = {"param1": "value1", "param2": "value2"}

# Sending a POST request
post_response = send_post_request(post_url, data=post_data)
print("POST Response:", post_response)

# Sending a GET request
get_response = send_get_request(get_url, params=get_params)
print("GET Response:", get_response)

