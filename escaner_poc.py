"""
Prueba de Concepto (PoC) - NetGuard
Autores: Rubén Castellanos y Giany Marian
Descripción: Script para escanear la red local y detectar dispositivos conectados
mediante peticiones ARP. Demuestra la viabilidad técnica del motor de escaneo.
"""

from scapy.all import ARP, Ether, srp

def escanear_red(ip_rango):
    print(f"[*] Iniciando escaneo en el rango: {ip_rango}...\n")
    
    # 1. Crear paquete ARP para preguntar quién tiene cada IP en el rango
    arp_request = ARP(pdst=ip_rango)
    
    # 2. Crear paquete Ethernet para enviar la petición a la dirección MAC de difusión (broadcast)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    
    # 3. Combinar ambos paquetes
    arp_request_broadcast = broadcast / arp_request
    
    # 4. Enviar el paquete y capturar las respuestas (srp envía y recibe a nivel de capa 2)
    # timeout=2 espera 2 segundos la respuesta; verbose=False oculta el texto basura
    respuestas_recibidas = srp(arp_request_broadcast, timeout=2, verbose=False)[0]
    
    # 5. Organizar los resultados en una lista de diccionarios
    dispositivos_encontrados = []
    for enviado, recibido in respuestas_recibidas:
        dispositivos_encontrados.append({'ip': recibido.psrc, 'mac': recibido.hwsrc})
        
    return dispositivos_encontrados

if __name__ == "__main__":
    # Sustituid esta IP por el rango de vuestra red local (ej. 192.168.1.1/24 o 192.168.0.1/24)
    rango_red_local = "192.168.1.1/24" 
    
    resultado = escanear_red(rango_red_local)
    
    print("Dispositivos detectados en la red:")
    print("-----------------------------------------")
    print("IP\t\t\tDIRECCIÓN MAC")
    print("-----------------------------------------")
    
    for dispositivo in resultado:
        print(f"{dispositivo['ip']}\t\t{dispositivo['mac']}")