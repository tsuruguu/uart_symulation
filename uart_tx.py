import serial
import time

PORT = '/tmp/ttyV1'
BAUDRATE = 9600

ser = serial.Serial(PORT, BAUDRATE)
time.sleep(1)

try:
    while True:
        msg = input("Enter msg to send: ")
        ser.write((msg + '\n').encode('utf-8'))
except KeyboardInterrupt:
    print("\nInterrupted.")
finally:
    ser.close()
    print("Serial port closed.")
