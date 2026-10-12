# Actividad Académica II — Informe Práctico de Instalación y Hardening de un SGBD

> **Universidad Privada Domingo Savio (UPDS)**  
> **Facultad de Ingeniería — Carrera de Ingeniería en Sistemas**  
> **Materia:** Taller de Base de Datos II  
> **Docente:** Ing. Pablo Moscoso Zeballos  
> **Autores:** Adriana Rodríguez Sotelo | Gabriel Kevin Alcon Maydana  
> **Sede y Fecha:** Santa Cruz de la Sierra - Bolivia, 08 de octubre de 2026  
> **Plataforma Evaluada:** PostgreSQL 16 sobre Ubuntu Server 24.04 LTS  

---

## 📌 Resumen Ejecutivo de la Práctica

El presente proyecto documenta la práctica de instalación y bastionado (*hardening*) de **PostgreSQL 16** desplegado sobre **Ubuntu Server 24.04 LTS**, bajo un enfoque académico de laboratorio orientado a la defensa técnica presencial.

El objetivo central consistió en partir de una instalación básica predeterminada (*"vanilla"*) y aplicar controles esenciales de seguridad que reduzcan la superficie de exposición y accesos innecesarios, tomando como referencia buenas prácticas de:
* **PostgreSQL Global Development Group (2026)**
* **Canonical / Documentación de Ubuntu Server (2026)**
* **Instituto Nacional de Ciberseguridad de España — INCIBE (2023)**
* **Center for Internet Security (CIS Benchmarks)**

> [!NOTE]
> **Alcance del Proyecto:**  
> El informe mantiene total transparencia metodológica: su alcance es académico y de laboratorio controlado, demostrando de forma clara y reproducible cómo configuraciones sencillas fortalecen sustancialmente un SGBD, sin sobredimensionar el trabajo con certificaciones o auditorías empresariales no aplicadas.

---

## 🖥️ Estructura de la Presentación Oficial (14 Diapositivas)

Las diapositivas fueron diseñadas en formato panorámico (16:9) bajo el sistema editorial tecnológico *"Obsidian & Electric Sapphire"*, con subpaneles de comandos destacados (`#0b162c`, borde cían `#38bdf8` y etiquetas terminales `⚡ COMANDOS`), distribuidas de la siguiente manera:

| Nº | Título de la Diapositiva | Eje Temático y Cobertura Técnica del PDF |
| :---: | :--- | :--- |
| **01** | **Portada y Ficha Técnica Académica** | UPDS, Facultad de Ingeniería, autores, autoridades académicas, entorno y ficha técnica. |
| **02** | **Resumen y Enfoque Metodológico** | Justificación del proyecto, los 6 ejes técnicos y delimitación del alcance demostrable. |
| **03** | **Introducción al Hardening de SGBD** | Definición de bastionado según INCIBE (2023), justificación de PostgreSQL 16 y Ubuntu 24.04. |
| **04** | **Objetivo y Entorno de Laboratorio** | Tabla oficial de parámetros: SGBD, SO, red `192.168.1.0/24`, BD `app_practica`, usuario `app_user`. |
| **05** | **Instalación de PostgreSQL 16** | Comandos `apt update`, `apt upgrade -y`, `apt install postgresql postgresql-contrib -y`, `systemctl status` y acceso con `sudo -u postgres psql`. |
| **06** | **Medida 1: Actualización del Sistema** | Seguridad por capas recomendada por Canonical (2026), mitigación de vulnerabilidades conocidas. |
| **07** | **Medida 2: Restricción de Conexiones** | Configuración de `pg_hba.conf`: `peer` local, acceso `hostssl` para `app_user` en `192.168.1.0/24` y reglas `reject` generales. |
| **08** | **Medida 3: Autenticación Robusta** | Cifrado obligatorio `password_encryption = 'scram-sha-256'`, creación de `app_practica` y usuario `app_user`. |
| **09** | **Medida 4: Mínimo Privilegio (Roles)** | Segregación de roles `rol_lectura` y `rol_escritura` con cláusula `NOLOGIN`, asignación controlada a `app_user`. |
| **10** | **Medida 4 (Cont.): Esquema Public** | Saneamiento y mitigación de abusos mediante `REVOKE CREATE ON SCHEMA public FROM PUBLIC;`. |
| **11** | **Medidas 5 y 6: Archivos de Datos y TLS** | Permisos del SO `chown -R postgres:postgres` y `chmod 0700` en `/var/lib/postgresql/16/main`. Certificado X.509 RSA 2048 (`server.crt`/`server.key` en `0600`) y `ssl = on`. |
| **12** | **Medidas 7 y 8: Registros y Respaldo** | Activación de colector nativo (`logging_collector`, `log_connections`, `log_disconnections`, `log_line_prefix`) y copia lógica comprimida con `pg_dump -F c`. |
| **13** | **Verificación Experimental** | Batería de 7 comprobaciones directas en terminal (servicio activo, versión, roles `\du`, SCRAM, TLS con `\conninfo`, rechazo de red y backup). |
| **14** | **Resultados y Conclusiones** | Tabla comparativa de Sección 6 (Básica vs Post-Hardening) en 6 dimensiones, conclusiones y trabajo futuro. |

---

## 📁 Entregables del Repositorio

* **[`index.html`](index.html):** Presentación web interactiva completa de 14 diapositivas, con Bento Grids, cambio de tema Claro/Oscuro (`[T]`), modo pantalla completa (`[F]`), cajón de miniaturas (`[G]`) y copiado de comandos.
* **[`style.css`](style.css):** Hoja de estilos con paleta de alto contraste, iluminación ambiental y terminales de comandos destacados.
* **[`app.js`](app.js):** Controlador JavaScript con gestión de estado, atajos de teclado y sincronización de títulos.
* **[`presentacion_hardening_sgbd.pptx`](presentacion_hardening_sgbd.pptx):** Presentación oficial generada en PowerPoint (16:9), 100% fiel al contenido del PDF.
* **[`presentacion_hardening_sgbd_actualizada.pptx`](presentacion_hardening_sgbd_actualizada.pptx):** Copia de sincronización de la presentación PowerPoint.
* **[`generar_pptx.py`](generar_pptx.py):** Script en Python (`python-pptx`) para regenerar determinísticamente las diapositivas.

---

# 🚀 RECOMENDACIONES PARA MEJORAR EL INFORME ACADÉMICO

A continuación se presenta un conjunto estructurado de **recomendaciones técnicas, metodológicas y visuales** diseñadas específicamente para enriquecer el informe presentado, elevar su calificación y asegurar una defensa oral sobresaliente.

---

### 1. Inclusión de Evidencias Visuales de Consola (Capturas de Pantalla Reales)
* **Diagnóstico actual:** La Sección 5 del informe presenta una tabla muy clara con 7 pruebas ejecutadas, pero solo en formato de texto descriptivo.
* **Recomendación:** Incorporar en el cuerpo del informe o en un anexo técnico capturas de pantalla reales de la terminal de Ubuntu Server.
* **Detalle de capturas sugeridas:**
  1. Captura de `$ sudo systemctl is-active postgresql` y `$ psql --version`.
  2. Captura dentro de psql ejecutando `\du` mostrando la existencia de `app_user`, `rol_lectura` y `rol_escritura`.
  3. Captura de `SHOW password_encryption;` respondiendo `scram-sha-256`.
  4. Captura del cliente remoto ejecutando `\conninfo` donde se aprecie claramente el texto:  
     `SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, bits: 256)`.
  5. Captura del intento de conexión desde una máquina cliente fuera del segmento `192.168.1.0/24` mostrando el mensaje de denegación:  
     `FATAL: no pg_hba.conf entry for host "...".`
  6. Captura de `$ ls -lh app_practica.backup` evidenciando el tamaño real y permisos del archivo.
* **Impacto académico:** Convierte afirmaciones teóricas en evidencias empíricas irrefutables para el docente evaluador.

---

### 2. Implementación de Cortafuegos del Sistema Operativo con UFW (Defensa en Profundidad)
* **Diagnóstico actual:** El informe menciona en sus conclusiones que un cortafuegos podría ser trabajo futuro.
* **Recomendación:** Integrar una subsección práctica con el cortafuegos `ufw` nativo de Ubuntu Server como parte de la estrategia de seguridad por capas citada de Canonical.
* **Comandos sugeridos para incorporar:**
  ```bash
  # 1. Habilitar política restrictiva por defecto
  sudo ufw default deny incoming
  sudo ufw default allow outgoing

  # 2. Permitir acceso de administración remota SSH
  sudo ufw allow 22/tcp comment 'SSH Administrativo'

  # 3. Permitir tráfico de PostgreSQL únicamente desde la subred autorizada
  sudo ufw allow proto tcp from 192.168.1.0/24 to any port 5432 comment 'PostgreSQL LAN Laboratorio'

  # 4. Activar cortafuegos y verificar reglas
  sudo ufw enable
  sudo ufw status verbose
  ```
* **Justificación técnica:** Si un administrador comete un error de sintaxis en `pg_hba.conf` o el servicio queda expuesto accidentalmente en `0.0.0.0`, el filtro de paquetes a nivel de kernel (Netfilter) descarta el tráfico no deseado antes de que siquiera llegue al puerto de PostgreSQL.

---

### 3. Validación y Demostración de Restauración del Backup (`pg_restore`)
* **Diagnóstico actual:** La Sección 4.8 aborda la generación del respaldo con `pg_dump`, pero no documenta el proceso de recuperación ante desastres. En auditoría de bases de datos se dice: *"Un respaldo no probado no es un respaldo garantizado"*.
* **Recomendación:** Agregar un procedimiento de prueba de restauración en una base de datos secundaria para comprobar la integridad del archivo generado.
* **Comandos sugeridos:**
  ```bash
  # Crear una base de datos de pruebas de restauración
  sudo -u postgres psql -c "CREATE DATABASE app_practica_restore;"

  # Restaurar el respaldo lógico generado
  sudo -u postgres pg_restore -d app_practica_restore -v app_practica.backup

  # Verificar que las tablas y registros existen íntegramente
  sudo -u postgres psql -d app_practica_restore -c "\dt"
  ```
* **Justificación técnica:** Demuestra comprensión del ciclo completo de vida del dato y de métricas clave de continuidad como el RPO (*Recovery Point Objective*) y RTO (*Recovery Time Objective*).

---

### 4. Automatización del Respaldo con Tarea Programada (`Cron Job`)
* **Diagnóstico actual:** El comando `pg_dump` se ejecuta manualmente. En un escenario operativo, los respaldos manuales son propensos a olvidos humanos.
* **Recomendación:** Documentar un script bash sencillo en `/usr/local/bin/backup_postgresql.sh` con política de retención automática programado en `crontab`.
* **Script sugerido:**
  ```bash
  #!/bin/bash
  BACKUP_DIR="/var/backups/postgresql"
  FECHA=$(date +"%Y%m%d_%H%M%S")
  mkdir -p $BACKUP_DIR
  pg_dump -U postgres -F c -d app_practica -f "$BACKUP_DIR/app_practica_$FECHA.backup"
  # Retener únicamente los últimos 7 días de respaldos
  find $BACKUP_DIR -name "*.backup" -type f -mtime +7 -delete
  ```
  ```bash
  # Programar ejecución diaria a las 02:00 AM en el crontab de postgres:
  0 2 * * * /usr/local/bin/backup_postgresql.sh
  ```

---

### 5. Política de Rotación y Limpieza de Logs de Actividad
* **Diagnóstico actual:** En la Sección 4.7 se habilitó `logging_collector = on`, `log_connections = on` y `log_disconnections = on`, pero no se especificaron parámetros de rotación. En servidores reales, esto puede provocar el llenado descontrolado del disco duro.
* **Recomendación:** Añadir en `postgresql.conf` la política de rotación de logs recomendada por CIS Benchmark:
  ```ini
  # En /etc/postgresql/16/main/postgresql.conf
  log_directory = 'log'
  log_filename = 'postgresql-%Y-%m-%d_%H%M%S.log'
  log_file_mode = 0600
  log_rotation_age = 1d          # Rotación diaria automática
  log_rotation_size = 100MB      # Rotación si supera los 100 megabytes
  log_truncate_on_rotation = on  # Sobrescribe archivos homónimos viejos
  ```

---

### 6. Diagrama de Topología y Arquitectura del Laboratorio
* **Diagnóstico actual:** El informe describe la subred `192.168.1.0/24` y el usuario `app_user` en tablas de texto.
* **Recomendación:** Insertar en la Sección 2 una figura con el diagrama de topología de red.
* **Diagrama conceptual de la práctica:**

```
                  ┌────────────────────────────────────────────────────────┐
                  │                 RED LOCAL DE LABORATORIO               │
                  │                     192.168.1.0/24                     │
                  └───────────────────────────┬────────────────────────────┘
                                              │
                    ┌─────────────────────────┴─────────────────────────┐
                    │                                                   │
                    ▼                                                   ▼
      ┌───────────────────────────┐                       ┌───────────────────────────┐
      │   Estación de Aplicación  │                       │   Servidor Ubuntu 24.04   │
      │       192.168.1.25        │                       │       192.168.1.10        │
      ├───────────────────────────┤                       ├───────────────────────────┤
      │ • Cliente psql / App      │                       │ • UFW Firewall (TCP 5432) │
      │ • Usuario: app_user       │═══ TLS 1.3 / SCRAM ══▶│ • PostgreSQL 16           │
      │ • Rol: rol_escritura      │   (hostssl cifrado)   │ • BD: app_practica        │
      └───────────────────────────┘                       │ • pg_hba.conf restrictivo │
                                                          │ • Backups: pg_dump        │
                                                          └─────────────▲─────────────┘
                                                                        │
      ┌───────────────────────────┐                                     │
      │   Red Externa No Válida   │                                     │
      │        10.0.0.50          │═════════ RECHAZADO (REJECT) ════════╝
      └───────────────────────────┘
```

---

### 7. Pulido de Citas Bibliográficas y Normalización APA 7ma Edición
* **Diagnóstico actual:** En la página 12 del PDF, algunos hipervínculos contienen caracteres de sustitución causados por la codificación del archivo fuente (por ejemplo: `howto/security/` y `sistemasel-caso-de-linux`).
* **Recomendación:** Corregir dichos enlaces en el documento Word final para que sean accesibles y añadir el DOI o enlace limpio:
  * Canonical. (2026). *Security - Ubuntu Server documentation*. Canonical Ltd. Recuperado de: https://ubuntu.com/server/docs/how-to/security/
  * Instituto Nacional de Ciberseguridad [INCIBE]. (2023, 2 de marzo). *Bastionado de sistemas: el caso de Linux*. INCIBE-CERT. Recuperado de: https://www.incibe.es/incibe-cert/blog/bastionado-de-sistemas-el-caso-de-linux
  * PostgreSQL Global Development Group. (2026). *PostgreSQL 16.0 Documentation*. PGDG. Recuperado de: https://www.postgresql.org/docs/16/

---

## 📊 Matriz de Prioridad de Mejoras para la Defensa

| Propuesta de Mejora | Dificultad Técnica | Tiempo Estimado | Impacto en Calificación |
| :--- | :---: | :---: | :---: |
| **1. Capturas de pantalla reales de las 7 pruebas** | Baja | 15 min | ⭐⭐⭐⭐⭐ (Crítico) |
| **2. Reglas de cortafuegos UFW** | Media | 10 min | ⭐⭐⭐⭐⭐ (Excelente) |
| **3. Comprobación de restauración con `pg_restore`** | Baja | 10 min | ⭐⭐⭐⭐ (Muy alto) |
| **4. Diagrama visual de topología** | Baja | 15 min | ⭐⭐⭐⭐ (Muy alto) |
| **5. Automatización de copias con cron** | Media | 20 min | ⭐⭐⭐ (Recomendable) |
| **6. Parámetros de rotación de logs** | Baja | 5 min | ⭐⭐⭐ (Recomendable) |
| **7. Corrección de enlaces APA 7ma** | Muy baja | 5 min | ⭐⭐⭐ (Formalidad) |

---

## 🎯 Guía Rápida para la Exposición Oral ante el Docente

1. **Apertura (1 min):** Enfatizar la filosofía de la práctica: *"Nuestro objetivo no fue activar parámetros al azar, sino partir de una instalación vanilla y aplicar un bastionado sistemático y verificable bajo el modelo de capas de Canonical e INCIBE"*.
2. **Desarrollo de Medidas (3-4 min):** Explicar la lógica de cada control:
   * Por qué `peer` local y `hostssl` remoto con `reject` previene ataques de fuerza bruta externa.
   * Por qué `SCRAM-SHA-256` mitiga ataques de interceptación y supera a MD5.
   * Por qué separar `rol_lectura` y `rol_escritura` con `NOLOGIN` y revocar `CREATE` en `public` cumple con el principio de menor privilegio.
   * Cómo los permisos `0700` en `/var/lib/postgresql/16/main` y `0600` en `server.key` previenen fugas desde otros usuarios del sistema operativo.
3. **Demostración de Verificación (2 min):** Mostrar la tabla de la Sección 5 y ejecutar en vivo 2 o 3 comandos clave (ej. `\conninfo`, `\du` o el rechazo de conexión).
4. **Cierre (1 min):** Concluir que el hardening es un proceso iterativo de reducción de riesgos conjuntos y mencionar el cortafuegos UFW y la automatización de respaldos como las mejoras inmediatas a implementar.