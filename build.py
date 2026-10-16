"""Build the self-contained, bilingual static site into dist/. No network or packages."""
from __future__ import annotations

ADS_LOADER = '<script defer src="https://vijeron.com/assets/vijeron-ads.js"></script>'

import html
import json
import shutil
from datetime import date
from pathlib import Path
from xml.etree.ElementTree import Element, SubElement, ElementTree

from articles import ARTICLES, SOURCES

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "dist"
SITE = "https://energi.vijeron.com"
TODAY = date(2026, 10, 9).isoformat()

T = {
    "id": {
        "site": "Energi Sehari-hari", "tagline": "Pahami angka. Uji asumsi. Gunakan energi dengan sadar.",
        "nav_guides": "Panduan", "nav_tools": "Kalkulator", "nav_method": "Metode & sumber", "nav_about": "Tentang",
        "home_title": "Pahami listrik rumah dari angka yang bisa Anda periksa",
        "home_desc": "Panduan orisinal dan dua kalkulator untuk memahami watt, kWh, biaya energi, dan perbandingan perangkat. Tarif serta pola pemakaian diisi oleh Anda.",
        "home_intro": "Label daya, tagihan, dan iklan produk sering memakai satuan berbeda. Energi Sehari-hari membantu Anda menghubungkannya dengan rumus terbuka, contoh yang bisa dihitung ulang, dan batas perkiraan yang terlihat.",
        "start": "Mulai dari watt dan kWh", "try_tools": "Coba kalkulator", "hero_small": "Laboratorium literasi listrik rumah · Vijeron",
        "hero_note_title": "Satu angka bukan seluruh tagihan", "hero_note": "Biaya nyata dapat mencakup tarif bertingkat, pajak, biaya tetap, dan kebiasaan pemakaian yang berubah. Kami tidak menerbitkan tarif otomatis yang berisiko kedaluwarsa.",
        "step_title": "Tiga langkah yang dapat diuji", "step1": "Baca angka pada label atau meter, lalu catat sumbernya.", "step2": "Masukkan jam dan hari yang sesuai dengan pemakaian Anda.", "step3": "Bandingkan perkiraan dengan kWh pada tagihan yang periodenya sama.",
        "guide_title": "Panduan dari dasar sampai keputusan", "guide_intro": "Sepuluh bacaan pendek disusun sebagai jalur belajar. Setiap halaman memiliki contoh, kekeliruan yang perlu dihindari, dan tautan ke sumber primer.",
        "tool_title": "Dua alat dengan rumus terbuka", "tool_intro": "Perhitungan berlangsung di peramban Anda. Angka yang dimasukkan tidak dikirim ke server kami.",
        "tool_usage": "Perkiraan pemakaian perangkat", "tool_usage_desc": "Ubah watt, jam, hari, dan jumlah perangkat menjadi kWh. Tambahkan tarif sendiri bila ingin perkiraan biaya energi.",
        "tool_compare": "Bandingkan dua pilihan", "tool_compare_desc": "Lihat selisih kWh dua perangkat pada jadwal yang sama. Cocok untuk membandingkan lampu dengan keluaran cahaya yang setara.",
        "learn_more": "Baca panduan", "open_tool": "Buka alat", "source_line": "Ditulis untuk Vijeron; sumber dipakai untuk memeriksa konsep, bukan untuk menyalin artikelnya.",
        "breadcrumb_home": "Beranda", "guide_label": "Panduan", "worked": "Contoh yang bisa dihitung ulang", "mistake": "Perlu dihindari", "references": "Rujukan yang dapat diperiksa", "related": "Lanjutkan belajar",
        "method_title": "Metode editorial dan sumber", "method_desc": "Apa yang dihitung, dari mana konsepnya berasal, dan apa yang tidak dapat disimpulkan dari hasil alat.",
        "about_title": "Tentang Energi Sehari-hari", "about_desc": "Proyek literasi energi rumah dari Vijeron dengan contoh orisinal, sumber terbuka, dan alat yang transparan.",
        "privacy_title": "Kebijakan privasi", "privacy_desc": "Informasi data yang dipakai oleh kalkulator, analitik, dan iklan di Energi Sehari-hari.",
        "footer": "Panduan literasi energi rumah dari Vijeron. Bukan penyedia listrik, auditor bersertifikat, atau penjual perangkat.",
        "privacy": "Privasi", "contact": "Kontak", "skip": "Lewati ke isi", "updated": "Diperbarui 9 Oktober 2026",
        "usage_title": "Hitung kWh dari satu jenis perangkat", "usage_desc": "Masukkan daya listrik masuk dan jadwal pemakaian. Untuk perangkat yang daya masuknya berubah, gunakan hasil ini sebagai ilustrasi, lalu periksa label energi atau ukur kWh nyata.",
        "compare_title": "Bandingkan energi dua perangkat", "compare_desc": "Gunakan dua pilihan yang memberikan fungsi setara pada jam dan hari yang sama. Selisih biaya hanyalah perkiraan berdasarkan tarif yang Anda masukkan.",
        "power": "Daya masuk (W)", "power_a": "Daya pilihan A (W)", "power_b": "Daya pilihan B (W)", "hours": "Jam pemakaian per hari", "days": "Hari pemakaian dalam periode", "quantity": "Jumlah unit", "rate": "Tarif per kWh (opsional)", "currency": "Mata uang (opsional)",
        "calculate": "Hitung", "result_title": "Hasil perkiraan", "initial_result": "Isi data dan tekan Hitung. Angka Anda tetap di peramban ini.", "formula_usage": "Rumus: W × jam/hari × hari × unit ÷ 1.000 = kWh.", "formula_compare": "Rumus tiap pilihan: W × jam/hari × hari × unit ÷ 1.000 = kWh. Selisih = B − A.",
        "assumption": "Perkiraan ini menganggap daya tetap selama jam yang dimasukkan. Belum mencakup mode siaga, siklus kompresor, pajak, atau biaya tetap.",
    },
    "en": {
        "site": "Everyday Energy", "tagline": "Understand the numbers. Test assumptions. Use energy thoughtfully.",
        "nav_guides": "Guides", "nav_tools": "Calculators", "nav_method": "Method & sources", "nav_about": "About",
        "home_title": "Understand household electricity with numbers you can check",
        "home_desc": "Original guides and two calculators for watts, kWh, energy cost, and appliance comparisons. You enter your own rate and usage pattern.",
        "home_intro": "Power labels, bills, and product ads often use different units. Everyday Energy connects them with open formulas, examples you can recalculate, and visible limits on every estimate.",
        "start": "Start with watts and kWh", "try_tools": "Try the calculators", "hero_small": "A household electricity literacy lab · Vijeron",
        "hero_note_title": "One number is not your whole bill", "hero_note": "Actual costs may include tiered rates, taxes, fixed charges, and changing habits. We do not publish an automatic electricity rate that could become outdated.",
        "step_title": "Three steps you can check", "step1": "Read a label or meter and record where the number came from.", "step2": "Enter hours and days that match your own use.", "step3": "Compare the estimate with billed kWh over a matching period.",
        "guide_title": "Guides from first principles to decisions", "guide_intro": "Ten short readings form a learning path. Each page includes a worked example, a common pitfall, and links to primary sources.",
        "tool_title": "Two tools with open formulas", "tool_intro": "Calculations run in your browser. Your inputs are not sent to our server.",
        "tool_usage": "Estimate an appliance's use", "tool_usage_desc": "Turn watts, hours, days, and quantity into kWh. Enter your own rate if you want an estimated energy charge.",
        "tool_compare": "Compare two options", "tool_compare_desc": "See the kWh difference between two appliances on the same schedule. Useful for lamps with comparable light output.",
        "learn_more": "Read guide", "open_tool": "Open tool", "source_line": "Written for Vijeron; sources verify concepts rather than supply copied articles.",
        "breadcrumb_home": "Home", "guide_label": "Guide", "worked": "A worked example", "mistake": "Avoid this mistake", "references": "Sources you can inspect", "related": "Continue learning",
        "method_title": "Editorial method and sources", "method_desc": "What the tools calculate, where the concepts come from, and what the results cannot establish.",
        "about_title": "About Everyday Energy", "about_desc": "A Vijeron household energy literacy project with original examples, open sources, and transparent tools.",
        "privacy_title": "Privacy policy", "privacy_desc": "How Everyday Energy handles calculator inputs, analytics, and advertising.",
        "footer": "A Vijeron household energy guide. We are not an electricity provider, certified auditor, or appliance seller.",
        "privacy": "Privacy", "contact": "Contact", "skip": "Skip to content", "updated": "Updated 9 October 2026",
        "usage_title": "Estimate kWh for one type of appliance", "usage_desc": "Enter electrical input power and your usage schedule. For variable-power devices, treat this as an illustration, then check an energy label or measure actual kWh.",
        "compare_title": "Compare the energy use of two devices", "compare_desc": "Choose options delivering comparable service on the same schedule. Any cost difference is only an estimate based on the rate you enter.",
        "power": "Input power (W)", "power_a": "Option A input power (W)", "power_b": "Option B input power (W)", "hours": "Hours per day", "days": "Days used in the period", "quantity": "Number of units", "rate": "Rate per kWh (optional)", "currency": "Currency (optional)",
        "calculate": "Calculate", "result_title": "Estimated result", "initial_result": "Enter your values and select Calculate. Your numbers remain in this browser.", "formula_usage": "Formula: W × hours/day × days × units ÷ 1,000 = kWh.", "formula_compare": "Each option: W × hours/day × days × units ÷ 1,000 = kWh. Difference = B − A.",
        "assumption": "This estimate assumes steady power throughout the entered hours. It excludes standby modes, compressor cycling, taxes, and fixed charges.",
    },
}


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def local_path(lang: str, path: str = "") -> str:
    prefix = "" if lang == "id" else "/en"
    return f"{prefix}/{path}" if path else f"{prefix}/"


def write(path: str, content: str) -> None:
    destination = OUT / path.lstrip("/")
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(content, encoding="utf-8")


URLS: list[tuple[str, str | None]] = []


def source_links(keys: list[str]) -> str:
    return "<ul class='source-list'>" + "".join(
        f"<li><a href='{esc(SOURCES[key][1])}' rel='noopener noreferrer'>{esc(SOURCES[key][0])} <span aria-hidden='true'>↗</span></a></li>"
        for key in keys
    ) + "</ul>"


def head(lang: str, path: str, title: str, description: str, kind: str = "WebPage", ads: bool = True) -> str:
    url = SITE + local_path(lang, path)
    other = "en" if lang == "id" else "id"
    schema = {
        "@context": "https://schema.org", "@type": kind, "name": title, "description": description,
        "url": url, "inLanguage": lang, "datePublished": TODAY, "dateModified": TODAY,
        "author": {"@type": "Organization", "name": "Vijeron", "url": "https://www.vijeron.com/"},
        "publisher": {"@type": "Organization", "name": "Vijeron", "url": "https://www.vijeron.com/"},
        "isPartOf": {"@type": "WebSite", "name": "Energi Sehari-hari | Vijeron", "url": SITE + "/"},
    }
    tags = (
        "<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments)}"
        "gtag('consent','default',{ad_storage:'denied',analytics_storage:'denied',ad_user_data:'denied',ad_personalization:'denied',wait_for_update:500});</script>"
        "<script async src='https://fundingchoicesmessages.google.com/i/pub-6180580801533680?ers=1'></script>"
        "<script async src='https://www.googletagmanager.com/gtag/js?id=G-79X7K7H4MJ'></script>"
        "<script>gtag('js',new Date());gtag('config','G-79X7K7H4MJ');</script>"
        "<script async crossorigin='anonymous' src='https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6180580801533680'></script>"
    ) if ads else ""
    alternates = "".join(f"<link rel='alternate' hreflang='{code}' href='{esc(SITE + local_path(code, path))}'>" for code in ("id", "en"))
    alternates += f"<link rel='alternate' hreflang='x-default' href='{esc(SITE + local_path('id', path))}'>"
    return (
        "<!doctype html><html lang='" + lang + "'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'>"
        + ("<meta name='google-adsense-account' content='ca-pub-6180580801533680'>" if ads else "")
        + f"<title>{esc(title)} | Vijeron</title><meta name='description' content='{esc(description)}'>"
        + f"<link rel='canonical' href='{esc(url)}'>{alternates}"
        + f"<meta property='og:type' content='{'article' if kind == 'Article' else 'website'}'><meta property='og:title' content='{esc(title)} | Vijeron'>"
        + f"<meta property='og:description' content='{esc(description)}'><meta property='og:url' content='{esc(url)}'>"
        + "<meta name='theme-color' content='#102a2b'><link rel='icon' type='image/svg+xml' href='/assets/icon.svg'>"
        + "<link rel='stylesheet' href='/assets/site.css'>"
        + f"<script type='application/ld+json'>{json.dumps(schema, ensure_ascii=False, separators=(',', ':'))}</script>{tags}{ADS_LOADER if ads else ''}</head><body>"
    )


def chrome(lang: str, path: str) -> str:
    t = T[lang]
    links = [
        (t["nav_guides"], local_path(lang) + "#panduan"),
        (t["nav_tools"], local_path(lang) + "#alat"),
        (t["nav_method"], local_path(lang, "metode/")),
        (t["nav_about"], local_path(lang, "tentang/")),
    ]
    nav = "".join(f"<a href='{esc(url)}'>{esc(label)}</a>" for label, url in links)
    switch = "".join(
        f"<a href='{esc(local_path(code, path))}' lang='{code}'{' aria-current="page"' if code == lang else ''}>{name}</a>"
        for code, name in (("id", "Indonesia"), ("en", "English"))
    )
    return (
        f"<a class='skip' href='#main'>{esc(t['skip'])}</a>"
        f"<header class='header'><div class='wrap header-inner'><a class='logo' href='{local_path(lang)}'><span class='logo-mark'>e<span>·</span></span><span>{esc(t['site'])}<small>VIJERON / ENERGY LAB</small></span></a>"
        f"<nav class='primary' aria-label='Main navigation'>{nav}</nav><nav class='languages' aria-label='Language / Bahasa'>{switch}</nav></div></header>"
    )


def footer(lang: str) -> str:
    t = T[lang]
    return (
        f"<footer class='footer'><div class='wrap footer-grid'><div><strong>{esc(t['site'])}</strong><p>{esc(t['footer'])}</p></div>"
        f"<nav aria-label='Footer'><a href='{local_path(lang, 'metode/')}'>{esc(t['nav_method'])}</a>"
        f"<a href='{local_path(lang, 'privasi/')}'>{esc(t['privacy'])}</a>"
        f"<a href='https://www.vijeron.com/kontak.html'>{esc(t['contact'])}</a>"
        "<a href='https://www.vijeron.com/'>Vijeron.com</a></nav></div>"
        f"<div class='wrap footline'><span>© Vijeron · {esc(t['updated'])}</span><span>W × h ÷ {'1,000' if lang == 'en' else '1.000'} = kWh</span></div></footer>"
    )


def finish(lang: str, script: bool = False) -> str:
    return footer(lang) + (f"<script defer src='/assets/calculator.js'></script>" if script else "") + "</body></html>"


def article_card(lang: str, article: dict, number: int) -> str:
    item = article[lang]
    url = local_path(lang, f"panduan/{article['slug']}/")
    return f"<article class='article-card'><span class='card-number'>{number:02d} / 10</span><h3><a href='{url}'>{esc(item['title'])}</a></h3><p>{esc(item['summary'])}</p><a class='text-link' href='{url}'>{esc(T[lang]['learn_more'])} <span aria-hidden='true'>↗</span></a></article>"


def home(lang: str) -> None:
    t = T[lang]
    path = ""
    cards = "".join(article_card(lang, article, i) for i, article in enumerate(ARTICLES, 1))
    body = (
        f"<main id='main'><section class='hero wrap'><div class='hero-copy'><p class='eyebrow'>{esc(t['hero_small'])}</p>"
        f"<h1>{esc(t['home_title'])}</h1><p class='lead'>{esc(t['home_intro'])}</p>"
        f"<div class='actions'><a class='button' href='{local_path(lang, 'panduan/watt-dan-kwh/')}'>{esc(t['start'])} ↗</a>"
        f"<a class='button button-ghost' href='#alat'>{esc(t['try_tools'])}</a></div></div>"
        f"<div class='hero-visual'><div class='orbit orbit-one'></div><div class='orbit orbit-two'></div><div class='energy-disc'><span>100 W</span><b>× 10 h</b><em>= 1 kWh</em></div>"
        f"<aside class='hero-note'><strong>{esc(t['hero_note_title'])}</strong><p>{esc(t['hero_note'])}</p></aside></div></section>"
        f"<section class='steps'><div class='wrap'><p class='eyebrow'>01 / METHOD</p><h2>{esc(t['step_title'])}</h2><div class='step-grid'>"
        + "".join(f"<div><b>0{i}</b><p>{esc(t[f'step{i}'])}</p></div>" for i in range(1, 4))
        + "</div></div></section>"
        f"<section class='wrap section' id='alat'><div class='section-head'><p class='eyebrow'>02 / TOOLS</p><h2>{esc(t['tool_title'])}</h2><p>{esc(t['tool_intro'])}</p></div>"
        f"<div class='tool-grid'><article class='tool-card'><span>01 / kWh</span><h3>{esc(t['tool_usage'])}</h3><p>{esc(t['tool_usage_desc'])}</p><a class='button' href='{local_path(lang, 'alat/pemakaian/')}'>{esc(t['open_tool'])} ↗</a></article>"
        f"<article class='tool-card'><span>02 / Δ kWh</span><h3>{esc(t['tool_compare'])}</h3><p>{esc(t['tool_compare_desc'])}</p><a class='button' href='{local_path(lang, 'alat/perbandingan/')}'>{esc(t['open_tool'])} ↗</a></article></div></section>"
        f"<section class='wrap section' id='panduan'><div class='section-head'><p class='eyebrow'>03 / READ</p><h2>{esc(t['guide_title'])}</h2><p>{esc(t['guide_intro'])}</p></div><div class='article-grid'>{cards}</div></section>"
        f"<section class='wrap trust'><span class='eyebrow'>SOURCE NOTE</span><p>{esc(t['source_line'])}</p><a class='text-link' href='{local_path(lang, 'metode/')}'>{esc(t['nav_method'])} ↗</a></section></main>"
    )
    write(local_path(lang) + "index.html", head(lang, path, t["site"], t["home_desc"]) + chrome(lang, path) + body + finish(lang))
    URLS.append((SITE + local_path(lang), "home"))


def guide(lang: str, article: dict, index: int) -> None:
    t, item = T[lang], article[lang]
    path = f"panduan/{article['slug']}/"
    sections = "".join(f"<section class='prose-section'><h2>{esc(h)}</h2><p>{esc(p)}</p></section>" for h, p in item["sections"])
    next_article = ARTICLES[(index + 1) % len(ARTICLES)]
    body = (
        f"<main id='main' class='wrap article-layout'><article><nav class='crumb'><a href='{local_path(lang)}'>{esc(t['breadcrumb_home'])}</a><span>/</span>{esc(t['guide_label'])} {index+1:02d}</nav>"
        f"<header class='article-header'><p class='eyebrow'>{esc(t['guide_label'])} {index+1:02d} / 10</p><h1>{esc(item['title'])}</h1><p class='lead'>{esc(item['summary'])}</p><p class='byline'>Vijeron · {esc(t['updated'])}</p></header>"
        f"<div class='prose'>{sections}<aside class='example'><span class='eyebrow'>{esc(t['worked'])}</span><p>{esc(item['example'])}</p></aside>"
        f"<aside class='mistake'><strong>{esc(t['mistake'])}</strong><p>{esc(item['pitfall'])}</p></aside>"
        f"<section class='references'><h2>{esc(t['references'])}</h2>{source_links(article['sources'])}</section></div>"
        f"<div class='next-guide'><span>{esc(t['related'])}</span><a href='{local_path(lang, 'panduan/' + next_article['slug'] + '/')}'>{esc(next_article[lang]['title'])} ↗</a></div></article>"
        f"<aside class='article-aside'><div class='aside-panel'><span class='eyebrow'>TRY THE TOOL</span><h2>{esc(t['tool_usage'])}</h2><p>{esc(t['tool_usage_desc'])}</p><a class='text-link' href='{local_path(lang, 'alat/pemakaian/')}'>{esc(t['open_tool'])} ↗</a></div>"
        f"<div class='aside-panel'><h2>{esc(t['nav_method'])}</h2><p>{esc(t['source_line'])}</p><a class='text-link' href='{local_path(lang, 'metode/')}'>{esc(t['learn_more'])} ↗</a></div></aside></main>"
    )
    write(local_path(lang, path) + "index.html", head(lang, path, item["title"], item["summary"], "Article") + chrome(lang, path) + body + finish(lang))
    URLS.append((SITE + local_path(lang, path), None))


def field(field_id: str, label: str, value: str, maximum: str, required: bool = True, minimum: str = "0", step: str = "any") -> str:
    return (f"<label class='field' for='{field_id}'><span>{esc(label)}</span>"
            f"<input id='{field_id}' name='{field_id}' type='number' inputmode='decimal' min='{minimum}' max='{maximum}' step='{step}' value='{value}' {'required' if required else ''}></label>")


def tool(lang: str, compare: bool) -> None:
    t = T[lang]
    slug = "perbandingan" if compare else "pemakaian"
    path = f"alat/{slug}/"
    title = t["compare_title"] if compare else t["usage_title"]
    desc = t["compare_desc"] if compare else t["usage_desc"]
    powers = (field("power-a", t["power_a"], "60", "20000") + field("power-b", t["power_b"], "10", "20000")) if compare else field("power", t["power"], "50", "20000")
    fields = powers + field("hours", t["hours"], "5", "24") + field("days", t["days"], "30", "366", minimum="0.01") + field("quantity", t["quantity"], "1", "100", minimum="1", step="1") + field("rate", t["rate"], "", "10000000", False)
    fields += f"<label class='field' for='currency'><span>{esc(t['currency'])}</span><input id='currency' name='currency' type='text' maxlength='12' placeholder='IDR, USD, EUR'></label>"
    body = (
        f"<main id='main' class='wrap tool-layout'><nav class='crumb'><a href='{local_path(lang)}'>{esc(t['breadcrumb_home'])}</a><span>/</span>{esc(t['nav_tools'])}</nav>"
        f"<div class='tool-heading'><p class='eyebrow'>{'02 / COMPARISON' if compare else '01 / ESTIMATE'}</p><h1>{esc(title)}</h1><p class='lead'>{esc(desc)}</p></div>"
        f"<div class='calculator-layout'><form class='calc-form' id='calculator' data-tool='{'compare' if compare else 'usage'}' data-language='{lang}'>"
        f"<div class='field-grid'>{fields}</div><button class='button' type='submit'>{esc(t['calculate'])} ↗</button></form>"
        f"<div class='calc-result' id='result' role='status' aria-live='polite'><span class='eyebrow'>{esc(t['result_title'])}</span><strong>—</strong><p>{esc(t['initial_result'])}</p></div></div>"
        f"<div class='tool-notes'><div><h2>{esc(t['nav_method'])}</h2><p>{esc(t['formula_compare'] if compare else t['formula_usage'])}</p><p>{esc(t['assumption'])}</p>"
        f"<a class='text-link' href='{local_path(lang, 'metode/')}'>{esc(t['nav_method'])} ↗</a></div>"
        f"<div><h2>{esc(t['related'])}</h2><p>{esc(ARTICLES[2][lang]['summary'])}</p><a class='text-link' href='{local_path(lang, 'panduan/hitung-kwh-bulanan/')}'>{esc(ARTICLES[2][lang]['title'])} ↗</a></div></div></main>"
    )
    write(local_path(lang, path) + "index.html", head(lang, path, title, desc) + chrome(lang, path) + body + finish(lang, script=True))
    URLS.append((SITE + local_path(lang, path), None))


def info_page(lang: str, kind: str) -> None:
    t = T[lang]
    data = {
        "metode": (t["method_title"], t["method_desc"],
            [
                ("Rumus / Formula", "Energi perkiraan = watt × jam pemakaian per hari × hari × jumlah unit ÷ 1.000. Hasilnya kWh bila daya dianggap tetap. Selisih dua pilihan dihitung B − A pada jam, hari, dan jumlah unit yang sama." if lang == "id" else "Estimated energy = watts × hours per day × days × units ÷ 1,000. This gives kWh when power is assumed steady. Two options are compared as B − A on the same schedule and quantity."),
                ("Tarif dan tagihan / Rate and bill", "Biaya energi perkiraan = kWh × tarif per kWh yang Anda masukkan. Kami tidak mengisi tarif nasional otomatis. Pajak, biaya tetap, tarif bertingkat, subsidi, dan ketentuan penyedia tidak dimodelkan." if lang == "id" else "Estimated energy charge = kWh × the rate you enter. We do not insert an automatic national rate. Taxes, fixed charges, tiers, subsidies, and provider rules are not modeled."),
                ("Batas / Limits", "Daya dari label mungkin tidak sama dengan rata-rata nyata. Pendingin, pemanas, dan perangkat bermode siaga dapat berubah dayanya. Ukur kWh nyata selama periode yang mewakili kebiasaan Anda untuk keputusan penting. Contoh di situs ini dibuat untuk menjelaskan rumus, bukan hasil uji produk." if lang == "id" else "Rated power may differ from real average draw. Cooling, heating, and standby devices can vary their power. Measure actual kWh over a representative period for important decisions. The site's examples explain arithmetic; they are not product test results."),
                ("Proses editorial / Editorial process", "Panduan dan contoh ditulis khusus untuk Vijeron pada 9 Oktober 2026. Sumber primer di bawah dipakai untuk memeriksa definisi dan batas metode. Kami tidak menyalin artikel, foto, tabel tarif, atau hasil pengujian milik sumber tersebut." if lang == "id" else "These guides and examples were written for Vijeron on 9 October 2026. The primary sources below check definitions and methodological limits. We do not republish their articles, images, rate tables, or test results."),
            ]),
        "tentang": (t["about_title"], t["about_desc"],
            [
                ("Tujuan / Purpose", "Energi Sehari-hari membantu pembaca mengubah angka daya menjadi perkiraan energi yang dapat dihitung ulang. Panduan disusun sebagai bahan literasi umum, bukan audit teknis rumah tertentu atau rekomendasi pembelian." if lang == "id" else "Everyday Energy helps readers turn power figures into energy estimates they can reproduce. It is a general literacy project, not a technical audit of a particular home or a product recommendation."),
                ("Siapa yang menerbitkan / Publisher", "Situs ini diterbitkan oleh Vijeron sebagai bagian dari katalog alat dan panduan di www.vijeron.com. Tidak ada afiliasi dengan lembaga sumber yang ditautkan. Koreksi dapat dikirim melalui halaman kontak Vijeron dengan URL dan penjelasan bagian yang perlu diperiksa." if lang == "id" else "Vijeron publishes this site as part of its guide and tool catalog at www.vijeron.com. Linked source organizations are not affiliated with us. Send corrections through the Vijeron contact page with the URL and the passage to review."),
                ("Iklan / Advertising", "Kami memasang kode Google AdSense pada halaman konten; penayangan bergantung pada persetujuan akun dan pilihan privasi. Iklan tidak menentukan rumus, contoh, atau kesimpulan editorial. Tidak ada tautan afiliasi produk pada peluncuran ini." if lang == "id" else "Google AdSense code is present on content pages; ad serving depends on account approval and privacy choices. Ads do not determine formulas, examples, or editorial conclusions. This launch has no product affiliate links."),
            ]),
        "privasi": (t["privacy_title"], t["privacy_desc"],
            [
                ("Masukan kalkulator / Calculator inputs", "Watt, jam, hari, jumlah perangkat, tarif, dan mata uang diproses di peramban Anda. Situs ini tidak mengirim, menyimpan, atau mencatat nilai yang Anda masukkan pada server Vijeron." if lang == "id" else "Watts, hours, days, units, rate, and currency are processed in your browser. This site does not transmit, store, or log your entered values on a Vijeron server."),
                ("Analitik / Analytics", "Google Analytics 4 dipakai untuk mengukur kunjungan dan peristiwa pemakaian alat. Peristiwa mencatat nama alat dan bahasa halaman, tanpa angka masukan atau hasil. Ketersediaan analitik bergantung pada pilihan persetujuan yang berlaku." if lang == "id" else "Google Analytics 4 measures visits and tool-use events. Events include the tool name and page language, not inputs or results. Analytics availability depends on applicable consent choices."),
                ("Iklan dan persetujuan / Ads and consent", "Kode Google AdSense dan Google Funding Choices dapat dimuat pada halaman konten. Penyimpanan iklan, personalisasi iklan, dan analitik dimulai dalam keadaan ditolak sampai pilihan persetujuan yang berlaku diperoleh. Google dapat memproses data sesuai kebijakan layanannya; baca pesan persetujuan saat muncul." if lang == "id" else "Google AdSense and Google Funding Choices code may load on content pages. Ad storage, ad personalization, and analytics storage start denied until an applicable consent choice is obtained. Google may process data under its policies; review the consent message when presented."),
                ("Kontak / Contact", "Untuk pertanyaan privasi atau koreksi, gunakan halaman kontak di portal Vijeron. Jangan mengirim rincian tagihan atau data pribadi yang tidak diperlukan." if lang == "id" else "For privacy questions or corrections, use the Vijeron portal contact page. Do not send unnecessary bill details or personal information."),
            ]),
    }
    title, desc, sections = data[kind]
    path = kind + "/"
    body = f"<main id='main' class='wrap info-page'><nav class='crumb'><a href='{local_path(lang)}'>{esc(t['breadcrumb_home'])}</a><span>/</span>{esc(title)}</nav><p class='eyebrow'>VIJERON / ENERGY LAB</p><h1>{esc(title)}</h1><p class='lead'>{esc(desc)}</p><div class='prose'>"
    body += "".join(f"<section class='prose-section'><h2>{esc(h)}</h2><p>{esc(p)}</p></section>" for h, p in sections)
    if kind == "metode":
        body += f"<section class='references'><h2>{esc(t['references'])}</h2>{source_links(list(SOURCES))}</section>"
    body += "</div></main>"
    write(local_path(lang, path) + "index.html", head(lang, path, title, desc, ads=False) + chrome(lang, path) + body + finish(lang))
    URLS.append((SITE + local_path(lang, path), None))


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "assets").mkdir(parents=True)
    for asset in ("site.css", "calculator.js", "icon.svg"):
        shutil.copy2(ROOT / "assets" / asset, OUT / "assets" / asset)
    for lang in ("id", "en"):
        home(lang)
        for index, article in enumerate(ARTICLES):
            guide(lang, article, index)
        tool(lang, False)
        tool(lang, True)
        for kind in ("metode", "tentang", "privasi"):
            info_page(lang, kind)
    write("404.html", "<!doctype html><html lang='id'><meta charset='utf-8'><title>Halaman tidak ditemukan | Vijeron</title><link rel='stylesheet' href='/assets/site.css'><main class='wrap info-page'><h1>Halaman tidak ditemukan</h1><p>Periksa alamat atau kembali ke <a href='/'>Energi Sehari-hari</a>.</p></main></html>")
    write("robots.txt", "User-agent: *\nAllow: /\nSitemap: https://energi.vijeron.com/sitemap.xml\n")
    write("ads.txt", "google.com, pub-6180580801533680, DIRECT, f08c47fec0942fa0\n")
    write("_headers", "/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n  X-Frame-Options: SAMEORIGIN\n  Permissions-Policy: camera=(), microphone=(), geolocation=()\n  Cache-Control: public, max-age=0, must-revalidate\n\n/assets/*\n  Cache-Control: public, max-age=3600, must-revalidate\n\n/sitemap.xml\n  Content-Type: application/xml; charset=utf-8\n\n/ads.txt\n  Content-Type: text/plain; charset=utf-8\n")
    root = Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    for url, priority in URLS:
        node = SubElement(root, "url")
        SubElement(node, "loc").text = url
        SubElement(node, "lastmod").text = TODAY
        if priority == "home":
            SubElement(node, "priority").text = "1.0"
    ElementTree(root).write(OUT / "sitemap.xml", encoding="utf-8", xml_declaration=True)
    print(f"Built {len(URLS)} pages in {OUT}")


if __name__ == "__main__":
    main()
