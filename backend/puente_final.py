import requests
import serial
import time

# CONFIGURACIÓN
IP_SERVIDOR = "http://143.244.153.38:5000/leer_comando"
PUERTO_SERIAL = "COM7"  # <--- ¡CAMBIA ESTO POR TU COM!

try:
    arduino = serial.Serial(PUERTO_SERIAL, 115200, timeout=1)
    time.sleep(2) # Esperar a que el Arduino despierte
    print(f"--- CONECTADO AL ARDUINO EN {PUERTO_SERIAL} ---")
except:
    print("ERROR: No se detecta el Arduino. Revisa el cable y el puerto COM.")
    exit()

while True:
    try:
        # 1. Leer qué orden hay en la nube
        response = requests.get(IP_SERVIDOR, timeout=5)
        data = response.json()
        comando = data.get("comando")

        if comando != "esperar":
            print(f"¡Orden detectada en la nube!: {comando}")
            
            # 2. Enviarla por USB al Arduino
            arduino.write(f"{comando}\n".encode())
            
            # 3. Limpiar la orden en la nube para que no se repita infinitamente
            requests.post("http://143.244.153.38:5000/mandar_comando", json={"comando": "esperar"})
            print("Esperando nueva orden...")

    except Exception as e:
        print(f"Error de conexión: {e}")
    
    time.sleep(1) # Revisar cada segundo