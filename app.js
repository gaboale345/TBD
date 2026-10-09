/**
 * LOGICA INTERACTIVA DE PRESENTACION DE HARDENING DE SGBD
 * Sistema de Diseño: Obsidian & Electric Sapphire
 */

document.addEventListener('DOMContentLoaded', () => {
  // Estado de la presentación
  const state = {
    currentSlide: 1,
    totalSlides: 8,
    isDrawerOpen: false,
    isFullscreen: false,
    slideTitles: [
      { num: '01', title: 'Objetivos y Alcance Estratégico', sub: 'Defensa en Profundidad & CIS Benchmark' },
      { num: '02', title: 'Superficie de Ataque & STRIDE', sub: 'Identificación de 4 vectores críticos' },
      { num: '03', title: 'Fase I: Kernel & SO Hardening', sub: 'sysctl.conf, permisos 0700 y Systemd' },
      { num: '04', title: 'Fase II: Criptografía en Tránsito', sub: 'TLS 1.3 forzado y ciphers ECDHE' },
      { num: '05', title: 'Fase III: Autenticación & Red', sub: 'SCRAM-SHA-256 y firewall pg_hba.conf' },
      { num: '06', title: 'Fase IV: Control de Acceso RBAC', sub: 'Revocación de public y roles mínimos' },
      { num: '07', title: 'Fase V: Auditoría Forense pgaudit', sub: 'Trazabilidad DDL/Roles y envío SIEM' },
      { num: '08', title: 'Resultados CIS y Conclusiones', sub: 'Cumplimiento 98.4% y DevSecOps' }
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
  const btnDownloadMenu = document.getElementById('btnDownloadMenu');
  const downloadsDropdown = document.getElementById('downloadsDropdown');
  const toastNotification = document.getElementById('toastNotification');
  const toastMessage = document.getElementById('toastMessage');

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

  // Función de Cambio de Diapositiva
  function goToSlide(targetSlide) {
    if (targetSlide < 1 || targetSlide > state.totalSlides) return;

    // Desactivar diapositiva actual
    const currentEl = document.querySelector(`.slide[data-index="${state.currentSlide}"]`);
    if (currentEl) {
      currentEl.classList.remove('active');
    }

    // Activar nueva diapositiva
    state.currentSlide = targetSlide;
    const nextEl = document.querySelector(`.slide[data-index="${state.currentSlide}"]`);
    if (nextEl) {
      nextEl.classList.add('active');
      nextEl.scrollTop = 0;
    }

    // Actualizar UI (Contador, Barra de Progreso, Dots)
    currentSlideNum.textContent = String(state.currentSlide).padStart(2, '0');
    const percent = (state.currentSlide / state.totalSlides) * 100;
    progressFill.style.width = `${percent}%`;

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
  goToSlide(1);
});
