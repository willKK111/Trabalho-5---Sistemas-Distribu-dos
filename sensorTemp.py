import paho.mqtt.client as mqtt
import time
import random

# Configurações de Conexão
BROKER = "localhost"
PORTA = 1883
USER = "admin"      
PASSWORD = "hivemq" 

client = mqtt.Client()

client.username_pw_set(USER, PASSWORD)

print(f"Iniciando sensor de temperatura em {BROKER}...")
client.connect(BROKER, PORTA, 60)

try:
    while True:
        # Gera um valor de temperatura entre 20°C e 35°C
        temperatura = round(random.uniform(20.0, 35.0), 2)
        
        client.publish("agro/temperatura", temperatura)
        
        status = "ALTA" if temperatura > 30 else "NORMAL"
        print(f"Temperatura: {temperatura}°C | Status: {status}")
        
        time.sleep(5)

except KeyboardInterrupt:
    print("\nSensoriamento de temperatura interrompido.")
    client.disconnect()