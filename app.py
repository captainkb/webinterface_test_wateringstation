from flask import Flask, render_template, Response, request, redirect, url_for,jsonify
from datetime import datetime
import os
import sqlite3
import time

app = Flask(__name__)


#def index():
#    return render_template('index.html')

class local_clock:
    def __init__(self):
        self.start_time = 0.0

def log_sqlite3_watering_station_data(pumped_volume,pump_rate,motor_running_time,pump_active):
    with sqlite3.connect("C:\\Users\\i00504308\\Desktop\\python_project\\watering_station_data.db") as conn:
        TableName = "water_station_1"
        now = datetime.now()
        timeString = now.strftime("%Y-%m-%d %H:%M")
        sql = ''' INSERT INTO water_station_1(date,pumped_volume,pump_rate,motor_running_time,pump_active) VALUES('%s',%.3f,%.3f,%.3f,%.3f)''' % (timeString,pumped_volume,pump_rate,motor_running_time,pump_active)
        print(sql)
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()


class WateringStation:
    #Each pump, container -> Watering station
    # To Do: incorporate counting time when the pump is active through manual activation (i.g through HMI / in the future flask over route)
    def __init__(self,adafruit_motor,pump_rate):
        # pump_rate in l/min, adafruit_motor is the number of motor on the board
        self.pumped_volume = 0.0;
        self.pump_rate = pump_rate;
        self.adafruit_motor = adafruit_motor;
        self.motor_throttle = 1.0;
        self.motor_running_time = 0.0;
        self.pump_active = False;
        self.start_time = 0.0;



@app.route('/')
def hello():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    '''data = {pump1_volume': station1.pumped_volume,
            'pump1_pumprate': station1.pump_rate,
            'pump2_volume': station2.pumped_volume,
            'pump2_pumprate': station2.pump_rate,
            'pump3_volume': station3.pumped_volume,
            'pump3_pumprate': station3.pump_rate,
            'pump4_volume': station4.pumped_volume,
            'pump4_pumprate': station4.pump_rate
            'time' : dt_string
            }'''

    with sqlite3.connect("C:\\Users\\i00504308\\Desktop\\python_project\\watering_station_data.db") as conn:
        cursor = conn.execute('SELECT date,pumped_volume,pump_rate,motor_running_time,pump_active FROM water_station_1 order by date desc limit 10')
        return render_template('index2.html', data=cursor.fetchall())

@app.route('/get_toggled_status',methods =['get','POST'])
def toggled_status():
    current_status = None;

    #print(request.json['data'])
    if request.method == "POST":
        data = {}
        data['status'] = request.json['status']
        print(request.json['status'])
        if data['status'] == True:
            end_time = 0.0;
            station1.start_time = time.time();
        elif data['status'] == False:
            end_time = time.time();
            duration = (end_time - station1.start_time);
            if duration != 0.0:
                log_sqlite3_watering_station_data(station1.pumped_volume,station1.pump_rate,duration,station1.pump_active);


        return jsonify(data)
    else:
        print('whatever')
        return render_template('index2.html')

@app.route('/get_toggled_status_2',methods =['get','POST'])
def toggled_status_2():
    current_status = None;
    #print(request.json['data'])
    if request.method == "POST":
        data = {}
        data['status_pump2'] = request.json['status_pump2']
        print(request.json['status_pump2'])

        return jsonify(data)
    else:
        print('whatever')
        return render_template('index2.html')

@app.route('/get_toggled_status_3', methods=['get', 'POST'])
def toggled_status_3():
    current_status = None;

    if request.method == "POST":
        data = {}
        data['status_pump3'] = request.json['status_pump3']
        print(request.json['status_pump3'])

        return jsonify(data)
    else:
        print('whatever')
        return render_template('index2.html')

@app.route('/get_toggled_status_4', methods=['get', 'POST'])
def toggled_status_4():
    current_status = None;

    if request.method == "POST":
        data = {}
        data['status_pump4'] = request.json['status_pump4']
        print(request.json['status_pump4'])

        return jsonify(data)
    else:
        print('whatever')
        return render_template('index2.html')
@app.route('/get_toggled_status_mqtt', methods=['get', 'POST'])
def toggled_status_mqtt():
    current_status = None;

    if request.method == "POST":
        data = {}
        data['mqtt_active'] = request.json['mqtt_active']
        print(request.json['mqtt_active'])

        return jsonify(data)
    else:
        print('whatever')
        return render_template('index2.html')

@app.route('/reboot_pi',methods = ['POST'])
def reboot():
    print('sudo reboot');
    return 'reboot'
    #return render_template('index2.html')

@app.route('/print_items')
def print_items():
    with sqlite3.connect("C:\\Users\\i00504308\\Desktop\\python_project\\watering_station_data.db") as conn:
        cursor = conn.execute('SELECT date,pumped_volume,pump_rate,motor_running_time,pump_active FROM water_station_1')
        return render_template('index2.html', items=cursor.fetchall())



if __name__ == '__main__':

    station1 = WateringStation(1,0.05);
    station2 = WateringStation(2, 0.05);
    station3 = WateringStation(3, 0.05);
    station4 = WateringStation(4, 0.05);



    conn = None
    try:
        conn = sqlite3.connect("C:\\Users\\i00504308\\Desktop\\python_project\\watering_station_data.db")
    except sqlite3.Error as e:
        print(e)

    app.run(host="localhost", port=5000, debug=True)