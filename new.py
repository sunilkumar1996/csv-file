import csv
import sqlite3
import pymysql
# import mysql.connector
from mysql.connector import Error
import mysql.connector

#establishing the connection
conn = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='sunil')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

def generate_sql_from_csv(csv_filename):
    # ############################
    table1_values = '''DROP TABLE IF EXISTS `measurment`; CREATE TABLE `measurment` (`Date Time` DATETIME DEFAULT NULL, NOx real DEFAULT NULL, NO2 real DEFAULT NULL, NO real DEFAULT NULL, SiteID INTEGER DEFAULT NULL, PM10 real DEFAULT NULL, NVPM10 real DEFAULT NULL, VPM10 real DEFAULT NULL, `NVPM2.5` real DEFAULT NULL, `PM2.5` real DEFAULT NULL, `VPM2.5` real DEFAULT NULL, CO real DEFAULT NULL, O3 real DEFAULT NULL, SO2 real DEFAULT NULL, Temperature real DEFAULT NULL, RH real DEFAULT NULL, `Air Pressure` real DEFAULT NULL); DROP TABLE IF EXISTS `station`; CREATE TABLE `station` (SiteID INTEGER DEFAULT NULL, Location VARCHAR(50) DEFAULT NULL, longtitude real DEFAULT NULL, latitude real DEFAULT NULL, DateStart DATETIME DEFAULT NULL, DateEnd DATETIME DEFAULT NULL, Current VARCHAR(45) DEFAULT NULL, `Instrument Type` VARCHAR(45) DEFAULT NULL);'''

    ############################
    # table2_values = '''DROP TABLE IF EXISTS `station`; CREATE TABLE `station` (SiteID INTEGER DEFAULT NULL, Location VARCHAR(50) DEFAULT NULL, longtitude real DEFAULT NULL, latitude real DEFAULT NULL, DateStart DATETIME DEFAULT NULL, DateEnd DATETIME DEFAULT NULL, Current VARCHAR(45) DEFAULT NULL, `Instrument Type` VARCHAR(45) DEFAULT NULL);'''


    # open the csv for read the data 
    with open(csv_filename, 'r') as file:
        # reader = csv.reader(file, quoting=csv.QUOTE_ALL, skipinitialspace=True)
        reader = csv.reader(file, delimiter=";")
        next(reader)
        ################
        for row in reader:
            table1_values += f" INSERT INTO `measurment` VALUES ('{row[0]}', '{row[1]}', '{row[2]}', '{row[3]}', '{row[4]}', '{row[5]}', '{row[6]}', '{row[7]}', '{row[8]}', '{row[9]}', '{row[10]}', '{row[11]}', '{row[12]}', '{row[13]}', '{row[14]}', '{row[15]}', '{row[16]}'); INSERT INTO `station` VALUES ('{row[4]}', '{row[17]}', '{row[18].split(',')[0]}', '{row[18].split(',')[1]}', '{row[19]}', '{row[20]}', '{row[21]}', '{row[22]}');"

            # table2_values += f" INSERT INTO `station` VALUES ('{row[4]}', '{row[17]}', '{row[18].split(',')[0]}', '{row[18].split(',')[1]}', '{row[19]}', '{row[20]}', '{row[21]}', '{row[22]}');"
            # print(table1_values)
            # print(table2_values)

    output_sql_filename = f'{csv_filename.split(".")[0]}.sql'
    # output_sql_filename = '/home/sunil/workspace/pph/mustfa/new.sql'

    with open(output_sql_filename, 'w') as sql_file:

        sql_file.write(table1_values)
    #     print("sqlfile")
    #     # Finally return the file name of the sql file

    # return output_sql_filename

air_quality_sql = generate_sql_from_csv('/home/sunil/workspace/pph/mustfa/bristol-air-quality-data.csv')


with open(air_quality_sql, 'r') as sql:
    con = sqlite3.connect(":memory:")
    cur = con.cursor()
    cur.executescript(sql.read())  
    con.commit()
    df = pd.read_sql("select * from `bristol_air_quality`;", con)
    print(df.info)