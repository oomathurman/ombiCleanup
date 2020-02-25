# Imports
import requests
import json

url = 'http://ombiurl:5000'  # URL For OMBI
apikey = '1111111111111111111111111111' # OMBI ApiKey, can be found in ombi settings
adminUser = 'yourAdminUser' # Required for v4 Preview

# Authorization headers
headers = {
    "ApiKey": apikey,
    "UserName": adminUser
}

### MOVIES
# Send request to get movies
response = requests.get(url + '/api/v1/Request/movie', headers=headers)

# Clean request and make pretty
jsonResponse = json.loads(response.content)

# Find each movie in the requests that is available on plex
for availability in jsonResponse:
    if availability["markedAsAvailable"]:
        deleteRequest = requests.delete(url + '/api/v1/Request/movie/' + str(availability["id"]), headers=headers)


### TV Shows
# Send request to get movies
response = requests.get(url + '/api/v1/Request/tv', headers=headers)

# Clean request and make pretty
jsonResponse = json.loads(response.content)

# Find each movie in the requests that is available on plex
for series in jsonResponse:
    # Availability is hiding in a subkey
    subkey = series["childRequests"]
    for availability in subkey:
        if availability["markedAsAvailable"]:
            deleteRequest = requests.delete(url + '/api/v1/Request/tv/' + str(series["id"]), headers=headers)
