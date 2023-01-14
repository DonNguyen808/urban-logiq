import csv
import os

# Finds the CSV files in the CSV folder
csvFolderPath = os.listdir('csv/')
os.chdir('csv/')

# grabs csv file 
csvFolder = csvFolderPath
initialSiteCode = []

# Loops through each csv file and inputs data in final deliverable
for csvFile in csvFolder:
    csvFolderPath = os.listdir()

    # Reads CSV files
    with open(csvFile, newline='') as f:
        reader = csv.reader(f)
        csv_list = list(reader)

        siteCode = csv_list[5][1]
        date = csv_list[7][1]

        initialSiteCode.append(siteCode)

        # puts all the formatted data into a list to print onto the csv file
        final_list = []
        indexCount = 0
        
        # Finds All Vehicle Volume start and end rows
        for idx, row in enumerate(csv_list):
            if row[0] == 'ALL-VEHICLE VOLUMES':
                allVehicleVolumeStart = idx + 2
            if row[0] == 'HEAVY-VEHICLE VOLUMES':
                allVehicleVolumeEnd = idx - 2

        # Finds Heavy Vehicle Volume start and end rows
        for idx, row in enumerate(csv_list):
            if row[0] == 'HEAVY-VEHICLE VOLUMES':
                heavyVehicleVolumeStart = idx + 2
            if row[0] == 'BUS VOLUMES':
                heavyVehicleVolumeEnd = idx - 1
        
        # Grabs only all vehicle volume data
        for idx, row in enumerate(csv_list) :
            if idx >= allVehicleVolumeStart and idx < allVehicleVolumeEnd:
                time = row[0]
                # all vehicle volume NB
                nbr = int(row[3]) - int(csv_list[heavyVehicleVolumeStart + indexCount][3])
                nbt = int(row[2]) - int(csv_list[heavyVehicleVolumeStart + indexCount][2])
                nbl = int(row[1]) - int(csv_list[heavyVehicleVolumeStart + indexCount][1])
                nbu = row[4]

                NBR = [date, time, "Cars", "Right", "NB", nbr, siteCode]
                NBT = [date, time, "Cars", "Thru", "NB", nbt, siteCode]
                NBL = [date, time, "Cars", "Left", "NB", nbl, siteCode]
                NBU = [date, time, "Cars", "U-Turn", "NB", nbu, siteCode]

                # all vehicle volume SB
                sbr = int(row[8]) - int(csv_list[heavyVehicleVolumeStart + indexCount][6])
                sbt = int(row[7]) - int(csv_list[heavyVehicleVolumeStart + indexCount][5])
                sbl = int(row[6]) - int(csv_list[heavyVehicleVolumeStart + indexCount][4])
                sbu = row[9]

                SBR = [date, time, "Cars", "Right", "SB", sbr, siteCode]
                SBT = [date, time, "Cars", "Thru", "SB", sbt, siteCode]
                SBL = [date, time, "Cars", "Left", "SB", sbl, siteCode]
                SBU = [date, time, "Cars", "U-Turn", "SB", sbu, siteCode]

                # all vehicle volume EB
                ebr = int(row[13]) - int(csv_list[heavyVehicleVolumeStart + indexCount][9])
                ebt = int(row[12]) - int(csv_list[heavyVehicleVolumeStart + indexCount][8])
                ebl = int(row[11]) - int(csv_list[heavyVehicleVolumeStart + indexCount][7])
                ebu = row[14]

                EBR = [date, time, "Cars", "Right", "EB", ebr, siteCode]            
                EBT = [date, time, "Cars", "Thru", "EB", ebt, siteCode]
                EBL = [date, time, "Cars", "Left", "EB", ebl, siteCode]
                EBU = [date, time, "Cars", "U-Turn", "EB", ebu, siteCode]

                # all vehicle volume WB
                wbr = int(row[18]) - int(csv_list[heavyVehicleVolumeStart + indexCount][12])
                wbt = int(row[17]) - int(csv_list[heavyVehicleVolumeStart + indexCount][11])
                wbl = int(row[16]) - int(csv_list[heavyVehicleVolumeStart + indexCount][10])
                wbu = row[19]

                WBR = [date, time, "Cars", "Right", "WB", wbr, siteCode]
                WBT = [date, time, "Cars", "Thru", "WB", wbt, siteCode]
                WBL = [date, time, "Cars", "Left", "WB", wbl, siteCode]
                WBU = [date, time, "Cars", "U-Turn", "WB", wbu, siteCode]

                # 
                indexCount += 1

                nb = [NBR, NBT, NBL, NBU]
                sb = [SBR, SBT, SBL, SBU]
                eb = [EBR, EBT, EBL, EBU]
                wb = [WBR, WBT, WBL, WBU]

                for element in nb:
                    final_list.append(element)
                for element in sb:
                    final_list.append(element)
                for element in eb:
                    final_list.append(element)
                for element in wb:
                    final_list.append(element)
                
        # Grabs only Heavy Vehicle Volume data
        for idx, row in enumerate(csv_list) :
            if idx >= heavyVehicleVolumeStart and idx < heavyVehicleVolumeEnd:

            # NB Truck count
                time = row[0]
                nbr = row[3]
                nbt = row[2]
                nbl = row[1]

                NBR = [date, time, "Trucks", "Right", "NB", nbr, siteCode]
                NBT = [date, time, "Trucks", "Thru", "NB", nbt, siteCode]
                NBL = [date, time, "Trucks", "Left", "NB", nbl, siteCode]

                # SB Truck Count
                sbr = row[6]
                sbt = row[5]
                sbl = row[4]

                SBR = [date, time, "Trucks", "Right", "SB", sbr, siteCode]
                SBT = [date, time, "Trucks", "Thru", "SB", sbt, siteCode]
                SBL = [date, time, "Trucks", "Left", "SB", sbl, siteCode]

                # EB Truck Count
                ebr = row[9]
                ebt = row[8]
                ebl = row[7]

                EBR = [date, time, "Trucks", "Right", "EB", ebr, siteCode]
                EBT = [date, time, "Trucks", "Thru", "EB", ebt, siteCode]
                EBL = [date, time, "Trucks", "Left", "EB", ebl, siteCode]

                # WB Truck Count
                wbr = row[12]
                wbt = row[11]
                wbl = row[10]

                WBR = [date, time, "Trucks", "Right", "WB", wbr, siteCode]
                WBT = [date, time, "Trucks", "Thru", "WB", wbt, siteCode]
                WBL = [date, time, "Trucks", "Left", "WB", wbl, siteCode]

                nb = [NBR, NBT, NBL]
                sb = [SBR, SBT, SBL]
                eb = [EBR, EBT, EBL]
                wb = [WBR, WBT, WBL]

                for element in nb:
                    final_list.append(element)
                for element in sb:
                    final_list.append(element)
                for element in eb:
                    final_list.append(element)
                for element in wb:
                    final_list.append(element)

        # Finds BICYCLE VOLUMES start and end rows 
        for idx, row in enumerate(csv_list):
            if row[0] == 'BICYCLE VOLUMES':
                BicycleStart = idx + 1
            if row[0] == 'SCOOTER VOLUMES':
                bicycleEnd = idx - 1

        # Grabs only Bicycle Volume data
        for idx, row in enumerate(csv_list) :
            if idx > BicycleStart and idx < bicycleEnd:

                time = row[0]
                nbr = row[3]
                nbt = row[2]
                nbl = row[1]
                NBR = [date, time, "Bicycles", "Right", "NB", nbr, siteCode]
                NBT = [date, time, "Bicycles", "Thru", "NB", nbt, siteCode]
                NBL = [date, time, "Bicycles", "Left", "NB", nbl, siteCode]

                # SB Bikes Count
                sbr = row[6]
                sbt = row[5]
                sbl = row[4]
                SBR = [date, time, "Bicycles", "Right", "SB", sbr, siteCode]
                SBT = [date, time, "Bicycles", "Thru", "SB", sbt, siteCode]
                SBL = [date, time, "Bicycles", "Left", "SB", sbl, siteCode]

                # EB Bikes Count
                ebr = row[9]
                ebt = row[8]
                ebl = row[7]
                EBR = [date, time, "Bicycles", "Right", "EB", ebr, siteCode]
                EBT = [date, time, "Bicycles", "Thru", "EB", ebt, siteCode]
                EBL = [date, time, "Bicycles", "Left", "EB", ebl, siteCode]

                # WB Bikes Count
                wbr = row[12]
                wbt = row[11]
                wbl = row[10]

                WBR = [date, time, "Bicycles", "Right", "WB", wbr, siteCode]
                WBT = [date, time, "Bicycles", "Thru", "WB", wbt, siteCode]
                WBL = [date, time, "Bicycles", "Left", "WB", wbl, siteCode]

                nb = [NBR, NBT, NBL]
                sb = [SBR, SBT, SBL]
                eb = [EBR, EBT, EBL]
                wb = [WBR, WBT, WBL]

                for element in nb:
                    final_list.append(element)
                for element in sb:
                    final_list.append(element)
                for element in eb:
                    final_list.append(element)
                for element in wb:
                    final_list.append(element)
        
        if 'complete' not in csvFolderPath :
            os.makedirs('complete')
            os.chdir('complete')
            # puts all data onto a final deliverable file
            with open(f'{siteCode}_TMC.csv', 'w+', newline='') as f:
                writer = csv.writer(f)
                headers = ['Date', 'Time', 'Road_User', 'Turn', 'Direction', 'Count', 'Location_ID']
                writer.writerow(headers)
                writer.writerows(final_list)
            os.chdir('C:\\Users\\Dawn\\Desktop\\urban-logiq\\csv\\')
            print(f'{initialSiteCode[0]}_TMC.csv created file in complete folder')
        else:
            os.chdir('complete')
            with open(f'{initialSiteCode[0]}_TMC.csv', 'a', newline='') as f:
                writer = csv.writer(f)
                f.write(siteCode)
                f.write('\n')
                writer.writerows(final_list)
            os.chdir('C:\\Users\\Dawn\\Desktop\\urban-logiq\\csv\\')
            print(f'{siteCode} has been added')

print('Done')

        

# if __name__ == '__main__':
#     main()




