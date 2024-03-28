
# PATH = "100-python-projects/Day-25/trial/weather_data.csv"

# import csv
# with open(PATH) as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)
    
# import pandas as pd

# data = pd.read_csv(PATH)
# temperatures = data["temp"]
# print(data)
# print(Temperatures)

# converting dataframe to dict
# data_dict = data.to_dict()
# print(data_dict)

#converting series to list
# temp_list = temperatures.to_list()
# print(temp_list)


# average temperature
# no_of_records = len(temp_list)
# sum_of_records = temperatures.sum() #or sum(temp_list)
# avg_temp = sum_of_records/no_of_records
# print(avg_temp)

# better solution
# print(f"Mean of series: {temperatures.mean()}")

# find max from series
# print(f"max from series: {temperatures.max()}")

# Get data in columns
# print(data["temp"])
# print(data.temp)

# Get data in row
# print(data[data.day == "Monday"])

# highest temperature in week
# print(data[data.temp == data.temp.max()])

# Create dataframe from scratch
# data_dict = {
#     "students": ["A", "B", "C"],
#     "scores": [76,65,98]
# }

# df = pd.DataFrame(data_dict)
# df.to_csv("100-python-projects/Day-25/trial/new_file.csv")
# print(df)
# print(type(df))

import pandas as pd
PATH_TO_DIR = "100-python-projects/Day-25/trial"
PATH_TO_SQUIRREL_DATA = "100-python-projects/Day-25/trial/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240328.csv"

data = pd.read_csv(PATH_TO_SQUIRREL_DATA)
fur_colors_list = data["Primary Fur Color"].unique()
cleanedList_fur_colors_list = [x for x in fur_colors_list if str(x) != 'nan']
gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])

cinnamon_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

req_dict = {
    "Fur Color": cleanedList_fur_colors_list,
    "Count": [gray_squirrel_count, cinnamon_squirrel_count, black_squirrel_count]
}

df = pd.DataFrame(req_dict)
df.to_csv(f"{PATH_TO_DIR}/fur_data.csv")

