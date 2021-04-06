import pandas

# data = pandas.read_csv("weather_data.csv")
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# print(monday_temp)
# mon_temp_far = (monday_temp * 9/5) + 32
# print(mon_temp_far)


data = pandas.read_csv("Central_Park_Squirrel_Data.csv")
count = data.groupby(["Primary Fur Color"]).size().reset_index(name='Count')

df = pandas.DataFrame(count)
df.to_csv("sq_count.csv")



