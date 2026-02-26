# NetGuard - Prueba de Concepto (PoC) 🛡️

**Titulación:** Desarrollo de Aplicaciones Multiplataforma (DAM)
**Autores:** Rubén Castellanos de la Peña y Giany Marian Sarbu

## Descripción
Este repositorio contiene la Prueba de Concepto (PoC) para el Trabajo de Fin de Grado (TFG) del proyecto **NetGuard**. 

El script `escaner_poc.py` demuestra la viabilidad técnica del motor central de auditoría de red. Utiliza la librería **Scapy** de Python para emitir peticiones ARP (Address Resolution Protocol) a la dirección de difusión (*broadcast*) y capturar las respuestas en la capa 2 del modelo OSI. 

Esto permite identificar de forma precisa y en tiempo real las direcciones IP y MAC de los dispositivos conectados a la red local, sentando las bases para el futuro módulo de control de acceso y notificaciones.

## Tecnologías empleadas
* Python 3.x
* Scapy (Manipulación de paquetes de red)
* Npcap (Driver de captura para entornos Windows)

## Ejecución
Para probar el script en un entorno local, ejecutar con privilegios de administrador:
```bash
python escaner_poc.py
