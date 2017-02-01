from flask import Flask, render_template

# for reading from the usb serial
import sys
import serial
import time

app = Flask(__name__)

# init serial, open arduino to check the port that the arduino is using
ser = serial.Serial('/dev/ttyACM0')

# route to read from arduino
@app.route("/read_from_arduino")
def read_from_arduino():
	
	# output what the serial is saying
	output = ser.readline()

	# return the values
	return output

# route to turn on the water pomp
@app.route('/pomp/aan')
def pomp_state_on():
	# let the arduino rest
	time.sleep(1.5)

	ser.write('pomp_aan')

	return 'pomp_aan'

# route to turn off the water pomp
@app.route('/pomp/uit')
def pomp_state_off():
	# let the arduino rest
	time.sleep(1.5)

	ser.write('pomp_uit')

	return 'pomp_uit'

# render the dashboard
@app.route("/")
def hello():
	return render_template('home.html')

# run the app
if __name__ == "__main__":
    app.run()