import pymysql
# import mysql.connector
from mysql.connector import Error
import mysql.connector

#establishing the connection
conn = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='sunil')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

# This is table schema both tables
sql = '''DROP TABLE IF EXISTS `measurment`; DROP TABLE IF EXISTS `station`; CREATE TABLE `measurment` (`Date Time` DATETIME DEFAULT NULL, NOx real DEFAULT NULL, NO2 real DEFAULT NULL, NO real DEFAULT NULL, SiteID INTEGER DEFAULT NULL, PM10 real DEFAULT NULL, NVPM10 real DEFAULT NULL, VPM10 real DEFAULT NULL, `NVPM2.5` real DEFAULT NULL, `PM2.5` real DEFAULT NULL, `VPM2.5` real DEFAULT NULL, CO real DEFAULT NULL, O3 real DEFAULT NULL, SO2 real DEFAULT NULL, Temperature real DEFAULT NULL, RH real DEFAULT NULL, `Air Pressure` real DEFAULT NULL); CREATE TABLE `station` (SiteID INTEGER DEFAULT NULL, Location VARCHAR(50) DEFAULT NULL, longtitude real DEFAULT NULL, latitude real DEFAULT NULL, DateStart DATETIME DEFAULT NULL, DateEnd DATETIME DEFAULT NULL, Current VARCHAR(45) DEFAULT NULL, `Instrument Type` VARCHAR(45) DEFAULT NULL);'''

# execute the query with values in mysql database alredy created
cursor.execute(sql)
print("ok")

#Closing the connection
conn.close()