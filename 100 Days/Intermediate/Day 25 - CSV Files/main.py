# # with open("weather_data.csv", "r") as data:
# #     data_list = data.readlines()
# #     print(data_list)
#
# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures_list = []
#     for row in data:
#         temperatures_list.append(row[1])
#     temperatures_list.pop(0)
#     temperatures = []
#     for i in temperatures_list:
#         temperatures.append(int(i))
#     print(temperatures)


import pandas as pd

df = pd.read_csv('weather_data.csv')
print(df["temperature"])