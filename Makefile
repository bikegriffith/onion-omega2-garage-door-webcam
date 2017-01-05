default: run

run:
	FLASK_APP=app/main.py python -m flask run --host=0.0.0.0

install:
	opkg update && opkg install git git-http python python-pip pyOnionGpio
	pip install -r requirements.txt
	# echo "cd /root/onion-omega2-garage-door-webcam && make" > /etc/rc.local
