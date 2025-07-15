# uart_symulation
Symulating uart communication

Download "socat":\
sudo apt install socat

Then make simulated virtual ports by entering: \
socat -d -d pty,raw,echo=0,link=/tmp/ttyV0 
             pty,raw,echo=0,link=/tmp/ttyV1


If you want only one direct communication:\
on first terminal enter: python3 uart_rx.py\
on second terminal enter: python3 uart_tx.py\

If you want two direct communication:\
on first terminal enter: python3 uart_chat_1.py\
on first terminal enter: python3 uart_chat_2.py\