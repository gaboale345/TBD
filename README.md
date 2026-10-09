# Informe Práctico de Instalación y Hardening de SGBD

> **Proyecto de Ciberseguridad y Despliegue de Alta Seguridad para PostgreSQL 16 LTS**  
> **Estándares:** CIS PostgreSQL 16 Benchmark v1.3.0 (Nivel 1 y 2) | NIST SP 800-123 | PCI-DSS v4.0 | ISO/IEC 27001:2022  
> **Sistema de Diseño Visual:** Editorial Tecnológico *"Obsidian & Electric Sapphire"* (`diseño.md`)

---

## 🛡️ Resumen del Proyecto

Este repositorio contiene la entrega completa del **Informe Práctico de Instalación y Hardening de Sistemas Gestores de Bases de Datos (SGBD)**. El objetivo principal es la transformación determinista de una instalación básica (*"vanilla"*) de PostgreSQL 16 en una infraestructura hiper-securizada bajo el paradigma de **Defensa en Profundidad (Defense-in-Depth)**.

### Indicadores Clave de Desempeño (KPIs):
* **Índice de Cumplimiento CIS:** De **34.2%** (Vanilla) a **98.4%** (Post-Hardening).
* **Superficie de Exposición de Red:** Reducción del **-89%**.
* **Vulnerabilidades Críticas:** **0** (Cero hallazgos abiertos).

---

## 📦 Estructura del Repositorio y Entregables

| Archivo / Componente | Descripción |
| :--- | :--- |
| **[`index.html`](index.html)** | **Presentación interactiva de 8 diapositivas** estilo PowerPoint con Bento Grids, navegación por teclado y modo pantalla completa. |
| **[`style.css`](style.css)** | Hoja de estilos con separación estricta, efecto *glassmorphism*, animaciones fluidas y paleta *Obsidian & Sapphire*. |
| **[`app.js`](app.js)** | Lógica JavaScript de navegación, atajos de teclado (`[←]`, `[→]`, `[F]`, `[G]`, `[↓]`, `[↑]`), rueda de ratón y copiado de comandos. |
| **[`informe_hardening_sgbd.docx`](informe_hardening_sgbd.docx)** | **Informe oficial detallado en formato Word (.DOCX)** listo para entrega ejecutiva. |
| **[`presentacion_hardening_sgbd.pptx`](presentacion_hardening_sgbd.pptx)** | **Presentación oficial en PowerPoint (.PPTX)** con 8 diapositivas formato Widescreen 16:9. |
| **[`presentacion_hardening_sgbd_actualizada.pptx`](presentacion_hardening_sgbd_actualizada.pptx)** | Versión actualizada con Bento Grids de 2 filas completas en diapositivas 1 y 2. |
| **[`INFORME_TECNICO_HARDENING_SGBD.md`](INFORME_TECNICO_HARDENING_SGBD.md)** | Documentación técnica completa en Markdown con comandos y configuraciones comentadas. |
| **[`informe_doc_viewer.html`](informe_doc_viewer.html)** | Visor web interactivo para lectura e impresión directa / guardado en PDF del informe. |
| **[`generar_docx.py`](generar_docx.py)** | Script Python con `python-docx` para compilar y personalizar el documento Word. |
| **[`generar_pptx.py`](generar_pptx.py)** | Script Python con `python-pptx` para generar la presentación en PowerPoint. |
| **[`diseño.md`](diseño.md)** | Guía maestra del Sistema de Diseño *"Obsidian & Electric Sapphire"*. |

---

## 🖥️ Diapositivas de la Presentación

1. **Slide 01 — Portada y Objetivos Estratégicos:** Filosofía de Defensa en Profundidad, 3 pilares de seguridad y pipeline de 4 capas.
2. **Slide 02 — Superficie de Ataque & STRIDE:** Análisis de los 4 vectores críticos, matriz cuantitativa CVSS v3.1 y *Kill-Chain* mitigada.
3. **Slide 03 — Fase I: Kernel & SO Hardening:** Parámetros `sysctl.conf`, ASLR nivel 2, permisos `0700` y sandboxing con Systemd.
4. **Slide 04 — Fase II: Criptografía en Tránsito:** Cero tráfico plano, forzado de TLS 1.3 y suites autenticadas AEAD (ECDHE-ECDSA/RSA).
5. **Slide 05 — Fase III: Autenticación & Red:** Sustitución de MD5 por SCRAM-SHA-256 y cortafuegos perimetral `pg_hba.conf` (*Zero Trust*).
6. **Slide 06 — Fase IV: Control de Acceso RBAC:** Revocación de privilegios en esquema `public`, funciones bloqueadas y matriz de roles.
7. **Slide 07 — Fase V: Auditoría Forense con `pgaudit`:** Captura inmutable de DDL/DML, rotación `0600` y reenvío seguro a SIEM.
8. **Slide 08 — Matriz de Cumplimiento CIS y Conclusiones:** Balance cuantitativo de 28 controles y recomendaciones continuas DevSecOps.

---

## 🚀 Cómo Visualizar y Utilizar el Proyecto

### 1. Presentación Web Interactiva
Abre directamente [`index.html`](index.html) en cualquier navegador moderno o sirve los archivos localmente:
```bash
python -m http.server 8080
```
Luego visita `http://localhost:8080/index.html`.

**Atajos de Teclado:**
* <kbd>→</kbd> / <kbd>N</kbd> / <kbd>Espacio</kbd>: Siguiente diapositiva.
* <kbd>←</kbd> / <kbd>P</kbd> / <kbd>K</kbd>: Diapositiva anterior.
* <kbd>↓</kbd> / <kbd>↑</kbd> o Rueda del ratón: Desplazamiento vertical fluido dentro de la diapositiva.
* <kbd>F</kbd>: Alternar Pantalla Completa (*Fullscreen*).
* <kbd>G</kbd>: Abrir/cerrar cajón de miniaturas (*Slide Drawer*).
* <kbd>R</kbd>: Reproducir de nuevo la animación original de la diapositiva activa.
* <kbd>T</kbd>: Alternar entre Modo Claro y Modo Oscuro (*Theme Switch*).
* <kbd>1</kbd> a <kbd>8</kbd>: Salto directo a la diapositiva seleccionada.

### 2. Generación de Documentos Office
Para regenerar los archivos `.docx` o `.pptx` desde código:
```bash
python generar_docx.py
python generar_pptx.py
```

---

## 🎨 Sistema de Diseño Visual

El proyecto implementa la guía de estilo **"Obsidian & Electric Sapphire"**:
* **Fondo Base Profundo:** `#090c15` (Obsidiana con subtono azul noche).
* **Superficies Elevadas:** `#101524` con *glassmorphism* (`rgba(255, 255, 255, 0.04)`).
* **Acentos Lumínicos:** Electric Sapphire (`#38bdf8`), Blue 500 (`#3b82f6`) y Sapphire Deep (`#2563eb`).
* **Tipografía:** *Poppins* para títulos de impacto, *Inter* para cuerpo de texto y *JetBrains Mono* para código y métricas.