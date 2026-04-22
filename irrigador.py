import paho.mqtt.client as mqtt

# Configurações de Conexão
BROKER = "78262e395b904e27b6d8063d6d83424a.s1.eu.hivemq.cloud"
PORTA = 8883
USER = "admin"
PASSWORD = "hivemq"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado ao HiveMQ!")
        
        client.subscribe("agro/umidade")
    else:
        print(f"Falha na conexão. Código: {rc}")

def on_message(client, userdata, msg):
    try:
        
        umidade = float(msg.payload.decode())
        print(f"Umidade atual: {umidade}%")

        if umidade < 30:
            status = "ON"
            print("Solo seco! Irrigador: LIGADO")
        else:
            status = "OFF"
            print("Solo úmido. Irrigador: DESLIGADO")
        
        
        client.publish("agro/irrigador", status)
        
    except ValueError:
        print(f"Erro: Mensagem inválida recebida em {msg.topic}")

# Inicialização do Cliente
client = mqtt.Client()

# Define usuário e senha 
client.username_pw_set(USER, PASSWORD)

# Configura as funções de callback
client.on_connect = on_connect
client.on_message = on_message

# Conecta ao broker
client.connect(BROKER, PORTA, 60)

# Mantém o script rodando
client.loop_forever()