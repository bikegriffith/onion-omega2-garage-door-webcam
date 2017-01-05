import time
from flask import Flask, render_template
from onionGpio import OnionGpio

GARAGE_STATE_PIN = 1
GARAGE_RELAY_PIN = 11

GARAGE_STATE_OPEN_VALUE = 0
GARAGE_STATE_CLOSE_VALUE = 1
GARAGE_RELAY_OPEN_VALUE = 0
GARAGE_RELAY_CLOSE_VALUE = 1

gpio_state = OnionGpio(GARAGE_STATE_PIN)
gpio_relay = OnionGpio(GARAGE_RELAY_PIN)

app = Flask(__name__)

###
###  Web Routes
###

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/api/open', methods=['POST'])
def open():
    if _status() == GARAGE_STATE_OPEN_VALUE:
        return 'noop'
    else:
        _toggle()
        return 'opened'

@app.route('/api/close', methods=['POST'])
def close():
    if _status() == GARAGE_STATE_CLOSE_VALUE:
        return 'noop'
    else:
        _toggle()
        return 'closed'

@app.route('/api/status', methods=['GET'])
def status():
	return '%s' % _status()


###
### Private Helpers
###

def _status():
    return int(gpio_state.getValue())

def _toggle():
    gpio_relay.setValue(GARAGE_STATE_OPEN_VALUE)
    time.sleep(1)
    gpio_relay.setValue(GARAGE_STATE_CLOSE_VALUE)
