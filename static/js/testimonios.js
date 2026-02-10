(function(){
  const slider = document.querySelector('[data-slider="testi"]');
  if(!slider) return;

  const track = slider.querySelector('.testi-track');
  const slides = Array.from(slider.querySelectorAll('.testi-slide'));
  const btnPrev = slider.querySelector('[data-prev]');
  const btnNext = slider.querySelector('[data-next]');
  const dotsWrap = slider.querySelector('[data-dots]');

  let index = 0;

  // ===== AUTOPLAY =====
  let autoplay = true;
  let interval = null;
  const DELAY = 2000; // 8 segundos

  function stopAutoplay(){
    if(interval){
      clearInterval(interval);
      interval = null;
    }
  }

  function startAutoplay(){
    if(!autoplay || slides.length <= 1) return;
    stopAutoplay();
    interval = setInterval(()=>{
      index = (index + 1) % slides.length; // loop
      update();
    }, DELAY);
  }
  // ====================

  // dots
  const dots = slides.map((_, i) => {
    const b = document.createElement('button');
    b.type = 'button';
    b.setAttribute('aria-label', `Ir al testimonio ${i+1}`);
    b.addEventListener('click', () => {
      stopAutoplay();
      goTo(i);
    });
    dotsWrap.appendChild(b);
    return b;
  });

  function update(){
    track.style.transform = `translateX(-${index * 100}%)`;
    dots.forEach((d,i)=> d.classList.toggle('is-active', i === index));

    // Si quieres que las flechas NO se deshabiliten por el loop, comenta estas 2 líneas:
    if(btnPrev){
      btnPrev.disabled = false;
      btnPrev.style.opacity = 1;
    }
    if(btnNext){
      btnNext.disabled = false;
      btnNext.style.opacity = 1;
    }
  }

  function goTo(i){
    index = ((i % slides.length) + slides.length) % slides.length; // loop seguro
    update();
  }

  if(btnPrev) btnPrev.addEventListener('click', ()=>{
    stopAutoplay();
    goTo(index - 1);
  });

  if(btnNext) btnNext.addEventListener('click', ()=>{
    stopAutoplay();
    goTo(index + 1);
  });

  // swipe móvil
  let startX = 0, isDown = false;
  slider.addEventListener('pointerdown', (e)=>{ isDown=true; startX=e.clientX; });

  slider.addEventListener('pointerup', (e)=>{
    if(!isDown) return;
    isDown=false;

    const dx = e.clientX - startX;
    if(Math.abs(dx) > 45){
      stopAutoplay();
      if(dx < 0) goTo(index + 1);
      else goTo(index - 1);
    }
  });

  // Pausa con hover (desktop)
  slider.addEventListener('mouseenter', stopAutoplay);
  slider.addEventListener('mouseleave', startAutoplay);

  update();
  startAutoplay();
})();