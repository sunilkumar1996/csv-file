import pymysql
import mysql.connector
from mysql.connector import Error


def create_server_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query, multi=True)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

measurment = '''DROP TABLE IF EXISTS `measurment`; CREATE TABLE `measurment` (`Date Time` text, NOx real, NO2 real, NO real, SiteID INTEGER, PM10 real, NVPM10 real, VPM10 real, `NVPM2.5` real, `PM2.5` real, `VPM2.5` real, CO real, O3 real, SO2 real, Temperature real, RH real, `Air Pressure` real);'''
station = '''DROP TABLE IF EXISTS `station`; CREATE TABLE `station` (Location text, longtitude real, latitude real, DateStart text, DateEnd text, Current text, `Instrument Type` text);'''
connection = create_server_connection("localhost", "root", "root", "working")
execute_query(connection, measurment)
execute_query(connection, station)