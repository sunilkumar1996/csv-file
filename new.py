import csv

measurment = '''DROP TABLE IF EXISTS `measurment`; CREATE TABLE `measurment` (`Date Time` text DEFAULT NULL, NOx real DEFAULT NULL, NO2 real, NO real, SiteID INTEGER, PM10 real, NVPM10 real, VPM10 real, `NVPM2.5` real, `PM2.5` real, `VPM2.5` real, CO real, O3 real, SO2 real, Temperature real, RH real, `Air Pressure` real);'''

station = '''DROP TABLE IF EXISTS `station`; CREATE TABLE `station` (Location text, longtitude real, latitude real, DateStart text, DateEnd text, Current text, `Instrument Type` text);'''

with open('/home/sunil/workspace/pph/mustfa/bristol-air-quality-data.csv', 'r') as file:
    # reader = csv.reader(file, quoting=csv.QUOTE_ALL, skipinitialspace=True)
    reader = csv.reader(file, delimiter=";")
    for row in reader:
        a = f"('{row[0]}', '{row[1]}', '{row[2]}', '{row[3]}', '{row[4]}', '{row[5]}', '{row[6]}', '{row[7]}', '{row[8]}', '{row[9]}', '{row[10]}', '{row[11]}', '{row[12]}', '{row[13]}', '{row[14]}', '{row[15]}', '{row[16]}')"
        print(a)
        measurment += f"INSERT INTO `measurment` VALUES {a};"
        print(measurment)
    # for row in reader:
    #     measurment += f"INSERT INTO `measurment` VALUES {tuple          };"
    #     print(measurment)
    #     station += f"INSERT INTO `station` VALUES {tuple(row[17], row[18].split(',')[0], row[18].split(',')[1], row[19], row[20], row[21], row[22])};"
    #     print(station)


