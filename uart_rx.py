import serial

PORT = '/tmp/ttyV0'
BAUDRATE = 9600

ser = serial.Serial(PORT,BAUDRATE)
print(f"Listening on port: {PORT} ...")

while True:
	if ser.in_waiting:
		data = ser.readline().decode('utf-8').strip()
		print(f"Received: {data}")
