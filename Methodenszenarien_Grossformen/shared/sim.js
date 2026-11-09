/* Gemeinsame Helfer: Theme-Schalter, Tabs, Timer, Speichern (nur lokal, optional) */
(function () {
  const root = document.documentElement;
  function store(k, v) { try { if (v === undefined) return localStorage.getItem(k); localStorage.setItem(k, v); } catch (e) { return null; } }
  const saved = store("mszen-theme");
  if (saved) root.setAttribute("data-theme", saved);

  window.Sim = {
    store,
    initTheme(btn) {
      if (!btn) return;
      const label = () => { btn.textContent = (root.getAttribute("data-theme") === "dark" || (!root.getAttribute("data-theme") && matchMedia("(prefers-color-scheme: dark)").matches)) ? "☀︎ Hell" : "☾ Dunkel"; };
      label();
      btn.addEventListener("click", () => {
        const dark = root.getAttribute("data-theme") === "dark" || (!root.getAttribute("data-theme") && matchMedia("(prefers-color-scheme: dark)").matches);
        root.setAttribute("data-theme", dark ? "light" : "dark");
        store("mszen-theme", dark ? "light" : "dark");
        label();
      });
    },
    initTabs(container, onChange) {
      const btns = [...container.querySelectorAll(".tabs button")];
      const panels = [...container.querySelectorAll(".panel")];
      function show(id) {
        btns.forEach(b => b.classList.toggle("on", b.dataset.tab === id));
        panels.forEach(p => p.classList.toggle("on", p.id === id));
        if (onChange) onChange(id);
      }
      btns.forEach(b => b.addEventListener("click", () => { show(b.dataset.tab); history.replaceState(null, "", "#" + b.dataset.tab); }));
      const h = location.hash.slice(1);
      show(btns.some(b => b.dataset.tab === h) ? h : btns[0].dataset.tab);
      return show;
    },
    /* Countdown-Timer: el zeigt mm:ss; gibt Steuerobjekt zurück */
    timer(el, seconds, onEnd) {
      let left = seconds, id = null;
      const fmt = s => { const a = Math.abs(s); return (s < 0 ? "−" : "") + String(Math.floor(a / 60)).padStart(1, "0") + ":" + String(a % 60).padStart(2, "0"); };
      const draw = () => { el.textContent = fmt(left); el.classList.toggle("over", left < 0); };
      draw();
      return {
        start() { if (id) return; id = setInterval(() => { left--; draw(); if (left === 0 && onEnd) onEnd(); }, 1000); },
        stop() { clearInterval(id); id = null; },
        reset(s) { this.stop(); left = s ?? seconds; draw(); },
        get running() { return !!id; }
      };
    },
    /* Pahl-Leiste: markiert erledigte Schritte */
    markStep(list, n) { [...list.children].forEach((li, i) => { if (i < n) li.classList.add("done"); }); }
  };
})();
