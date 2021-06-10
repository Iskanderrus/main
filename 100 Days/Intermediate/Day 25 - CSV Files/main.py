# # # with open("weather_data.csv", "r") as data:
# # #     data_list = data.readlines()
# # #     print(data_list)
# #
# # import csv
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures_list = []
# #     for row in data:
# #         temperatures_list.append(row[1])
# #     temperatures_list.pop(0)
# #     temperatures = []
# #     for i in temperatures_list:
# #         temperatures.append(int(i))
# #     print(temperatures)
#
#
# import pandas as pd
#
# df = pd.read_csv('weather_data.csv')
# # print(type(df))
# print(type(df["temperature"]))
#
# data_dict = df.to_dict()
# print(data_dict)
#
# temp_list = df["temperature"].to_list()
# print(temp_list)
# avg_temp = df["temperature"].mean()
# max_temp = df["temperature"].max()
# print(max_temp)
# print(avg_temp)
#
# # Get data in columns
# print(df["condition"])
# print(df.condition)
#
# # Get data from row
# print(df[df["temperature"] == max_temp])
# print(df[df.temperature == df.temperature.max()])
# print(df[df.day == "Monday"])
#
# monday = df[df.day == "Monday"]
# print(monday.condition)
# f_temp = monday.temperature * 9 / 5 + 32
# print(f_temp)
#
# # Adding the column
# df["Fahrenheit_temp"] = df.temperature * 9 / 5 + 32
# print(df)
#
# # Creating DF from scratch
#
# my_data = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# new_df = pd.DataFrame(my_data)
# new_df.to_csv("new_data.csv")
# print(new_df)
#
import pandas as pd
df = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
print(df["Primary Fur Color"].value_counts())
