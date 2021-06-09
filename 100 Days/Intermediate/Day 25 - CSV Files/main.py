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
# print(type(df))
print(type(df["temperature"]))

data_dict = df.to_dict()
print(data_dict)

temp_list = df["temperature"].to_list()
print(temp_list)
avg_temp = df["temperature"].mean()
max_temp = df["temperature"].max()
print(max_temp)
print(avg_temp)

# Get data in columns
print(df["condition"])
print(df.condition)

# Get data from row
print(df[df["temperature"] == max_temp])
print(df[df.temperature == df.temperature.max()])
print(df[df.day == "Monday"])
