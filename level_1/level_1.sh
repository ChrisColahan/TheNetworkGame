#netcat -lv 5554 < ../pipe | python level_1.py > ../pipe
tcpserver -v -B "--THE NETWORK GAME--" 127.0.0.1 5554 python level_1.py
