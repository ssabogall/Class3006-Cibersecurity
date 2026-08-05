## Punto 7: Recomendaciones de seguridad y reconocimiento adicional

### a. Recomendaciones de seguridad para el manejo del segmento 10.10.1.0/24

**Segmentación y control de acceso**
- Aislar el servidor de base de datos (10.10.1.99) en una VLAN dedicada, separada de la red general de empleados, con reglas de firewall que solo permitan tráfico desde los hosts/servicios necesarios.
- Implementar NAC (802.1X) para controlar qué dispositivos pueden conectarse al segmento, dado que las IPs se asignan dinámicamente por DHCP.
- Usar reservas DHCP / MAC binding para los servidores críticos.
- Activar DHCP snooping para evitar servidores DHCP no autorizados (rogue DHCP).

**Servicios inseguros expuestos**
- **Puerto 23 (Telnet):** reemplazarlo por SSH. Telnet transmite credenciales en texto plano.
- **Puerto 21 (FTP):** migrar a SFTP o FTPS y validar que no haya acceso anónimo habilitado.
- **Puerto 5000 (API de redirección de Excel):** candidata a SSRF o inclusión de archivos si no valida bien los parámetros. Requiere autenticación obligatoria, validación estricta de inputs (allowlist), no exposición sin auth, y logging de cada solicitud.


**Gestión general**
- Cifrado de datos en tránsito y en reposo.
- Privilegio mínimo de acceso a la base de datos.
- Parcheo y actualización regular de los servicios expuestos.
- Monitoreo/IDS-IPS en el segmento.
- Auditoría y logging centralizado de accesos.

### b. Información adicional a levantar del scan

- Banner grabbing en puertos 21, 23 y 5000 para identificar software y versión exacta.
- Escaneo completo de puertos (no solo top ports) sobre 10.10.1.99 y todo el /24.
- Fingerprinting de sistema operativo del servidor y otros hosts.
- Descubrimiento de hosts activos en todo el segmento /24.
- Enumeración de endpoints de la API en el puerto 5000 (buscar Swagger/OpenAPI, rutas comunes).
- Verificar acceso FTP anónimo y credenciales por defecto en Telnet (solo documentar, no explotar).
- Confirmar comportamiento del DHCP (rango de IPs, tiempo de lease, autenticación) para planear las pruebas.
- Esta información sustenta ante el cliente el valor del contrato de +$300.000 USD, identificando tres vectores concretos (Telnet en claro, FTP en claro, posible SSRF) desde el reconocimiento.