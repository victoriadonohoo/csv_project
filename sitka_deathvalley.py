import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'death_valley_2018_simple.csv'
filename1 = 'sitka_weather_2018_simple.csv'
place_name = ''
place_name1 = ''
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    print(header_row)
    date_index = header_row.index('DATE')
    high_index = header_row.index('TMAX')
    low_index = header_row.index('TMIN')
    name_index = header_row.index('NAME')

    dates, highs, lows = [], [], []
    for row in reader:
        if not place_name:
            place_name = row[name_index]
            print(place_name)
            
        current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
        try:
            high = int(row[high_index])
            low = int(row[low_index])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

import matplotlib.pyplot as plt 

fig = plt.figure()
plt.plot(dates, highs, c="red")
plt.plot(dates, lows, c="blue")

fig.autofmt_xdate()
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

plt.title("DEATH VALLEY, CA US", fontsize=16)
plt.xlabel("", fontsize=12)
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis="both", labelsize=12)

with open(filename1) as f1:
    reader1 = csv.reader(f1)
    header_row1 = next(reader1)

    print(header_row)
    date_index1 = header_row1.index('DATE')
    high_index1 = header_row1.index('TMAX')
    low_index1 = header_row1.index('TMIN')
    name_index1 = header_row1.index('NAME')

    dates1, highs1, lows1 = [], [], []
    for row in reader1:
        if not place_name1:
            place_name1 = row[name_index1]
            print(place_name1)
            
        current_date1 = datetime.strptime(row[date_index1], '%Y-%m-%d')
        try:
            high1 = int(row[high_index1])
            low1 = int(row[low_index1])
        except ValueError:
            print(f"Missing data for {current_date1}")
        else:
            dates1.append(current_date1)
            highs1.append(high1)
            lows1.append(low1)

fig2=plt.figure()
plt.plot(dates1, highs1, c="red")
plt.plot(dates1, lows1, c="blue")

fig.autofmt_xdate()
plt.fill_between(dates1, highs1, lows1, facecolor='blue', alpha=0.1)

plt.title("SITKA AIRPORT, AK US", fontsize=16)
plt.xlabel("", fontsize=12)
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis="both", labelsize=12)
plt.show()

fig, ax = plt.subplots(2, 2)

plt.show()


