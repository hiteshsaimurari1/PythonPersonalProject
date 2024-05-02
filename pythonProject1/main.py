# with open("/Users/hites/PycharmProjects/Day-25/weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)
import csv
with open("/Users/hites/PycharmProjects/Day-25/weather_data.csv") as data_file:
    data = csv.reader(data_file)
    for i in data:
        print(i[1])
