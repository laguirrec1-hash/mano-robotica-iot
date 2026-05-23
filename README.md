# 🦾 Sistema de Control End-to-End
## Mano Robótica Biónica Interactiva

Sistema IoT distribuido para el control remoto y en tiempo real de una mano robótica biónica basada en ESP32, Docker y microservicios REST.

---

## 🚀 Tecnologías

![ESP32](https://img.shields.io/badge/ESP32-IoT-blue)
![Python](https://img.shields.io/badge/Python-Flask-yellow)
![Docker](https://img.shields.io/badge/Docker-Containers-blue)
![DigitalOcean](https://img.shields.io/badge/Cloud-DigitalOcean-0080FF)
![C++](https://img.shields.io/badge/Firmware-C++-orange)

---

# 📐 Arquitectura del Sistema

```text
Frontend Web
     │
     ▼
API REST (Flask + Docker)
     │
     ▼
ESP32 Firmware (C++)
     │
     ▼
PCA9685 PWM Controller
     │
     ▼
Servomotores
```

---

# 🌐 Frontend Web

Interfaz responsiva desarrollada con:

- HTML5
- CSS3
- JavaScript

Funciones:

- Control remoto en tiempo real
- Comunicación HTTP asíncrona
- Activación de movimientos con un clic

---

# ⚙️ Backend API REST

Microservicio Flask desplegado en Docker sobre DigitalOcean.

## Endpoint principal

```text
http://143.244.153.38:5000
```

## Endpoints

| Endpoint | Función |
|---|---|
| `/mandar_comando` | Envía comandos |
| `/leer_comando` | Obtiene comandos pendientes |

---

# 🧠 Firmware ESP32

Firmware embebido en C++ ejecutado sobre ESP32 de doble núcleo.

## Funciones principales

- Polling HTTP cada 200ms
- Decodificación JSON
- Comunicación I2C
- Control PWM sincronizado

---

# 🔌 Control de Potencia

Controlador PWM PCA9685 conectado vía I2C.

## Configuración

| ESP32 | PCA9685 |
|---|---|
| GPIO 21 | SDA |
| GPIO 22 | SCL |
| 5V | VCC |
| GND | GND |

---

# 🛡️ Protección de Hardware

Los servomotores de rotación continua pueden dañarse si reciben PWM continuo.

## Solución implementada

```cpp
ejecutarMovimiento(pin, velocidad)
```

### Flujo

1. Activa el movimiento
2. Espera 800ms
3. Envía valor `4096`
4. Corta completamente el PWM

## Beneficios

- ✅ Sin drift
- ✅ Sin vibraciones
- ✅ Protección mecánica
- ✅ Menor consumo energético

---

# 🐳 Docker Deployment

## Construcción de la imagen

```bash
docker build -t mano-robotica-backend .
```

## Ejecución del contenedor

```bash
docker run -d -p 5000:5000 \
--name api-mano-iot \
mano-robotica-backend
```

---

# 📡 API de Comandos

Todos los comandos se envían mediante:

```http
POST /mandar_comando
```

---

# ✋ Comandos Básicos

| Acción | Comando |
|---|---|
| Cerrar Pulgar | `cerrar1` |
| Abrir Pulgar | `abrir1` |
| Cerrar Índice | `cerrar2` |
| Abrir Índice | `abrir2` |

---

# 🤖 Gestos Disponibles

| Gesto | Comando |
|---|---|
| ✊ Puño | `todo_cerrar` |
| 🖐️ Mano abierta | `todo_abrir` |
| ✌️ Paz | `gesto_paz` |
| 🤘 Rock | `gesto_rock` |
| 👌 OK | `gesto_ok` |

---

# 🧪 Ejemplo CURL

```bash
curl -X POST http://143.244.153.38:5000/mandar_comando \
-H "Content-Type: application/json" \
-d "{\"comando\":\"gesto_rock\"}"
```

---

# 🛑 Parada de Emergencia

```bash
curl -X POST http://143.244.153.38:5000/mandar_comando \
-H "Content-Type: application/json" \
-d "{\"comando\":\"parar\"}"
```

---

# 📊 Monitoreo Docker

## Crear contexto remoto

```bash
docker context create digitalocean-live \
--description "Servidor Cloud Produccion" \
--docker "host=ssh://root@143.244.153.38"
```

## Ver logs

```bash
docker logs -f api-mano-iot
```

---

# ⚠️ Nota de Potencia

Los servomotores requieren:

```text
Fuente externa 5V / mínimo 3A
```

❌ Nunca alimentar directamente desde el ESP32.

---

# 🚀 Estado del Proyecto

- ✅ Arquitectura funcional
- ✅ Control síncrono
- ✅ Infraestructura cloud
- ✅ Protección electrónica
- 🚧 Futuras mejoras IA + visión artificial

---

# 👨‍💻 Autor

Proyecto enfocado en:

- Robótica biónica
- Sistemas embebidos
- IoT distribuido
- Automatización en tiempo real
