# TheNetworkGame
The network game I came up with to teach some people I know about networking and some priciples of security.

Server Instructions
------
Currently windows is not supported! If you want to run this on another windows, you will need to rewrite all of the .sh files.
You will need to install tcpserver to run the levels. See http://cr.yp.to/ucspi-tcp/tcpserver.html. On debian based systems, you can install the ucspi-tcp package or the ipv6 version, ucspi-tcp-ipv6:
`sudo git install ucspi-tcp`
Next, clone the git repo, (`git clone https://github.com/ChrisColahan/TheNetworkGame.git`) then run the levels via the .sh files. For example:`level_1/level_1.sh` will start level 1.

Client Instructions
------
Either find a server ip and port that is hosting The Network Game, or download your own.
It is recommended that you use netcat for playing. For example:`netcat <host> <port>` will connect to the game.
