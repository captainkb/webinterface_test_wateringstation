from flask import Flask,render_template,request,jsonify
#def index():
#    return render_template('index.html')
import app
from datetime import datetime



@app.route('/')
def hello():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    data = {''''pump1_volume': station1.pumped_volume,
            'pump1_pumprate': station1.pump_rate,
            'pump2_volume': station2.pumped_volume,
            'pump2_pumprate': station2.pump_rate,
            'pump3_volume': station3.pumped_volume,
            'pump3_pumprate': station3.pump_rate,
            'pump4_volume': station4.pumped_volume,
            'pump4_pumprate': station4.pump_rate'''
            'time' : dt_string
            }
    return render_template('index2.html',data=data)

@app.route('/get_toggled_status',methods =['get','POST'])
def toggled_status():
    current_status = None;
    #print(request.json['data'])
    if request.method == "POST":
        data = {}
        data['status'] = request.json['status']
        print(request.json['status'])

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