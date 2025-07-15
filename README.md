# UART Simulation

This repository contains a simple simulation of UART (Universal Asynchronous Receiver-Transmitter) communication using Python and virtual serial ports.

## 🛠 Requirements

- Linux system (recommended: native Ubuntu; WSL2 has limitations)
- [socat](https://linux.die.net/man/1/socat)
- Python 3
- `pyserial` library

### Install dependencies

Install `socat`:

```bash
sudo apt install socat
```

Install `pyserial`:

```bash
pip install pyserial
```

---

## 🔌 Creating Virtual UART Ports

Use `socat` to create two connected virtual serial ports:

```bash
socat -d -d pty,raw,echo=0,link=/tmp/ttyV0 \
             pty,raw,echo=0,link=/tmp/ttyV1
```

This creates a virtual UART cable:

```
/tmp/ttyV0 <-------> /tmp/ttyV1
```

---

## ▶️ One-Way Communication

To simulate one-way communication:

- **Terminal 1**: receiver
  ```bash
  python3 uart_rx.py
  ```

- **Terminal 2**: sender
  ```bash
  python3 uart_tx.py
  ```

Ensure the scripts use the correct ports, e.g.:

- `uart_rx.py`: `PORT = '/tmp/ttyV0'`
- `uart_tx.py`: `PORT = '/tmp/ttyV1'`

---

## 🔁 Two-Way Communication (Chat)

To simulate bidirectional UART communication:

- **Terminal 1**:
  ```bash
  python3 uart_chat_1.py
  ```

- **Terminal 2**:
  ```bash
  python3 uart_chat_2.py
  ```

Make sure that the ports are set like this:

- `uart_chat_1.py`:
  - `RX_PORT = '/tmp/ttyV0'`
  - `TX_PORT = '/tmp/ttyV1'`

- `uart_chat_2.py`:
  - `RX_PORT = '/tmp/ttyV1'`
  - `TX_PORT = '/tmp/ttyV0'`

---

## 📎 Notes

- This works best on native Linux.
- On WSL2, `socat` may behave unexpectedly.
- Use `Ctrl+C` to terminate any script.

---

## 📁 Files

| File              | Description                            |
|-------------------|----------------------------------------|
| `uart_tx.py`      | Sends typed messages over UART         |
| `uart_rx.py`      | Receives and prints incoming messages  |
| `uart_chat_1.py`  | Sends/receives messages (side A)       |
| `uart_chat_2.py`  | Sends/receives messages (side B)       |

---

Feel free to clone, modify and extend these scripts to suit your project.
