# -*- coding: utf-8 -*-
"""Güçlü Koltuk Yıkama — static site builder."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import rich_content as rc

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://www.antalyakoltukyikamaci.com.tr"
PHONE = "+905446304003"
PHONE_NICE = "+90 544 630 40 03"
EMAIL = "guclunur238@gmail.com"
GA = "AW-17270904841"

ICONS = {
    "wa": '<svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor" aria-hidden="true"><path d="M20 11.5A8.5 8.5 0 1 1 8.3 18.9L4 20l1.2-4.1A8.5 8.5 0 0 1 20 11.5zm-8.4 5.3c3 0 5.4-2.4 5.4-5.3s-2.4-5.3-5.4-5.3-5.4 2.4-5.4 5.3c0 1 .3 2 .8 2.8l-.5 1.9 2-.5a5.3 5.3 0 0 0 3.1.8zm3-4c.2-.1.3-.2.3-.4l-.7-2.3c-.1-.2-.3-.2-.5-.1l-1.2.6c-.2.1-.4 0-.5-.1-.7-.7-1.1-1.6-1.2-1.7-.1-.2 0-.3.1-.4l.6-.7c.1-.2.1-.4 0-.5L8.7 6c-.2-.3-.4-.3-.6-.2-1 .5-1.6 1.6-1.6 3 0 3.2 3.1 6.2 3.4 6.4.3.3 3.4 2.2 5.7 1.7.6-.1 1.4-.6 1.6-1.2.1-.3.1-.6 0-.8l-1.2-1.1c-.1-.2-.3-.2-.5-.1l-1 .5c-.2.1-.4 0-.5-.1-.3-.3-.7-.8-.8-1.1-.1-.2 0-.4.1-.5l.8-1z"/></svg>',
    "phone": '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M6.5 3.8h2.2l1.1 3-1.5 1.2a12 12 0 0 0 6.7 6.7l1.2-1.5 3 1.1v2.2A2 2 0 0 1 17.2 19 15.2 15.2 0 0 1 5 6.8a2 2 0 0 1 1.5-3z"/></svg>',
}


def svg_placeholder(path: Path, title: str, w=1600, h=900, c1="#8d6b4a", c2="#3a2c22"):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
  <defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/>
  </linearGradient></defs>
  <rect width="{w}" height="{h}" fill="url(#g)"/>
  <circle cx="{int(w*0.18)}" cy="{int(h*0.22)}" r="{int(h*0.18)}" fill="#fffbf5" fill-opacity=".08"/>
  <text x="50%" y="50%" text-anchor="middle" fill="#fffbf5" font-family="Georgia,serif" font-size="{int(h*0.055)}" opacity=".9">{title}</text>
  <text x="50%" y="{int(h*0.58)}" text-anchor="middle" fill="#ede4d4" font-family="sans-serif" font-size="{int(h*0.028)}" opacity=".8">Güçlü Koltuk Yıkama — fotoğrafı bu dosyanın yerine koyun</text>
</svg>''',
        encoding="utf-8",
    )


def head(title, desc, path, image, geo_name="Antalya", lat="36.8841", lng="30.7056", type_="website", extra=""):
    url = SITE + path
    img = SITE + image
    return f'''<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="author" content="Güçlü Koltuk Yıkama">
  <meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">
  <meta name="googlebot" content="index,follow">
  <meta name="theme-color" content="#c45c26">
  <meta name="color-scheme" content="light">
  <meta name="format-detection" content="telephone=yes">
  <meta name="geo.region" content="TR-07">
  <meta name="geo.placename" content="{geo_name}">
  <meta name="geo.position" content="{lat};{lng}">
  <meta name="ICBM" content="{lat}, {lng}">
  <meta name="language" content="Turkish">
  <meta name="revisit-after" content="7 days">
  <link rel="canonical" href="{url}">
  <link rel="alternate" hreflang="tr" href="{url}">
  <link rel="alternate" hreflang="x-default" href="{url}">
  <meta property="og:type" content="{type_}">
  <meta property="og:locale" content="tr_TR">
  <meta property="og:site_name" content="Güçlü Koltuk Yıkama">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{img}">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="Güçlü Koltuk Yıkama Antalya">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="{img}">
  <link rel="icon" href="assets/icons/favicon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="assets/images/logo.svg">
  <link rel="manifest" href="manifest.webmanifest">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,650&family=Nunito+Sans:wght@400;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/css/style.css">
  <script async src="https://www.googletagmanager.com/gtag/js?id={GA}"></script>
  <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','{GA}');</script>
  {extra}
</head>'''


def nav(current):
    links = [
        ("index.html", "Ana Sayfa"),
        ("hizmetlerimiz.html", "Hizmetler"),
        ("hakkimizda.html", "Hakkımızda"),
        ("blog.html", "Blog"),
        ("iletisim.html", "İletişim"),
    ]
    items = []
    for href, label in links:
        cur = ' aria-current="page"' if href == current else ""
        items.append(f'<a href="{href}"{cur}>{label}</a>')
    return f'''<a class="skip" href="#icerik">İçeriğe geç</a>
<header class="site-header">
  <div class="wrap nav">
    <a class="brand" href="index.html">
      <img src="assets/images/logo.svg" width="40" height="40" alt="Güçlü Koltuk Yıkama logo">
      <span class="brand-text"><strong>Güçlü Koltuk Yıkama</strong><span>Antalya • Kadın ekip</span></span>
    </a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-label="Menüyü aç"><span></span></button>
    <nav class="nav-links" aria-label="Ana menü">{''.join(items)}</nav>
    <a class="btn btn-whatsapp nav-cta" href="https://wa.me/905446304003" target="_blank" rel="noopener">{ICONS['wa']} WhatsApp</a>
  </div>
</header>'''


def footer():
    return f'''<footer class="footer">
  <div class="wrap grid grid-3">
    <div>
      <h3>Güçlü Koltuk Yıkama</h3>
      <p>2018’den beri Antalya’da yerinde koltuk, yatak ve sandalye yıkama. Kadın ekip, Karcher buharlı sistem ve doğal şampuan.</p>
      <div class="social">
        <a href="https://www.instagram.com/guclukoltuk/" target="_blank" rel="noopener" aria-label="Instagram">IG</a>
        <a href="https://wa.me/905446304003" target="_blank" rel="noopener" aria-label="WhatsApp">WA</a>
        <a href="https://www.youtube.com/@guclukoltuk" target="_blank" rel="noopener" aria-label="YouTube">YT</a>
      </div>
    </div>
    <div>
      <h3>Hizmet bölgeleri</h3>
      <ul>
        <li><a href="muratpasa-koltuk-yikama.html">Muratpaşa koltuk yıkama</a></li>
        <li><a href="konyaalti-koltuk-yikama.html">Konyaaltı koltuk yıkama</a></li>
        <li><a href="kepez-koltuk-yikama.html">Kepez koltuk yıkama</a></li>
        <li><a href="dosemealti-koltuk-yikama.html">Döşemealtı koltuk yıkama</a></li>
        <li><a href="kemer-koltuk-yikama.html">Kemer koltuk yıkama</a></li>
        <li><a href="aksu-koltuk-yikama.html">Aksu koltuk yıkama</a></li>
      </ul>
    </div>
    <div>
      <h3>İletişim</h3>
      <ul>
        <li><a href="tel:+905446304003">{PHONE_NICE}</a></li>
        <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li>Her gün 09:00–18:00</li>
        <li><a href="gizlilik-politikasi.html">Gizlilik politikası</a></li>
        <li><a href="kvkk.html">KVKK</a></li>
      </ul>
    </div>
  </div>
  <div class="wrap copy">© 2026 Güçlü Koltuk Yıkama Antalya. Tüm hakları saklıdır.</div>
</footer>
<a class="wa-fab" href="https://wa.me/905446304003" target="_blank" rel="noopener" aria-label="WhatsApp ile yazın">{ICONS['wa']}</a>
<div class="mobile-cta">
  <a class="btn btn-dark" href="tel:+905446304003">{ICONS['phone']} Ara</a>
  <a class="btn btn-whatsapp" href="https://wa.me/905446304003" target="_blank" rel="noopener">{ICONS['wa']} Fiyat al</a>
</div>
<script src="assets/js/main.js" defer></script>
</body></html>'''


def form(district=""):
    opts = "\n".join(
        f'<option>{x}</option>'
        for x in ["Koltuk yıkama", "Yatak yıkama", "Sandalye yıkama", "Araç koltuğu temizliği"]
    )
    hidden = f'<input type="hidden" name="district" value="{district}">' if district else ""
    district_field = ""
    if not district:
        district_field = '''<div class="field"><label for="district">Bölge</label>
        <select id="district" name="district" required>
          <option value="">İlçe seçiniz</option>
          <option>Muratpaşa</option><option>Konyaaltı</option><option>Kepez</option>
          <option>Döşemealtı</option><option>Kemer</option><option>Aksu</option>
        </select></div>'''
    return f'''<form class="contact-card" data-whatsapp novalidate>
  <h2>Hızlı fiyat teklifi</h2>
  <p class="lead">Form WhatsApp’a gider; 1 dakikada dönüş yaparız.</p>
  {hidden}
  <div class="field"><label for="name">Adınız</label><input id="name" name="name" required autocomplete="name"></div>
  <div class="field"><label for="phone">Telefon</label><input id="phone" name="phone" type="tel" required autocomplete="tel" placeholder="05xx xxx xx xx"></div>
  <div class="field"><label for="service">Hizmet</label><select id="service" name="service" required><option value="">Seçiniz</option>{opts}</select></div>
  {district_field}
  <div class="field"><label for="message">Notunuz</label><textarea id="message" name="message" rows="4" placeholder="Koltuk tipi, leke, mahalle..."></textarea></div>
  <button class="btn btn-whatsapp btn-full" type="submit">{ICONS['wa']} WhatsApp’tan gönder</button>
</form>'''


def local_schema(name, url, desc, lat, lng, locality, postal, extra=""):
    return f'''<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@graph": [
    {{
      "@type": ["LocalBusiness", "HouseCleaner"],
      "@id": "{SITE}/#business",
      "name": "{name}",
      "url": "{url}",
      "image": "{SITE}/assets/images/og-cover.svg",
      "telephone": "{PHONE}",
      "email": "{EMAIL}",
      "priceRange": "$$",
      "description": "{desc}",
      "address": {{
        "@type": "PostalAddress",
        "addressLocality": "{locality}",
        "addressRegion": "Antalya",
        "postalCode": "{postal}",
        "addressCountry": "TR"
      }},
      "geo": {{ "@type": "GeoCoordinates", "latitude": "{lat}", "longitude": "{lng}" }},
      "openingHoursSpecification": {{
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
        "opens": "09:00",
        "closes": "18:00"
      }},
      "areaServed": ["Antalya","Muratpaşa","Konyaaltı","Kepez","Döşemealtı","Kemer","Aksu"],
      "sameAs": [
        "https://www.instagram.com/guclukoltuk/",
        "https://www.youtube.com/@guclukoltuk"
      ],
      "founder": {{ "@type": "Person", "name": "Nurhayat Güçlü" }}
    }}{extra}
  ]
}}
</script>'''


def faq_schema(items):
    els = ",".join(
        json.dumps(
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}},
            ensure_ascii=False,
        )
        for q, a in items
    )
    return f''', {{
      "@type": "FAQPage",
      "mainEntity": [{els}]
    }}'''


def faqs(items):
    bits = []
    for q, a in items:
        bits.append(f"<details><summary>{q}</summary><p>{a}</p></details>")
    return '<div class="faq">' + "".join(bits) + "</div>"


def write(name, html):
    (ROOT / name).write_text(html, encoding="utf-8")


def make_placeholders():
    # Sadece eksik yer tutucuları yaz; mevcut SVG'leri ezme
    if (ROOT / "assets/images/hero/ana-sayfa.svg").exists():
        return
    svg_placeholder(ROOT / "assets/images/og-cover.svg", "Güçlü Koltuk Yıkama", 1200, 630, "#c45c26", "#2a2118")
    svg_placeholder(ROOT / "assets/images/hero/ana-sayfa.svg", "Yerinde koltuk yıkama", 1920, 1080)
    svg_placeholder(ROOT / "assets/images/hero/hakkimizda.svg", "Kadın ekibimiz", 1920, 900, "#6b8f71", "#2a2118")
    svg_placeholder(ROOT / "assets/images/hero/hizmetler.svg", "Hizmetlerimiz", 1920, 900)
    svg_placeholder(ROOT / "assets/images/hero/iletisim.svg", "Bize ulaşın", 1920, 900, "#7a5c3e", "#2a2118")
    svg_placeholder(ROOT / "assets/images/hero/blog.svg", "Blog", 1920, 900)
    svg_placeholder(ROOT / "assets/images/hero/kampanya.svg", "Kampanya", 1920, 900, "#c45c26", "#9a3f16")
    svg_placeholder(ROOT / "assets/images/hakkimizda-ekip.svg", "Ekip", 900, 1100, "#b08968", "#4a3728")
    for slug, title in [
        ("koltuk", "Koltuk yıkama"),
        ("yatak", "Yatak yıkama"),
        ("sandalye", "Sandalye yıkama"),
        ("arac", "Araç koltuğu"),
    ]:
        svg_placeholder(ROOT / f"assets/images/hizmetler/{slug}.svg", title, 1200, 800)
    for slug, title in [
        ("muratpasa", "Muratpaşa"),
        ("konyaalti", "Konyaaltı"),
        ("kepez", "Kepez"),
        ("dosemealti", "Döşemealtı"),
        ("kemer", "Kemer"),
        ("aksu", "Aksu"),
    ]:
        svg_placeholder(ROOT / f"assets/images/ilceler/{slug}.svg", title, 1600, 900)
    for slug, title in [
        ("koltuk", "Koltuk yazısı"),
        ("yatak", "Yatak yazısı"),
        ("sandalye", "Sandalye yazısı"),
        ("arac", "Araç yazısı"),
        ("hijyen", "Hijyen yazısı"),
    ]:
        svg_placeholder(ROOT / f"assets/images/blog/{slug}.svg", title, 1280, 720)


def page_index():
    faq = [
        ("Kadın ekip evde güvenli mi?", "Evet. Ekibimiz referanslı, deneyimli kadın personelden oluşur. Evde yalnız olan müşterilerimiz için bu özellikle tercih edilir."),
        ("Koltuklar evden çıkarılıyor mu?", "Hayır. Tüm yıkama evinizde, yerinde yapılır. Koltuklar taşınmaz, merdiven ve asansör derdi olmaz."),
        ("Kuruma süresi ne kadar?", "İşlem çoğu evde 1–2 saat sürer. Kuruma 4–6 saattir. Nemli günde biraz uzayabilir; bunu baştan söyleriz."),
        ("Ürünler bebek ve evcil hayvan için uygun mu?", "Doğal şampuan ve kontrollü buhar kullanırız. Çocuklu ve evcil hayvanlı evlere uygundur; ağır kimyasal koku bırakmayız."),
        ("Hangi ilçelere geliyorsunuz?", "Muratpaşa, Konyaaltı, Kepez, Döşemealtı, Kemer, Aksu ve Antalya merkez mahallelerine yerinde geliyoruz."),
        ("Fiyat nasıl belli olur?", "Takımın büyüklüğü, kumaş ve lekeye göre WhatsApp’tan konuşulur. Kapıda zam yapılmaz."),
        ("Aynı gün randevu olur mu?", "Mümkünse söyleriz. Değilse en yakın gerçekçi saati veririz; bekletmeyiz."),
    ]
    extra = local_schema(
        "Güçlü Koltuk Yıkama",
        SITE + "/",
        "Antalya genelinde yerinde koltuk, yatak ve sandalye yıkama. Kadın ekip, Karcher buharlı sistem, doğal şampuan.",
        "36.8841",
        "30.7056",
        "Antalya",
        "07040",
        faq_schema(faq)
        + ''', {
      "@type":"WebSite","url":"''' + SITE + '''/","name":"Güçlü Koltuk Yıkama","inLanguage":"tr-TR"
    }''',
    )
    html = head(
        "Antalya Koltuk Yıkama | Güçlü Koltuk Yıkama — Kadın Ekip",
        "Antalya’da yerinde koltuk, yatak ve sandalye yıkama. Kadın ekip, Karcher buharlı sistem ve doğal şampuan. Muratpaşa, Konyaaltı, Kepez, Döşemealtı, Kemer ve Aksu.",
        "/",
        "/assets/images/og-cover.svg",
        extra=extra,
    )
    html += f'''
<body>
{nav("index.html")}
<main id="icerik">
  <section class="hero" style="background-image:url('assets/images/hero/ana-sayfa.svg')">
    <div class="wrap hero-inner">
      <p class="kicker">2018’den beri Antalya • Kadın ekip</p>
      <h1>Evinizin kokusu, yeniden temiz.</h1>
      <p>Koltuk, yatak ve sandalye yıkamasını evinizde yapıyoruz. Kadın ekip, Karcher buhar, doğal şampuan. Taşıma yok, ağır kimyasal koku yok; dürüst fiyat ve acele etmeden biten bir iş var.</p>
      <div class="hero-actions">
        <a class="btn btn-whatsapp" href="https://wa.me/905446304003" target="_blank" rel="noopener">{ICONS['wa']} WhatsApp’tan fiyat al</a>
        <a class="btn btn-ghost" href="hizmetlerimiz.html">Hizmetleri gör</a>
      </div>
      <div class="hero-stats">
        <div><strong>7+ yıl</strong><span>saha tecrübesi</span></div>
        <div><strong>6 ilçe</strong><span>Antalya geneli</span></div>
        <div><strong>%100</strong><span>yerinde hizmet</span></div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap center">
      <p class="eyebrow">Neden biz</p>
      <h2>İnsan gibi temizlik: acele etmeden, evinize saygı duyarak.</h2>
      <p class="lead">Makine ve şampuan önemli. Ama asıl fark, evinize giren ekibin güveni ve işini bitirene kadar yanınızda durması.</p>
    </div>
    <div class="wrap grid grid-4" style="margin-top:1.5rem">
      <article class="trust"><h3>Kadın ekip</h3><p>Evde yalnızken de rahat olmanız için deneyimli kadın personel. Referanslı, sakin, işini bitirene kadar yanınızda.</p></article>
      <article class="trust"><h3>Doğal şampuan</h3><p>Bebekler ve evcil hayvanlar için uygun, kalıntı bırakmayan formüller. Ev “temizlikçi kokmasın” diye.</p></article>
      <article class="trust"><h3>Karcher buhar</h3><p>Alman ekipmanla derin leke, koku ve akarlara inilir. Kumaşı boğmadan, ölçülü nemle.</p></article>
      <article class="trust"><h3>Yerinde yıkama</h3><p>Koltuklarınız evinizde kalır. Merdiven yok, kamyon yok; aynı gün ferahlar.</p></article>
    </div>
  </section>
{rc.index_extra()}
  <section class="section section-alt">
    <div class="wrap">
      <p class="eyebrow">Hizmetler</p>
      <h2>Evinizde, kumaşına göre.</h2>
      <p class="lead">Dört hizmet aynı randevuda birleşebilir. WhatsApp’tan takımı yazmanız yeter.</p>
      <div class="grid grid-2" style="margin-top:1.2rem">
        <article class="card"><img src="assets/images/hizmetler/koltuk.svg" alt="Antalya koltuk yıkama" width="1200" height="800"><div class="card-body"><h3>Koltuk yıkama</h3><p>Kumaş, deri, nubuk, kadife. Leke ve koku giderilir, renk canlanır. Koltuklar taşınmaz.</p><a href="hizmetlerimiz.html#koltuk">Nasıl yıkıyoruz →</a></div></article>
        <article class="card"><img src="assets/images/hizmetler/yatak.svg" alt="Antalya yatak yıkama" width="1200" height="800"><div class="card-body"><h3>Yatak yıkama</h3><p>Akar ve neme karşı derin hijyen. Kontrollü kurutma; “oda kokusu” sandığınız şey çoğu zaman yataktır.</p><a href="hizmetlerimiz.html#yatak">Nasıl yıkıyoruz →</a></div></article>
        <article class="card"><img src="assets/images/hizmetler/sandalye.svg" alt="Antalya sandalye yıkama" width="1200" height="800"><div class="card-body"><h3>Sandalye yıkama</h3><p>Yemek lekesi kumaşa dik işler. Ev, ofis ve restoranda yerinde, hızlı uygulama.</p><a href="hizmetlerimiz.html#sandalye">Nasıl yıkıyoruz →</a></div></article>
        <article class="card"><img src="assets/images/hizmetler/arac.svg" alt="Antalya araç koltuğu temizliği" width="1200" height="800"><div class="card-body"><h3>Araç koltuğu</h3><p>Koku çoğu zaman klimadan değil, kumaşın içinden gelir. Vakum, buhar, ferah iç hacim.</p><a href="hizmetlerimiz.html#arac">Nasıl temizliyoruz →</a></div></article>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap center">
      <p class="eyebrow">Müşteriler</p>
      <h2>Kısa cümleler, gerçek evler.</h2>
    </div>
    <div class="wrap grid grid-3" style="margin-top:1.2rem">
      <blockquote class="quote"><div class="stars">★★★★★</div><p>“Koltuklarım yepyeni oldu. Ekip acele etmeden, çok özenli çalıştı.”</p><cite>— Ayşe T., Muratpaşa</cite></blockquote>
      <blockquote class="quote"><div class="stars">★★★★★</div><p>“Yatak yıkama sonrası evin kokusu değişti. Sabah uyanmak başka oldu.”</p><cite>— Mehmet B., Kepez</cite></blockquote>
      <blockquote class="quote"><div class="stars">★★★★★</div><p>“Kadın ekip olması güven verdi. Fiyat da baştan netti, kapıda değişmedi.”</p><cite>— Derya S., Konyaaltı</cite></blockquote>
    </div>
  </section>

  <section class="section section-alt">
    <div class="wrap">
      <p class="eyebrow">Bölgeler</p>
      <h2>Antalya’nın her noktasına.</h2>
      <p class="lead">İlçe sayfalarında mahalle mahalle anlattık. Kendi bölgenize tıklayın; tempo, nem ve ev tipi orada ayrı durur.</p>
      <div class="chips" style="margin:1rem 0 1.2rem">
        <a class="chip" href="muratpasa-koltuk-yikama.html">Muratpaşa</a>
        <a class="chip" href="konyaalti-koltuk-yikama.html">Konyaaltı</a>
        <a class="chip" href="kepez-koltuk-yikama.html">Kepez</a>
        <a class="chip" href="dosemealti-koltuk-yikama.html">Döşemealtı</a>
        <a class="chip" href="kemer-koltuk-yikama.html">Kemer</a>
        <a class="chip" href="aksu-koltuk-yikama.html">Aksu</a>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <p class="eyebrow">Sık sorulanlar</p>
      <h2>Net cevaplar.</h2>
      {faqs(faq)}
    </div>
  </section>

  <section class="section section-alt">
    <div class="wrap grid grid-2">
      <div class="contact-card">
        <h2>Güçlü Koltuk Yıkama</h2>
        <p>Antalya genelinde yerinde hizmet. Her gün 09:00–18:00. En hızlı yol WhatsApp; kısa bir not yeter.</p>
        <ul>
          <li>Telefon: <a href="tel:+905446304003">{PHONE_NICE}</a></li>
          <li>E-posta: <a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li>Instagram: <a href="https://www.instagram.com/guclukoltuk/" target="_blank" rel="noopener">@guclukoltuk</a></li>
        </ul>
      </div>
      {form()}
    </div>
  </section>
</main>
{footer()}'''
    write("index.html", html)


DISTRICTS = [
    dict(
        file="muratpasa-koltuk-yikama.html",
        slug="muratpasa",
        name="Muratpaşa",
        title="Muratpaşa Koltuk Yıkama | Antalya — Güçlü Koltuk Yıkama",
        desc="Muratpaşa koltuk yıkama: Lara, Fener, Şirinyalı, Bahçelievler ve tüm mahallelerde yerinde kadın ekip, Karcher buhar ve doğal şampuan.",
        lat="36.8841",
        lng="30.7056",
        postal="07040",
        mahalle="Bahçelievler, Fener, Lara, Meltem, Kızıltoprak, Şirinyalı, Meydan, Çağlayan, Yüksekalan, Güzeloba, Memurevleri, Yeşilbahçe, Gebizli, Cumhuriyet, Konuksever",
        intro="Muratpaşa’da koltuk yıkama demek, Lara’dan Fener’e, Şirinyalı’dan Bahçelievler’e kadar apartman ve villa hayatının temposuna uymak demek. Ekibimiz aynı gün randevuda evinize gelir; koltuklar yerinden oynatılmaz.",
        extra_h="Kumaş ve leke türüne göre temizlik",
        extra_p="Kadife, keten, mikrofiber, deri ve nubuk için ayrı yöntem kullanırız. Çay, kahve, meyve suyu ve evcil hayvan lekelerinde ön işlem uygularız.",
    ),
    dict(
        file="konyaalti-koltuk-yikama.html",
        slug="konyaalti",
        name="Konyaaltı",
        title="Konyaaltı Koltuk Yıkama | Antalya — Güçlü Koltuk Yıkama",
        desc="Konyaaltı koltuk yıkama: Liman, Hurma, Uncalı, Gürsu ve Altınkum’da yerinde koltuk ve yatak yıkama. Kadın ekip, doğal ürün.",
        lat="36.8622",
        lng="30.6372",
        postal="07070",
        mahalle="Gürsu, Liman, Hurma, Uncalı, Altınkum, Sarısu, Arapsuyu, Akkuyu, Kuşkavağı, Toros, Uluç, Bahtılı, Altıntaş",
        intro="Konyaaltı’nda deniz nemi kumaşa işler; koltuklarda koku ve leke daha inatçı olur. Buharlı sistem ve doğal şampuanla nem kokusunu kırar, kumaşı yormadan derin temizlik yaparız.",
        extra_h="Sahil evleri için koku kontrolü",
        extra_p="Liman, Hurma ve Uncalı hattında sık görülen nem kokusuna karşı vakum + buhar + doğal şampuan sırasını uygularız.",
    ),
    dict(
        file="kepez-koltuk-yikama.html",
        slug="kepez",
        name="Kepez",
        title="Kepez Koltuk Yıkama | Antalya — Güçlü Koltuk Yıkama",
        desc="Kepez koltuk yıkama: Varsak, Ahatlı, Şafak, Göksu ve tüm mahallelerde yerinde hijyenik koltuk ve yatak yıkama.",
        lat="36.9280",
        lng="30.7150",
        postal="07020",
        mahalle="Yeni Emek, Kültür, Ahatlı, Şafak, Gülveren, Duacı, Yeşiltepe, Altınova, Varsak, Habipler, Göksu, Karşıyaka, Kepezaltı",
        intro="Kepez’de aile evleri kalabalık kullanılır. Koltuk ve yatak yıkamada hedefimiz görünür leke değil; kumaşın içindeki toz, akar ve günlük yaşam kokusudur.",
        extra_h="Aile evlerine uygun plan",
        extra_p="Varsak ve Ahatlı başta olmak üzere randevuyu sizin saatlerinize göre kurarız. Çocuk ve evcil hayvan varken de çalışılabilir.",
    ),
    dict(
        file="dosemealti-koltuk-yikama.html",
        slug="dosemealti",
        name="Döşemealtı",
        title="Döşemealtı Koltuk Yıkama | Antalya — Güçlü Koltuk Yıkama",
        desc="Döşemealtı koltuk yıkama: Yeşilbayır, Bademağacı, Dağbeli ve villa bölgelerinde yerinde koltuk, yatak ve sandalye yıkama.",
        lat="37.0230",
        lng="30.6010",
        postal="07190",
        mahalle="Yeşilbayır, Bademağacı, Dağbeli, Yeniköy, Camili, Karaveliler, Killik, Ekşili, Ilıca, Çıplaklı, Yalınlı, Dereli, Çığlık, Kovanlık, Selimiye",
        intro="Döşemealtı’nda villa ve müstakil evlerde koltuk takımları daha büyük, kumaşlar daha çeşitli olur. Ekipmanımızı eve göre ayarlarız; bahçe ve girişe zarar vermeden çalışırız.",
        extra_h="Villa ve müstakil evler",
        extra_p="Büyük L koltuk, birden fazla yatak ve dış mekân kumaşları için süre ve kuruma planını baştan konuşuruz.",
    ),
    dict(
        file="kemer-koltuk-yikama.html",
        slug="kemer",
        name="Kemer",
        title="Kemer Koltuk Yıkama | Antalya — Güçlü Koltuk Yıkama",
        desc="Kemer koltuk yıkama: Beldibi, Göynük, Kiriş, Çamyuva, Tekirova. Ev, villa ve turizm işletmelerine yerinde hizmet.",
        lat="36.5978",
        lng="30.5606",
        postal="07980",
        mahalle="Kemer Merkez, Beldibi, Göynük, Kiriş, Çamyuva, Tekirova, Çıralı, Olympos",
        intro="Kemer’de hem yazlık ev hem pansiyon ve butik otel koltukları yıkıyoruz. Sezon öncesi hızlı randevu, koku kontrolü ve aynı gün kullanım planı sunuyoruz.",
        extra_h="Turizm ve villa çözümleri",
        extra_p="Toplu sandalye, berjer ve oda koltuklarında işletme takvimine göre çalışırız. Çıralı ve Tekirova dahil geliriz.",
    ),
    dict(
        file="aksu-koltuk-yikama.html",
        slug="aksu",
        name="Aksu",
        title="Aksu Koltuk Yıkama | Antalya — Güçlü Koltuk Yıkama",
        desc="Aksu koltuk yıkama: Kundu, Pınarlı, Çalkaya, Kemerağzı ve tüm mahallelerde yerinde koltuk ve yatak yıkama.",
        lat="36.9500",
        lng="30.8500",
        postal="07112",
        mahalle="Pınarlı, Güzelyurt, Kemerağzı, Altıntaş, Çalkaya, Topallı, Kundu, Macun, Çamköy, Hacıaliler, Solak, Yurtpınar, Boztepe",
        intro="Aksu ve Kundu hattında otel lojmanları, site daireleri ve müstakil evlere aynı standartta geliyoruz. Randevu WhatsApp’tan netleşir; fiyat önceden konuşulur.",
        extra_h="Kundu ve site yaşamı",
        extra_p="Site yönetmeliğine uygun giriş-çıkış, sessiz çalışma ve hızlı kuruma planı ile hizmet veririz.",
    ),
]


def page_district(d):
    faq = [
        (f"{d['name']} koltuk yıkama ne kadar sürer?", "Çoğu evde işlem 1–2 saat. Kuruma 4–6 saattir. Büyük L takım veya birkaç yatak varsa süreyi baştan konuşuruz."),
        ("Yıkama sonrası koku kalır mı?", "Ağır kimyasal koku bırakmayız. Doğal şampuanla ferah, temiz bir koku kalır. Nemli günde pencereyi aralamak kuruma ve kokuyu hızlandırır."),
        ("Koltuklar evde mi yıkanıyor?", "Evet, yerinde. Taşıma yoktur. Site asansörü veya villa girişi varsa WhatsApp’tan yazın, plana ekleriz."),
        (f"{d['name']} hangi mahallelere geliyorsunuz?", f"{d['mahalle']} ve çevre mahalleler. Listede yoksa da yazın; büyük ihtimalle geliyoruz."),
        ("Kadın ekip güvenli mi?", "Evet. Referanslı, deneyimli kadın personel evinizde çalışır. Evde yalnızsanız bunu özellikle belirtin."),
        ("Fiyat kapıda değişir mi?", "Hayır. Takım ve kumaşa göre WhatsApp’ta konuşulan fiyat kapıda değişmez."),
    ]
    extra = local_schema(
        f"Güçlü Koltuk Yıkama — {d['name']}",
        SITE + "/" + d["file"],
        d["desc"],
        d["lat"],
        d["lng"],
        d["name"],
        d["postal"],
        faq_schema(faq),
    )
    html = head(d["title"], d["desc"], "/" + d["file"], f"/assets/images/ilceler/{d['slug']}.svg", d["name"], d["lat"], d["lng"], extra=extra)
    html += f'''
<body>
{nav("")}
<main id="icerik">
  <section class="hero page-hero" style="background-image:url('assets/images/ilceler/{d['slug']}.svg')">
    <div class="wrap hero-inner">
      <nav class="breadcrumbs" aria-label="Yol tarifi"><a href="index.html">Ana sayfa</a> · {d['name']}</nav>
      <h1>{d['name']} koltuk yıkama</h1>
      <p>Yerinde, doğal, acele etmeden. Kadın ekip ile {d['name']}’nın mahallelerinde.</p>
      <div class="hero-actions">
        <a class="btn btn-whatsapp" href="https://wa.me/905446304003?text={d['name']}%20koltuk%20y%C4%B1kama%20fiyat%20almak%20istiyorum" target="_blank" rel="noopener">{ICONS['wa']} Ücretsiz bilgi al</a>
      </div>
    </div>
  </section>
{rc.district_body(d, faqs(faq), form(d['name']), rc.PROCESS, PHONE_NICE)}
</main>
{footer()}'''
    write(d["file"], html)


def page_about():
    extra = local_schema("Güçlü Koltuk Yıkama", SITE + "/hakkimizda.html", "2018’den beri Antalya’da kadın ekip ile koltuk yıkama.", "36.8841", "30.7056", "Antalya", "07040")
    html = head(
        "Hakkımızda | Güçlü Koltuk Yıkama Antalya — Kadın Ekip",
        "2018’den beri Antalya’da kadın ekip, Karcher ve doğal şampuanla yerinde koltuk ve yatak yıkama. Nurhayat Güçlü ve ekibinin hikâyesi.",
        "/hakkimizda.html",
        "/assets/images/hero/hakkimizda.svg",
        extra=extra,
    )
    html += f'''
<body>
{nav("hakkimizda.html")}
<main id="icerik">
  <section class="hero page-hero" style="background-image:url('assets/images/hero/hakkimizda.svg')">
    <div class="wrap hero-inner">
      <p class="kicker">Hikâyemiz</p>
      <h1>Temizlik bir makine işi değil, bir insan işi.</h1>
      <p>2018’den beri Antalya evlerinde, kadın ekiple, acele etmeden.</p>
    </div>
  </section>
{rc.about_body()}
</main>
{footer()}'''
    write("hakkimizda.html", html)


def page_services():
    extra = local_schema("Güçlü Koltuk Yıkama", SITE + "/hizmetlerimiz.html", "Koltuk, yatak, sandalye ve araç koltuğu temizliği.", "36.8841", "30.7056", "Antalya", "07040")
    html = head(
        "Hizmetlerimiz | Antalya Koltuk, Yatak ve Sandalye Yıkama",
        "Antalya’da koltuk yıkama, yatak yıkama, sandalye yıkama ve araç koltuğu temizliği. Kadın ekip, Karcher, doğal şampuan. Kumaşa göre yöntem.",
        "/hizmetlerimiz.html",
        "/assets/images/hero/hizmetler.svg",
        extra=extra,
    )
    html += f'''
<body>
{nav("hizmetlerimiz.html")}
<main id="icerik">
  <section class="hero page-hero" style="background-image:url('assets/images/hero/hizmetler.svg')">
    <div class="wrap hero-inner">
      <h1>Hizmetlerimiz</h1>
      <p>Antalya’da yerinde, hijyenik ve kumaşa saygılı temizlik. Aşağıda her işi ayrı ayrı anlattık.</p>
    </div>
  </section>
{rc.services_body()}
</main>
{footer()}'''
    write("hizmetlerimiz.html", html)


def page_contact():
    extra = local_schema("Güçlü Koltuk Yıkama", SITE + "/iletisim.html", "Antalya koltuk yıkama iletişim.", "36.8841", "30.7056", "Antalya", "07040")
    html = head(
        "İletişim | Antalya Koltuk Yıkama — Güçlü Koltuk Yıkama",
        "WhatsApp, telefon ve form ile Antalya koltuk yıkama fiyatı alın. Muratpaşa, Konyaaltı, Kepez, Döşemealtı, Kemer, Aksu.",
        "/iletisim.html",
        "/assets/images/hero/iletisim.svg",
        extra=extra,
    )
    html += f'''
<body>
{nav("iletisim.html")}
<main id="icerik">
  <section class="hero page-hero" style="background-image:url('assets/images/hero/iletisim.svg')">
    <div class="wrap hero-inner">
      <h1>Bize ulaşın</h1>
      <p>Kısa bir not yeter. Her gün 09:00–18:00, en hızlı dönüş WhatsApp.</p>
    </div>
  </section>
{rc.contact_body(form(), PHONE_NICE, EMAIL)}
</main>
{footer()}'''
    write("iletisim.html", html)


def page_blog():
    extra = '''<script type="application/ld+json">{"@context":"https://schema.org","@type":"Blog","name":"Güçlü Koltuk Yıkama Blog","url":"''' + SITE + '''/blog.html","inLanguage":"tr-TR"}</script>'''
    html = head(
        "Blog | Antalya Koltuk ve Yatak Yıkama Rehberi",
        "Koltuk, yatak, sandalye ve araç koltuğu temizliği hakkında sade, ayrıntılı yazılar. Antalya evlerinde gördüğümüz gerçekler.",
        "/blog.html",
        "/assets/images/hero/blog.svg",
        extra=extra,
    )
    html += f'''
<body>
{nav("blog.html")}
<main id="icerik">
  <section class="hero page-hero" style="background-image:url('assets/images/hero/blog.svg')">
    <div class="wrap hero-inner">
      <h1>Blog</h1>
      <p>Koltuk ve yatak hijyeni üzerine, satış vaadi olmadan, sade dilde.</p>
    </div>
  </section>
{rc.blog_body()}
</main>
{footer()}'''
    write("blog.html", html)


def page_kampanya():
    extra = local_schema("Güçlü Koltuk Yıkama", SITE + "/kampanya.html", "Antalya bayram ve sezon koltuk yıkama kampanyası.", "36.8841", "30.7056", "Antalya", "07040")
    html = head(
        "Kampanya | Antalya Koltuk ve Yatak Yıkama — Güçlü Koltuk Yıkama",
        "Antalya’da bayram, tatil ve taşınma öncesi yerinde koltuk ve yatak yıkama. Kadın ekip, doğal şampuan, net randevu.",
        "/kampanya.html",
        "/assets/images/hero/kampanya.svg",
        extra=extra,
    )
    html += f'''
<body>
{nav("")}
<main id="icerik">
  <section class="banner">
    <div class="wrap">
      <span class="badge">Sezon kampanyası</span>
      <h1>Misafir gelmeden ev ferahlasın.</h1>
      <p>Bayram, tatil veya taşınma öncesi koltuk ve yatak yıkama. En yakın randevu WhatsApp’tan.</p>
      <a class="btn btn-dark" href="https://wa.me/905446304003?text=Kampanya%20fiyat%20almak%20istiyorum" target="_blank" rel="noopener">{ICONS['wa']} Kampanya fiyatı al</a>
    </div>
  </section>
{rc.kampanya_body()}
</main>
{footer()}'''
    write("kampanya.html", html)

def page_legal():
    giz = head(
        "Gizlilik Politikası | Güçlü Koltuk Yıkama",
        "Güçlü Koltuk Yıkama gizlilik politikası. İletişim formu ve WhatsApp verilerinin kullanımı.",
        "/gizlilik-politikasi.html",
        "/assets/images/og-cover.svg",
    )
    giz += f'''
<body>
{nav("")}
<main id="icerik" class="section"><div class="wrap prose">
<h1>Gizlilik politikası</h1>
<p>Güçlü Koltuk Yıkama olarak form, telefon ve WhatsApp üzerinden ilettiğiniz ad, telefon ve adres bilgilerini yalnızca randevu ve fiyat teklifi için kullanırız. Üçüncü kişilerle pazarlama amacıyla paylaşmayız. Google Ads dönüşüm ölçümü için tarayıcı çerezleri kullanılabilir.</p>
<p>Haklarınız için: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
</div></main>
{footer()}'''
    write("gizlilik-politikasi.html", giz)

    kvkk = head(
        "KVKK Aydınlatma Metni | Güçlü Koltuk Yıkama",
        "6698 sayılı KVKK kapsamında Güçlü Koltuk Yıkama aydınlatma metni.",
        "/kvkk.html",
        "/assets/images/og-cover.svg",
    )
    kvkk += f'''
<body>
{nav("")}
<main id="icerik" class="section"><div class="wrap prose">
<h1>KVKK aydınlatma metni</h1>
<p>Veri sorumlusu: Güçlü Koltuk Yıkama, Antalya. Toplanan veriler: ad-soyad, telefon, mahalle/ilçe, hizmet talebi. Hukuki sebep: sözleşme öncesi görüşme ve meşru menfaat. Saklama: teklif sürecinin makul süresi. Talepleriniz için {EMAIL}.</p>
</div></main>
{footer()}'''
    write("kvkk.html", kvkk)

    n404 = head("Sayfa bulunamadı | Güçlü Koltuk Yıkama", "Aradığınız sayfa yok.", "/404.html", "/assets/images/og-cover.svg")
    n404 = n404.replace('content="index,follow', 'content="noindex,follow')
    n404 += f'''
<body>
{nav("index.html")}
<main id="icerik" class="section"><div class="wrap center">
<h1>Bu sayfa taşınmış olabilir.</h1>
<p class="lead">Ana sayfadan koltuk yıkama, hizmetler veya iletişim bölümüne geçebilirsiniz.</p>
<p><a class="btn btn-primary" href="index.html">Ana sayfaya dön</a></p>
</div></main>
{footer()}'''
    write("404.html", n404)


def extras():
    pages = [
        "index.html",
        "hakkimizda.html",
        "hizmetlerimiz.html",
        "iletisim.html",
        "blog.html",
        "kampanya.html",
        "gizlilik-politikasi.html",
        "kvkk.html",
        "muratpasa-koltuk-yikama.html",
        "konyaalti-koltuk-yikama.html",
        "kepez-koltuk-yikama.html",
        "dosemealti-koltuk-yikama.html",
        "kemer-koltuk-yikama.html",
        "aksu-koltuk-yikama.html",
    ]
    urls = "\n".join(
        f"  <url><loc>{SITE + '/' if p=='index.html' else SITE+'/'+p}</loc><changefreq>weekly</changefreq><priority>{'1.0' if p=='index.html' else '0.8'}</priority></url>"
        for p in pages
    )
    (ROOT / "sitemap.xml").write_text(
        f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls}
</urlset>
''',
        encoding="utf-8",
    )
    (ROOT / "robots.txt").write_text(
        f"""User-agent: *
Allow: /
Disallow: /_arsiv/

Sitemap: {SITE}/sitemap.xml
""",
        encoding="utf-8",
    )
    (ROOT / "llms.txt").write_text(
        f"""# Güçlü Koltuk Yıkama
> Antalya’da 2018’den beri yerinde koltuk, yatak ve sandalye yıkama. Kadın ekip. Karcher buharlı sistem. Doğal şampuan.

- Telefon: {PHONE_NICE}
- WhatsApp: https://wa.me/905446304003
- E-posta: {EMAIL}
- Saat: 09:00–18:00 her gün
- Bölgeler: Muratpaşa, Konyaaltı, Kepez, Döşemealtı, Kemer, Aksu
- Site: {SITE}

Koltuklar evden çıkarılmaz. Kuruma 4–6 saat. Bebek ve evcil hayvan dostu ürünler.
""",
        encoding="utf-8",
    )
    (ROOT / "humans.txt").write_text(
        """/* TEAM */
Firma: Güçlü Koltuk Yıkama
Kurucu: Nurhayat Güçlü
Konum: Antalya, Türkiye

/* SITE */
Dil: Türkçe
Standartlar: HTML5, CSS3
""",
        encoding="utf-8",
    )
    (ROOT / "CNAME").write_text("www.antalyakoltukyikamaci.com.tr\n", encoding="utf-8")
    (ROOT / ".nojekyll").write_text("", encoding="utf-8")
    (ROOT / "manifest.webmanifest").write_text(
        """{
  "name": "Güçlü Koltuk Yıkama",
  "short_name": "Güçlü KY",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#f6f1e8",
  "theme_color": "#c45c26",
  "lang": "tr",
  "icons": [
    { "src": "assets/images/logo.svg", "sizes": "any", "type": "image/svg+xml" }
  ]
}
""",
        encoding="utf-8",
    )


def main():
    make_placeholders()
    page_index()
    page_about()
    page_services()
    page_contact()
    page_blog()
    page_kampanya()
    page_legal()
    for d in DISTRICTS:
        page_district(d)
    extras()
    print("OK")


if __name__ == "__main__":
    main()
