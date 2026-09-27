(function () {
  const nav = document.querySelector("[data-nav]");
  const toggle = document.querySelector(".nav-toggle");
  const menu = document.getElementById("nav-menu");
  const reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function onScroll() {
    if (nav) nav.classList.toggle("is-scrolled", window.scrollY > 8);
    applyParallax();
  }

  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  if (toggle && menu) {
    toggle.addEventListener("click", () => {
      const open = toggle.getAttribute("aria-expanded") === "true";
      toggle.setAttribute("aria-expanded", String(!open));
      menu.classList.toggle("is-open", !open);
    });
    menu.querySelectorAll("a").forEach((link) => {
      link.addEventListener("click", () => {
        toggle.setAttribute("aria-expanded", "false");
        menu.classList.remove("is-open");
      });
    });
  }

  const reveals = document.querySelectorAll(".reveal");
  if (reveals.length && !reduced) {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            observer.unobserve(entry.target);
          }
        });
      },
      { rootMargin: "0px 0px -8% 0px", threshold: 0.1 }
    );
    reveals.forEach((el) => observer.observe(el));
  } else {
    reveals.forEach((el) => el.classList.add("is-visible"));
  }

  function animateCounter(el) {
    const target = parseInt(el.dataset.count, 10);
    if (Number.isNaN(target)) return;
    const duration = 1600;
    const start = performance.now();
    function frame(now) {
      const t = Math.min((now - start) / duration, 1);
      const eased = 1 - Math.pow(1 - t, 4);
      el.textContent = Math.round(target * eased);
      if (t < 1) requestAnimationFrame(frame);
    }
    requestAnimationFrame(frame);
  }

  const counters = document.querySelectorAll("[data-count]");
  if (counters.length && !reduced) {
    const counterObserver = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            animateCounter(entry.target);
            counterObserver.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.5 }
    );
    counters.forEach((el) => counterObserver.observe(el));
  } else {
    counters.forEach((el) => {
      el.textContent = el.dataset.count;
    });
  }

  const flashes = document.querySelectorAll(".flash-stack .flash");
  if (flashes.length) {
    setTimeout(() => {
      const stack = document.querySelector(".flash-stack");
      if (stack) {
        stack.style.transition = "opacity 0.4s";
        stack.style.opacity = "0";
        setTimeout(() => stack.remove(), 400);
      }
    }, 5000);
  }

  const hero = document.querySelector(".hero");
  const showcase = document.querySelector(".showcase-device");
  if (hero && showcase && !reduced) {
    hero.addEventListener("mousemove", (e) => {
      const rect = hero.getBoundingClientRect();
      const x = (e.clientX - rect.left - rect.width / 2) / rect.width;
      const y = (e.clientY - rect.top - rect.height / 2) / rect.height;
      showcase.style.transform = `rotateY(${-12 + x * 6}deg) rotateX(${8 + y * -4}deg) translateZ(0)`;
    });
    hero.addEventListener("mouseleave", () => {
      showcase.style.transform = "";
    });
  }

  function applyParallax() {
    if (reduced) return;
    const scrolled = window.scrollY;
    const gradients = document.querySelectorAll(".hero-gradient");
    gradients.forEach((g, i) => {
      const speed = (i + 1) * 0.08;
      g.style.transform = `translateY(${scrolled * speed}px)`;
    });
    const showcaseEl = document.querySelector(".showcase-device");
    if (showcaseEl && scrolled < window.innerHeight) {
      showcaseEl.style.setProperty("--parallax-y", `${scrolled * 0.15}px`);
    }
    const blobs = document.querySelectorAll(".blob");
    const ctaSection = document.querySelector(".section-cta-final");
    if (ctaSection && blobs.length) {
      const ctaRect = ctaSection.getBoundingClientRect();
      if (ctaRect.top < window.innerHeight && ctaRect.bottom > 0) {
        const progress = 1 - ctaRect.top / window.innerHeight;
        blobs.forEach((b, i) => {
          const speed = (i + 1) * 30;
          b.style.transform = `translateY(${(progress - 0.5) * -speed}px)`;
        });
      }
    }
  }

  const marquee = document.querySelector(".marquee-track");
  if (marquee && !reduced) {
    const chips = marquee.parentElement;
    chips.addEventListener("mouseenter", () => {
      marquee.style.animationPlayState = "paused";
    });
    chips.addEventListener("mouseleave", () => {
      marquee.style.animationPlayState = "running";
    });
  }

  const buttons = document.querySelectorAll(".btn-primary, .btn-secondary, .btn-pill, .bento-cta");
  if (buttons.length && !reduced) {
    buttons.forEach((btn) => {
      if (getComputedStyle(btn).position === "static") {
        btn.style.position = "relative";
        btn.style.overflow = "hidden";
      }
      btn.addEventListener("mousemove", (e) => {
        const rect = btn.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        btn.style.setProperty("--mx", `${x}px`);
        btn.style.setProperty("--my", `${y}px`);
      });
    });
  }

  const bentoCards = document.querySelectorAll("[data-project]");
  if (bentoCards.length && !reduced && window.matchMedia("(min-width: 734px)").matches) {
    bentoCards.forEach((card) => {
      card.addEventListener("mousemove", (e) => {
        const rect = card.getBoundingClientRect();
        const x = (e.clientX - rect.left) / rect.width - 0.5;
        const y = (e.clientY - rect.top) / rect.height - 0.5;
        card.style.transform = `translateY(-4px) rotateX(${y * -4}deg) rotateY(${x * 4}deg)`;
        const visual = card.querySelector(".bento-visual");
        if (visual) {
          visual.style.transform = `translate(${-6 + x * -10}px, ${-6 + y * -10}px) scale(1.05)`;
        }
      });
      card.addEventListener("mouseleave", () => {
        card.style.transform = "";
        const visual = card.querySelector(".bento-visual");
        if (visual) visual.style.transform = "";
      });
    });
  }

  const smoothLinks = document.querySelectorAll('a[href^="#"]');
  smoothLinks.forEach((link) => {
    link.addEventListener("click", (e) => {
      const href = link.getAttribute("href");
      if (href.length <= 1) return;
      const target = document.querySelector(href);
      if (!target) return;
      e.preventDefault();
      const top = target.getBoundingClientRect().top + window.scrollY - 40;
      window.scrollTo({ top, behavior: reduced ? "auto" : "smooth" });
    });
  });

  const navHeight = 48;
  const sections = document.querySelectorAll("section[id]");
  const navAnchors = document.querySelectorAll('.nav-links a[href*="#"]');
  if (sections.length && navAnchors.length && !reduced) {
    const spyObserver = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            const id = entry.target.id;
            navAnchors.forEach((a) => {
              const href = a.getAttribute("href") || "";
              a.classList.toggle("active", href.includes(`#${id}`));
            });
          }
        });
      },
      { rootMargin: `-${navHeight + 100}px 0px -60% 0px`, threshold: 0 }
    );
    sections.forEach((s) => spyObserver.observe(s));
  }

  const codeWindow = document.querySelector(".code-window");
  if (codeWindow && !reduced) {
    const codeObserver = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            const lines = entry.target.querySelectorAll(".c-line");
            lines.forEach((line, i) => {
              line.style.opacity = "0";
              line.style.transform = "translateX(-8px)";
              setTimeout(() => {
                line.style.transition = "opacity 0.3s, transform 0.3s";
                line.style.opacity = "1";
                line.style.transform = "";
              }, i * 80 + 100);
            });
            codeObserver.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.4 }
    );
    codeObserver.observe(codeWindow);
  }
})();
