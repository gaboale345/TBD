from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml import parse_xml

def create_deck():
    prs = Presentation()
    # Formato panorámico widescreen 16:9
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6] # Diapositiva en blanco

    # Paleta de Colores Editorial Tecnológico "Obsidian & Electric Sapphire"
    C_BG = RGBColor(9, 12, 21)          # #090c15 Obsidiana base profunda
    C_CARD = RGBColor(16, 21, 36)       # #101524 Superficie elevada contenedor
    C_CARD_HI = RGBColor(20, 28, 48)    # #141c30 Contenedor destacado
    C_TERMINAL = RGBColor(11, 22, 44)   # #0b162c Fondo azul medianoche zafiro con alto contraste
    C_BORDER = RGBColor(35, 45, 70)     # #232d46 Borde sutil
    C_BORDER_CODE = RGBColor(56, 189, 248) # #38bdf8 Borde cían eléctrico resplandeciente
    C_PILL_CODE = RGBColor(20, 42, 80)  # #142a50 Fondo de la etiqueta superior del comando
    C_PROMPT = RGBColor(52, 211, 153)   # #34d399 Verde esmeralda para prompt $
    C_BLUE = RGBColor(59, 130, 246)     # #3b82f6 Azul primario
    C_CYAN = RGBColor(56, 189, 248)     # #38bdf8 Azul eléctrico / cían
    C_PURPLE = RGBColor(216, 180, 254)  # #d8b4fe Púrpura brillante para valores y parámetros
    C_WHITE = RGBColor(255, 255, 255)   # #ffffff Blanco puro
    C_GRAY = RGBColor(148, 163, 184)    # #94a3b8 Gris plateado de lectura
    C_MUTED = RGBColor(100, 116, 139)   # #64748b Gris apagado metadatos
    C_GREEN = RGBColor(16, 185, 129)    # #10b981 Emerald de validación
    C_RED = RGBColor(239, 68, 68)       # #ef4444 Rose de riesgo
    C_AMBER = RGBColor(245, 158, 11)    # #f59e0b Ámbar de advertencia

    def add_bg(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = C_BG
        bg.line.fill.background()
        return bg

    def add_header(slide, badge_text, title_text, sub_text, slide_num):
        # Badge Pill en cabecera
        pill_w = max(Inches(3.8), Inches(len(badge_text) * 0.105))
        pill = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.38), pill_w, Inches(0.30))
        pill.fill.solid()
        pill.fill.fore_color.rgb = RGBColor(18, 28, 52)
        pill.line.color.rgb = C_BLUE
        pill.line.width = Pt(1)
        tf_p = pill.text_frame
        tf_p.word_wrap = True
        tf_p.margin_left = Inches(0.10)
        tf_p.margin_right = Inches(0.10)
        tf_p.margin_top = Inches(0.02)
        tf_p.margin_bottom = Inches(0.02)
        p_p = tf_p.paragraphs[0]
        p_p.alignment = PP_ALIGN.CENTER
        r_p = p_p.add_run()
        r_p.text = f"●  {badge_text.upper()}"
        r_p.font.name = "Arial"
        r_p.font.size = Pt(8.5)
        r_p.font.bold = True
        r_p.font.color.rgb = C_CYAN

        # Número de diapositiva (Total: 14)
        num_box = slide.shapes.add_textbox(Inches(10.5), Inches(0.38), Inches(2.0), Inches(0.30))
        tf_num = num_box.text_frame
        p_num = tf_num.paragraphs[0]
        p_num.alignment = PP_ALIGN.RIGHT
        r_n = p_num.add_run()
        r_n.text = f"SLIDE {slide_num:02d} / 14"
        r_n.font.name = "Consolas"
        r_n.font.size = Pt(9.5)
        r_n.font.bold = True
        r_n.font.color.rgb = C_MUTED

        # Título principal de la diapositiva
        t_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.74), Inches(11.7), Inches(0.48))
        tf_t = t_box.text_frame
        tf_t.word_wrap = True
        tf_t.margin_left = 0
        tf_t.margin_top = 0
        p_t = tf_t.paragraphs[0]
        r_t = p_t.add_run()
        r_t.text = title_text
        r_t.font.name = "Arial"
        r_t.font.size = Pt(20)
        r_t.font.bold = True
        r_t.font.color.rgb = C_WHITE

        # Subtítulo explicativo
        if sub_text:
            s_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.24), Inches(11.7), Inches(0.32))
            tf_s = s_box.text_frame
            tf_s.word_wrap = True
            tf_s.margin_left = 0
            tf_s.margin_top = 0
            p_s = tf_s.paragraphs[0]
            r_s = p_s.add_run()
            r_s.text = sub_text
            r_s.font.name = "Arial"
            r_s.font.size = Pt(10.5)
            r_s.font.color.rgb = C_GRAY

    def add_card(slide, left, top, width, height, title, items, is_highlight=False, code_box=None, footer_tag=None):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = C_CARD_HI if is_highlight else C_CARD
        card.line.color.rgb = C_BLUE if is_highlight else C_BORDER
        card.line.width = Pt(1.5 if is_highlight else 1)

        has_subbox = code_box is not None
        has_footer = footer_tag is not None
        
        reserve_bottom = Inches(0.35)
        if has_subbox:
            reserve_bottom += Inches(1.35)
        if has_footer and not has_subbox:
            reserve_bottom += Inches(0.40)

        tx_height = height - reserve_bottom - Inches(0.20)
        tx_box = slide.shapes.add_textbox(left + Inches(0.22), top + Inches(0.18), width - Inches(0.44), tx_height)
        tf = tx_box.text_frame
        tf.word_wrap = True
        tf.margin_left = 0
        tf.margin_right = 0
        tf.margin_top = 0
        tf.margin_bottom = 0

        # Título de la tarjeta
        p0 = tf.paragraphs[0]
        p0.space_after = Pt(8)
        r0 = p0.add_run()
        r0.text = title
        r0.font.name = "Arial"
        r0.font.size = Pt(12)
        r0.font.bold = True
        r0.font.color.rgb = C_CYAN if is_highlight else C_WHITE

        # Párrafos estructurados
        for item in items:
            p = tf.add_paragraph()
            p.space_after = Pt(5)
            p.line_spacing = 1.15

            if item.startswith("• "):
                raw_body = item[2:]
                parts = raw_body.split(":", 1)
                
                # Viñeta
                r_dot = p.add_run()
                r_dot.text = "•  "
                r_dot.font.name = "Arial"
                r_dot.font.size = Pt(9)
                r_dot.font.bold = True
                r_dot.font.color.rgb = C_CYAN if is_highlight else C_BLUE

                if len(parts) == 2:
                    r_lbl = p.add_run()
                    r_lbl.text = parts[0] + ":"
                    r_lbl.font.name = "Arial"
                    r_lbl.font.size = Pt(9)
                    r_lbl.font.bold = True
                    r_lbl.font.color.rgb = C_WHITE

                    r_desc = p.add_run()
                    r_desc.text = " " + parts[1].strip()
                    r_desc.font.name = "Arial"
                    r_desc.font.size = Pt(8.5)
                    r_desc.font.color.rgb = C_GRAY
                else:
                    r_desc = p.add_run()
                    r_desc.text = raw_body
                    r_desc.font.name = "Arial"
                    r_desc.font.size = Pt(8.5)
                    r_desc.font.color.rgb = C_GRAY
            else:
                r_txt = p.add_run()
                r_txt.text = item
                r_txt.font.name = "Arial"
                r_txt.font.size = Pt(8.5)
                r_txt.font.color.rgb = C_GRAY

        # SUB-PANEL DE CÓDIGO / CONFIGURACIÓN / COMANDO (Con fondo diferente y resalte visual)
        if code_box:
            sub_h = Inches(1.24)
            sub_top = top + height - sub_h - Inches(0.16)
            sub_w = width - Inches(0.44)
            sub_l = left + Inches(0.22)

            sub_bg = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, sub_l, sub_top, sub_w, sub_h)
            sub_bg.fill.solid()
            sub_bg.fill.fore_color.rgb = C_TERMINAL
            sub_bg.line.color.rgb = C_BORDER_CODE
            sub_bg.line.width = Pt(1.5)

            # Insignia de encabezado de terminal
            label_text = code_box.get('label', 'DIRECTIVA / COMANDO').upper()
            pill_w = min(Inches(3.4), max(Inches(1.8), Inches(len(label_text) * 0.08 + 0.35)))
            pill_h = Inches(0.20)
            tag_pill = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, sub_l + Inches(0.10), sub_top + Inches(0.08), pill_w, pill_h)
            tag_pill.fill.solid()
            tag_pill.fill.fore_color.rgb = C_PILL_CODE
            tag_pill.line.color.rgb = C_BORDER_CODE
            tag_pill.line.width = Pt(0.75)
            tf_tp = tag_pill.text_frame
            tf_tp.margin_left = Inches(0.05)
            tf_tp.margin_right = Inches(0.05)
            tf_tp.margin_top = 0
            tf_tp.margin_bottom = 0
            p_tp = tf_tp.paragraphs[0]
            p_tp.alignment = PP_ALIGN.CENTER
            r_tp = p_tp.add_run()
            r_tp.text = f"⚡ {label_text}"
            r_tp.font.name = "Consolas"
            r_tp.font.size = Pt(7)
            r_tp.font.bold = True
            r_tp.font.color.rgb = C_CYAN

            # Cuadro de texto para líneas de código
            tb_code = slide.shapes.add_textbox(sub_l + Inches(0.12), sub_top + Inches(0.30), sub_w - Inches(0.24), sub_h - Inches(0.34))
            tf_c = tb_code.text_frame
            tf_c.word_wrap = True
            tf_c.margin_left = 0
            tf_c.margin_top = 0
            tf_c.margin_bottom = 0
            tf_c.margin_right = 0

            lines = code_box.get('lines', [])
            for idx, line in enumerate(lines):
                p_l = tf_c.paragraphs[0] if idx == 0 else tf_c.add_paragraph()
                p_l.space_after = Pt(2)
                
                if line.startswith("$") or line.startswith(">"):
                    r_prm = p_l.add_run()
                    r_prm.text = "$ "
                    r_prm.font.name = "Consolas"
                    r_prm.font.size = Pt(8.5)
                    r_prm.font.bold = True
                    r_prm.font.color.rgb = C_PROMPT
                    
                    r_cmd = p_l.add_run()
                    r_cmd.text = line[2:] if line.startswith("$ ") else line[1:]
                    r_cmd.font.name = "Consolas"
                    r_cmd.font.size = Pt(8.5)
                    r_cmd.font.bold = True
                    r_cmd.font.color.rgb = C_WHITE
                elif line.startswith("#") or line.startswith("--"):
                    r_l = p_l.add_run()
                    r_l.text = line
                    r_l.font.name = "Consolas"
                    r_l.font.size = Pt(8)
                    r_l.font.italic = True
                    r_l.font.color.rgb = C_MUTED
                elif "=" in line:
                    parts = line.split("=", 1)
                    r_k = p_l.add_run()
                    r_k.text = parts[0] + "="
                    r_k.font.name = "Consolas"
                    r_k.font.size = Pt(8.5)
                    r_k.font.bold = True
                    r_k.font.color.rgb = C_CYAN
                    
                    r_v = p_l.add_run()
                    r_v.text = parts[1]
                    r_v.font.name = "Consolas"
                    r_v.font.size = Pt(8.5)
                    r_v.font.color.rgb = C_PURPLE
                else:
                    r_l = p_l.add_run()
                    r_l.text = line
                    r_l.font.name = "Consolas"
                    r_l.font.size = Pt(8.5)
                    r_l.font.color.rgb = C_CYAN

        # FOOTER BADGE / STATUS (Ancla inferior)
        if footer_tag:
            tag_top = top + height - Inches(0.36)
            tag_box = slide.shapes.add_textbox(left + Inches(0.22), tag_top, width - Inches(0.44), Inches(0.28))
            tf_tag = tag_box.text_frame
            tf_tag.margin_left = 0
            tf_tag.margin_top = 0
            p_tag = tf_tag.paragraphs[0]
            r_tag = p_tag.add_run()
            r_tag.text = footer_tag.get('text', '')
            r_tag.font.name = "Arial"
            r_tag.font.size = Pt(8)
            r_tag.font.bold = True
            r_tag.font.color.rgb = footer_tag.get('color', C_GREEN)

    # Coordenadas estándar
    TOP_STD = Inches(1.72)
    HEIGHT_STD = Inches(5.35)

    # =========================================================================
    # SLIDE 01: PORTADA ACADÉMICA OFICIAL (UPDS)
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    add_bg(s1)
    add_header(s1, "UNIVERSIDAD PRIVADA DOMINGO SAVIO // FACULTAD DE INGENIERÍA",
               "Informe Práctico de Instalación y Hardening de un SGBD",
               "Actividad Académica II — Práctica de Laboratorio en PostgreSQL 16 sobre Ubuntu Server 24.04 LTS", 1)

    # Tarjeta Izquierda (Hero Académico)
    add_card(s1, Inches(0.8), TOP_STD, Inches(6.5), HEIGHT_STD,
             "🎓 Ficha Técnica de la Actividad Académica",
             ["• Institución: Universidad Privada Domingo Savio (UPDS) — Sede Santa Cruz de la Sierra.",
              "• Autores de la Práctica: Adriana Rodríguez Sotelo y Gabriel Kevin Alcon Maydana.",
              "• Carrera Profesional: Ingeniería en Sistemas.",
              "• Docente de la Materia: Ing. Pablo Moscoso Zeballos.",
              "• Autoridades Académicas: MSc. Wilmer Campos Saavedra (Decano) | MSc. José Antonio Landriel P. (Vicerrector).",
              "• Fecha de Publicación: 08 de octubre de 2026."],
             is_highlight=True,
             code_box={'label': 'METADATOS DEL PROYECTO ACADÉMICO',
                       'lines': ['Carrera: Ingeniería en Sistemas | Semestre II-2026',
                                 'Materia: Taller de Base de Datos II / Seguridad',
                                 'Sede: Santa Cruz de la Sierra — Bolivia']},
             footer_tag={'text': '● ACTIVIDAD ACADÉMICA II — DOCUMENTO TÉCNICO OFICIAL', 'color': C_GREEN})

    # Derecha Superior (Alcance Real)
    add_card(s1, Inches(7.55), TOP_STD, Inches(4.98), Inches(2.55),
             "🛡️ Propósito & Alcance Real de la Práctica",
             ["• Objetivo Central: Partir de una instalación básica ('vanilla') y aplicar medidas sencillas que reduzcan accesos innecesarios.",
              "• Enfoque de Laboratorio: Demostrar de forma comprensible cómo configuraciones básicas mejoran la seguridad.",
              "• Transparencia Metodológica: El trabajo no pretende certificar el servidor ni afirmar porcentajes de cumplimiento empresarial."],
             is_highlight=False,
             footer_tag={'text': '● ENFOQUE: LABORATORIO COMPRENSIBLE Y DEMOSTRABLE', 'color': C_CYAN})

    # Derecha Inferior (Stack Base)
    add_card(s1, Inches(7.55), TOP_STD + Inches(2.75), Inches(4.98), Inches(2.60),
             "🖥️ Entorno de Trabajo Desplegado",
             ["• SGBD Seleccionado: PostgreSQL 16 LTS (Gestión nativa de roles y conexiones).",
              "• Sistema Operativo Base: Ubuntu Server 24.04 LTS.",
              "• Tipo de Despliegue: Entorno académico controlado de laboratorio.",
              "• Referencias Guía: Documentación PostgreSQL, Ubuntu, INCIBE y CIS Benchmarks."],
             is_highlight=False,
             code_box={'label': 'ENTORNO DE RED DE LABORATORIO',
                       'lines': ['Red Autorizada: 192.168.1.0/24',
                                 'Base de Datos: app_practica | Usuario: app_user']})

    # =========================================================================
    # SLIDE 02: RESUMEN Y ENFOQUE METODOLÓGICO
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    add_bg(s2)
    add_header(s2, "SECCIÓN RESUMEN // ENFOQUE DE LA ACTIVIDAD",
               "Resumen Ejecutivo y Criterio de Selección de Medidas",
               "Filosofía de fortificación progresiva sin sobredimensionamiento ni afirmaciones no demostrables", 2)

    add_card(s2, Inches(0.8), TOP_STD, Inches(3.65), HEIGHT_STD,
             "📋 Justificación del Proyecto",
             ["• Almacenamiento Crítico: Un SGBD contiene información esencial para una organización; no basta con dejar la configuración por defecto.",
              "• Bastionado según INCIBE: Consiste en revisar opciones y reducir parámetros que generen riesgos innecesarios.",
              "• Selección de PostgreSQL: Permite administrar usuarios, roles, permisos, conexiones y registros de manera clara y estructurada."],
             is_highlight=False,
             code_box={'label': 'DEFINICIÓN DE BASTIONADO (INCIBE 2023)',
                       'lines': ['"El bastionado permite identificar configuraciones',
                                 ' seguras y aplicar medidas adicionales para',
                                 ' mejorar la protección de un sistema."']},
             footer_tag={'text': '● FUNDAMENTO: INCIBE & BUENAS PRÁCTICAS', 'color': C_GREEN})

    add_card(s2, Inches(4.83), TOP_STD, Inches(3.65), HEIGHT_STD,
             "🎯 6 Ejes de Endurecimiento",
             ["• Actualización: Mantener Ubuntu y PostgreSQL al día con parches vigentes.",
              "• Control de Conexiones: Filtrado estricto por red y usuario en pg_hba.conf.",
              "• Autenticación Segura: Algoritmo SCRAM-SHA-256 en contraseñas.",
              "• Mínimo Privilegio: Creación de roles de lectura/escritura y revoke public.",
              "• Comunicaciones TLS: Cifrado en tránsito con certificados X.509.",
              "• Registro y Respaldo: Logs de conexiones y backup lógico con pg_dump."],
             is_highlight=True,
             code_box={'label': 'PALABRAS CLAVE DEL INFORME',
                       'lines': ['PostgreSQL | Seguridad | Hardening',
                                 'Autenticación | Roles | Respaldo']},
             footer_tag={'text': '● COBERTURA EN 6 MEDIDAS BÁSICAS', 'color': C_CYAN})

    add_card(s2, Inches(8.86), TOP_STD, Inches(3.65), HEIGHT_STD,
             "⚖️ Delimitación del Alcance",
             ["• Eliminación de Afirmaciones Excesivas: Se descartaron porcentajes de cumplimiento o certificaciones comerciales sin evidencia de laboratorio.",
              "• Defensa en Exposición: Se priorizan configuraciones que puedan ser ejecutadas, verificadas y explicadas durante la defensa oral.",
              "• Criterio Académico: Demostrar de forma transparente el impacto positivo de pequeñas configuraciones de seguridad."],
             is_highlight=False,
             code_box={'label': 'CRITERIO DE DEFENSA ACADÉMICA',
                       'lines': ['"Es preferible utilizar configuraciones que puedan',
                                 ' ejecutarse y verificarse correctamente, en lugar',
                                 ' de controles avanzados que no hayan sido probados."']},
             footer_tag={'text': '● ALCANCE: 100% DEMOSTRABLE EN VIVO', 'color': C_GREEN})

    # =========================================================================
    # SLIDE 03: INTRODUCCIÓN AL HARDENING DE SGBD
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    add_bg(s3)
    add_header(s3, "SECCIÓN 1 // INTRODUCCIÓN Y FUNDAMENTOS",
               "Concepto de Hardening y Selección de la Tecnología",
               "Por qué una instalación por defecto es insuficiente y justificación de la plataforma elegida", 3)

    add_card(s3, Inches(0.8), TOP_STD, Inches(3.65), HEIGHT_STD,
             "🛡️ El Concepto de Hardening",
             ["• También llamado 'Bastionado' o 'Endurecimiento' de servidores.",
              "• Riesgo de la Instalación por Defecto: Prioriza compatibilidad inmediata sobre seguridad, habilitando opciones abiertas innecesarias.",
              "• Objetivo Principal: Cerrar vectores innecesarios, reducir la superficie de ataque y fortalecer la autenticación y permisos."],
             is_highlight=False,
             code_box={'label': 'PRINCIPIO DEFENSIVO BÁSICO',
                       'lines': ['# Un sistema no configurado expone:',
                                 '• Conexiones no cifradas en la red',
                                 '• Usuarios con privilegios excesivos',
                                 '• Falta de registros de auditoría']},
             footer_tag={'text': '● REFERENCIA: INCIBE (2023)', 'color': C_GREEN})

    add_card(s3, Inches(4.83), TOP_STD, Inches(3.65), HEIGHT_STD,
             "🐘 Elección de PostgreSQL 16",
             ["• Robustez y Madurez: Motor de base de datos relacional de código abierto ampliamente adoptado.",
              "• Gestión Granular: Administración clara de roles independientes del sistema operativo.",
              "• Control Fino de Red: Archivo pg_hba.conf para control de acceso basado en host.",
              "• Criptografía Integrada: Soporte nativo para SCRAM-SHA-256 y cifrado TLS/SSL."],
             is_highlight=True,
             code_box={'label': 'CARACTERÍSTICAS EVALUADAS EN PG 16',
                       'lines': ['password_encryption = scram-sha-256',
                                 'pg_hba.conf host-based authentication',
                                 'Roles NOLOGIN para mínimo privilegio',
                                 'ssl = on con cifrado X.509']},
             footer_tag={'text': '● MOTOR: POSTGRESQL 16 LTS', 'color': C_CYAN})

    add_card(s3, Inches(8.86), TOP_STD, Inches(3.65), HEIGHT_STD,
             "🐧 Selección de Ubuntu Server 24.04",
             ["• Plataforma LTS: Estabilidad y soporte a largo plazo para servidores.",
              "• Seguridad en Capas (Canonical 2026): Aislamiento de usuarios, firewall de red y ciclo de actualizaciones constante.",
              "• Integración con Systemd: Control de estado del servicio y gestión de procesos del motor."],
             is_highlight=False,
             code_box={'label': 'VERIFICACIÓN DE VERSIÓN Y ESTADO',
                       'lines': ['$ lsb_release -d',
                                 '  Description: Ubuntu 24.04 LTS',
                                 '$ sudo systemctl is-active postgresql',
                                 '  active']},
             footer_tag={'text': '● SISTEMA: UBUNTU SERVER 24.04', 'color': C_BLUE})

    # =========================================================================
    # SLIDE 04: OBJETIVO Y ENTORNO DE LA PRÁCTICA
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    add_bg(s4)
    add_header(s4, "SECCIÓN 2 // PARÁMETROS DEL LABORATORIO",
               "Objetivo y Entorno Controlado de la Práctica",
               "Parámetros del entorno de pruebas, guías de referencia y delimitación del alcance", 4)

    add_card(s4, Inches(0.8), TOP_STD, Inches(5.65), HEIGHT_STD,
             "📊 Cuadro Resumen del Entorno (Tabla del Informe)",
             ["• SGBD: PostgreSQL 16 instalado y configurado.",
              "• Sistema Operativo: Ubuntu Server 24.04 LTS (instalación limpia).",
              "• Tipo de Práctica: Entorno académico / laboratorio de sistemas.",
              "• Objetivo de Seguridad: Reducir accesos innecesarios y aplicar controles básicos.",
              "• Principales Medidas: Actualizaciones, autenticación, permisos, TLS, registros y respaldo."],
             is_highlight=True,
             code_box={'label': 'TABLA: ELEMENTOS Y DESCRIPCIÓN DEL LABORATORIO',
                       'lines': ['SGBD             | PostgreSQL 16',
                                 'Sistema Operativo| Ubuntu Server 24.04 LTS',
                                 'Tipo de Práctica | Entorno académico / laboratorio',
                                 'Objetivo         | Reducir accesos innecesarios',
                                 'Medidas Clave    | Actualización, Auth, Roles, TLS, Logs, Backup']},
             footer_tag={'text': '● TABLA OFICIAL: SECCIÓN 2 DEL INFORME', 'color': C_GREEN})

    add_card(s4, Inches(6.88), TOP_STD, Inches(5.65), HEIGHT_STD,
             "📚 Marcos de Referencia Metodológica",
             ["• Documentación Oficial de PostgreSQL: Capítulos 21 (Autenticación), 22 (Roles) y 19.9 (SSL).",
              "• Recomendaciones de Seguridad de Ubuntu: Documentación oficial de Canonical (2026).",
              "• Material Técnico de INCIBE (2023): Guías de bastionado de sistemas Linux.",
              "• CIS Benchmarks: Utilizados como guía de referencia de buenas prácticas.",
              "• Delimitación Explícita: Sirven de guía, pero no se declara certificación formal."],
             is_highlight=False,
             code_box={'label': 'DOCUMENTACIÓN CONSULTADA',
                       'lines': ['• PostgreSQL Client Authentication (cap. 21)',
                                 '• PostgreSQL Database Roles (cap. 22)',
                                 '• Ubuntu Server Security Guide (Canonical, 2026)',
                                 '• CIS PostgreSQL 16 Benchmark (Guía de referencia)']},
             footer_tag={'text': '● REFERENCIAS TÉCNICAS VERIFICADAS', 'color': C_CYAN})

    # =========================================================================
    # SLIDE 05: INSTALACIÓN DE POSTGRESQL 16
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    add_bg(s5)
    add_header(s5, "SECCIÓN 3 // PROCEDIMIENTO TÉCNICO",
               "Instalación de PostgreSQL y Comprobación Inicial",
               "Aprovisionamiento de paquetes, verificación del servicio e ingreso inicial administrativo", 5)

    add_card(s5, Inches(0.8), TOP_STD, Inches(3.65), HEIGHT_STD,
             "📦 Actualización e Instalación",
             ["• Medida Básica Inicial: Actualizar los índices de paquetes antes de instalar software.",
              "• Paquete postgresql: Binarios del motor de base de datos.",
              "• Paquete postgresql-contrib: Módulos y extensiones adicionales proporcionados con el motor.",
              "• Recepción de Correcciones: Garantiza contar con parches recientes de estabilidad y seguridad."],
             is_highlight=False,
             code_box={'label': 'COMANDOS DE INSTALACIÓN',
                       'lines': ['$ sudo apt update',
                                 '$ sudo apt upgrade -y',
                                 '$ sudo apt install postgresql postgresql-contrib -y']},
             footer_tag={'text': '● PAQUETES INSTALADOS CORRECTAMENTE', 'color': C_GREEN})

    add_card(s5, Inches(4.83), TOP_STD, Inches(3.65), HEIGHT_STD,
             "🔍 Comprobación del Servicio",
             ["• Verificación de Ejecución: Comprobar mediante systemd que el servicio esté activo.",
              "• Comprobación de Versión: Validar que se encuentre instalada la versión 16 de PostgreSQL.",
              "• Arranque Automático: El servicio queda habilitado para iniciar con el sistema."],
             is_highlight=True,
             code_box={'label': 'VERIFICACIÓN DE ESTADO Y VERSIÓN',
                       'lines': ['$ sudo systemctl status postgresql',
                                 '  Active: active (running)',
                                 '$ psql --version',
                                 '  psql (PostgreSQL) 16.x']},
             footer_tag={'text': '● SERVICIO EN EJECUCIÓN (ACTIVE)', 'color': C_CYAN})

    add_card(s5, Inches(8.86), TOP_STD, Inches(3.65), HEIGHT_STD,
             "🔑 Primer Ingreso Administrativo",
             ["• Usuario 'postgres': Usuario administrativo local creado durante la instalación.",
              "• Conexión Local: Se ejecuta directamente desde la consola del propio servidor.",
              "• Sesión Inicial: Permite efectuar las configuraciones de seguridad posteriores (bases, usuarios y roles)."],
             is_highlight=False,
             code_box={'label': 'CONEXIÓN INICIAL ADMINISTRATIVA',
                       'lines': ['$ sudo -u postgres psql',
                                 'psql (16.x)',
                                 'Type "help" for help.',
                                 'postgres=#']},
             footer_tag={'text': '● ACCESO LOCAL VERIFICADO', 'color': C_GREEN})

    # =========================================================================
    # SLIDE 06: MEDIDA 1 - SISTEMA ACTUALIZADO
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    add_bg(s6)
    add_header(s6, "SECCIÓN 4.1 // MEDIDAS DE HARDENING",
               "Medida 1: Mantener el Sistema Operativo Actualizado",
               "Corrección de vulnerabilidades conocidas y estrategia de seguridad por capas", 6)

    add_card(s6, Inches(0.8), TOP_STD, Inches(5.65), HEIGHT_STD,
             "🛡️ Fundamento de la Medida",
             ["• Primera Línea de Defensa: Mantener Ubuntu y PostgreSQL actualizados reduce la probabilidad de explotación de fallos conocidos.",
              "• Mitigación de Vulnerabilidades: Aplica correcciones que ya cuentan con solución oficial publicada por los desarrolladores.",
              "• Estabilidad del Entorno: Evita fallos imprevistos y comportamientos anómalos en el motor.",
              "• Recomendación de Canonical (2026): Complementar la instalación con seguridad por capas (actualizaciones, usuarios y red)."],
             is_highlight=True,
             code_box={'label': 'RUTINA PERIÓDICA DE ACTUALIZACIÓN',
                       'lines': ['$ sudo apt update',
                                 '$ sudo apt upgrade -y',
                                 '# Mantiene al día el SO y las librerías compartidas']},
             footer_tag={'text': '● RECOMENDACIÓN: CANONICAL (2026)', 'color': C_GREEN})

    add_card(s6, Inches(6.88), TOP_STD, Inches(5.65), HEIGHT_STD,
             "🧱 Estrategia de Seguridad por Capas",
             ["• Capa 1 (Parches de SO): Actualizaciones continuas del kernel y utilitarios del sistema.",
              "• Capa 2 (Parches de PostgreSQL): Actualizaciones del motor relacional mediante repositorios APT.",
              "• Capa 3 (Administración de Cuentas): Control estricto de usuarios locales y del gestor.",
              "• Capa 4 (Protección de Red): Reglas de acceso perimetral para aislar el puerto de base de datos."],
             is_highlight=False,
             code_box={'label': 'BENEFICIO DE LA ACTUALIZACIÓN CONTINUA',
                       'lines': ['• Cierra brechas de seguridad documentadas',
                                 '• Previene ataques automatizados basados en CVEs',
                                 '• Mantiene la compatibilidad con librerías TLS']},
             footer_tag={'text': '● ENFOQUE POR CAPAS VERIFICADO', 'color': C_CYAN})

    # =========================================================================
    # SLIDE 07: MEDIDA 2 - RESTRINGIR CONEXIONES EN PG_HBA.CONF
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    add_bg(s7)
    add_header(s7, "SECCIÓN 4.2 // MEDIDAS DE HARDENING",
               "Medida 2: Restringir las Conexiones Permitidas (pg_hba.conf)",
               "Filtrado estricto por subred y regla de denegación explícita para tráfico no autorizado", 7)

    add_card(s7, Inches(0.8), TOP_STD, Inches(5.65), HEIGHT_STD,
             "🧱 Control de Acceso Basado en Host (pg_hba.conf)",
             ["• Función del Archivo: Decide qué usuarios pueden conectarse, desde qué direcciones y con qué método de autenticación.",
              "• Evaluación de Reglas (PGDG 2026a): Las reglas se evalúan en orden secuencial según tipo de conexión, base, usuario y origen.",
              "• Acceso Administrativo Local: El usuario 'postgres' se mantiene restringido exclusivamente a acceso local mediante socket 'peer'.",
              "• Coherencia de Usuario: Se define el usuario 'app_user' para evitar inconsistencias con los permisos creados posteriormente."],
             is_highlight=True,
             code_box={'label': 'REGLAS CONFIGURADAS EN pg_hba.conf',
                       'lines': ['local   all           postgres   peer',
                                 'hostssl app_practica  app_user   192.168.1.0/24  scram-sha-256',
                                 'host    all           all        0.0.0.0/0       reject',
                                 'host    all           all        ::/0            reject']},
             footer_tag={'text': '● REGLAS FIJADAS SEGÚN SECCIÓN 4.2 DEL INFORME', 'color': C_GREEN})

    add_card(s7, Inches(6.88), TOP_STD, Inches(5.65), HEIGHT_STD,
             "🛑 Explicación de las Reglas Configuradas",
             ["• local all postgres peer: El superusuario no puede ser accedido a través de la red; solo usuarios locales con permiso de SO.",
              "• hostssl app_practica app_user 192.168.1.0/24 scram-sha-256: Permite al usuario de la aplicación conectarse únicamente desde la subred definida y exigiendo TLS.",
              "• host all all 0.0.0.0/0 reject: Rechaza explícitamente cualquier otra conexión IPv4 no autorizada.",
              "• host all all ::/0 reject: Rechaza explícitamente cualquier intento de conexión IPv6 no catalogado."],
             is_highlight=False,
             code_box={'label': 'SEGMENTACIÓN DE RED DE PRUEBAS',
                       'lines': ['Red Autorizada: 192.168.1.0/24 (LAN de laboratorio)',
                                 'Base Específica: app_practica (sin acceso a otras BD)',
                                 'Método de Red: hostssl (requiere cifrado TLS)']},
             footer_tag={'text': '● PRINCIPIO: LO NO PERMITIDO SE RECHAZA', 'color': C_RED})

    # =========================================================================
    # SLIDE 08: MEDIDA 3 - AUTENTICACIÓN SEGURA SCRAM-SHA-256
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    add_bg(s8)
    add_header(s8, "SECCIÓN 4.3 // MEDIDAS DE HARDENING",
               "Medida 3: Usar Autenticación Segura (SCRAM-SHA-256)",
               "Configuración del motor criptográfico y creación de la base de datos de práctica", 8)

    add_card(s8, Inches(0.8), TOP_STD, Inches(5.65), HEIGHT_STD,
             "🔑 Configuración de SCRAM-SHA-256 en postgresql.conf",
             ["• Cifrado de Contraseñas Moderno: Sustituye esquemas antiguos (como MD5) por SCRAM-SHA-256.",
              "• Almacenamiento Seguro: Genera un hash criptográfico robusto con salt aleatorio para cada contraseña.",
              "• Resistencia Criptográfica: Protege los secretos almacenados en el catálogo ante posibles extracciones no autorizadas.",
              "• Activación en postgresql.conf: Se define el parámetro 'password_encryption' antes de crear los usuarios."],
             is_highlight=True,
             code_box={'label': 'DIRECTIVA EN /etc/postgresql/16/main/postgresql.conf',
                       'lines': ['# En postgresql.conf',
                                 "password_encryption = 'scram-sha-256'",
                                 '# Garantiza que todo nuevo usuario almacene hash SCRAM']},
             footer_tag={'text': '● SCRAM-SHA-256 ACTIVADO EN postgresql.conf', 'color': C_GREEN})

    add_card(s8, Inches(6.88), TOP_STD, Inches(5.65), HEIGHT_STD,
             "👤 Creación de Base de Datos y Usuario de Práctica",
             ["• Base de Datos Específica: Se crea la base 'app_practica' dedicada a la actividad.",
              "• Usuario de Aplicación: Se crea el usuario 'app_user' asociado a la regla de conexión.",
              "• Contraseña de Ejemplo: Se asigna una contraseña robusta de laboratorio ('ClaveDeEjemplo_2026!').",
              "• Aclaración del Informe: Las contraseñas mostradas son de ejemplo y no deben reutilizarse en producción."],
             is_highlight=False,
             code_box={'label': 'COMANDOS SQL EJECUTADOS EN psql',
                       'lines': ['-- Conectado en psql:',
                                 'CREATE DATABASE app_practica;',
                                 "CREATE USER app_user WITH PASSWORD 'ClaveDeEjemplo_2026!';"]},
             footer_tag={'text': '● BASE app_practica Y USUARIO app_user CREADOS', 'color': C_CYAN})

    # =========================================================================
    # SLIDE 09: MEDIDA 4 - ROLES Y MÍNIMO PRIVILEGIO (PARTE 1)
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    add_bg(s9)
    add_header(s9, "SECCIÓN 4.4 // MEDIDAS DE HARDENING",
               "Medida 4: Aplicar el Principio de Mínimo Privilegio (Roles)",
               "Creación de roles segregados para lectura y escritura sin privilegios de administrador", 9)

    add_card(s9, Inches(0.8), TOP_STD, Inches(5.65), HEIGHT_STD,
             "👥 Segregación de Funciones mediante Roles",
             ["• Principio de Menor Privilegio: Un usuario de aplicación no debe tener permisos de superusuario.",
              "• Cada usuario recibe únicamente los permisos estrictamente necesarios para su función.",
              "• Roles de Grupo NOLOGIN: Se crean 'rol_lectura' y 'rol_escritura' que no permiten inicio de sesión directo.",
              "• Administración de Objetos (PGDG 2026b): PostgreSQL permite conceder o revocar privilegios específicos sobre objetos."],
             is_highlight=True,
             code_box={'label': 'CREACIÓN DE ROLES GRUPALES EN psql',
                       'lines': ['CREATE ROLE rol_lectura NOLOGIN;',
                                 'CREATE ROLE rol_escritura NOLOGIN;']},
             footer_tag={'text': '● ROLES NOLOGIN CREADOS CON ÉXITO', 'color': C_GREEN})

    add_card(s9, Inches(6.88), TOP_STD, Inches(5.65), HEIGHT_STD,
             "📋 Asignación Selectiva de Privilegios",
             ["• Permiso de Conexión: Se permite conectar a 'app_practica' a ambos roles.",
              "• Permiso en Esquema: Se otorga USAGE sobre el esquema 'public'.",
              "• Rol de Lectura: Recibe exclusivamente SELECT en todas las tablas.",
              "• Rol de Escritura: Recibe SELECT, INSERT, UPDATE, DELETE para operaciones de la aplicación.",
              "• Membresía: Se asigna 'rol_escritura' al usuario 'app_user'."],
             is_highlight=False,
             code_box={'label': 'SENTENCIAS SQL DE CONCESIÓN (GRANT)',
                       'lines': ['GRANT CONNECT ON DATABASE app_practica TO rol_lectura, rol_escritura;',
                                 'GRANT USAGE ON SCHEMA public TO rol_lectura, rol_escritura;',
                                 'GRANT SELECT ON ALL TABLES IN SCHEMA public TO rol_lectura;',
                                 'GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO rol_escritura;',
                                 'GRANT rol_escritura TO app_user;']},
             footer_tag={'text': '● PRIVILEGIOS ASIGNADOS A app_user', 'color': C_CYAN})

    # =========================================================================
    # SLIDE 10: MEDIDA 4 - SANEAMIENTO DEL ESQUEMA PUBLIC (PARTE 2)
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    add_bg(s10)
    add_header(s10, "SECCIÓN 4.4 // MEDIDAS DE HARDENING (CONT.)",
               "Medida 4: Saneamiento del Esquema Public",
               "Revocación del permiso de creación indiscriminada de objetos para usuarios no autorizados", 10)

    add_card(s10, Inches(0.8), TOP_STD, Inches(5.65), HEIGHT_STD,
             "🚫 Revocación del Permiso CREATE en Esquema Public",
             ["• Comportamiento Predeterminado en PostgreSQL: Cualquier usuario conectado tiene la capacidad de crear tablas en el esquema public.",
              "• Riesgo Identificado: Posibilidad de polución de la base de datos o creación desordenada de objetos por parte de usuarios comunes.",
              "• Medida Aplicada: Se revoca de forma explícita el permiso de creación al rol 'PUBLIC'.",
              "• Resultado Defensivo: Ningún usuario ordinario puede crear objetos en el esquema sin autorización expresa."],
             is_highlight=True,
             code_box={'label': 'SENTENCIA SQL DE REVOCACIÓN',
                       'lines': ['-- Revocación de creación en esquema public:',
                                 'REVOKE CREATE ON SCHEMA public FROM PUBLIC;']},
             footer_tag={'text': '● REVOCACIÓN APLICADA EXITOSAMENTE', 'color': C_GREEN})

    add_card(s10, Inches(6.88), TOP_STD, Inches(5.65), HEIGHT_STD,
             "🛡️ Beneficios Obtenidos en la Práctica",
             ["• Control de Estructura: Solo el administrador puede modificar el esquema de base de datos.",
              "• Prevención de Conflictos: Evita que scripts o usuarios de aplicación creen tablas temporales descontroladas.",
              "• Facilidad de Explicación: Es una medida sencilla de ejecutar que demuestra de forma clara el principio de menor privilegio.",
              "• Comprobación Directa: Puede verificarse intentando crear una tabla con un usuario sin permisos."],
             is_highlight=False,
             code_box={'label': 'EFECTO INMEDIATO DEL SANEAMIENTO',
                       'lines': ['• Usuario app_user puede: SELECT, INSERT, UPDATE, DELETE',
                                 '• Usuario app_user NO puede: CREATE TABLE',
                                 '• Esquema protegido contra alteraciones no autorizadas']},
             footer_tag={'text': '● ESQUEMA PUBLIC ENDURECIDO', 'color': C_CYAN})

    # =========================================================================
    # SLIDE 11: MEDIDAS 5 Y 6 - ARCHIVOS Y CIFRADO TLS
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    add_bg(s11)
    add_header(s11, "SECCIÓN 4.5 Y 4.6 // MEDIDAS DE HARDENING",
               "Medidas 5 y 6: Proteger Archivos de Datos y Habilitar TLS",
               "Permisos del sistema de archivos chmod 0700 y cifrado de conexiones con certificados X.509", 11)

    add_card(s11, Inches(0.8), TOP_STD, Inches(5.65), HEIGHT_STD,
             "📁 Medida 5: Proteger Archivos de Datos",
             ["• Importancia: Los archivos físicos contienen la información real de las bases de datos.",
              "• Propiedad Exclusiva: Se verifica que el directorio pertenezca únicamente al usuario 'postgres'.",
              "• Permisos 0700: Asegura que otros usuarios locales del sistema operativo no puedan leer ni listar los datos.",
              "• Comando chown y chmod: Aplicación inmediata sobre `/var/lib/postgresql/16/main`."],
             is_highlight=True,
             code_box={'label': 'COMANDOS SOBRE EL DIRECTORIO DE DATOS',
                       'lines': ['$ sudo chown -R postgres:postgres /var/lib/postgresql/16/main',
                                 '$ sudo chmod 0700 /var/lib/postgresql/16/main']},
             footer_tag={'text': '● PERMISOS 0700 Y PROPIEDAD POSTGRES VERIFICADOS', 'color': C_GREEN})

    add_card(s11, Inches(6.88), TOP_STD, Inches(5.65), HEIGHT_STD,
             "🔐 Medida 6: Habilitar Conexiones Cifradas con TLS",
             ["• Necesidad del Cifrado: Evitar que los datos y credenciales viajen de forma legible por la red.",
              "• Certificado de Laboratorio: Generación con openssl autofirmado (RSA 2048 bits) para la práctica.",
              "• Permisos de Clave Privada: Archivo `server.key` restringido a chmod 0600.",
              "• Configuración en postgresql.conf: Parámetros `ssl = on`, `ssl_cert_file` y `ssl_key_file`."],
             is_highlight=False,
             code_box={'label': 'GENERACIÓN DE CERTIFICADO Y CONFIGURACIÓN',
                       'lines': ['$ sudo openssl req -new -x509 -nodes -days 365 -newkey rsa:2048 \\',
                                 '  -keyout /etc/postgresql/16/main/server.key \\',
                                 '  -out /etc/postgresql/16/main/server.crt',
                                 '$ sudo chown postgres:postgres /etc/postgresql/16/main/server.*',
                                 '$ sudo chmod 0600 /etc/postgresql/16/main/server.key',
                                 '# En postgresql.conf: ssl = on']},
             footer_tag={'text': '● CIFRADO TLS HABILITADO EN EL SERVICIO', 'color': C_CYAN})

    # =========================================================================
    # SLIDE 12: MEDIDAS 7 Y 8 - REGISTROS BÁSICOS Y RESPALDO
    # =========================================================================
    s12 = prs.slides.add_slide(blank_layout)
    add_bg(s12)
    add_header(s12, "SECCIÓN 4.7 Y 4.8 // MEDIDAS DE HARDENING",
               "Medidas 7 y 8: Registros Básicos de Actividad y Copia de Seguridad",
               "Seguimiento de conexiones y desconexiones, y respaldo lógico de base de datos con pg_dump", 12)

    add_card(s12, Inches(0.8), TOP_STD, Inches(5.65), HEIGHT_STD,
             "📝 Medida 7: Activar Registros Básicos de Actividad",
             ["• Utilidad de los Logs: Permiten revisar quién se conecta, cuándo y desde dónde.",
              "• Enfoque de Laboratorio: Es suficiente habilitar el registro básico nativo sin instalar componentes externos.",
              "• logging_collector = on: Habilita el recopilador de registros del motor.",
              "• log_connections y log_disconnections = on: Registra inicio y cierre de sesiones.",
              "• log_line_prefix: Define timestamp, PID, usuario y base de datos (`%m [%p] %u@%d `)."],
             is_highlight=True,
             code_box={'label': 'PARÁMETROS EN postgresql.conf',
                       'lines': ['# En postgresql.conf',
                                 'logging_collector = on',
                                 'log_connections = on',
                                 'log_disconnections = on',
                                 "log_line_prefix = '%m [%p] %u@%d '"]},
             footer_tag={'text': '● REGISTROS NATIVOS HABILITADOS EN PG', 'color': C_GREEN})

    add_card(s12, Inches(6.88), TOP_STD, Inches(5.65), HEIGHT_STD,
             "💾 Medida 8: Realizar una Copia de Seguridad",
             ["• Importancia: El hardening no previene todos los incidentes; el respaldo es imprescindible.",
              "• Herramienta pg_dump: Herramienta estándar incluida con PostgreSQL para respaldo lógico.",
              "• Formato Custom (-F c): Formato comprimido y flexible de PostgreSQL.",
              "• Almacenamiento Seguro: La copia debe guardarse fuera del directorio principal y en otro equipo o medio."],
             is_highlight=False,
             code_box={'label': 'COMANDO DE RESPALDO CON pg_dump',
                       'lines': ['$ pg_dump -U postgres -F c -d app_practica \\',
                                 '  -f app_practica.backup',
                                 '# Genera archivo de respaldo lógico comprobable']},
             footer_tag={'text': '● ARCHIVO app_practica.backup GENERADO', 'color': C_CYAN})

    # =========================================================================
    # SLIDE 13: VERIFICACIÓN EXPERIMENTAL DE LA CONFIGURACIÓN
    # =========================================================================
    s13 = prs.slides.add_slide(blank_layout)
    add_bg(s13)
    add_header(s13, "SECCIÓN 5 // VALIDACIÓN EXPERIMENTAL",
               "Verificación de la Configuración y Pruebas de Laboratorio",
               "Tabla completa de pruebas realizadas para demostrar los controles durante la defensa", 13)

    add_card(s13, Inches(0.8), TOP_STD, Inches(6.0), HEIGHT_STD,
             "🧪 Tabla de Pruebas de Verificación (Sección 5 del Informe)",
             ["• 1. Servicio activo: `systemctl is-active postgresql` ➔ Debe mostrar 'active'.",
              "• 2. Versión instalada: `psql --version` ➔ Debe mostrar 'PostgreSQL 16.x'.",
              "• 3. Roles creados: `\\du` dentro de psql ➔ Deben aparecer 'app_user', 'rol_lectura' y 'rol_escritura'.",
              "• 4. Método de contraseña: `SHOW password_encryption;` ➔ Debe mostrar 'scram-sha-256'.",
              "• 5. Conexión cifrada: `\\conninfo` desde conexión remota ➔ Debe indicar que la conexión utiliza SSL/TLS.",
              "• 6. Restricción de acceso: Intentar conexión desde red no autorizada ➔ La conexión debe ser rechazada.",
              "• 7. Respaldo: Verificar archivo `app_practica.backup` ➔ El archivo debe existir y tener contenido."],
             is_highlight=True,
             code_box={'label': 'REINICIO PREVIO DEL SERVICIO',
                       'lines': ['$ sudo systemctl restart postgresql',
                                 '$ sudo systemctl is-active postgresql',
                                 '  active']},
             footer_tag={'text': '● 7 PRUEBAS DEMOSTRABLES EN VIVO', 'color': C_GREEN})

    add_card(s13, Inches(7.05), TOP_STD, Inches(5.48), HEIGHT_STD,
             "🎯 Criterio de Evaluación de la Defensa",
             ["• Finalidad de las Pruebas: Verificar que las configuraciones principales quedaron activas y pueden demostrarse ante el docente.",
              "• Sin Auditoría Compleja: No se requiere software externo de auditoría; las comprobaciones se ejecutan con comandos estándar de psql y Linux.",
              "• Facilidad de Demostración: Comandos directos y reproducibles en pocos segundos durante la exposición oral.",
              "• Evidencia de Respaldo: Comprobación de que el archivo generado no está vacío y es utilizable."],
             is_highlight=False,
             code_box={'label': 'COMANDOS DE COMPROBACIÓN EN TERMINAL',
                       'lines': ['$ psql -U app_user -d app_practica -h 192.168.1.50',
                                 'app_practica=> \\conninfo',
                                 'You are connected to database "app_practica"',
                                 'SSL connection (protocol: TLSv1.3, bits: 256)']},
             footer_tag={'text': '● VALIDACIÓN SATISFACTORIA', 'color': C_CYAN})

    # =========================================================================
    # SLIDE 14: RESULTADOS Y CONCLUSIONES ACADÉMICAS
    # =========================================================================
    s14 = prs.slides.add_slide(blank_layout)
    add_bg(s14)
    add_header(s14, "SECCIÓN 6 Y 7 // RESULTADOS Y CONCLUSIONES",
               "Resultados de la Práctica y Conclusiones Académicas",
               "Comparativa básica vs hardening, lecciones aprendidas y propuestas de trabajo futuro", 14)

    # Izquierda (Tabla Comparativa)
    add_card(s14, Inches(0.8), TOP_STD, Inches(6.5), HEIGHT_STD,
             "📊 Tabla Comparativa: Antes vs Después del Hardening",
             ["• Acceso: Reglas generales por defecto ➔ Acceso limitado por usuario y red en pg_hba.conf.",
              "• Contraseñas: Configuración estándar ➔ Uso forzado de SCRAM-SHA-256.",
              "• Permisos: Riesgo de otorgar permisos amplios ➔ Roles con permisos separados (lectura/escritura).",
              "• Comunicación: Puede existir conexión sin cifrado ➔ Regla hostssl para conexión cifrada TLS.",
              "• Registros: Información limitada para seguimiento ➔ Registro de conexiones y desconexiones.",
              "• Respaldo: Sin copia definida en la práctica ➔ Copia lógica funcional mediante pg_dump."],
             is_highlight=True,
             code_box={'label': 'TABLA OFICIAL DE RESULTADOS (SECCIÓN 6)',
                       'lines': ['Aspecto      | Config. Básica         | Post-Hardening',
                                 'Acceso       | General por defecto    | Limitado usuario/red',
                                 'Contraseñas  | Estándar               | SCRAM-SHA-256',
                                 'Permisos     | Riesgo permisos amplios| Roles separados',
                                 'Comunicación | Sin cifrado opcional   | Regla hostssl (TLS)',
                                 'Registros    | Información limitada   | Log conexiones/descon.',
                                 'Respaldo     | Sin copia definida     | pg_dump lógico']},
             footer_tag={'text': '● MEJORA DIRECTA Y VERIFICABLE EN LOS 6 ASPECTOS', 'color': C_GREEN})

    # Derecha Superior (Conclusiones)
    add_card(s14, Inches(7.55), TOP_STD, Inches(4.98), Inches(2.55),
             "💡 Conclusiones Principales del Trabajo",
             ["• Seguridad Integral: El hardening no consiste en aplicar una sola configuración, sino en combinar varias medidas sencillas.",
              "• Adaptación al Entorno: Para una actividad académica es preferible utilizar configuraciones que puedan ejecutarse, verificarse y explicarse correctamente.",
              "• Enfoque Práctico: Pequeñas configuraciones coordinadas reducen riesgos de forma significativa."],
             is_highlight=False,
             footer_tag={'text': '● APRENDIZAJE: COMBINACIÓN DE MEDIDAS SENCILLAS', 'color': C_CYAN})

    # Derecha Inferior (Trabajo Futuro)
    add_card(s14, Inches(7.55), TOP_STD + Inches(2.75), Inches(4.98), Inches(2.60),
             "🚀 Recomendaciones de Trabajo Futuro",
             ["• Cortafuegos del Sistema: Incorporar UFW o iptables para restringir el puerto 5432 a nivel de SO.",
              "• Herramientas de Auditoría: Evaluar extensiones especializadas en entornos avanzados.",
              "• Política Formal de Respaldos: Automatizar la ejecución de respaldos con cron y rotación periódica."],
             is_highlight=False,
             code_box={'label': 'LÍNEAS DE EVOLUCIÓN ACADÉMICA',
                       'lines': ['1. Firewall UFW en Ubuntu Server',
                                 '2. Automatización de copias con cron',
                                 '3. Pruebas de restauración pg_restore']})

    # Aplicación de transiciones
    apply_transitions(prs)

    output_path = "d:/TDB2/presentacion_hardening_sgbd.pptx"
    try:
        prs.save(output_path)
        print(f"Presentación PPTX generada exitosamente en: {output_path}")
    except PermissionError:
        alt_path = "d:/TDB2/presentacion_hardening_sgbd_actualizada.pptx"
        prs.save(alt_path)
        print(f"Aviso: Archivo principal abierto en PowerPoint. Se guardó la versión en: {alt_path}")

def apply_transitions(prs):
    """Aplica efectos de transición cinematográficos a las 14 diapositivas de PowerPoint."""
    transitions = [
        '<p:transition xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" spd="med"><p:zoom/></p:transition>',       # Slide 01: Apertura UPDS
        '<p:transition xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" spd="med"><p:fade/></p:transition>',       # Slide 02: Resumen
        '<p:transition xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" spd="med"><p:wipe dir="r"/></p:transition>',  # Slide 03: Introducción
        '<p:transition xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" spd="med"><p:push dir="l"/></p:transition>',  # Slide 04: Entorno
        '<p:transition xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" spd="med"><p:split dir="in"/></p:transition>', # Slide 05: Instalación
        '<p:transition xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" spd="med"><p:push dir="u"/></p:transition>',  # Slide 06: Actualizaciones
        '<p:transition xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" spd="med"><p:fade/></p:transition>',       # Slide 07: pg_hba.conf
        '<p:transition xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" spd="med"><p:wheel/></p:transition>',      # Slide 08: SCRAM-SHA-256
        '<p:transition xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" spd="med"><p:wipe dir="d"/></p:transition>',  # Slide 09: Roles
        '<p:transition xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" spd="med"><p:split dir="out"/></p:transition>',# Slide 10: Revoke Public
        '<p:transition xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" spd="med"><p:push dir="l"/></p:transition>',  # Slide 11: Archivos & TLS
        '<p:transition xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" spd="med"><p:push dir="u"/></p:transition>',  # Slide 12: Logs & Respaldo
        '<p:transition xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" spd="med"><p:fade/></p:transition>',       # Slide 13: Verificación
        '<p:transition xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" spd="med"><p:checker/></p:transition>',   # Slide 14: Resultados & Conclusiones
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
