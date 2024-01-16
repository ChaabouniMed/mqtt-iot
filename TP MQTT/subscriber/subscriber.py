from flask import Flask, render_template, jsonify, send_from_directory
import paho.mqtt.client as mqtt
from flask_cors import CORS

app = Flask(__name__, static_url_path='')
CORS(app)

# Variable pour stocker la dernière valeur de température
last_temperature = "N/A"

# Callbacks for MQTT events
def on_connect(client, userdata, flags, rc, properties=None):
    print("Connected with result code "+str(rc))
    client.subscribe("Temp", qos=1)

def on_message(client, userdata, msg):
    global last_temperature
    last_temperature = msg.payload.decode('utf-8')
    print("Received temperature: " + last_temperature)

# MQTT client setup
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("MedChaabouni", "21473913med")
client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)
client.connect("61d4b7c5d97d42858b6836273e6b8e39.s2.eu.hivemq.cloud", 8883, 60)

# Flask route pour afficher l'interface web
# @app.route('/')
# def index():
#     return render_template('index.html')

# Flask route pour récupérer les données de température via une API
@app.route('/api/temperature', methods=['GET'])
def get_temperature():
    global last_temperature
    return jsonify({"temperature": last_temperature})

# @app.route('/')
# def serve_html():
#     return send_from_directory('', 'index.html')

# Commencez la boucle du client MQTT dans un thread séparé
client.loop_start()

# Commencez l'application Flask
if __name__ == '__main__':
    app.run(debug=True)
