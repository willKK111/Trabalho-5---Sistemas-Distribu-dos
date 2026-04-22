import paho.mqtt.client as mqtt
import time
import random

# Configurações de Conexão
BROKER = "78262e395b904e27b6d8063d6d83424a.s1.eu.hivemq.cloud"
PORTA = 8883
USER = "admin"      
PASSWORD = "hivemq" 

client = mqtt.Client()

client.username_pw_set(USER, PASSWORD)

print(f"Conectando ao broker em {BROKER}...")
client.connect(BROKER, PORTA, 60)

try:
    while True:
        # Gera um valor aleatório de umidade
        umidade = round(random.uniform(10, 80), 2)
        
        client.publish("agro/umidade", umidade)
        
        print(f"Sensor enviando -> Umidade: {umidade}%")
        
        time.sleep(5)

except KeyboardInterrupt:
    print("\nSimulação encerrada pelo usuário.")
    client.disconnect()