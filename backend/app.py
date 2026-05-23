from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Variable global para guardar el comando actual
comando_actual = {"comando": "esperar"}

@app.route('/')
def home():
    return "Servidor Phantom Funcionando"

# 1. ESTA RUTA ES LA QUE USA EL NAVEGADOR/CURL PARA MANDAR LA ORDEN
@app.route('/mandar_comando', methods=['POST', 'GET'])
def mandar_comando():
    global comando_actual
    # Si viene por URL (?comando=saludar) o por JSON
    nuevo = request.args.get('comando') or request.json.get('comando')
    
    if nuevo:
        comando_actual["comando"] = nuevo
        return jsonify({"status": "ok", "comando_actualizado": nuevo}), 200
    return jsonify({"error": "No enviaste un comando"}), 400

# 2. ESTA RUTA ES LA QUE EL ESP32 REVISA CADA 2 SEGUNDOS
@app.route('/leer_comando', methods=['GET'])
def leer_comando():
    global comando_actual
    # Enviamos el comando y luego lo reseteamos a "esperar" 
    # para que el robot no lo repita infinitamente
    respuesta = jsonify(comando_actual)
    comando_actual = {"comando": "esperar"} 
    return respuesta, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)