import csv
import os
from datetime import datetime
from datetime import timedelta


# find csv file
# open it
# grab site code, date, time, value, all vehicle, heavies, bikes
# write it

# keep the print
# understand each process


# Finds the CSV files
csvFolder = os.listdir('CSV/')
os.chdir('CSV/')
# test 1st csv file - loop csv later
firstCSV = csvFolder[0]
csvList = []

def getCSVData(csvFile) :
    # Opens a csv file
    with open(csvFile, newline='') as f:
        reader = csv.reader(f)
        # Displays whole excel data
        csv_list = list(reader)
        return csv_list

# print(firstCSV,'16004701 - Compass Creek Pkwy  -- Dulles Greenway WB Off RampShared Business Dwy.csv')
# print(getCSVData(firstCSV), 'whole excel sheet')
csvList = getCSVData(firstCSV)
date = csvList[7][1]
print(date)
# print(csvList)


# careful how I name variables
# nicely print excel in console


# print(openCSVFiles(searchCSVFiles))



# Will initial count still work

# Given timestamp in string
# grabs the 5:00
# startTime = '04:45'
# stopTime = '10:00'
# timeList = []

# while startTime != stopTime:
#     date_format_str = '%H:%M'
#     # create datetime object from timestamp string
#     given_time = datetime.strptime(startTime, date_format_str)
#     n = 15
#     # Add 15 minutes to datetime object
#     final_time = given_time + timedelta(minutes=n)
#     # Convert datetime object to string in specific format 
#     final_time_str = final_time.strftime('%H:%M')
#     startTime = final_time_str
#     timeList.append(startTime + ' AM')

# print(timeList)



# 

#    while startTime != stopTime:
#             date_format_str = '%H:%M'
#             # create datetime object from timestamp string
#             given_time = datetime.strptime(startTime, date_format_str)
#             n = 15
#             # Add 15 minutes to datetime object
#             final_time = given_time + timedelta(minutes=n)
#             # Convert datetime object to string in specific format 
#             final_time_str = final_time.strftime('%H:%M')
#             startTime = final_time_str
#             generalCount.append(startTime)

