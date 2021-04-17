import csv

measurment = '''DROP TABLE IF EXISTS `measurment`; CREATE TABLE `measurment` (`Date Time` text, NOx real, NO2 real, NO real, SiteID INTEGER, PM10 real, NVPM10 real, VPM10 real, `NVPM2.5` real, `PM2.5` real, `VPM2.5` real, CO real, O3 real, SO2 real, Temperature real, RH real, `Air Pressure` real);'''

with open('/home/sunil/workspace/pph/mustfa/bristol-air-quality-data.csv', 'r') as file:
    # reader = csv.reader(file, quoting=csv.QUOTE_ALL, skipinitialspace=True)
    reader = csv.reader(file, delimiter=";")
    for row in reader:
        # measurment += f"INSERT INTO `measurment` VALUES {tuple(row)};"
        # print(measurment)
        for i in row:
            print(i)

