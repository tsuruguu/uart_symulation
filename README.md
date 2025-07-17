# UART Simulation

This repository contains simple and advanced simulations of UART (Universal Asynchronous Receiver-Transmitter) communication using Python and virtual serial ports.

## 📁 Structure

- `basic/` – minimal UART communication examples
- `better/` – more robust and feature-rich UART simulation scripts (e.g. better UX, multithreading)

---

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

## 📦 `basic/` – Basic UART Simulation

### ▶️ One-Way Communication

- **Terminal 1** (receiver):
  ```bash
  python3 basic/uart_rx.py
  ```

- **Terminal 2** (sender):
  ```bash
  python3 basic/uart_tx.py
  ```

Use the correct ports:

- `uart_rx.py`: `PORT = '/tmp/ttyV0'`
- `uart_tx.py`: `PORT = '/tmp/ttyV1'`

---

### 🔁 Two-Way Communication (Chat)

- **Terminal 1**:
  ```bash
  python3 basic/uart_chat_1.py
  ```

- **Terminal 2**:
  ```bash
  python3 basic/uart_chat_2.py
  ```

Port settings:

- `uart_chat_1.py`:  
  - `RX_PORT = '/tmp/ttyV0'`  
  - `TX_PORT = '/tmp/ttyV1'`

- `uart_chat_2.py`:  
  - `RX_PORT = '/tmp/ttyV1'`  
  - `TX_PORT = '/tmp/ttyV0'`

---

## 🚀 `better/` – Improved UART Simulation

This directory contains more advanced UART simulation scripts, each experimenting with different communication methods, structure, and level of abstraction.

### `task1_UART_BasicCommunication_v1.py`

A basic simulation of UART communication. Implements simple one-way message transmission without using threads or advanced I/O handling. It's a good starting point for understanding how UART works at a minimal level.

### `task2_E32_CommunicationSymulation.py`

Introduces support for simulating E32 (LoRa-based) modules. This version includes both sending and receiving functionality and lays the groundwork for a basic protocol layer over UART, suitable for mimicking long-range radio modules.

### `task3_E32_CommunicationSymulation_v2.py`

An improved version of `task2`, with more robust buffering logic and better handling of transmission issues. It likely introduces simple retry/acknowledge mechanisms, structured messages (e.g., headers, checksums), and more modular code.

> Note: These scripts are **work-in-progress**. They implement basic communication logic in different ways but still need testing, documentation, and refinement before they are fully ready for practical use.

---

## 📎 Notes

- Native Linux is recommended.
- On WSL2, `socat` may behave unexpectedly.
- Use `Ctrl+C` to terminate any script.

---

## 📄 File Overview

### `basic/`

| File              | Description                            |
|-------------------|----------------------------------------|
| `uart_tx.py`      | Sends typed messages over UART         |
| `uart_rx.py`      | Receives and prints incoming messages  |
| `uart_chat_1.py`  | Sends/receives messages (side A)       |
| `uart_chat_2.py`  | Sends/receives messages (side B)       |

### `better/`

| File        | Description                                   |
|-------------|-----------------------------------------------|
| `chat.py`   | Bidirectional UART chat with CLI arguments    |
| *(more...)* | More advanced examples planned or coming soon |

---

Feel free to clone, modify, and extend these scripts to suit your project.
