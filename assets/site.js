{
const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
const fine = matchMedia('(pointer: fine)').matches;
const $ = (s, r = document) => r.querySelector(s);
const $$ = (s, r = document) => Array.from(r.querySelectorAll(s));
const play = v => { v.muted = true; const p = v.play(); if (p && p.catch) p.catch(() => {}); };

// header
const top = $('.top');
const onScroll = () => top.classList.toggle('solid', scrollY > 40);
addEventListener('scroll', onScroll, { passive: true }); onScroll();
const menu = $('.menu');
if (menu) menu.addEventListener('click', () => {
  const open = top.classList.toggle('open');
  menu.setAttribute('aria-expanded', open); menu.textContent = open ? 'Close' : 'Menu';
});

// broken remote thumbs fall back to a local frame
$$('img[data-fb]').forEach(i => i.addEventListener('error', () => { if (i.dataset.fb && i.src.indexOf(i.dataset.fb) < 0) i.src = i.dataset.fb; }, { once: false }));

requestAnimationFrame(() => requestAnimationFrame(() => document.body.classList.add('loaded')));
// hero reel
const reel = $('.reel');
if (reel) {
  requestAnimationFrame(() => document.body.classList.add('loaded'));
  const slides = $$('.slide', reel), dots = $$('.dots button', reel), now = $('.now', reel);
  let i = 0, timer;
  const go = n => {
    slides[i].classList.remove('on'); const v0 = $('video', slides[i]); if (v0) v0.pause();
    i = (n + slides.length) % slides.length;
    slides[i].classList.add('on'); const v = $('video', slides[i]); if (v) play(v);
    dots.forEach((d, k) => d.setAttribute('aria-current', k === i));
    const s = slides[i].dataset;
    now.innerHTML = `<a href="${s.href}"><span class="q small">${s.client}</span><b>${s.title}</b><span class="small">${s.href.indexOf("work/")>-1?"View the case":"Read the story"}</span></a>`;
  };
  const run = () => { clearInterval(timer); if (!reduce) timer = setInterval(() => go(i + 1), 6500); };
  dots.forEach((d, k) => d.addEventListener('click', () => { go(k); run(); }));
  go(0); run();
  document.addEventListener('visibilitychange', () => document.hidden ? clearInterval(timer) : run());
}

// work list peek
const peek = $('.peek');
if (peek && fine) {
  let x = 0, y = 0, px = 0, py = 0, raf;
  const loop = () => { px += (x - px) * .18; py += (y - py) * .18; peek.style.left = px + 'px'; peek.style.top = py + 'px'; raf = requestAnimationFrame(loop); };
  $$('.list .row').forEach(r => {
    r.addEventListener('mouseenter', e => {
      const t = $('.thumb', r); if (!t) return;
      peek.innerHTML = t.innerHTML; x = px = e.clientX; y = py = e.clientY;
      peek.classList.add('on'); cancelAnimationFrame(raf); if (!reduce) loop(); else { peek.style.left = x + 'px'; peek.style.top = y + 'px'; }
    });
    r.addEventListener('mousemove', e => { x = e.clientX; y = e.clientY; if (reduce) { peek.style.left = x + 'px'; peek.style.top = y + 'px'; } });
    r.addEventListener('mouseleave', () => { peek.classList.remove('on'); cancelAnimationFrame(raf); });
  });
}

// filter
const filter = $('.filter');
if (filter) {
  const btns = $$('button', filter), rows = $$('.list .row');
  const set = k => {
    btns.forEach(b => b.setAttribute('aria-pressed', b.dataset.k === k));
    rows.forEach(r => r.hidden = !(k === 'all' || r.dataset.k === k));
    try { localStorage.setItem('wolve-filter', k); } catch (e) {}
  };
  btns.forEach(b => b.addEventListener('click', () => set(b.dataset.k)));
  let saved = 'all'; try { saved = localStorage.getItem('wolve-filter') || 'all'; } catch (e) {}
  set(btns.some(b => b.dataset.k === saved) ? saved : 'all');
}

// youtube: inline on cases, modal in the archive
const ytSrc = id => `https://www.youtube-nocookie.com/embed/${id}?autoplay=1&rel=0&modestbranding=1&playsinline=1`;
$$('[data-inline]').forEach(b => b.addEventListener('click', () => {
  b.parentNode.innerHTML = `<iframe src="${ytSrc(b.dataset.inline)}" title="Film" allow="autoplay; encrypted-media; fullscreen" allowfullscreen></iframe>`;
}));
const dlg = $('#dlg'), dbody = $('#dbody');
const openD = html => { dbody.innerHTML = html; dlg.showModal(); $$('video', dbody).forEach(play); };
if (dlg) {
  dlg.addEventListener('close', () => { dbody.innerHTML = ''; });
  dlg.addEventListener('click', e => { if (e.target === dlg) dlg.close(); });
  $('#dx').addEventListener('click', () => dlg.close());
}
$$('[data-yt]').forEach(b => b.addEventListener('click', () =>
  openD(`<div class="yt"><iframe src="${ytSrc(b.dataset.yt)}" title="${b.dataset.title || 'Film'}" allow="autoplay; encrypted-media; fullscreen" allowfullscreen></iframe></div>`)));

// frames
const wall = $('.wall');
if (wall) {
  const dbtn = $$('.density button');
  const setD = d => { wall.dataset.d = d; dbtn.forEach(b => b.setAttribute('aria-pressed', b.dataset.d === d)); try { localStorage.setItem('wolve-density', d); } catch (e) {} };
  dbtn.forEach(b => b.addEventListener('click', () => setD(b.dataset.d)));
  let d = 'm'; try { d = localStorage.getItem('wolve-density') || 'm'; } catch (e) {}
  setD(d);
  $$('button', wall).forEach(b => b.addEventListener('click', () => {
    const v = $('video', b), img = $('img', b);
    const media = v ? `<video src="${v.getAttribute('src')}" muted loop playsinline autoplay></video>` : `<img src="${img.currentSrc || img.src}" alt="${img.alt}">`;
    const link = b.dataset.case ? `<a href="${b.dataset.case}">See the case</a>` : '';
    openD(`<div class="lb">${media}<div class="bar"><span>${b.dataset.cap}</span>${link}</div></div>`);
  }));
  if (fine) $$('video', wall).forEach(v => { const b = v.closest('button'); b.addEventListener('mouseenter', () => play(v)); b.addEventListener('mouseleave', () => v.pause()); });
}

// autoplay loops that are meant to run, only while visible
const io = 'IntersectionObserver' in window ? new IntersectionObserver(es => es.forEach(e => e.isIntersecting ? play(e.target) : e.target.pause()), { threshold: .2 }) : null;
$$('video[data-auto]').forEach(v => { if (reduce) return; io ? io.observe(v) : play(v); });
}
