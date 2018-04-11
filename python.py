import requests

response = requests.get(
    'https://api.stormglass.io/forecast?lat=58.5&lng=17.8',
    headers={
        'Authentication-Token': 'YOUR API KEY'  # Get your key by emailing account@stormglass.io
    }
)

# Do something with response data.
json_data = response.json()