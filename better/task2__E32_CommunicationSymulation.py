import serial, sys, time
from crc import Calculator, Crc16

crc_calc = Calculator(Crc16.CCITT, optimized=True)

RX_PORT = 'RXD'
TX_PORT = 'TXD'
BAUDRATE = 9600
MAX_FRAME_SIZE = 58
HEADER = bytes([0xAA, 0xAA])
POWER_LEVEL = 3

FAKE_FILE_LIST = ["file1.txt", "data.bin", "config.json"]

try:
    ser_tx = serial.Serial(TX_PORT, BAUDRATE, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=1)
    ser_rx = serial.Serial(RX_PORT, BAUDRATE, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=1)
except serial.SerialException as e:
    print(f"Error opening serial port: {e}")
    sys.exit(1)

def send_uart_byte(data):
    if isinstance(data, str):
        data = data.encode('utf-8', errors='replace')
    ser_tx.write(data)

def send_data(data: bytes):
    for i in range(0, len(data), MAX_FRAME_SIZE):
        fragment = data[i:i + MAX_FRAME_SIZE]

        crc = crc_calc.checksum(fragment)
        crc_bytes = crc.to_bytes(2, byteorder='big')  # sprawdzic czemu takie parametry

        frame = HEADER + fragment + crc_bytes

        ser_tx.write(frame)

def wait_for_command():
    if ser_rx.in_waiting > 0:
        data = ser_rx.readline().decode('utf-8', errors='replace').strip()
        print(f"Received: {data}")
        return data
    return None

def handle_command(command):
    if command == "AT":
        send_uart_byte("+OK\r\n")

    elif command == "AT+POWER=3":
        send_uart_byte("+OK\r\n")
    elif command == "AT+POWER?":
        send_uart_byte(f"+POWER:{POWER_LEVEL}\r\n")
    elif command.startswith("AT+POWER="):
        send_uart_byte("+ERROR\r\n")

    elif command == "list":
        file_list = " ".join(FAKE_FILE_LIST)
        send_uart_byte(file_list + "\r\n")

    elif command == "status":
        send_uart_byte(f"Power={POWER_LEVEL} (21 dBm)\r\n")

    elif command.startswith("send "):
        parts = command.split(maxsplit=1)
        if len(parts) == 2:
            filename = parts[1]
            try:
                with open(filename, 'rb') as f:
                    content = f.read()
                    send_data(content)  # sends framed binary over UART
                    send_uart_byte(f"File '{filename}' sent\r\n")
            except FileNotFoundError:
                send_uart_byte("+ERROR: File not found\r\n")
        else:
            send_uart_byte("+ERROR\r\n")

    else:
        send_uart_byte("+ERROR\r\n")

print(f"Serial ports opened: RX={ser_rx.port}, TX={ser_tx.port} @ {BAUDRATE} baud")
print("E32 module simulation started (Power=21 dBm)\n")

print("E32 symulation started\n")

try:
    while True:
        command = wait_for_command()
        if command:
            handle_command(command)
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\n Simulation stopped by user")

finally:
    ser_rx.close()
    ser_tx.close()
    print("Serial ports closed")