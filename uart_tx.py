import serial
import time

PORT = '/tmp/ttyV1'
BAUDRATE = 9600

ser = serial.Serial(PORT, BAUDRATE)
time.sleep(1)

while True:
	msg = input("Enter msg to send: ")
	ser.write((msg + '\n').encode('utf-8'))
