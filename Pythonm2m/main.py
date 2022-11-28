import time
import baro
import Moisture_Sensor as MS
import realy_2 as rl
import DHT22 as DH
import datetime
#import fake_val as baro
import mysql.connector

"""mydb = mysql.connector.connect(host="185.27.134.10",user="epiz_30583800",password="KaygBrYUyfZn9O",port="3306",database="epiz_30583800_m2m")


local_date_time = datetime.datetime.now()
local_time = local_date_time.time()
print (local_time)
hour1 = datetime.time(11, 0, 0)
hour2 = datetime.time(15, 0, 0)
time_count=0
"""



while True:
    watering=0
    pressure  = baro.get_pressure()
    #temperature, pressure, humidity = baro.get_temperature_pressure_humidity()
    humidity,temperature  = DH.get_humtemp_temperature()
    Moisture_Sensor=MS.get_moisture_sensor() 
 
    print('Temperature:',(temperature))
    print('Pressure:', pressure)
    print('Humidity:', humidity)
    print('Moisture_Sensor:', (Moisture_Sensor))


"""
    dt_object = datetime.datetime.now()
    time_count +=1
    local_date_time = datetime.datetime.now()
    local_time = local_date_time.time()
    print(time_count)
"""
#les valeurs sont variables
    if ((temperature>18 and temperature<31 ) and (Moisture_Sensor >180) and (pressure >1000 and humidity > 50)) :
            rl.vanne_on()
            print('vanne on')
            time.sleep(5)
            rl.vanne_off()
            print('vanne off')

    time.sleep(5)



    """ 
    mycursor = mydb.cursor()

    sql = "INSERT INTO statistique ( temperature, pressure,humidity,Moisture_Sensor,watering) VALUES (%s, %s,%s,%s,%s)"
    val =  ( temperature, pressure,humidity,Moisture_Sensor,watering)
    mycursor.execute(sql, val)

    mydb.commit()
    """

