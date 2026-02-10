(() => {
  const onReady = (fn) => {
    if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", fn);
    } else {
      fn();
    }
  };

  onReady(() => {
    /* =========================
       REVEAL ON SCROLL (ROBUSTO)
    ========================= */
    const revealEls = document.querySelectorAll(".reveal");

    const showAll = () => {
      revealEls.forEach(el => el.classList.add("is-visible"));
    };

    // Si no hay elementos, salimos
    if (!revealEls.length) {
      // seguimos igual con el form si existe
    } else if (!("IntersectionObserver" in window)) {
      // Fallback: si el navegador no soporta IO, mostramos todo
      showAll();
    } else {
      const io = new IntersectionObserver((entries) => {
        entries.forEach((e) => {
          if (e.isIntersecting) {
            e.target.classList.add("is-visible");
            // opcional: dejar de observar para rendimiento
            io.unobserve(e.target);
          }
        });
      }, {
        threshold: 0.12,
        // Compensa header sticky (evita que quede “oculto” al borde superior)
        rootMargin: "-80px 0px -10% 0px"
      });

      revealEls.forEach(el => io.observe(el));

      // Extra safety: si por alguna razón nada se activa en 800ms, mostramos todo
      setTimeout(() => {
        const anyVisible = Array.from(revealEls).some(el => el.classList.contains("is-visible"));
        if (!anyVisible) showAll();
      }, 800);
    }

    /* =========================
       FORM VALIDATION UI
    ========================= */
    const form = document.getElementById("contactForm");
    if (!form) return;

    const okBox = document.getElementById("formOk");
    const errBox = document.getElementById("formErr");
    const btnSend = document.getElementById("btnSend");

    const fields = Array.from(form.querySelectorAll("input, textarea"))
      .filter(el => el.name && el.type !== "hidden");

    const show = (box) => box && box.classList.add("is-show");
    const hide = (box) => box && box.classList.remove("is-show");

    const setState = (el, valid) => {
      const field = el.closest(".field");
      if (!field) return;
      field.classList.toggle("is-valid", valid);
      field.classList.toggle("is-invalid", !valid);
    };

    const validate = (el) => {
      const valid = el.checkValidity();
      setState(el, valid);
      return valid;
    };

    // validar mientras escribe
    fields.forEach(el => {
      el.addEventListener("input", () => validate(el));
      el.addEventListener("blur", () => validate(el));
    });

    form.addEventListener("submit", (e) => {
      hide(okBox);
      hide(errBox);

      const allValid = fields.map(validate).every(Boolean);

      if (!allValid) {
        e.preventDefault();
        show(errBox);

        const firstBad = fields.find(el => !el.checkValidity());
        if (firstBad) firstBad.focus();
        return;
      }

      // Si no hay botón, igual dejamos enviar
      if (!btnSend) return;

      // UI loading simple (para POST real)
      btnSend.disabled = true;
      btnSend.style.opacity = "0.85";
      btnSend.textContent = "Enviando…";

      // Si tu backend AÚN NO procesa, puedes usar demo:
      /*
      e.preventDefault();
      setTimeout(() => {
        show(okBox);
        form.reset();
        fields.forEach(el => {
          const f = el.closest(".field");
          if (f) f.classList.remove("is-valid", "is-invalid");
        });
        btnSend.disabled = false;
        btnSend.style.opacity = "1";
        btnSend.textContent = "Enviar mensaje";
      }, 650);
      */
    });
  });
})();
