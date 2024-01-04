import requests
from datetime import datetime

USERNAME= 'won'
TOKEN = 'ahwonseethestory1234'

pixela_endpoint = 'https://pixe.la/v1/users'

user_params ={
    'token' : TOKEN,
    'username': USERNAME,
    'agreeTermsOfService' : 'yes',
    'notMinor' : 'yes',
}

response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

graph_config = {
    'id': "graph1",
    'name': 'Cycling Graph',
    'unit':'Km',
    'type':'float',
    'color':'ajisai',
}

headers={
    'X-USER-TOKEN':TOKEN,
}
response =requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f'{graph_endpoint}/graph1'

headers={
    'X-USER-TOKEN':TOKEN,
}

today = datetime.now()

pixel_config ={
    'date' : today.strftime('%Y%m%d'),
    'quantity' : '12',
    
}

put_pixel_endpoint = f'{pixel_endpoint}/20240104'
response = requests.delete(url=put_pixel_endpoint, json=pixel_config,headers=headers)