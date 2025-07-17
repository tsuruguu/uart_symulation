import serial
import sys

PORT = '/dev/ttyUSB0'
BAUDRATE = 9600
LOG_FILE = "log_uart.txt"

try:
    ser = serial.Serial(PORT, BAUDRATE, timeout=1, write_timeout=1)
except serial.SerialException as e:
    print(f"Error opening serial port: {e}")
    sys.exit(1)

print(f"Serial port opened: {PORT} with {BAUDRATE} baudrate\n")

try:
    while True:
        print("========MENU========")
        print("[1] Send text")
        print("[2] Receive one byte")
        print("[3] Receive one line")
        print("[4] Show received data from file")
        print("[5] Exit")
        print("====================")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            text = input("Enter text: ").strip()
            ser.write(text.encode())
            print("✓ Text sent successfully.")

        elif choice == "2":
            data = ser.read(1)
            with open(LOG_FILE, "a", encoding="utf-8") as f:
                f.write(data.decode(errors='replace'))
            print(f"✓ Byte received: {data}")

        elif choice == "3":
            data = ser.readline()
            with open(LOG_FILE, "a", encoding="utf-8") as f:
                f.write(data.decode(errors='replace'))
            print(f"✓ Line received: {data}")

        elif choice == "4":
            try:
                with open(LOG_FILE, "r", encoding="utf-8") as f:
                    print("\n-------File's contents-------")
                    print(f.read())
                    print("-----------------------------")
            except FileNotFoundError:
                print("File not found.")

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice.")

finally:
    if ser.is_open:
        ser.close()
    print("Serial port closed.")
