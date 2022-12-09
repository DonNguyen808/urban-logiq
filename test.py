import csv
import os
from datetime import datetime
from datetime import timedelta



# Finds every CSV file in the CSV folder
csvFolderFiles = os.listdir('CSV')




for csvDataFile in csvFolderFiles :
    with open(csvDataFile, newline='') as f:
        reader = csv.reader(f)
        csv_list = list(reader)
        # Start time // how to get end time? 
        startTime = csv_list[46][0]
        # Site code
        qc_sitecode = csv_list[5][1]
        # Date
        count_date = csv_list[7][1]
        i = 0
    
        # print(startTime)



# Will initial count still work?

# Given timestamp in string
# grabs the 5:00
startTime = '04:45'
stopTime = '10:00'
timeList = []

while startTime != stopTime:
    date_format_str = '%H:%M'
    # create datetime object from timestamp string
    given_time = datetime.strptime(startTime, date_format_str)
    n = 15
    # Add 15 minutes to datetime object
    final_time = given_time + timedelta(minutes=n)
    # Convert datetime object to string in specific format 
    final_time_str = final_time.strftime('%H:%M')
    startTime = final_time_str
    timeList.append(startTime + ' AM')

print(timeList)



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

