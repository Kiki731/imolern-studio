// Compare a built page against its mock-up, element by element.
//
// Run in the browser console (or a browser tool's JavaScript runner) on any page served from
// the same origin as both URLs, e.g. the built site with the mock-ups proxied, or two tabs on one server.
// Usage:
//   await compareLayouts('/design/mockups/03-pricing.html?still', '/pricing/?still', { width: 1440 })
// Returns { same, mockupCount, builtCount, diffs: [first 25 differences] }.
// Uses ?still so motion is at rest. Repeat at width 375 and in dark theme (opts.theme = 'dark').

async function compareLayouts(mockupUrl, builtUrl, opts = {}) {
  const width = opts.width || 1440;
  const height = opts.height || 900;
  const theme = opts.theme; // 'light' | 'dark' | undefined
  const root = opts.root || 'body';

  const load = url => new Promise((resolve, reject) => {
    const f = document.createElement('iframe');
    f.style.cssText = `position:fixed;left:-99999px;top:0;width:${width}px;height:${height}px;border:0`;
    f.onload = () => setTimeout(() => resolve(f), opts.settle || 1200);
    f.onerror = reject;
    f.src = url;
    document.body.appendChild(f);
  });

  const snapshot = f => {
    const d = f.contentDocument;
    if (theme) d.documentElement.dataset.theme = theme;
    const out = [];
    const walk = el => {
      const r = el.getBoundingClientRect();
      const cs = f.contentWindow.getComputedStyle(el);
      if (r.width > 0 && r.height > 0 && cs.visibility !== 'hidden' && cs.display !== 'none') {
        const text = el.children.length ? '' : (el.textContent || '').trim().slice(0, 40);
        out.push({
          tag: el.tagName.toLowerCase(),
          text,
          x: Math.round(r.left), y: Math.round(r.top + f.contentWindow.scrollY),
          w: Math.round(r.width), h: Math.round(r.height),
        });
      }
      for (const c of el.children) if (!['SCRIPT', 'STYLE', 'CANVAS'].includes(c.tagName)) walk(c);
    };
    walk(d.querySelector(root));
    return out;
  };

  const [a, b] = await Promise.all([load(mockupUrl), load(builtUrl)]);
  await new Promise(r => setTimeout(r, 300));
  const A = snapshot(a), B = snapshot(b);
  a.remove(); b.remove();

  const diffs = [];
  const n = Math.max(A.length, B.length);
  for (let i = 0; i < n && diffs.length < 25; i++) {
    const p = A[i], q = B[i];
    if (!p || !q || p.tag !== q.tag || p.x !== q.x || p.y !== q.y || p.w !== q.w || p.h !== q.h) {
      diffs.push({ i, mockup: p || null, built: q || null });
    }
  }
  return { same: diffs.length === 0 && A.length === B.length, mockupCount: A.length, builtCount: B.length, diffs };
}
