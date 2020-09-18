# -*- coding: utf-8 -*-

sensor_filename = "/sys/bus/w1/devices/28-0317977998cd/w1_slave"

sensorfile = open(sensor_filename, 'r')
for i, line in enumerate(sensorfile):
    if i == 1:  # 2de lijn
        temp = int(line.strip('\n')[line.find('t=')+2:])/1000.0
        print("Het is {}°C".format(temp))
sensorfile.close()