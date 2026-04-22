import paho.mqtt.client as mqtt

#Configuração da Conexão
Porta = 8883
BROKER = "78262e395b904e27b6d8063d6d83424a.s1.eu.hivemq.cloud"

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


client.connect(BROKER, Porta, 60)

print("Iniciando loop de escuta...")
client.loop_forever()