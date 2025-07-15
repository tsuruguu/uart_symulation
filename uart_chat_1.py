import serial
import threading

RX_PORT = '/tmp/ttyV0'
TX_PORT = '/tmp/ttyV1'
BAUDRATE = 9600

def receiver():
	rx = serial.Serial(RX_PORT, BAUDRATE)
	while True:
		if rx.in_waiting:
			data = rx.readline().decode('utf-8').strip()
			print(f"\n[REMOTE SITE]: {data}")

def sender():
	tx = serial.Serial(TX_PORT, BAUDRATE)
	while True:
		msg = input("[ME]: ")
		tx.write((msg + '\n').encode('utf-8'))

threading.Thread(target = receiver, daemon = True).start()
sender()
