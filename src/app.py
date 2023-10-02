from flask import Flask, render_template, request, redirect
import main
from flask_socketio import SocketIO


app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process_input', methods=['POST'])
def process_input():
    location = request.form.get('location')
    min_temp = request.form.get('min_temp')
    max_temp = request.form.get('max_temp')

    # Call the process_data function with the form values
    location_result, min_temp_result, max_temp_result = main.process_data(location, min_temp, max_temp)
    return redirect('/')
@socketio.on('weather_alert')
def handle_weather_alert(data):
    print('Received weather alert:', data)
    # Pass the results to the function in other_file.py
    # main.process_results(location_result, min_temp_result, max_temp_result)
   

if __name__ == "__main__":
    socketio.run(app, debug=True)
