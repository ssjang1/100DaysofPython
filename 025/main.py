# import pandas as pd

# with open('./025/weather_data.csv') as data_file:
#     data= data_file.readlines()
#     print(data)

# import csv

# with open('./025/weather_data.csv') as data_file:
#     data= csv.reader(data_file)
#     temperatures =[]
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
    
#     print(temperatures)

# import subprocess
# import sys

# def install(package):
#     subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# # pandas 설치
# install("pandas")

import pandas as pd
data = pd.read_csv('./025/weather_data.csv')
print(data)