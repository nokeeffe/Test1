# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 13:39:50 2021

@author: nokeeffe
"""

import serial
#from serial.tools import list_ports
#list_ports.comports()  # Outputs list of available serial ports
ser = serial.Serial
ser.baudrate = 115200
ser.port = 'COM3'
#ser
ser.close()
ser.open()
#ser.is_open
ser.close()
#ser.is_open