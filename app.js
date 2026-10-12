/**
 * LOGICA INTERACTIVA DE PRESENTACION DE HARDENING DE SGBD
 * Sistema de Diseño: Obsidian & Electric Sapphire
 */

document.addEventListener('DOMContentLoaded', () => {
  // Estado de la presentación
  const state = {
    currentSlide: 1,
    totalSlides: 14,
    theme: 'light',
    isDrawerOpen: false,
    isFullscreen: false,
    isTransitioning: false,
    slideTitles: [
      { num: '01', title: 'Portada y Ficha Técnica Académica', sub: 'Universidad Privada Domingo Savio — Ingeniería en Sistemas', fx: 'Cyber Nexus' },
      { num: '02', title: 'Resumen y Enfoque Metodológico', sub: 'Endurecimiento Progresivo y Alcance Demostrable', fx: 'Methodology Shield' },
      { num: '03', title: 'Introducción al Hardening de SGBD', sub: 'Conceptos Clave de Bastionado e INCIBE 2023', fx: 'Threat Radar' },
      { num: '04', title: 'Objetivo y Entorno de Laboratorio', sub: 'PostgreSQL 16 en Ubuntu Server 24.04 LTS', fx: 'Lab Matrix' },
      { num: '05', title: 'Instalación de PostgreSQL 16', sub: 'Aprovisionamiento de Paquetes y Comprobación del Servicio', fx: 'Provisioning' },
      { num: '06', title: 'Medida 1: Actualización del Sistema', sub: 'Seguridad en Capas y Mitigación de Vulnerabilidades (Canonical)', fx: 'Patch Shield' },
      { num: '07', title: 'Medida 2: Restricción de Conexiones', sub: 'Control de Acceso Perimetral en pg_hba.conf y Denegación', fx: 'Firewall Gate' },
      { num: '08', title: 'Medida 3: Autenticación Robusta', sub: 'Cifrado de Credenciales con SCRAM-SHA-256', fx: 'Crypto Vault' },
      { num: '09', title: 'Medida 4: Principio de Mínimo Privilegio', sub: 'Segregación Funcional de Roles (rol_lectura y rol_escritura)', fx: 'RBAC Matrix' },
      { num: '10', title: 'Medida 4: Saneamiento de Schema Public', sub: 'Revocación de Permiso CREATE para Prevención de Abusos', fx: 'Logic Shield' },
      { num: '11', title: 'Medidas 5 y 6: Archivos de Datos y TLS', sub: 'Permisos Restrictivos 0700/0600 y Criptografía X.509', fx: 'Cipher Stream' },
      { num: '12', title: 'Medidas 7 y 8: Registros y Respaldo Lógico', sub: 'Logging Nativo de Conexiones y Backup con pg_dump', fx: 'Resilience Lock' },
      { num: '13', title: 'Verificación Experimental de la Configuración', sub: 'Matriz de 7 Pruebas Técnicas Demostrables en Defensa', fx: 'Audit Scan' },
      { num: '14', title: 'Resultados Comparativos y Conclusiones', sub: 'Balance Antes vs Después del Hardening y Trabajo Futuro', fx: 'Executive Triumph' }
    ]
  };

  // Referencias al DOM
  const slides = document.querySelectorAll('.slide');
  const progressFill = document.getElementById('progressFill');
  const currentSlideNum = document.getElementById('currentSlideNum');
  const btnPrev = document.getElementById('btnPrev');
  const btnNext = document.getElementById('btnNext');
  const btnGrid = document.getElementById('btnGrid');
  const btnCloseDrawer = document.getElementById('btnCloseDrawer');
  const slideGridDrawer = document.getElementById('slideGridDrawer');
  const drawerThumbnails = document.getElementById('drawerThumbnails');
  const slideDotsContainer = document.getElementById('slideDotsContainer');
  const btnFullscreen = document.getElementById('btnFullscreen');
  const btnThemeToggle = document.getElementById('btnThemeToggle');
  const themeLabel = document.getElementById('themeLabel');
  const themeIcon = document.getElementById('themeIcon');
  const btnReplay = document.getElementById('btnReplay');
  const animLabel = document.getElementById('animLabel');
  const btnDownloadMenu = document.getElementById('btnDownloadMenu');
  const downloadsDropdown = document.getElementById('downloadsDropdown');
  const toastNotification = document.getElementById('toastNotification');
  const toastMessage = document.getElementById('toastMessage');

  // Control de Tema (Modo Claro / Modo Oscuro)
  function applyTheme(theme) {
    state.theme = theme;
    const isLight = theme === 'light';
    document.body.classList.toggle('light-mode', isLight);
    localStorage.setItem('presentation-theme', theme);

    if (themeLabel) {
      themeLabel.textContent = isLight ? 'Modo Claro' : 'Modo Oscuro';
    }
    if (themeIcon) {
      themeIcon.innerHTML = isLight ? `
        <circle cx="12" cy="12" r="5"></circle>
        <line x1="12" y1="1" x2="12" y2="3"></line>
        <line x1="12" y1="21" x2="12" y2="23"></line>
        <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
        <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
        <line x1="1" y1="12" x2="3" y2="12"></line>
        <line x1="21" y1="12" x2="23" y2="12"></line>
        <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
        <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
      ` : `
        <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
      `;
    }
    if (btnThemeToggle) {
      btnThemeToggle.setAttribute('title', isLight ? 'Cambiar a Modo Oscuro [T]' : 'Cambiar a Modo Claro [T]');
    }
  }

  function toggleTheme() {
    const nextTheme = state.theme === 'light' ? 'dark' : 'light';
    applyTheme(nextTheme);
    showToast(nextTheme === 'light' ? '☀️ Modo Claro activado' : '🌙 Modo Oscuro activado');
  }

  // Actualizar Badge de Animación
  function updateAnimBadge(index) {
    if (animLabel && state.slideTitles[index - 1]) {
      animLabel.textContent = `FX: ${state.slideTitles[index - 1].fx}`;
    }
  }

  // Inicializar Dots de Navegación
  function initDots() {
    slideDotsContainer.innerHTML = '';
    for (let i = 1; i <= state.totalSlides; i++) {
      const dot = document.createElement('button');
      dot.className = `slide-dot ${i === 1 ? 'active' : ''}`;
      dot.setAttribute('title', `Ir a diapositiva ${i}`);
      dot.setAttribute('aria-label', `Diapositiva ${i}`);
      dot.addEventListener('click', () => goToSlide(i));
      slideDotsContainer.appendChild(dot);
    }
  }

  // Inicializar Drawer de Miniaturas
  function initDrawer() {
    drawerThumbnails.innerHTML = '';
    state.slideTitles.forEach((item, idx) => {
      const slideIndex = idx + 1;
      const card = document.createElement('div');
      card.className = `drawer-card-thumb ${slideIndex === state.currentSlide ? 'active' : ''}`;
      card.innerHTML = `
        <span class="thumb-num">${item.num}</span>
        <div class="thumb-info">
          <span class="thumb-title">${item.title}</span>
          <span class="thumb-subtitle">${item.sub}</span>
        </div>
      `;
      card.addEventListener('click', () => {
        goToSlide(slideIndex);
        toggleDrawer(false);
      });
      drawerThumbnails.appendChild(card);
    });
  }

  // Función de Cambio de Diapositiva con Animación de Entrada y Salida
  function goToSlide(targetSlide, forceDirection) {
    if (targetSlide < 1 || targetSlide > state.totalSlides) return;
    if (targetSlide === state.currentSlide && !forceDirection) return;
    if (state.isTransitioning) return; // Evitar solapamiento de animaciones

    const currentEl = document.querySelector(`.slide[data-index="${state.currentSlide}"]`);
    const nextEl = document.querySelector(`.slide[data-index="${targetSlide}"]`);
    if (!nextEl) return;

    const direction = forceDirection || (targetSlide >= state.currentSlide ? 'next' : 'prev');
    state.currentSlide = targetSlide;
    state.isTransitioning = true;

    // Actualizar UI (Contador, Barra de Progreso, Badge FX)
    currentSlideNum.textContent = String(state.currentSlide).padStart(2, '0');
    const percent = (state.currentSlide / state.totalSlides) * 100;
    progressFill.style.width = `${percent}%`;
    updateAnimBadge(state.currentSlide);

    // Actualizar estado de dots
    const dots = document.querySelectorAll('.slide-dot');
    dots.forEach((dot, idx) => {
      dot.classList.toggle('active', idx + 1 === state.currentSlide);
    });

    // Actualizar miniaturas del drawer
    const thumbs = document.querySelectorAll('.drawer-card-thumb');
    thumbs.forEach((thumb, idx) => {
      thumb.classList.toggle('active', idx + 1 === state.currentSlide);
    });

    // Estado de botones prev/next
    btnPrev.disabled = state.currentSlide === 1;
    btnNext.disabled = state.currentSlide === state.totalSlides;
    btnPrev.style.opacity = state.currentSlide === 1 ? '0.45' : '1';
    btnNext.style.opacity = state.currentSlide === state.totalSlides ? '0.45' : '1';

    // Carga inicial o misma diapositiva
    if (!currentEl || currentEl === nextEl) {
      document.querySelectorAll('.slide').forEach(s => {
        s.classList.remove('active', 'is-exiting', 'is-entering', 'exit-next', 'exit-prev', 'enter-next', 'enter-prev');
      });
      nextEl.classList.add('active', 'is-entering', direction === 'next' ? 'enter-next' : 'enter-prev');
      nextEl.scrollTop = 0;
      setTimeout(() => {
        nextEl.classList.remove('is-entering', 'enter-next', 'enter-prev');
        state.isTransitioning = false;
      }, 500);
      return;
    }

    // ANIMACIÓN DE SALIDA EN DIAPOSITIVA ACTUAL
    currentEl.classList.remove('is-entering', 'enter-next', 'enter-prev');
    currentEl.classList.add('is-exiting', direction === 'next' ? 'exit-next' : 'exit-prev');

    // ANIMACIÓN DE ENTRADA EN NUEVA DIAPOSITIVA
    nextEl.classList.remove('is-exiting', 'exit-next', 'exit-prev');
    nextEl.classList.add('active', 'is-entering', direction === 'next' ? 'enter-next' : 'enter-prev');
    nextEl.scrollTop = 0;

    // Concluir transición cinemática (480ms)
    setTimeout(() => {
      currentEl.classList.remove('active', 'is-exiting', 'exit-next', 'exit-prev');
      nextEl.classList.remove('is-entering', 'enter-next', 'enter-prev');
      state.isTransitioning = false;
    }, 480);
  }

  // Reproducir animación original de la diapositiva actual
  function replayCurrentAnimation() {
    if (state.isTransitioning) return;
    const currentEl = document.querySelector(`.slide[data-index="${state.currentSlide}"]`);
    if (!currentEl) return;

    state.isTransitioning = true;
    if (btnReplay) btnReplay.classList.add('is-spinning');

    currentEl.classList.remove('is-entering', 'enter-next', 'enter-prev', 'is-exiting', 'exit-next', 'exit-prev');
    void currentEl.offsetWidth; // Forzar reflujo de renderizado
    currentEl.classList.add('is-entering', 'enter-next');

    const fxName = state.slideTitles[state.currentSlide - 1]?.fx || 'Efecto';
    showToast(`✨ Reproduciendo animación original: ${fxName}`);

    setTimeout(() => {
      currentEl.classList.remove('is-entering', 'enter-next');
      if (btnReplay) btnReplay.classList.remove('is-spinning');
      state.isTransitioning = false;
    }, 500);
  }

  // Navegación Siguiente / Anterior
  function nextSlide() {
    if (state.currentSlide < state.totalSlides) {
      goToSlide(state.currentSlide + 1);
    }
  }

  function prevSlide() {
    if (state.currentSlide > 1) {
      goToSlide(state.currentSlide - 1);
    }
  }

  // Control del Drawer
  function toggleDrawer(forceState) {
    state.isDrawerOpen = typeof forceState === 'boolean' ? forceState : !state.isDrawerOpen;
    slideGridDrawer.classList.toggle('open', state.isDrawerOpen);
  }

  // Control de Pantalla Completa Multi-navegador y Fallback CSS
  function getFullscreenElement() {
    return document.fullscreenElement ||
           document.webkitFullscreenElement ||
           document.mozFullScreenElement ||
           document.msFullscreenElement ||
           null;
  }

  function updateFullscreenUI(isActive) {
    state.isFullscreen = isActive;
    document.body.classList.toggle('is-fullscreen', isActive);
    if (btnFullscreen) {
      if (isActive) {
        btnFullscreen.innerHTML = `
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M8 3v3a2 2 0 0 1-2 2H3m18 0h-3a2 2 0 0 1-2-2V3m0 18v-3a2 2 0 0 1 2-2h3M3 16h3a2 2 0 0 1 2 2v3"></path></svg>
          <span class="btn-label">Salir</span>
          <span class="key-shortcut">[F]</span>
        `;
        btnFullscreen.setAttribute('title', 'Salir de pantalla completa [F o Esc]');
      } else {
        btnFullscreen.innerHTML = `
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M8 3H5a2 2 0 0 0-2 2v3m18 0V5a2 2 0 0 0-2-2h-3m0 18h3a2 2 0 0 0 2-2v-3M3 16v3a2 2 0 0 0 2 2h3"></path></svg>
          <span class="btn-label">Pantalla Completa</span>
          <span class="key-shortcut">[F]</span>
        `;
        btnFullscreen.setAttribute('title', 'Alternar pantalla completa [F]');
      }
    }
  }

  function toggleFullscreen() {
    const docEl = document.documentElement;
    const currentFs = getFullscreenElement();
    const isCssFs = document.body.classList.contains('is-fullscreen');

    if (!currentFs && !isCssFs) {
      const rfs = docEl.requestFullscreen ||
                  docEl.webkitRequestFullscreen ||
                  docEl.mozRequestFullScreen ||
                  docEl.msRequestFullscreen;

      if (rfs) {
        try {
          const promise = rfs.call(docEl);
          if (promise && promise.then) {
            promise.then(() => {
              updateFullscreenUI(true);
              showToast('Pantalla completa activada [F o Esc para salir]');
            }).catch((err) => {
              console.warn('Fallback a modo pantalla completa CSS:', err);
              updateFullscreenUI(true);
              showToast('Modo presentación maximizado activo [F para salir]');
            });
          } else {
            updateFullscreenUI(true);
            showToast('Pantalla completa activada [F o Esc para salir]');
          }
        } catch (err) {
          updateFullscreenUI(true);
          showToast('Modo presentación maximizado activo [F para salir]');
        }
      } else {
        updateFullscreenUI(true);
        showToast('Modo presentación maximizado activo [F para salir]');
      }
    } else {
      const efs = document.exitFullscreen ||
                  document.webkitExitFullscreen ||
                  document.mozCancelFullScreen ||
                  document.msExitFullscreen;

      if (currentFs && efs) {
        try {
          const promise = efs.call(document);
          if (promise && promise.catch) {
            promise.catch((err) => {
              console.warn('Error al salir de fullscreen:', err);
            });
          }
        } catch (err) {
          console.warn('Error al invocar exitFullscreen:', err);
        }
      }
      updateFullscreenUI(false);
      showToast('Pantalla completa desactivada');
    }
  }

  // Sincronizar eventos nativos de fullscreen
  ['fullscreenchange', 'webkitfullscreenchange', 'mozfullscreenchange', 'MSFullscreenChange'].forEach(evt => {
    document.addEventListener(evt, () => {
      const isFs = !!getFullscreenElement();
      updateFullscreenUI(isFs);
    });
  });

  // Control de Toast
  let toastTimeout;
  function showToast(message) {
    toastMessage.textContent = message;
    toastNotification.classList.add('show');
    clearTimeout(toastTimeout);
    toastTimeout = setTimeout(() => {
      toastNotification.classList.remove('show');
    }, 2800);
  }

  // Copiado de bloques de código
  document.querySelectorAll('.btn-copy').forEach(btn => {
    btn.addEventListener('click', (e) => {
      const targetId = btn.getAttribute('data-target');
      const targetEl = document.getElementById(targetId);
      if (targetEl) {
        const textToCopy = targetEl.innerText;
        navigator.clipboard.writeText(textToCopy).then(() => {
          showToast('Código copiado al portapapeles');
          const originalText = btn.textContent;
          btn.textContent = '¡Copiado!';
          btn.style.color = '#34d399';
          setTimeout(() => {
            btn.textContent = originalText;
            btn.style.color = '';
          }, 2000);
        }).catch(() => {
          showToast('Error al acceder al portapapeles');
        });
      }
    });
  });

  // Toggle Menú de Descargas
  btnDownloadMenu.addEventListener('click', (e) => {
    e.stopPropagation();
    downloadsDropdown.classList.toggle('show');
  });

  document.addEventListener('click', (e) => {
    if (!downloadsDropdown.contains(e.target) && e.target !== btnDownloadMenu) {
      downloadsDropdown.classList.remove('show');
    }
  });

  // Listeners de Botones de Navegación
  btnNext.addEventListener('click', nextSlide);
  btnPrev.addEventListener('click', prevSlide);
  btnGrid.addEventListener('click', () => toggleDrawer());
  btnCloseDrawer.addEventListener('click', () => toggleDrawer(false));
  btnFullscreen.addEventListener('click', toggleFullscreen);
  if (btnThemeToggle) {
    btnThemeToggle.addEventListener('click', toggleTheme);
  }
  if (btnReplay) {
    btnReplay.addEventListener('click', replayCurrentAnimation);
  }

  // Atajos de Teclado Profesionales
  document.addEventListener('keydown', (e) => {
    // Si el usuario está escribiendo en algún input (si hubiera), ignorar
    if (['INPUT', 'TEXTAREA'].includes(e.target.tagName)) return;

    switch (e.key) {
      case 'ArrowRight':
      case 'PageDown':
      case 'n':
      case 'N':
      case ' ':
        e.preventDefault();
        nextSlide();
        break;

      case 'ArrowLeft':
      case 'PageUp':
      case 'p':
      case 'P':
      case 'k':
      case 'K':
        e.preventDefault();
        prevSlide();
        break;

      case 'f':
      case 'F':
        e.preventDefault();
        toggleFullscreen();
        break;

      case 'g':
      case 'G':
        e.preventDefault();
        toggleDrawer();
        break;

      case 'Escape':
        if (state.isFullscreen || document.body.classList.contains('is-fullscreen')) {
          toggleFullscreen();
        }
        if (state.isDrawerOpen) {
          toggleDrawer(false);
        }
        if (downloadsDropdown.classList.contains('show')) {
          downloadsDropdown.classList.remove('show');
        }
        break;

      case 'ArrowDown':
        e.preventDefault();
        const activeDown = document.querySelector('.slide.active');
        if (activeDown) activeDown.scrollTop += 80;
        break;

      case 'ArrowUp':
        e.preventDefault();
        const activeUp = document.querySelector('.slide.active');
        if (activeUp) activeUp.scrollTop -= 80;
        break;

      case 'r':
      case 'R':
        e.preventDefault();
        replayCurrentAnimation();
        break;

      case 't':
      case 'T':
        e.preventDefault();
        toggleTheme();
        break;

      case '1': case '2': case '3': case '4':
      case '5': case '6': case '7': case '8':
        goToSlide(parseInt(e.key, 10));
        break;
    }
  });

  // Soporte de rueda de ratón para desplazamiento vertical en la diapositiva activa
  const stage = document.getElementById('presentationStage');
  stage.addEventListener('wheel', (e) => {
    const activeSlide = document.querySelector('.slide.active');
    if (activeSlide) {
      if (Math.abs(e.deltaY) > Math.abs(e.deltaX)) {
        activeSlide.scrollTop += e.deltaY;
      }
    }
  }, { passive: true });

  // Soporte de gestos táctiles (Swipe en móviles/tablets)
  let touchStartX = 0;
  let touchEndX = 0;

  stage.addEventListener('touchstart', (e) => {
    touchStartX = e.changedTouches[0].screenX;
  }, { passive: true });

  stage.addEventListener('touchend', (e) => {
    touchEndX = e.changedTouches[0].screenX;
    handleGesture();
  }, { passive: true });

  function handleGesture() {
    const swipeThreshold = 50;
    if (touchEndX < touchStartX - swipeThreshold) {
      nextSlide(); // Swipe izquierda -> siguiente
    }
    if (touchEndX > touchStartX + swipeThreshold) {
      prevSlide(); // Swipe derecha -> anterior
    }
  }

  // Inicializar componentes
  initDots();
  initDrawer();
  const initialTheme = localStorage.getItem('presentation-theme') || 'light';
  applyTheme(initialTheme);
  goToSlide(1);
});
