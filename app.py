from flask import Flask, render_template
from flask_socketio import SocketIO
import paho.mqtt.client as mqtt

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")


def on_connect(client, userdata, flags, rc):
    print("Flask conectado ao HiveMQ")
    client.subscribe("agro/#")


def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    
    socketio.emit('mqtt_update', {'topic': msg.topic, 'value': payload})

mqtt_client = mqtt.Client()
mqtt_client.username_pw_set("admin", "hivemq")
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message


mqtt_client.connect("localhost", 1883, 60)
mqtt_client.loop_start()

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Usar debug=True ajuda no desenvolvimento, mas desative em produção
    socketio.run(app, port=5000, debug=True)