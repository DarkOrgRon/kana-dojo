// Service Worker: macht die App offline nutzbar.
// Strategie: HTML immer zuerst frisch aus dem Netz laden (Updates sofort sichtbar),
// nur bei fehlender Verbindung aus dem Cache. Übrige Dateien Cache-First.
const CACHE = 'kana-dojo-v5';
const CORE = ['./', './index.html', './manifest.json', './icon-192.png', './icon-512.png'];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(CORE)));
  self.skipWaiting();
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys().then(keys => Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k))))
  );
  self.clients.claim();
});

self.addEventListener('fetch', e => {
  if (e.request.method !== 'GET') return;

  // Seitenaufrufe: Netzwerk zuerst, Cache nur als Offline-Fallback
  if (e.request.mode === 'navigate') {
    e.respondWith(
      fetch(e.request).then(res => {
        const clone = res.clone();
        caches.open(CACHE).then(c => { c.put('./index.html', clone); });
        return res;
      }).catch(() => caches.match('./index.html'))
    );
    return;
  }

  // Übrige Dateien (Icons, Manifest, Fonts-Cache): Cache zuerst
  e.respondWith(
    caches.match(e.request).then(hit => {
      if (hit) return hit;
      return fetch(e.request).then(res => {
        if (res.ok && new URL(e.request.url).origin === location.origin) {
          const clone = res.clone();
          caches.open(CACHE).then(c => c.put(e.request, clone));
        }
        return res;
      }).catch(() => caches.match('./index.html'));
    })
  );
});
