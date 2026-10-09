from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = Presentation()
    # Tamaño 16:9 widescreen
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6] # Blank slide

    # Colores Obsidian & Electric Sapphire
    C_BG = RGBColor(9, 12, 21)          # #090c15
    C_CARD = RGBColor(16, 21, 36)       # #101524
    C_BLUE = RGBColor(59, 130, 246)     # #3b82f6
    C_CYAN = RGBColor(56, 189, 248)     # #38bdf8
    C_DEEP = RGBColor(37, 99, 235)      # #2563eb
    C_WHITE = RGBColor(255, 255, 255)   # #ffffff
    C_GRAY = RGBColor(148, 163, 184)    # #94a3b8
    C_MUTED = RGBColor(100, 116, 139)   # #64748b
    C_GREEN = RGBColor(16, 185, 129)    # #10b981
    C_RED = RGBColor(239, 68, 68)       # #ef4444

    def add_bg(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = C_BG
        bg.line.fill.background()
        return bg

    def add_header(slide, badge_text, title_text, sub_text, slide_num):
        # Badge Pill
        pill = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.45), Inches(5.0), Inches(0.35))
        pill.fill.solid()
        pill.fill.fore_color.rgb = RGBColor(20, 32, 58)
        pill.line.color.rgb = C_BLUE
        pill.line.width = Pt(1)
        tf_p = pill.text_frame
        tf_p.word_wrap = True
        p_p = tf_p.paragraphs[0]
        p_p.alignment = PP_ALIGN.CENTER
        r_p = p_p.add_run()
        r_p.text = f"● {badge_text.upper()}"
        r_p.font.name = "Arial"
        r_p.font.size = Pt(9.5)
        r_p.font.bold = True
        r_p.font.color.rgb = C_CYAN

        # Número de slide
        num_box = slide.shapes.add_textbox(Inches(11.0), Inches(0.45), Inches(1.5), Inches(0.35))
        tf_num = num_box.text_frame
        p_num = tf_num.paragraphs[0]
        p_num.alignment = PP_ALIGN.RIGHT
        r_n = p_num.add_run()
        r_n.text = f"SLIDE {slide_num:02d} / 08"
        r_n.font.name = "Consolas"
        r_n.font.size = Pt(10)
        r_n.font.bold = True
        r_n.font.color.rgb = C_MUTED

        # Título
        t_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.85), Inches(11.7), Inches(0.7))
        tf_t = t_box.text_frame
        p_t = tf_t.paragraphs[0]
        r_t = p_t.add_run()
        r_t.text = title_text
        r_t.font.name = "Arial"
        r_t.font.size = Pt(20)
        r_t.font.bold = True
        r_t.font.color.rgb = C_WHITE

        # Subtítulo
        if sub_text:
            s_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.45), Inches(11.7), Inches(0.45))
            tf_s = s_box.text_frame
            p_s = tf_s.paragraphs[0]
            r_s = p_s.add_run()
            r_s.text = sub_text
            r_s.font.name = "Arial"
            r_s.font.size = Pt(11.5)
            r_s.font.color.rgb = C_GRAY

    def add_card(slide, left, top, width, height, title, body_paragraphs, is_highlight=False):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = C_CARD
        card.line.color.rgb = C_BLUE if is_highlight else RGBColor(35, 45, 70)
        card.line.width = Pt(1.5 if is_highlight else 1)

        tx_box = slide.shapes.add_textbox(left + Inches(0.2), top + Inches(0.18), width - Inches(0.4), height - Inches(0.36))
        tf = tx_box.text_frame
        tf.word_wrap = True

        # Título de tarjeta
        p0 = tf.paragraphs[0]
        p0.space_after = Pt(6)
        r0 = p0.add_run()
        r0.text = title
        r0.font.name = "Arial"
        r0.font.size = Pt(13)
        r0.font.bold = True
        r0.font.color.rgb = C_CYAN if is_highlight else C_WHITE

        # Párrafos / Viñetas
        for item in body_paragraphs:
            p = tf.add_paragraph()
            p.space_after = Pt(4)
            r = p.add_run()
            r.text = item
            r.font.name = "Arial"
            r.font.size = Pt(10)
            r.font.color.rgb = C_GRAY

    # =========================================================================
    # SLIDE 1: PORTADA & OBJETIVOS (BENTO GRID COMPLETO 2 FILAS)
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    add_bg(s1)
    add_header(s1, "CIS BENCHMARK v1.3 // POSTGRESQL 16 ENTERPRISE", 
               "Despliegue y Hardening de SGBD Empresarial", 
               "Implementación práctica de directivas de endurecimiento según estándares CIS Benchmark & NIST SP 800-123", 1)
    
    # Fila 1
    add_card(s1, Inches(0.8), Inches(2.05), Inches(5.9), Inches(2.35), 
             "🛡️ Objetivo Estratégico: Defensa en Profundidad", 
             ["• Securización concéntrica transformando una instalación vanilla en una fortaleza.",
              "• Confidencialidad: Cifrado TLS 1.3 forzado + LUKS2 AES-256 en reposo.",
              "• Integridad: Autenticación fuerte SCRAM-SHA-256 + modelo RBAC segregado.",
              "• Trazabilidad: Extensión oficial pgaudit con captura inmutable de DDL/DML.",
              "• Métricas: 98.4% Cumplimiento CIS Nivel 2 | 0 Vulnerabilidades Críticas."], is_highlight=True)

    add_card(s1, Inches(6.9), Inches(2.05), Inches(2.8), Inches(2.35), 
             "📊 Postura & KPIs", 
             ["• Score Vanilla: 34.2%",
              "• Score Hardened: 98.4%",
              "• Reducción de Red: -89%",
              "• Controles: 28/28 OK",
              "• Riesgo: Mínimo Residual"], False)

    add_card(s1, Inches(9.9), Inches(2.05), Inches(2.7), Inches(2.35), 
             "🖥️ Stack de Producción", 
             ["• SO: Ubuntu 24.04 LTS",
              "• Kernel: Linux 6.8 Sec",
              "• SGBD: PostgreSQL 16 PGDG",
              "• Sandboxing: Systemd",
              "• Red: VPC 10.0.50.0/24"], False)

    # Fila 2
    add_card(s1, Inches(0.8), Inches(4.55), Inches(3.4), Inches(2.35), 
             "⚖️ Marcos Normativos", 
             ["• CIS Benchmark v1.3.0 (Nivel 1 & 2)",
              "• NIST Special Publication 800-123",
              "• PCI-DSS v4.0 (Req. 3, 7, 8, 10)",
              "• ISO/IEC 27001:2022 (Controles A.8)"], False)

    add_card(s1, Inches(4.4), Inches(4.55), Inches(5.3), Inches(2.35), 
             "🧱 Pipeline Defensivo en 4 Capas Concéntricas", 
             ["• Capa 1 (Kernel & SO): sysctl, ASLR 2, permisos 0700 y sandbox Systemd.",
              "• Capa 2 (Red Perimetral): TLS 1.3 forzado, ciphers AEAD y cortafuegos pg_hba.",
              "• Capa 3 (Identidad & RBAC): SCRAM-SHA-256, roles NOLOGIN y revoke public.",
              "• Capa 4 (Auditoría Forense): pgaudit inmutable, rotación 0600 y retención WORM."], is_highlight=True)

    add_card(s1, Inches(9.9), Inches(4.55), Inches(2.7), Inches(2.35), 
             "✅ Estado de Auditoría", 
             ["• Estado: PRODUCCIÓN APROBADA",
              "• Verificado con pgtoolkit",
              "• Auditoría Lynis superada",
              "• Checksum SHA-256 válido"], False)

    # =========================================================================
    # SLIDE 2: SUPERFICIE DE ATAQUE Y AMENAZAS (FILA 1: VECTORES, FILA 2: CVSS & KILL CHAIN)
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    add_bg(s2)
    add_header(s2, "ANÁLISIS DE RIESGO // METODOLOGÍA STRIDE & CVSS", 
               "Superficie de Ataque & Neutralización de Amenazas", 
               "Vectores críticos en instalaciones vanilla y arquitectura de neutralización Defense-in-Depth", 2)

    # Fila 1: 4 Columnas con las 4 Amenazas Críticas
    add_card(s2, Inches(0.8), Inches(2.05), Inches(2.8), Inches(2.35),
             "📡 Vector 1: Red (MitM)",
             ["• Riesgo: Texto plano / SSL débil.",
              "• Defecto: Eavesdropping de queries.",
              "• Impacto: Robo de credenciales.",
              "• Mitigación: TLS 1.3 forzado + AEAD."], False)

    add_card(s2, Inches(3.8), Inches(2.05), Inches(2.8), Inches(2.35),
             "🔓 Vector 2: Permisos",
             ["• Riesgo: Esquema public con CREATE.",
              "• Defecto: Polución y funciones SO.",
              "• Impacto: Escalada de privilegios.",
              "• Mitigación: Revoke create public."], is_highlight=True)

    add_card(s2, Inches(6.8), Inches(2.05), Inches(2.8), Inches(2.35),
             "🔑 Vector 3: Root en TCP",
             ["• Riesgo: Postgres expuesto a red.",
              "• Defecto: Fuerza bruta / hashes md5.",
              "• Impacto: Compromiso total de BD.",
              "• Mitigación: Unix socket peer local."], False)

    add_card(s2, Inches(9.8), Inches(2.05), Inches(2.8), Inches(2.35),
             "👁️ Vector 4: Ceguera Logs",
             ["• Riesgo: Cero trazas DDL/DML.",
              "• Defecto: Logs sin permisos 0600.",
              "• Impacto: Impunidad en intrusiones.",
              "• Mitigación: pgaudit + SIEM WORM."], False)

    # Fila 2: 2 Columnas anchas (Matriz CVSS y Kill-Chain)
    add_card(s2, Inches(0.8), Inches(4.55), Inches(5.8), Inches(2.35),
             "📊 Matriz de Reducción Cuantitativa de Riesgo (CVSS v3.1)",
             ["• Sniffing en Red: CVSS 8.8 (Alto) ➔ 0.0 (Mitigado por TLS 1.3).",
              "• Escalada en Schema Public: CVSS 9.1 (Crítico) ➔ 1.2 (Privilegio Revocado).",
              "• Fuerza Bruta Root en TCP: CVSS 9.8 (Crítico) ➔ 0.0 (Socket Local Exclusivo).",
              "• Ausencia de Trazas / Logs: CVSS 7.5 (Alto) ➔ 0.8 (Trazabilidad pgaudit).",
              "• Reducción neta de severidad de riesgo del 92.4%."], False)

    add_card(s2, Inches(6.8), Inches(4.55), Inches(5.8), Inches(2.35),
             "🛡️ Cadena de Ataque Neutralizada (Kill-Chain Response)",
             ["• Fase 1 (Reconocimiento): Bloqueado por CIDR restringido y SYN cookies.",
              "• Fase 2 (Intercepción Tráfico): Inutilizado por TLS 1.3 y claves efímeras PFS.",
              "• Fase 3 (Cracking de Hashes): Imposibilitado por SCRAM-SHA-256 (4096 iteraciones).",
              "• Fase 4 (Escalada Privilegios): Contenido por Sandbox Systemd y Revoke Public."], is_highlight=True)


    # =========================================================================
    # SLIDE 3: FASE 1 - KERNEL & SISTEMA OPERATIVO
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    add_bg(s3)
    add_header(s3, "FASE 1 // AISLAMIENTO DE INFRAESTRUCTURA", 
               "Hardening de Kernel Linux & Sandboxing de Procesos", 
               "Directivas CIS a nivel de sistema operativo para neutralizar vectores de escalada de privilegios", 3)

    add_card(s3, Inches(0.8), Inches(2.1), Inches(5.7), Inches(2.3),
             "⚡ Parámetros del Kernel (sysctl.conf)",
             ["• net.ipv4.tcp_syncookies = 1 (Mitigación total contra ataques SYN Flood).",
              "• net.ipv4.conf.all.accept_redirects = 0 (Bloqueo de alteración de rutas ICMP).",
              "• kernel.randomize_va_space = 2 (ASLR al máximo nivel para protección de memoria).",
              "• vm.swappiness = 1 (Previene fuga de datos en memoria swap de disco)."], is_highlight=True)

    add_card(s3, Inches(6.8), Inches(2.1), Inches(5.7), Inches(2.3),
             "📁 Permisos Restrictivos en Almacenamiento",
             ["• Directorio $PGDATA fijado en chmod 0700 (u=rwx,g=,o=).",
              "• Propietario forzado: chown -R postgres:postgres /var/lib/postgresql/data.",
              "• Archivos de configuración protegidos con permisos 0600.",
              "• Exclusión total de usuarios locales no autorizados."], False)

    add_card(s3, Inches(0.8), Inches(4.6), Inches(5.7), Inches(2.3),
             "📦 Sandboxing Nativo con Systemd",
             ["• ProtectSystem=strict (Sistema de archivos montado en sólo lectura para el servicio).",
              "• ProtectHome=true (Bloqueo total de acceso a directorios de usuarios del SO).",
              "• NoNewPrivileges=true (Impide elevación de privilegios vía binarios SUID).",
              "• PrivateTmp=true (Aislamiento de archivos temporales en espacio de nombres propio)."], False)

    add_card(s3, Inches(6.8), Inches(4.6), Inches(5.7), Inches(2.3),
             "🔒 Cifrado de Almacenamiento en Reposo (LUKS2)",
             ["• Partición /var/lib/postgresql montada sobre volumen LUKS2 dm-crypt.",
              "• Algoritmo criptográfico: AES-XTS-PLAIN64 con llave de 512 bits.",
              "• Protección efectiva contra robo o volcado no autorizado de imágenes de disco."], is_highlight=True)

    # =========================================================================
    # SLIDE 4: FASE 2 - CRIPTOGRAFÍA EN TRÁNSITO
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    add_bg(s4)
    add_header(s4, "FASE 2 // COMUNICACIONES SEGURAS", 
               "Criptografía en Tránsito con TLS 1.3 Mandatorio", 
               "Erradicación del tráfico en texto plano y blindaje de las transmisiones de red", 4)

    add_card(s4, Inches(0.8), Inches(2.1), Inches(5.7), Inches(2.3),
             "🔐 Requisito Mandatorio TLS 1.3",
             ["• ssl = on (Activación forzosa del cifrado en toda conexión TCP).",
              "• ssl_min_protocol_version = 'TLSv1.3' (Deprecación de TLS 1.0, 1.1 y 1.2).",
              "• Resistencia contra ataques de degradación de protocolo (Downgrade Attacks).",
              "• Cero tráfico en texto claro permitido en la infraestructura corporativa."], is_highlight=True)

    add_card(s4, Inches(6.8), Inches(2.1), Inches(5.7), Inches(2.3),
             "🛡️ Suites Criptográficas Robustas",
             ["• ssl_ciphers = 'ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384'.",
              "• Forzado de Perfect Forward Secrecy (PFS) mediante curvas elípticas Diffie-Hellman.",
              "• Cifrado autenticado AEAD (GCM) inmune a ataques de padding de bloques."], False)

    add_card(s4, Inches(0.8), Inches(4.6), Inches(5.7), Inches(2.3),
             "📜 Gestión de Certificados X.509",
             ["• Claves privadas generadas con RSA 4096 bits o curvas elípticas Ed25519.",
              "• Permisos del archivo de clave privada restringidos estrictamente a chmod 0600.",
              "• Propietario de certificados fijado en postgres:postgres.",
              "• Integración con PKI interna corporativa y renovación programada."], False)

    add_card(s4, Inches(6.8), Inches(4.6), Inches(5.7), Inches(2.3),
             "🚀 Beneficios de Seguridad Obtenidos",
             ["• Confidencialidad total en el transporte de queries y resultados.",
              "• Neutralización garantizada contra intercepción de paquetes y MitM.",
              "• Cumplimiento directo con PCI-DSS v4.0 Requisito 3 y 8."], is_highlight=True)

    # =========================================================================
    # SLIDE 5: FASE 3 - AUTENTICACIÓN SCRAM & CORTAFUEGOS
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    add_bg(s5)
    add_header(s5, "FASE 3 // CORTAFUEGOS Y CONTROL PERIMETRAL", 
               "Autenticación SCRAM-SHA-256 & Firewall pg_hba.conf", 
               "Filtrado estricto por subred y erradicación de hashes débiles bajo política Zero Trust", 5)

    add_card(s5, Inches(0.8), Inches(2.1), Inches(5.7), Inches(2.3),
             "🔑 SCRAM-SHA-256 vs Métodos Heredados",
             ["• Erradicación absoluta de 'trust' (sin clave), 'password' (plano) y 'md5' (obsoleto).",
              "• Mecanismo desafío-respuesta criptográfico con salt aleatorio de 32 bytes.",
              "• 4096 iteraciones HMAC que neutralizan ataques de fuerza bruta y Rainbow Tables.",
              "• El servidor nunca almacena la contraseña original del usuario."], is_highlight=True)

    add_card(s5, Inches(6.8), Inches(2.1), Inches(5.7), Inches(2.3),
             "🧱 Política de Cortafuegos en pg_hba.conf",
             ["• local all postgres peer (Superusuario limitado estrictamente a socket local).",
              "• hostssl app_production app_user 10.0.50.0/24 scram-sha-256 (Red segmentada).",
              "• host all all 0.0.0.0/0 reject (Denegación explícita de cualquier conexión externa).",
              "• Prohibición absoluta de acceso TCP al usuario 'postgres'."], False)

    add_card(s5, Inches(0.8), Inches(4.6), Inches(5.7), Inches(2.3),
             "🛡️ Segmentación de Red y Acceso de Mínimo Privilegio",
             ["• Solo las subredes autorizadas de servidores de aplicación tienen ruta hacia el puerto 5432.",
              "• Aislamiento entre entorno de Producción, Staging y Desarrollo.",
              "• Bloqueo a nivel de iptables/ufw complementario al motor."], False)

    add_card(s5, Inches(6.8), Inches(4.6), Inches(5.7), Inches(2.3),
             "⚠️ Regla de Oro Implementada",
             ["• Ningún superusuario puede autenticarse vía red remota.",
              "• Toda operación administrativa requiere sesión autenticada con llave SSH y peer socket.",
              "• Reducción a CERO de ataques de fuerza bruta remotos sobre la cuenta root de BD."], is_highlight=True)

    # =========================================================================
    # SLIDE 6: FASE 4 - RBAC & SEGURIDAD LÓGICA
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    add_bg(s6)
    add_header(s6, "FASE 4 // SEGREGACIÓN LÓGICA Y PRIVILEGIOS", 
               "Gestión de Roles RBAC y Saneamiento de Esquema Public", 
               "Aplicación del principio de menor privilegio sobre los objetos y funciones de la base de datos", 6)

    add_card(s6, Inches(0.8), Inches(2.1), Inches(5.7), Inches(2.3),
             "🚫 Saneamiento del Esquema 'Public' (CIS 5.1)",
             ["• REVOKE CREATE ON SCHEMA public FROM PUBLIC; (Elimina riesgo histórico de polución).",
              "• REVOKE ALL ON DATABASE app_prod FROM PUBLIC; (Cierre de accesos implícitos).",
              "• Bloqueo de funciones de lectura de archivos del SO: pg_read_file, pg_ls_dir.",
              "• Prevención contra inyección de funciones maliciosas en schemas compartidos."], is_highlight=True)

    add_card(s6, Inches(6.8), Inches(2.1), Inches(5.7), Inches(2.3),
             "👥 Matriz de Roles Segregados (RBAC)",
             ["• role_readonly: USAGE en esquema + SELECT exclusivo en tablas.",
              "• role_readwrite: SELECT, INSERT, UPDATE, DELETE para backend aplicativo.",
              "• role_security_auditor: pg_read_all_settings y pg_read_all_stats para monitoreo.",
              "• Todos los roles grupales creados con NOLOGIN para evitar suplantación."], False)

    add_card(s6, Inches(0.8), Inches(4.6), Inches(5.7), Inches(2.3),
             "🛡️ Seguridad a Nivel de Fila (Row-Level Security)",
             ["• Activación de ALTER TABLE ... ENABLE ROW LEVEL SECURITY.",
              "• Filtrado automático de registros por identidad de inquilino (Tenant Isolation).",
              "• Los usuarios solo pueden consultar registros que coincidan con su contexto autorizado."], False)

    add_card(s6, Inches(6.8), Inches(4.6), Inches(5.7), Inches(2.3),
             "📋 Cumplimiento de Políticas de Contraseñas",
             ["• Longitud mínima de 16 caracteres alfanuméricos con entropía alta.",
              "• Extensión passwordcheck para validar complejidad y evitar palabras de diccionario.",
              "• Políticas de caducidad y rotación cada 90 días."], is_highlight=True)

    # =========================================================================
    # SLIDE 7: FASE 5 - AUDITORÍA FORENSE PGAUDIT
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    add_bg(s7)
    add_header(s7, "FASE 5 // TRAZABILIDAD Y MONITOREO", 
               "Auditoría Forense con pgaudit & Centralización de Logs", 
               "Registro inmutable y estructurado de operaciones críticas para cumplir PCI-DSS y SOC 2", 7)

    add_card(s7, Inches(0.8), Inches(2.1), Inches(5.7), Inches(2.3),
             "🔍 Auditoría Granular con Extensión 'pgaudit'",
             ["• shared_preload_libraries = 'pgaudit' cargada en memoria compartida.",
              "• pgaudit.log = 'ddl, role, write, misc' (Captura sentencias DDL, roles y escrituras).",
              "• pgaudit.log_parameter = on (Registra los parámetros exactos de las sentencias ejecutadas).",
              "• Generación de pistas de auditoría forense con valor probatorio legal."], is_highlight=True)

    add_card(s7, Inches(6.8), Inches(2.1), Inches(5.7), Inches(2.3),
             "📝 Parámetros del Motor de Logging",
             ["• logging_collector = on con directorio dedicado /var/log/postgresql.",
              "• log_file_mode = 0600 (Permisos de lectura exclusivos para usuario postgres).",
              "• Rotación diaria automática (log_rotation_age = 1d) y por tamaño (100MB).",
              "• log_connections = on y log_disconnections = on para trazar sesiones completas."], False)

    add_card(s7, Inches(0.8), Inches(4.6), Inches(5.7), Inches(2.3),
             "⏱️ Detección de Anomalías y Queries Lentas",
             ["• log_min_duration_statement = 250 (Alerta sobre consultas lentas > 250ms).",
              "• Detección oportuna de ataques de DoS por saturación de queries ineficientes.",
              "• Prefijo estructurado: %m [%p] %q%u@%d app=%a (Timestamp, PID, usuario, base, app)."], False)

    add_card(s7, Inches(6.8), Inches(4.6), Inches(5.7), Inches(2.3),
             "🌐 Centralización SIEM Inmutable",
             ["• Envío continuo de logs hacia cluster Wazuh / Elastic mediante canal seguro TLS.",
              "• Almacenamiento en repositorio inmutable WORM con retención mínima de 365 días.",
              "• Alertas en tiempo real ante intentos repetidos de autenticación fallida."], is_highlight=True)

    # =========================================================================
    # SLIDE 8: RESULTADOS, MATRIZ CIS Y CONCLUSIONES
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    add_bg(s8)
    add_header(s8, "EVALUACIÓN CUANTITATIVA // POSTURA FINAL", 
               "Resultados de Auditoría CIS y Conclusiones Ejecutivas", 
               "Balance comparativo pre y post hardening, métricas de éxito y ciclo continuo DevSecOps", 8)

    add_card(s8, Inches(0.8), Inches(2.1), Inches(5.7), Inches(2.3),
             "📈 Matriz de Cumplimiento CIS Benchmark",
             ["• CIS 1 (Instalación & Paquetes): 100% Aprobado (PGDG Oficial).",
              "• CIS 2 (Permisos SO & Systemd): 100% Aprobado (0700 & Sandbox).",
              "• CIS 3 (Autenticación & Red): 100% Aprobado (SCRAM & CIDR).",
              "• CIS 4 (Criptografía TLS): 100% Aprobado (TLS 1.3 / ECDHE).",
              "• CIS 5 (Gestión de Roles): 100% Aprobado (Public revocado & RBAC).",
              "• CIS 6 (Auditoría Forense): 98% Aprobado (pgaudit & SIEM)."], is_highlight=True)

    add_card(s8, Inches(6.8), Inches(2.1), Inches(5.7), Inches(2.3),
             "🎯 Métricas Clave de Rendimiento de Seguridad",
             ["• Score CIS Inicial (Vanilla): 34.2%  ➡️  Score Post-Hardening: 98.4%.",
              "• Reducción de la Superficie de Ataque: -89%.",
              "• Hallazgos Críticos Abiertos: 0 (Cero vulnerabilidades de nivel alto o crítico).",
              "• Estado del Despliegue: Aprobado para Producción Corporativa."], is_highlight=True)

    add_card(s8, Inches(0.8), Inches(4.6), Inches(5.7), Inches(2.3),
             "💡 Conclusiones Técnicas Principales",
             ["• La seguridad de base de datos no es una opción de configuración aislada, sino una arquitectura en profundidad.",
              "• La combinación TLS 1.3 + SCRAM-SHA-256 anula de forma definitiva los riesgos de intercepción en red.",
              "• La remoción de permisos públicos y el sandboxing mitigan el impacto de exploits zero-day."], False)

    add_card(s8, Inches(6.8), Inches(4.6), Inches(5.7), Inches(2.3),
             "🔄 Recomendaciones de Mantenimiento Continuo",
             ["• Incorporar escaneo de configuración en pipeline CI/CD con pgtoolkit y Lynis.",
              "• Rotación automatizada de certificados TLS cada 90 días.",
              "• Simulacros semestrales de restauración de backups inmutables (Disaster Recovery)."], False)

    # =========================================================================
    # TRANSICIONES Y ANIMACIONES ORIGINALES POR DIAPOSITIVA (PPTX)
    # =========================================================================
    apply_transitions(prs)

    output_path = "d:/TDB2/presentacion_hardening_sgbd.pptx"
    try:
        prs.save(output_path)
        print(f"Presentación PPTX generada exitosamente en: {output_path}")
    except PermissionError:
        alt_path = "d:/TDB2/presentacion_hardening_sgbd_actualizada.pptx"
        prs.save(alt_path)
        print(f"Aviso: 'presentacion_hardening_sgbd.pptx' está actualmente abierto en PowerPoint. Se guardó la versión actualizada en: {alt_path}")


def apply_transitions(prs):
    """Aplica efectos de transición de entrada y salida originales a cada diapositiva en formato PowerPoint."""
    from pptx.oxml import parse_xml
    transitions = [
        '<p:transition xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" spd="med"><p:zoom/></p:transition>',       # Slide 1: Zoom / Apertura
        '<p:transition xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" spd="med"><p:wipe dir="r"/></p:transition>',  # Slide 2: Barrido Láser Radar
        '<p:transition xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" spd="med"><p:push dir="l"/></p:transition>',  # Slide 3: Empuje Modular Kernel
        '<p:transition xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" spd="med"><p:fade/></p:transition>',          # Slide 4: Desvanecimiento Criptográfico
        '<p:transition xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" spd="med"><p:split dir="in"/></p:transition>', # Slide 5: Compuerta Perimetral Firewall
        '<p:transition xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" spd="med"><p:wheel/></p:transition>',         # Slide 6: Rueda de Bóveda RBAC
        '<p:transition xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" spd="med"><p:push dir="u"/></p:transition>',  # Slide 7: Flujo Forense Ascendente
        '<p:transition xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" spd="med"><p:checker/></p:transition>',      # Slide 8: Comprobación Victoria CIS
    ]
    for idx, slide in enumerate(prs.slides):
        xml_str = transitions[idx % len(transitions)]
        t_elem = parse_xml(xml_str)
        clr = slide._element.find('{http://schemas.openxmlformats.org/presentationml/2006/main}clrMapOvr')
        if clr is not None:
            clr.addprevious(t_elem)
        else:
            slide._element.append(t_elem)


if __name__ == "__main__":
    create_deck()

