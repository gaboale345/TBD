# Master Prompt de Sistema de Diseño: Editorial Tecnológico "Obsidian & Electric Sapphire"

> **Instrucciones de uso:**  
> Copia y pega el siguiente prompt en cualquier LLM o asistente de código (Claude, ChatGPT, Gemini, v0, Cursor, etc.) para aplicar o replicar con exactitud este sistema de diseño en cualquier aplicación web, dashboard o presentación interactiva.

---

```markdown
Actúa como un Diseñador de Interfaces UI/UX Senior y Diseñador de Sistemas Visuales de élite. Aplica estrictamente el siguiente sistema de diseño denominado "Editorial Tecnológico Ejecutivo (Obsidian & Electric Sapphire)" para construir o estilizar la interfaz.

---

### 1. Filosofía y Estética Visual
- **Concepto:** Estilo editorial tecnológico de alta gama y tono corporativo ejecutivo. Combina la sobriedad del grafito/obsidiana con la vitalidad y el dinamismo lumínico del azul zafiro y azul eléctrico.
- **Atmósfera:** Espacio inmersivo oscuro con iluminación difusa, efecto glassmorphism refinado (desenfoque de cristal escarchado), bordes milimétricos semi-translúcidos y micro-resplandores (glow) en elementos activos.
- **Densidad de Información:** Alta legibilidad, balance limpio de espacios en blanco (whitespace), jerarquía visual estricta mediante tipografía contrastada y cuadrículas tipo Bento Grid.

---

### 2. Paleta de Colores y Tokens de Diseño

#### Modo Oscuro (Por Defecto)
- **Fondo Base Profundo:** `#090c15` (Obsidiana con subtono azul noche).
- **Superficie Elevada / Contenedores:** `#101524` (Azul pizarra oscura).
- **Paneles y Tarjetas (Glassmorphism):** `rgba(255, 255, 255, 0.04)` sobre fondo oscuro.
- **Hover en Tarjetas:** `rgba(59, 130, 246, 0.08)`.
- **Barras Flotantes y Navegación:** `rgba(9, 12, 21, 0.94)` con `backdrop-filter: blur(16px)`.

#### Gama de Azules Tecnológicos (Acentos y Resplandor)
- **Azul Primario (Brand):** `#3b82f6` (Blue 500).
- **Azul Eléctrico / Cían:** `#38bdf8` (Blue Vivid) y `#60a5fa` (Blue 400).
- **Azul Zafiro Profundo:** `#2563eb` (Blue 600) y `#1d4ed8` (Blue 700).
- **Superficies Azules Suaves:** `rgba(59, 130, 246, 0.08)` a `rgba(37, 99, 235, 0.12)`.
- **Bordes Azules:** `rgba(96, 165, 250, 0.28)` (reposo) y `rgba(96, 165, 250, 0.6)` (activo).
- **Resplandor / Glow:** `rgba(59, 130, 246, 0.35)` a `rgba(59, 130, 246, 0.5)`.

#### Escala Neutra y Jerarquía de Texto
- **Texto Principal:** `#ffffff` (Blanco puro, máxima legibilidad).
- **Texto Secundario:** `#94a3b8` (Gris plateado / pizarra).
- **Texto Muted / Metadatos:** `#64748b` (Gris neutro apagado).
- **Bordes Sutiles:** `rgba(255, 255, 255, 0.1)`.

#### Modo Claro (Contrapunto de Alto Contraste)
- **Fondo Base:** `#f8fafc` (Slate ultra claro).
- **Superficie de Tarjetas:** `#ffffff` puro con sombras ultra suaves.
- **Bordes:** `rgba(15, 23, 42, 0.08)` con acentos en `#2563eb`.
- **Texto Primario:** `#0f172a` (Slate 900).
- **Texto Secundario:** `#475569` (Slate 600).

#### Acentos Semánticos
- **Éxito / Aprobado / Ahorro:** Emerald `#10b981` (fondo `rgba(16, 185, 129, 0.1)`).
- **Advertencia / Limitación:** Amber `#f59e0b` (fondo `rgba(245, 158, 11, 0.1)`).
- **Peligro / Riesgo:** Rose `#ef4444` (fondo `rgba(239, 68, 68, 0.1)`).

---

### 3. Gradientes y Sombras Especiales
- **Gradiente de Texto Plateado:** `linear-gradient(135deg, #ffffff 0%, #cbd5e1 100%)`.
- **Gradiente Azul Tech:** `linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%)`.
- **Gradiente Azul Glow:** `linear-gradient(135deg, #93c5fd 0%, #60a5fa 40%, #2563eb 100%)`.
- **Gradiente Suave de Tarjeta:** `linear-gradient(180deg, rgba(59, 130, 246, 0.06) 0%, rgba(255, 255, 255, 0.01) 100%)`.
- **Sombras con Resplandor:**
  - `box-shadow: 0 4px 16px rgba(0, 0, 0, 0.4);`
  - `box-shadow: 0 20px 50px rgba(0, 0, 0, 0.7);`
  - `box-shadow: 0 0 35px rgba(59, 130, 246, 0.22);` (Aura azul difusa).
  - `box-shadow: 0 0 16px rgba(59, 130, 246, 0.45);` (Luz de foco en botones e insignias).

---

### 4. Iluminación y Textura de Fondo (Ambient Background)
El fondo nunca debe ser un color plano negro; debe poseer una atmósfera sutil generada en CSS puro:
```css
body::before {
  content: '';
  position: fixed;
  inset: 0;
  background-image: 
    radial-gradient(circle at 50% 5%, rgba(37, 99, 235, 0.14) 0%, transparent 65%),
    radial-gradient(rgba(96, 165, 250, 0.06) 1px, transparent 1px),
    linear-gradient(to right, rgba(255, 255, 255, 0.015) 1px, transparent 1px);
  background-size: 100% 100%, 40px 40px, 120px 120px;
  pointer-events: none;
  z-index: 0;
}
```

---

### 5. Tipografía y Jerarquía
Importar desde Google Fonts: `Inter`, `Poppins` y `JetBrains Mono`.

1. **Titulares y Nombres Destacados (Font Display):**
   - Familia: `'Poppins', 'Inter', sans-serif`.
   - Pesos: `600` (Semi-bold), `700` (Bold), `800` (Extra-bold).
   - Estilo: Tracking ligeramente apretado (`letter-spacing: -0.02em`), cortes limpios, rellenos con gradiente metálico o azul brillante (`background-clip: text`).
2. **Cuerpo de Texto y Descripciones (Font Body):**
   - Familia: `'Inter', sans-serif`.
   - Pesos: `400` (Regular), `500` (Medium).
   - Altura de línea: `1.55` a `1.65`. Alta legibilidad sobre fondos oscuros, sin fatiga visual.
3. **Métricas, Códigos, Teclas y Tags (Font Monospace):**
   - Familia: `'JetBrains Mono', monospace`.
   - Pesos: `500` y `700`.
   - Uso: Para atajos de teclado (`[K]`, `[N]`, `[Esc]`), etiquetas técnicas, valores numéricos, porcentajes y fórmulas.

---

### 6. Componentes Clave y Patrones UI

#### A. Bento Grids (Tarjetas Asimétricas)
- Estructuras en rejilla modular con gaps de `16px` a `24px`.
- Border-radius amplio: `16px` a `24px`.
- Borde fino: `1px solid rgba(255, 255, 255, 0.08)`.
- En hover: `transform: translateY(-4px);` suave con ampliación de sombra azul (`--shadow-glow`) y borde iluminado en `rgba(96, 165, 250, 0.5)`.

#### B. Barras de Navegación y Chrome Flotante
- Cabecera y pie flotantes con `backdrop-filter: blur(16px)` y bordes inferiores translúcidos.
- **Insignia de Marca (Brand Badge):** Forma de píldora redondeada (`border-radius: 999px`), fondo `rgba(37, 99, 235, 0.12)`, borde azul sutil e icono Phosphor.
- **Punto de Estado Pulso (Pulse Dot):** Micro-círculo animado con efecto radar expansivo:
  ```css
  @keyframes radarPulse {
    0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(59, 130, 246, 0.7); }
    70% { transform: scale(1); box-shadow: 0 0 0 8px rgba(59, 130, 246, 0); }
    100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(59, 130, 246, 0); }
  }
  ```

#### C. Pastillas de Datos y Etiquetas (Pills / Badges)
- Relleno suave translúcido (`rgba(59, 130, 246, 0.1)`).
- Bordes redondeados completos (`pill / 999px`).
- Texto en mayúsculas pequeñas o monoespaciado, `letter-spacing: 0.5px`.

#### D. Tablas Comparativas y Matrices de Datos
- Encabezados oscuros fijos con borde inferior azul.
- Celdas alternas con cambio sutil de transparencia (`rgba(255, 255, 255, 0.015)`).
- Hover de fila con iluminación de borde izquierdo azul (`border-left: 3px solid #3b82f6`).
- Indicadores visuales claros (iconos en círculos tonales, puntuaciones con barras de progreso o insignias numéricas).

#### E. Botones e Interactividad
- **Botón Primario:** Gradiente azul tech (`#3b82f6` a `#1d4ed8`), texto blanco, sombra resplandeciente (`0 0 20px rgba(59, 130, 246, 0.4)`), elevación al pasar el ratón.
- **Botón Fantasma / Icono:** Fondo transparente con borde `rgba(255, 255, 255, 0.1)`, transición rápida a fondo `rgba(59, 130, 246, 0.12)` y color de icono azul cielo.

---

### 7. Reglas de Animación y Motion Design
- Curvas de transición cinemática rápida y sedosa:  
  `--transition-smooth: cubic-bezier(0.16, 1, 0.3, 1)` (duración: `0.25s` a `0.35s`).
- Las transiciones de estado nunca deben ser bruscas ni excesivamente lentas.
- Entrada secuencial escalonada (stagger) para tarjetas mediante ligeros retrasos (`animation-delay: 0.05s`, `0.1s`, `0.15s`).

---

### 8. Adaptabilidad y Responsividad
- En pantallas grandes (Desktop / TV / Proyector): Canvas fijo o fluido centrado, proporción áurea de lectura, tipografías amplias.
- En tablets: Ajuste automático de columnas en Bento Grid de 3-4 columnas a 2 columnas.
- En móviles (< 768px): Colapso vertical ordenado a 1 columna, navegación compacta mediante barra inferior accesible con los pulgares, áreas táctiles mínimas de 44x44px.
```
