"""Build the Herbaferm Singapore prototype into one self-contained index.html (images inlined as data: URIs).

Run:  python3 build.py
Source: src/site.css, src/site.js, src/pages.py, assets/*.jpg
"""
import base64, pathlib, re, sys
root = pathlib.Path(__file__).parent
sys.path.insert(0, str(root / "src"))
import pages as P
import extra as X

def uri(name):
    f = root / "assets" / (name + ".jpg")
    return "data:image/jpeg;base64," + base64.b64encode(f.read_bytes()).decode()

IMGS = {"drops": "drops", "prefer": "prefer", "award": "award-cim-2026", "awardtop": "award-top10", "plate": "award-plate", "ai-jars": "ai-jars", "ai-morning": "ai-morning", "ai-meadow": "ai-meadow", "ai-porridge": "ai-porridge", "ai-fridge": "ai-fridge", "ai-herbs": "ai-herbs", "book": "book-microbiome", "flatlay": "herbs-flatlay"}
for h in P.HERBS:
    IMGS["herb-" + h[0]] = "herb-" + h[0]
IMGS["herbs-flatlay"] = "herbs-flatlay"
IMGS["hero-bark"] = "hero-bark"
IMGS["fiber"] = "fiber"
IMGS["drops-pour"] = "drops-pour"
IMGS["prefer-bark"] = "prefer-bark"
IMGS["range"] = "range"

drops = P.pcard("drops", "drops", "Signature product", "Herbaferm Drops",
                "Herbal extract made by natural fermentation, taken in a glass of water.", 55, "30 ml, about a month",
                '<img src="@@img:drops@@" alt="Herbaferm Drops bottle and carton">')
fiber = P.pcard("fiber", "fiber", "Everyday add-in", "Fiber Elite",
                "A fibre-rich additive for smoothies, shakes, yoghurt and porridge.", 55, "125 g, about a month",
                P.PACK_FIBER, white=True)
prefer = P.pcard("prefer", "prefer", "Optional add-on", "Prefer HF400",
                 "Capsules of fermented herb fibres, taken alongside Drops.", 45, "14 capsules",
                 '<img src="@@img:prefer@@" alt="Prefer HF400 bottle and capsule">', white=True)

TOK = {
    "PC_DROPS": drops, "PC_FIBER": fiber, "PC_PREFER": prefer,
    "HERBS": "".join(P.herb_card(h) for h in P.HERBS),
    "HERB_ROWS": "".join(P.herb_row(h) for h in P.HERBS),
    "FAQ_ITEMS": "".join(P.faq_item(*f) for f in P.FAQS),
    "PACK_FIBER": P.PACK_FIBER,
    "TAG_CONFIRM": '<span class="tag">To confirm</span>',
    "TAG_SUPPLY": '<span class="tag">To supply</span>',
    "TAG_RESULT": '<span class="tag">Name and result to confirm</span>',
}
for k, v in P.PHEROS.items():
    TOK["PHERO_" + k] = v
for k in ("LEAF DROP FLASK SHIELD WHEAT CAPS DOC MAIL GLOBE USERS BOOK SNOW CLOCK").split():
    TOK[k] = getattr(P, k)


# ---------- v3: swap in new pages, patch others, add articles ----------
def patch(pid, marker, add, before=True):
    for i, (k, t, h) in enumerate(P.PAGES):
        if k == pid:
            assert marker in h, (pid, marker[:40])
            h = h.replace(marker, (add + marker) if before else (marker + add), 1)
            P.PAGES[i] = (k, t, h)
            return
    raise KeyError(pid)

P.PAGES = [p for p in P.PAGES if p[0] not in ("home", "learn")]
P.PAGES.insert(0, ("home", "Herbaferm Singapore", X.HOME))

P.PAGES.append(("insight", "Design evidence | Herbaferm Singapore", X.INSIGHT))
P.PAGES.append(("awards", "Awards | Herbaferm Singapore", X.AWARDS))
P.PAGES.insert(8, ("learn", "Learn | Herbaferm Singapore", X.LEARN))
for i in range(len(X.ARTICLES)):
    P.PAGES.append(X.article_page(i))

SEC = '<section%s><div class="wrap">%s</div></section>'
patch("drops", '<section class="alt"><div class="wrap"><div class="sechead"><div><p class="eyebrow">Pairs well with',
      SEC % ("", X.CALC_DROPS))
patch("fiber", '<section class="alt"><div class="wrap"><div class="sechead"><div><p class="eyebrow">Pairs well with',
      SEC % ("", X.CALC_FIBER))
patch("shop", '<section class="alt"><div class="wrap">\n  <p class="eyebrow">Not sure where to start?</p>', SEC % ("", X.CALC_DROPS))
patch("science", '<section class="alt"><div class="wrap">\n  <p class="eyebrow">Plain-language glossary</p>',
      SEC % ("", '<h2>From herb to bottle</h2><p class="lede">Select a step, or let it play.</p>' + X.stepper()))
# remove small-caps eyebrows inside page bodies (page heroes keep theirs)
P.PAGES = [(k, t, re.sub(r'<p class="eyebrow"[^>]*>[^<]*</p>\s*', "", h)) for k, t, h in P.PAGES]
for _i, (_k, _t, _h) in enumerate(P.PAGES):
    if _k in X.PROD:
        _s = X.prod_sections(_k, P.FAQS)
        assert _h.count('<div class="tabs-wrap">') == 1 and _h.lstrip().startswith('<section style="padding-block:40px 70px">'), _k
        _h = _h.replace('<section style="padding-block:40px 70px">', '<section class="ptop" id="%s-top" style="--pt:%s">' % (_k, _s["pt"]), 1)
        _h = _h.replace('<div class="keyfacts">', _s["trust"] + '<div class="keyfacts">', 1)
        _h = _h.replace('<p class="note">', _s["deliv"] + '<p class="note">', 1)
        # tabs become visible cards
        _labels = dict(re.findall(r'aria-controls="([\w-]+)">([^<]+)</button>', _h))
        _h = re.sub(r'<div class="tabs" role="tablist">.*?</div>', '', _h, count=1, flags=re.S)
        _h = re.sub(r'<div class="tabpanel" id="([\w-]+)"( hidden)?>', lambda m: '<div class="tabpanel dcard" id="%s"><h3>%s</h3>' % (m.group(1), _labels.get(m.group(1), "")), _h)
        _h = _h.replace('<div class="tabs-wrap">', '</div></section>' + _s["nav"] + _s["after"], 1)
        _h, _n = re.subn(r'</div></section>\s*<section class="alt">', lambda m: _s["extra"] + '</div></div></section>' + _s["faq"] + '\n<section class="alt">', _h, count=1)
        assert _n == 1, _k
        _h = re.sub(r'<section class="(pglance|phow|pfit|pinside|pdet|pfaq)"', lambda m: '<section style="--pt:%s" class="%s"' % (_s["pt"], m.group(1)), _h)
        P.PAGES[_i] = (_k, _t, _h)

TOK["SLOT_MORNING"] = X.slot("r34", "Morning routine photo", "A real person with their morning drops. Faces and hands are what the eye finds first.")
TOK["SLOTS_HOME"] = X.slots([("r43", "Drops in water", "Glass and bottle close-up"), ("r43", "Fiber Elite in a bowl", "Porridge or yoghurt with a spoonful stirred in"), ("r43", "Prefer HF400 with breakfast", "Capsule beside a morning drink")])
TOK["SLOT_USE_DROPS"] = X.slot("r43", "Drops in use", "A person adding drops to a glass of water. Hands and faces draw the eye first.")
TOK["SLOT_USE_FIBER"] = X.slot("r43", "Fiber Elite in use", "A person stirring it into porridge or a smoothie.")
TOK["SLOT_USE_PREFER"] = X.slot("r43", "Prefer HF400 in use", "A person taking a capsule with water.")
TOK["EXPLORER"] = X.explorer()
TOK["QUIZ"] = X.QUIZ
TOK["JTEASE"] = "".join(X.jcard(a) for a in (X.ARTICLES[0], X.ARTICLES[1], X.ARTICLES[2]))
HCOL = {"chamomile": ("#f6d04d", "#2a2100", "#2a2100"), "yarrow": ("#f7b5c6", "#3a0f1f", "#3a0f1f"),
        "elderflower": ("#efe7c8", "#2c2a14", "#5a6b1f"), "rosehip": ("#e5484d", "#fff4f2", "#ffd6a0"),
        "propolis": ("#c9822b", "#1f1100", "#1f1100"), "oak-bark": ("#5b3d24", "#f6ead9", "#f2b73d"),
        "wormwood": ("#8fc29a", "#0c2a16", "#0c2a16")}
def _jh(i, h):
    bg, fg, ac = HCOL[h[0]]
    return ('<article class="hpane%s" data-bg="%s" data-fg="%s" data-ac="%s"><div class="hcopy"><h2>%s</h2><p class="lat">%s</p><p class="jp">%s</p></div>'
            '<div class="arch hph"><img src="@@img:herb-%s@@" alt="%s" loading="lazy"></div></article>') % (
            " on" if i == 0 else "", bg, fg, ac, h[1], h[2], h[4], h[0], h[3])
TOK["JHERBS"] = "".join(_jh(i, h) for i, h in enumerate(P.HERBS))
TOK["JALL"] = "".join(X.jcard(a) for a in X.ARTICLES)

def expand(s):
    for _ in range(4):  # tokens can nest (cards inside pages)
        s = re.sub(r"@@([A-Z_]+)@@", lambda m: TOK.get(m.group(1), m.group(0)), s)
    return s

def inline_imgs(s):
    return re.sub(r"@@img:([a-z\-]+)@@", lambda m: uri(IMGS[m.group(1)]), s)

DD = ('<div class="dd"><a href="#shop" data-r="shop">Shop</a><div class="ddm" role="menu">'
      '<a href="#drops" role="menuitem"><b>Herbaferm Drops</b><span>The signature product, S$55</span></a>'
      '<a href="#fiber" role="menuitem"><b>Fiber Elite</b><span>An everyday add-in, S$55</span></a>'
      '<a href="#prefer" role="menuitem"><b>Prefer HF400</b><span>Capsules to go with Drops, S$45</span></a>'
      '<a href="#shop" role="menuitem" class="all"><b>See the whole range</b></a></div></div>')
nav_links = "".join(DD if k == "shop" else '<a href="#%s" data-r="%s">%s</a>' % (k, k, v) for k, v in P.NAV)
mnav = "".join('<a href="#%s" data-r="%s">%s</a>' % (k, k, v) for k, v in P.NAV + [("faq", "FAQ"), ("contact", "Contact")])


# ---------- v8: fewer tabs. Ingredients and Science fold into Learn; Quality folds into About ----------
ORIG_PAGES = list(P.PAGES)
def _strip_phero(h):
    return re.sub(r"^\s*@@PHERO_[A-Z]+@@\s*", "", h)
def _merge(host, hero_tok, parts, tabs):
    """parts: [(page id, section id, heading, lede)] in order. tabs: [(hash, section id, label)]."""
    body = {k: (t, h) for k, t, h in P.PAGES}
    nav = '<nav class="subnav" aria-label="On this page"><div class="wrap">%s</div></nav>' % "".join(
        '<a href="#%s" data-sec="%s">%s</a>' % (hh, sid, lab) for hh, sid, lab in tabs)
    html = "@@%s@@" % hero_tok + nav
    for pid, sid, head, lede in parts:
        html += '<section class="subhead" id="%s"><div class="wrap"><h2>%s</h2><p class="lede">%s</p></div></section>' % (sid, head, lede)
        html += _strip_phero(body[pid][1])
    drop = {pid for pid, *_ in parts}
    P.PAGES = [(k, t, html if k == host else h) for k, t, h in P.PAGES if k == host or k not in drop]
P.PHEROS["LEARN"] = P.phero("Learn", "Learn", "Guides, ingredients and science", "Everything behind the range in one place: how to use it, what is in it and what the research does and does not say.")
P.PHEROS["ABOUT"] = P.phero("About", "About Herbaferm", "A Hungarian formula, in Singapore", "Who we are, where the range comes from, and the documents behind it.")
for _k in ("LEARN", "ABOUT"):
    TOK["PHERO_" + _k] = P.PHEROS[_k]
_merge("learn", "PHERO_LEARN", [("learn", "sec-guides", "Guides", "How to use the range, and the plain-English story behind it."),
        ("ingredients", "sec-ingredients", "Ingredients", "Seven herbs. Tap one to see what it is and which products use it. Descriptions refer to traditional use, not to health effects."),
        ("science", "sec-science", "Science", "How fermentation works and what each study does and does not cover.")],
       [("learn", "sec-guides", "Guides"), ("ingredients", "sec-ingredients", "Ingredients"), ("science", "sec-science", "Science")])
_merge("about", "PHERO_ABOUT", [("about", "sec-about", "Our story", "Who is behind Herbaferm and what we stand for."),
        ("awards", "sec-awards", "Awards", "What Herbaferm has been recognised for, and what is still to be confirmed."),
        ("quality", "sec-quality", "Quality and documents", "Registrations, lab documents and manufacturing information, with what is still being updated.")],
       [("about", "sec-about", "Our story"), ("awards", "sec-awards", "Awards"), ("quality", "sec-quality", "Quality")])

pages_html = ""
for pid, title, body in P.PAGES:
    hidden = "" if pid == "home" else " hidden"
    pages_html += '<main class="page" id="p-%s" data-title="%s"%s>%s</main>\n' % (pid, title, hidden, body)

cart_svg = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 7h14l-1.3 10.2a2 2 0 0 1-2 1.8H8.3a2 2 0 0 1-2-1.8z"/><path d="M9 7a3 3 0 0 1 6 0"/></svg>'

shell = '''<meta charset="utf-8">
<title>Herbaferm Singapore</title>
<style>
__CSS__
</style>
<div class="proto">Design prototype for review. Items marked <span class="tag">To confirm</span> or <span class="tag">To supply</span> need Herbaferm's input before launch.</div>
<header class="top"><div class="wrap nav">
  <a class="brand" href="#home" aria-label="Herbaferm Singapore home"><b>herbaferm</b><i>VITALITY &amp; BALANCE</i></a>
  <nav aria-label="Main">__NAV__</nav>
  <button class="icon-btn" id="search-open" type="button" aria-label="Search the site"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="6.5"/><path d="M16 16l4.5 4.5"/></svg><span class="sl">Search</span></button>
  <button class="icon-btn" id="theme" type="button">Dark</button>
  <button class="icon-btn" id="cart-open" type="button" aria-label="Open cart">__CART__<span class="cart-n" id="cart-n" hidden>0</span></button>
  <button class="icon-btn burger" id="burger" type="button" aria-label="Menu">Menu</button>
</div><div class="mnav">__MNAV__</div></header>
__PAGES__
<footer class="site"><div class="wrap">
  <div class="grid">
    <div><b class="logo">herbaferm</b>Vitality &amp; Balance. Fermented herbal food supplements, available in Singapore.<br><br>Herbaferm Pte. Ltd.<br>UEN 202350449W</div>
    <div><h4>Shop</h4><a href="#drops">Herbaferm Drops</a><a href="#fiber">Fiber Elite</a><a href="#prefer">Prefer HF400</a></div>
    <div><h4>Learn</h4><a href="#learn">Guides</a><a href="#ingredients">Ingredients</a><a href="#science">Science</a><a href="#about">About</a><a href="#awards">Awards</a><a href="#quality">Quality</a></div>
    <div><h4>Help</h4><a href="#partners">Partners</a><a href="#faq">FAQ</a><a href="#contact">Contact</a><a href="#policies">Policies</a><a href="#insight">Design evidence</a><a href="https://herbafermsg.com/" target="_blank" rel="noopener">Current store</a></div>
  </div>
  <div class="legal"><p>These products are food supplements. They are not intended to diagnose, treat, cure or prevent any disease and are not a substitute for a varied diet or medical advice. Speak to a healthcare professional if you are pregnant, breastfeeding, have a medical condition or take medication. Some scene and ingredient images on this site are AI-generated illustrations.</p><p>&copy; 2026 Herbaferm Pte. Ltd. Prototype built for the NUS FSP4003 consulting project. <button type="button" id="still" class="linkbtn" aria-pressed="false">Pause motion</button></p></div>
</div></footer>
<div class="srch" id="srch" hidden><div class="srchbox" role="dialog" aria-modal="true" aria-label="Search the site">
  <div class="srchin"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="6.5"/><path d="M16 16l4.5 4.5"/></svg><input id="srch-q" type="search" placeholder="Search products, ingredients, guides, questions" autocomplete="off" aria-label="Search"><button type="button" id="srch-x" aria-label="Close search">Esc</button></div>
  <div class="srchres" id="srch-res" role="listbox"></div>
</div></div>
<button class="totop" id="totop" type="button" aria-label="Back to top" hidden>&uarr;</button>
<div class="scrim" id="scrim"></div>
<aside class="drawer" id="drawer" aria-label="Cart"><header><h3>Your cart</h3><button class="icon-btn" id="cart-close" type="button">Close</button></header>
  <div class="items" id="cart-items"></div>
  <footer><div class="tot"><span>Subtotal</span><span id="cart-total">S$0.00</span></div><button class="btn btn-honey" id="cart-go" type="button">Checkout</button><p class="sent" id="cart-note" hidden>Prototype: checkout is not connected. In the live build this goes to the secure checkout.</p></footer></aside>
<div class="toast" id="toast" role="status"></div>
<div class="readbar" id="readbar"></div>
<button class="chat-fab" id="chat-fab" type="button" aria-label="Ask Herbaferm"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 5h14a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2h-7l-5 4v-4H5a2 2 0 0 1-2-2V7a2 2 0 0 1 2-2z"/></svg><span>Ask Herbaferm</span></button>
<div class="chat" id="chat" role="dialog" aria-label="Herbaferm assistant">
  <header><div class="dot">h</div><div><b>Herbaferm assistant</b><small>Prototype. Not medical advice.</small></div><button id="chat-close" type="button" aria-label="Close chat">&times;</button></header>
  <div class="log" id="chat-log" aria-live="polite"></div>
  <div class="sugg" id="chat-sugg"></div>
  <form id="chat-form"><input id="chat-in" type="text" placeholder="Ask about the products" aria-label="Your question" autocomplete="off"><button id="chat-send" type="submit">Send</button></form>
</div>
<script>
__JS__
</script>
'''

out = shell
out = out.replace("__CSS__", ((root / "src/site.css").read_text() + (root / "src/journey.css").read_text()))
out = out.replace("__NAV__", nav_links).replace("__MNAV__", mnav).replace("__CART__", cart_svg)
out = out.replace("__PAGES__", expand(pages_html))

# ---- site search index (pages, articles, FAQ items)
import json, html as _h
def _txt(h):
    h = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", h, flags=re.S)
    h = re.sub(r"<[^>]+>", " ", h)
    return re.sub(r"\s+", " ", _h.unescape(h)).strip()
HIDE = {"insight", "policies"}
KIND = lambda pid: "Guide" if pid.startswith("a-") else ("Product" if pid in ("drops", "fiber", "prefer") else "Page")
idx = []
_pg = expand(pages_html)
for pid, title, body in ORIG_PAGES:
    if pid in HIDE or pid == "faq":
        continue
    t = _txt(expand(body))
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", expand(body), re.S)
    name = _txt(h1.group(1)) if h1 else title.split(" | ")[0]
    idx.append({"id": pid, "t": name, "k": KIND(pid), "x": t[:1600]})
for cat, q, a in P.FAQS:
    idx.append({"id": "faq", "t": q, "k": "Question", "x": _txt(expand(a))[:400], "q": q})
out_js_pending = True
SEARCH_JS = "window.HFIDX=" + json.dumps(idx, ensure_ascii=False, separators=(",", ":")) + ";\n"
out = out.replace("__JS__", SEARCH_JS + ((root / "src/site.js").read_text() + "\n" + (root / "src/journey.js").read_text()) + "\n" + (root / "src/chat.js").read_text())
out_pre = out
out = inline_imgs(out)
leftover = set(re.findall(r"@@[A-Za-z_:\-]+@@", out))
if leftover:
    print("UNRESOLVED:", leftover)
(root / "index.html").write_text(out)
print(len(out) // 1024, "KB")

# ---------- v9: normal static site (separate html / css / js / image files) ----------
import shutil
def make_site(dest):
    dest = pathlib.Path(dest)
    for d in ("css", "js", "assets/images"):
        (dest / d).mkdir(parents=True, exist_ok=True)
    css = ((root / "src/site.css").read_text() + (root / "src/journey.css").read_text())
    site_js = ((root / "src/site.js").read_text() + "\n" + (root / "src/journey.js").read_text())
    chat_js = (root / "src/chat.js").read_text()
    html = out_pre
    html = html.replace("<style>\n" + css + "\n</style>", '<link rel="stylesheet" href="css/site.css">')
    html = html.replace("<script>\n" + SEARCH_JS + site_js + "\n" + chat_js + "\n</script>",
                        '<script src="js/search-index.js"></script>\n<script src="js/site.js"></script>\n<script src="js/chat.js"></script>')
    assert "css/site.css" in html and "js/chat.js" in html, "shell replacement failed"
    html = html.replace('<meta charset="utf-8">\n<title>Herbaferm Singapore</title>',
        '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        '<title>Herbaferm Singapore</title>\n<meta name="description" content="Herbaferm fermented herbal food supplements in Singapore: Drops, Fiber Elite and Prefer HF400.">\n'
        '<meta name="theme-color" content="#1f4d34">\n<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">', 1)
    html = html.replace('<link rel="stylesheet" href="css/site.css">', '<link rel="stylesheet" href="css/site.css">\n</head>\n<body>', 1)
    html += "\n</body>\n</html>\n"
    html = re.sub(r"@@img:([a-z\-]+)@@", lambda m: "assets/images/%s.jpg" % IMGS[m.group(1)], html)
    (dest / "index.html").write_text(html)
    (dest / "css/site.css").write_text(css)
    (dest / "js/search-index.js").write_text(SEARCH_JS)
    (dest / "js/site.js").write_text(site_js)
    (dest / "js/chat.js").write_text(chat_js)
    used = set(re.findall(r"assets/images/([\w\-]+\.jpg)", html))
    for f in used:
        shutil.copy(root / "assets" / f, dest / "assets/images" / f)
    (dest / "assets/favicon.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="8" fill="#1f4d34"/><path d="M16 7c5 3 7 8 4 13-1 2-3 3-4 5-1-2-3-3-4-5-3-5-1-10 4-13z" fill="#eaf3ea"/></svg>')
    print("site ->", dest, len(used), "images")

if "--site" in sys.argv:
    make_site(sys.argv[sys.argv.index("--site") + 1])
