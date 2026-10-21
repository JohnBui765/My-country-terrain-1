// Vietnam 63 offline cache. Change VERSION after editing any file so phones pick up the new copy.
const VERSION = 'vn63-v9';
const ASSETS = [
  "./",
  "./index.html",
  "./manifest.webmanifest",
  "./icon-192.png",
  "./icon-512.png",
  "./maskable-512.png",
  "./apple-touch-icon.png",
  "./favicon-32.png",
  "./be-vietnam-pro-vietnamese-400-normal.woff2",
  "./be-vietnam-pro-latin-400-normal.woff2",
  "./be-vietnam-pro-vietnamese-600-normal.woff2",
  "./be-vietnam-pro-latin-600-normal.woff2",
  "./be-vietnam-pro-vietnamese-700-normal.woff2",
  "./be-vietnam-pro-latin-700-normal.woff2",
  "./be-vietnam-pro-vietnamese-400-italic.woff2",
  "./be-vietnam-pro-latin-400-italic.woff2"
];

self.addEventListener('install', event => {
  // cache: 'reload' skips the browser's HTTP cache, so a new version never stores the old files.
  // The page itself must be cached; a missing icon or font must not block an update.
  event.waitUntil(caches.open(VERSION)
    .then(cache => Promise.all(ASSETS.map((url, i) => cache.add(new Request(url, { cache: 'reload' })).catch(err => { if (i < 2) throw err; }))))
    .then(() => self.skipWaiting()));
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys()
      .then(keys => Promise.all(keys.filter(k => k.startsWith('vn63-') && k !== VERSION).map(k => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', event => {
  const req = event.request;
  if (req.method !== 'GET' || new URL(req.url).origin !== self.location.origin) return;
  // The app page itself: network first, so going online always shows the latest version;
  // without a connection the saved copy opens instead.
  if (req.mode === 'navigate') {
    event.respondWith(fetch(req, { cache: 'no-cache' }).then(res => {
      if (res.ok) { const copy = res.clone(); caches.open(VERSION).then(c => c.put('./index.html', copy)); }
      return res;
    }).catch(() => caches.match('./index.html')));
    return;
  }
  event.respondWith(
    caches.match(req, { ignoreSearch: true }).then(hit => hit || fetch(req).then(res => {
      if (res.ok) { const copy = res.clone(); caches.open(VERSION).then(c => c.put(req, copy)); }
      return res;
    }).catch(() => (req.mode === 'navigate' ? caches.match('./index.html') : undefined)))
  );
});
