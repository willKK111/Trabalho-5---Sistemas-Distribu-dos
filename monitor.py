import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado com sucesso ao HiveMQ!")
        
        client.subscribe("agro/#")
    else:
        print(f"Falha na conexão. Código de erro: {rc}")

def on_message(client, userdata, msg):
    print(f"Tópico: {msg.topic} | Mensagem: {msg.payload.decode()}")

client = mqtt.Client()


client.username_pw_set("admin", "hivemq")

client.on_connect = on_connect
client.on_message = on_message


client.connect("localhost", 1883, 60)

print("Iniciando loop de escuta...")
client.loop_forever()