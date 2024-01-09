import requests
import datetime as dt
import smtplib
import time 
# 1XX:Hold On
# 2XX: Here You Go
# 3XX: Go Away
# 4XX: You Screwed up
# 5xx: I Screwed up

MY_LAT = 36.330101
MY_LONG = 127.422470

MY_EMAIL = ''
MY_PASSWORD = ''

def is_iss_overhead():
    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    response.raise_for_status()
    data = response.json()
 
    iss_longitude = data['iss_position']['longitude']
    iss_latitude = data['iss_position']['latitude']

    if MY_LAT-5 <=iss_latitude <= MY_LAT+5 and MY_LONG-5 <=iss_longitude <= MY_LONG+5:
        return True
    
    
## Sunrise, Sunset
def is_night():
    parameters ={
        'lat' : MY_LAT,
        'lng' : MY_LONG,
        'formatted' : 0,
    }
    response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = dt.datetime.now()
    
    if time_now >= sunset or time_now <= sunrise:
        return True
    
    
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP('smtp.gmail.com')
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg='Subject:Look Up\n\nThe Iss is above you in the sky.'
        )