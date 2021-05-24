# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures =[]
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
data_dict = data.to_dict()
#
# temp_list = data['temp'].to_list()
# print(sum(temp_list) / len(temp_list))
#
# print(data['temp'].max())
#
# # Get data in columns
# print(data['condition'])
# print(data.condition)

# Get data in row

# print(data[data.day == 'Monday'])
print(data[data.temp == data.temp.max()])

# monday = data[data.day == 'Monday']
# print((monday.temp * 9/5) + 32)

# Create a dataframe from scratch
# data_dict = {
#     "students":["Amy", "James", "Angela"],
#     "scores":[76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# gray = len(data[data['Primary Fur Color'] == "Gray"])
# red = len(data[data['Primary Fur Color'] == "Cinnamon"])
# black = len(data[data['Primary Fur Color'] == "Black"])
#
# data_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [gray, red, black]
# }
#
# output = pandas.DataFrame(data_dict)
# output.to_csv("squirrel_count.csv")