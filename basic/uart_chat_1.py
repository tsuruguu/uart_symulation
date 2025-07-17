import serial
import threading

RX_PORT = '/tmp/ttyV0'
TX_PORT = '/tmp/ttyV1'
BAUDRATE = 9600

def receiver():
    try:
        rx = serial.Serial(RX_PORT, BAUDRATE)
        while True:
            if rx.in_waiting:
                data = rx.readline().decode('utf-8').strip()
                print(f"\n[REMOTE SITE]: {data}")
    except KeyboardInterrupt:
        print("\n[Receiver] Interrupted.")
    finally:
        rx.close()
        print("[Receiver] Serial port closed.")

def sender():
    try:
        tx = serial.Serial(TX_PORT, BAUDRATE)
        while True:
            msg = input("[ME]: ")
            tx.write((msg + '\n').encode('utf-8'))
    except KeyboardInterrupt:
        print("\n[Sender] Interrupted.")
    finally:
        tx.close()
        print("[Sender] Serial port closed.")

threading.Thread(target=receiver, daemon=True).start()
sender()
