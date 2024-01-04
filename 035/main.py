# 433f7ce3e01054a936dc9dad4ab43ce7
# https://api.openweathermap.org/data/2.5/weather?lat={36.33}&lon={127.42}&appid={433f7ce3e01054a936dc9dad4ab43ce7}

# https://api.openweathermap.org/data/3.0/onecall?lat={36.33}&lon={127.42}&exclude={current}&appid={433f7ce3e01054a936dc9dad4ab43ce7} # open call 3.0
MY_LAT = 36.330101
MY_LONG = 127.422470

OWN_ENDPOINT = 'https://api.openweathermap.org/data/2.5/weather'
api_key= '94c82070bfe3ebe6558b485a2db2a887'

weather_params = {
    'lat' : MY_LAT,
    'lon' : MY_LONG,
    'appid' : api_key,
}

import requests
response = requests.get(OWN_ENDPOINT, params=weather_params)
print(response.status_code)