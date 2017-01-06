default: run

run:
	FLASK_APP=app/main.py FLASK_DEBUG=1 python -m flask run --host=0.0.0.0

install:
	opkg update && opkg install git git-http python python-pip pyOnionGpio
	pip install -r requirements.txt
	# echo "cd /root/onion-omega2-garage-door-webcam && screen -d -m make" > /etc/rc.local
	# echo "exit 0" >> /etc/rc.local
