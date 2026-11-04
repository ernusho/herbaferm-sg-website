"""Build the Herbaferm Singapore prototype into one self-contained index.html (images inlined as data: URIs).

Run:  python3 build.py
Source: src/site.css, src/site.js, src/pages.py, assets/*.jpg
"""
import base64, pathlib, re, sys
root = pathlib.Path(__file__).parent
sys.path.insert(0, str(root / "src"))
import pages as P
import extra as X
import blog as B
import reviews as RV

CSS = (root / "src/site.css").read_text() + (root / "src/journey.css").read_text() + (root / "src/blog.css").read_text() + (root / "src/reviews.css").read_text()
SITE_URL = (__import__("os").environ.get("HF_SITE_URL") or "https://ernusho.github.io/herbaferm-sg-website/").rstrip("/") + "/"  # GitHub Pages address (assumed); override with HF_SITE_URL

def uri(name):
    f = root / "assets" / (name + ".jpg")
    return "data:image/jpeg;base64," + base64.b64encode(f.read_bytes()).decode()

IMGS = {"drops": "drops", "prefer": "prefer", "award": "award-cim-2026", "awardtop": "award-top10", "plate": "award-plate", "ai-jars": "ai-jars", "ai-morning": "ai-morning", "ai-meadow": "ai-meadow", "ai-porridge": "ai-porridge", "ai-fridge": "ai-fridge", "ai-herbs": "ai-herbs", "book": "book-microbiome", "flatlay": "herbs-flatlay", "ai-field": "ai-field", "ai-chamomile": "ai-chamomile", "ai-kitchen": "ai-kitchen", "ai-oak": "ai-oak", "ai-rosehip": "ai-rosehip", "ai-propolis": "ai-propolis", "ai-shelf": "ai-shelf", "ai-clinic": "ai-clinic", "ai-elder": "ai-elder", "ai-wormwood": "ai-wormwood"}
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
# ---------- SEO: question-style headings, answer-first boxes and sources on the existing articles ----------
_QH = {"Where the herbs come in": "How are herbs fermented?", "What we can and cannot tell you": "What can Herbaferm tell you about its Drops?",
       "A community, not a single thing": "Is the gut microbiome one single thing?", "Why food comes up so often": "Why does food matter for the gut microbiome?",
       "Where Herbaferm fits": "Where do Herbaferm products fit?", "Want to read more?": "Where can I read more?",
       "Probiotic: the living bugs": "What is a probiotic?", "Prebiotic: the food for the bugs": "What is a prebiotic?",
       "Postbiotic: what is left of the bugs": "What is a postbiotic?", "So which is Herbaferm?": "Is Herbaferm a probiotic, prebiotic or postbiotic?",
       "Before you start": "Who should check with a professional first?", "At home": "How should I store Drops at home?",
       "If you run a clinic or a shop": "Can a clinic or shop stock Drops?", "Check the date": "How long does a bottle keep?"}
def _refs_block(keys):
    return '<h2>Sources</h2><ol class="refs">%s</ol>' % "".join('<li>%s <a href="%s" target="_blank" rel="noopener">Source</a></li>' % (B.REFS[k][0], B.REFS[k][1]) for k in keys)
_SRC = {"a-labels": ["hill2014", "gibson2017", "salminen2021"], "a-gut": ["lynch2016", "sender2016"], "a-ferment": ["marco2021"]}
_NEW = []
for _a in X.ARTICLES:
    _id, _cv, _cat, _t, _d, _b = _a
    for _o, _n in _QH.items():
        _b = _b.replace("<h2>%s</h2>" % _o, "<h2>%s</h2>" % _n)
    if _id == "a-gut":
        _b = _b.replace('See the <a href="#awards">About page</a> for details.', 'See <a href="learn/microbial-dysbiosis/">microbial dysbiosis and rebiosis</a> for an explainer based on it, and the <a href="#awards">About page</a> for the book.')
    if _id in _SRC:
        _b += _refs_block(_SRC[_id])
    _NEW.append((_id, _cv, _cat, _t, _d, _b))
X.ARTICLES[:] = _NEW
X.SHORT.update({
    "a-ferment": ["Fermentation is a food process in which microbes convert parts of the food, as in yoghurt, sourdough and kimchi.", "Herbaferm ferments seven herbs with a natural community of microorganisms and bottles the extract as a food supplement.", "No colony count is quoted because there is no verified figure."],
    "a-month": ["Start with 5 drops in water in the morning and evening for the first three days, then build up slowly as the leaflet describes.", "Keep the bottle in the fridge at 5 to 12 \u00b0C, because there are no preservatives.", "Go by the label on your pack, and speak to a doctor or pharmacist first if you take medication or are pregnant."],
    "a-fiber": ["Fiber Elite is a malty, flour-like fibre powder; the leaflet suggests 3.5 g with a meal.", "It can be heated, so it works in porridge as well as shakes, smoothies and yoghurt.", "It contains gluten (barley malt and oat flour)."],
    "a-labels": ["A probiotic is a live microorganism that benefits the person taking it; a prebiotic is food for microbes already in the gut; a postbiotic is a preparation of non-living microbes.", "Herbaferm does not call any product a probiotic."],
    "a-herbs": ["The seven herbs are chamomile, yarrow, elderflower, rosehip, propolis, oak bark and white wormwood.", "What is described is traditional use, not a health effect."],
    "a-gut": ["The gut microbiome is the community of microorganisms in the digestive tract. Researchers are still working out what a healthy mix looks like.", "Diet is one everyday influence; Herbaferm products are food supplements that sit beside a varied diet."],
    "a-fridge": ["Drops have no preservatives, so keep the bottle in the fridge at 5 to 12 \u00b0C.", "Fiber Elite and Prefer HF400 can sit on a normal shelf."],
})


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

# ---------- SEO: blog under Learn (articles are real pages at learn/<slug>/) ----------
CARDIMG = {"microbiome-test-singapore": "ai-clinic", "best-supplements-for-gut-health": "ai-shelf", "natural-supplements-for-gut-health": "ai-herbs",
           "gut-health-supplement-reviews": "ai-chamomile", "best-probiotics-for-gut-health": "ai-fridge",
           "best-supplements-for-gut-health-and-weight-loss": "ai-porridge", "what-is-gut-health": "ai-field",
           "how-to-improve-gut-health": "ai-morning", "fermented-foods-gut-health": "ai-jars", "microbial-dysbiosis": "ai-meadow"}


def _bcard(a, i):
    _ph = CARDIMG.get(a["slug"])
    _im = ('<img class="cimg" src="@@img:%s@@" alt="" loading="lazy" decoding="async">' % _ph) if _ph else ""
    return (('<a class="jcard rv" href="learn/%s/" data-c="Blog"><div class="cover cv%d%s">' % (a["slug"], (i % 6) + 1, " has-img" if _ph else "")) + _im
            + '<span>%s</span></div><div><small>%s</small><h3>%s</h3><p>%s</p></div></a>' % (a["kw"][0].upper() + a["kw"][1:], a["cat"], a["title"], a["dek"]))
_BL = B.ARTICLES
BLOG = ('<section><div class="wrap"><a class="jfeat rv" href="learn/microbial-dysbiosis/"><div class="cover cv4 has-img"><img class="cimg" src="@@img:ai-meadow@@" alt="" loading="lazy" decoding="async"><span>Microbial dysbiosis</span></div><div><p class="kicker" style="color:var(--leaf)">Start here</p>'
        '<h2>%s</h2><p>%s</p><p><span class="more">Read the explainer</span></p></div></a>'
        '<h3 style="margin-top:48px">Questions people search for</h3><div class="jgrid" id="b-grid">%s</div>'
        '<p class="note" style="margin-top:36px">Articles are drafts written from published research for Herbaferm to review. Each names its sources, and a medical reviewer is still to be added. @@TAG_CONFIRM@@</p></div></section>'
        % (B.DYS["title"], B.DYS["dek"], "".join(_bcard(a, i) for i, a in enumerate(_BL))))
P.PAGES.append(("blog", "Blog | Herbaferm Singapore", BLOG))


# remove small-caps eyebrows inside page bodies (page heroes keep theirs)
P.PAGES = [(k, t, re.sub(r'<p class="eyebrow"[^>]*>[^<]*</p>\s*', "", h)) for k, t, h in P.PAGES]
# keep heading order valid: pages whose first body heading after the h1 is an h3 get h2 (styled as h3)
def _fix_levels(h):
    if "@@PHERO_" not in h or "<h3" not in h:
        return h
    m = re.search(r"<h[23][\s>]", h)
    if not m or not m.group(0).startswith("<h3"):
        return h
    def one(mo):
        attrs = mo.group(1)
        if 'class="' in attrs:
            attrs = attrs.replace('class="', 'class="as3 ', 1)
        else:
            attrs += ' class="as3"'
        return "<h2%s>" % attrs
    return re.sub(r"</h3>", "</h2>", re.sub(r"<h3([^>]*)>", one, h))
P.PAGES = [(k, t, _fix_levels(h) if k in ("shop", "contact", "policies") else h) for k, t, h in P.PAGES]
for _i, (_k, _t, _h) in enumerate(P.PAGES):
    if _k in X.PROD:
        _s = X.prod_sections(_k, P.FAQS)
        assert _h.count('<div class="tabs-wrap">') == 1 and _h.lstrip().startswith('<section style="padding-block:40px 70px">'), _k
        _h = _h.replace('<section style="padding-block:40px 70px">', '<section class="ptop" id="%s-top" style="--pt:%s">' % (_k, _s["pt"]), 1)
        _h = _h.replace('<div class="keyfacts">', _s["trust"] + '<div class="keyfacts">', 1)
        _h = _h.replace('<p class="note">', _s["deliv"] + '<p class="note">', 1)
        _h = re.sub(r'(<div class="price">.*?</div>)', lambda m: m.group(1) + RV.jump(_k), _h, count=1, flags=re.S)
        # tabs become visible cards
        _labels = dict(re.findall(r'aria-controls="([\w-]+)">([^<]+)</button>', _h))
        _h = re.sub(r'<div class="tabs" role="tablist">.*?</div>', '', _h, count=1, flags=re.S)
        _h = re.sub(r'<div class="tabpanel" id="([\w-]+)"( hidden)?>', lambda m: '<div class="tabpanel dcard" id="%s"><h3>%s</h3>' % (m.group(1), _labels.get(m.group(1), "")), _h)
        _h = _h.replace('<div class="tabs-wrap">', '</div></section>' + _s["nav"] + _s["after"], 1)
        _h, _n = re.subn(r'</div></section>\s*<section class="alt">', lambda m: _s["extra"] + '</div></div></section>' + _s["faq"] + RV.product(_k, {"drops": "Herbaferm Drops", "fiber": "Fiber Elite", "prefer": "Prefer HF400"}[_k]) + '\n<section class="alt">', _h, count=1)
        assert _n == 1, _k
        _h = re.sub(r'<section class="(pglance|pviz|phow|pfit|pinside|pdet|pfaq)"', lambda m: '<section style="--pt:%s" class="%s"' % (_s["pt"], m.group(1)), _h)
        P.PAGES[_i] = (_k, _t, _h)

TOK["SLOT_MORNING"] = X.slot("r34", "Morning routine photo", "A real person with their morning drops. Faces and hands are what the eye finds first.")
TOK["SLOTS_HOME"] = X.slots([("r43", "Drops in water", "Glass and bottle close-up"), ("r43", "Fiber Elite in a bowl", "Porridge or yoghurt with a spoonful stirred in"), ("r43", "Prefer HF400 with breakfast", "Capsule beside a morning drink")])
TOK["SLOT_USE_DROPS"] = X.slot("r43", "Drops in use", "A person adding drops to a glass of water. Hands and faces draw the eye first.")
TOK["SLOT_USE_FIBER"] = X.slot("r43", "Fiber Elite in use", "A person stirring it into porridge or a smoothie.")
TOK["SLOT_USE_PREFER"] = X.slot("r43", "Prefer HF400 in use", "A person taking a capsule with water.")
TOK["EXPLORER"] = X.explorer()
TOK["QUIZ"] = X.QUIZ
TOK["JTEASE"] = "".join(X.jcard(a) for a in (X.ARTICLES[0], X.ARTICLES[1], X.ARTICLES[2]))
HCOL = {"chamomile": ("#e8c45e", "#2a2100", "#6b3d12"), "yarrow": ("#e9bdb0", "#3a1710", "#8a3a22"),
        "elderflower": ("#efe6cc", "#2c2a14", "#6b5a1f"), "rosehip": ("#b8473f", "#fff4ea", "#ffd9a0"),
        "propolis": ("#b9772a", "#241200", "#fff0cf"), "oak-bark": ("#5b3d24", "#f6ead9", "#e9b04a"),
        "wormwood": ("#aebb8c", "#1f2a10", "#4a3a14")}
HPHOTO = {"chamomile": ("ai-chamomile", "50% 50%"), "yarrow": ("ai-field", "62% 60%"), "elderflower": ("ai-elder", "50% 40%"),
          "oak-bark": ("hero-bark", "50% 35%"), "rosehip": ("ai-rosehip", "20% 70%"), "wormwood": ("ai-wormwood", "50% 50%"),
          "propolis": ("ai-propolis", "50% 50%")}
def _jh(i, h):
    bg, fg, ac = HCOL[h[0]]
    img, pos = HPHOTO[h[0]]
    return ('<article class="hslide%s" role="group" aria-roledescription="slide" aria-label="%d of 7" data-bg="%s" data-fg="%s" data-ac="%s"><div class="hcopy"><h2>%s</h2><p class="lat">%s</p><p class="jp">%s</p></div>'
            '<figure class="hph ph"><img src="@@img:%s@@" style="object-position:%s" alt="%s (illustrative image)" loading="lazy"><figcaption>Illustrative image</figcaption></figure></article>') % (
            " on" if i == 0 else "", i + 1, bg, fg, ac, h[1], h[2], h[4], img, pos, h[3])
TOK["JHERBS"] = "".join(_jh(i, h) for i, h in enumerate(P.HERBS))
TOK["JHDOTS"] = "".join('<button type="button" class="hdot%s" role="tab" aria-label="%s" aria-selected="%s" data-i="%d"></button>' % (" on" if i == 0 else "", h[1], "true" if i == 0 else "false", i) for i, h in enumerate(P.HERBS))
TOK["JALL"] = "".join(X.jcard(a) for a in X.ARTICLES)
TOK["JHOME"] = TOK["JALL"] + "".join(_bcard(a, i) for i, a in enumerate(B.ARTICLES[:4] + [B.DYS]))

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
P.PHEROS["LEARN"] = P.phero("Learn", "Learn", "Gut health guides, ingredients and science", "Gut health guides, a blog with sourced answers on microbiome tests, probiotics and fermented foods, and the ingredients and science behind the range.")
P.PHEROS["ABOUT"] = P.phero("About", "About Herbaferm", "A Hungarian formula, in Singapore", "Who we are, where the range comes from, and the documents behind it.")
for _k in ("LEARN", "ABOUT"):
    TOK["PHERO_" + _k] = P.PHEROS[_k]
_merge("learn", "PHERO_LEARN", [("learn", "sec-guides", "Guides", "How to use the range, and the plain-English story behind it."),
        ("ingredients", "sec-ingredients", "Ingredients", "Seven herbs. Tap one to see what it is and which products use it. Descriptions refer to traditional use, not to health effects."),
        ("science", "sec-science", "Science", "How fermentation works and what each study does and does not cover."),
        ("blog", "sec-blog", "Gut health blog", "Plain-language answers to the questions people search for, each with named sources.")],
       [("learn", "sec-guides", "Guides"), ("ingredients", "sec-ingredients", "Ingredients"), ("science", "sec-science", "Science"), ("blog", "sec-blog", "Blog")])
_merge("about", "PHERO_ABOUT", [("about", "sec-about", "Our story", "Who is behind Herbaferm and what we stand for."),
        ("awards", "sec-awards", "Awards", "What Herbaferm has been recognised for, and what is still to be confirmed."),
        ("quality", "sec-quality", "Quality and documents", "Registrations, lab documents and manufacturing information, with what is still being updated.")],
       [("about", "sec-about", "Our story"), ("awards", "sec-awards", "Awards"), ("quality", "sec-quality", "Quality")])

def _band(pid, before, img, alt, cap):
    """Insert a wide illustrative image band before the first occurrence of `before` on page pid."""
    fig = ('<section class="band"><div class="wrap"><figure><img src="@@img:%s@@" alt="%s (illustrative image)" loading="lazy">'
           '<figcaption><span>%s</span><span class="ill">Illustrative image</span></figcaption></figure></div></section>') % (img, alt, cap)
    for i, (k, t, h) in enumerate(P.PAGES):
        if k == pid and before in h:
            at = h.index(before)
            if before.startswith("<h"):
                at = h.rindex("<section", 0, at)
            P.PAGES[i] = (k, t, h[:at] + fig + h[at:])
            return
    raise SystemExit("band anchor not found: %s %s" % (pid, before))
_band("partners", '<h2>Five places to find Herbaferm</h2>', "ai-jars", "Chamomile and yarrow fermenting in glass jars", "Fermented in small batches, then bottled")
_band("about", '<section class="subhead" id="sec-awards">', "ai-field", "A flowering meadow with chamomile and yarrow", "A Hungarian formula built on traditional herbs")
_band("learn", '<section class="subhead" id="sec-science">', "ai-kitchen", "A glass of water, a dropper bottle and a bowl of oats on a kitchen counter", "Part of an ordinary morning")


# ---------- SEO: keyword-led titles and meta descriptions (brand deck slide 29) ----------
TITLES = {
    "home": "Herbaferm Singapore | Fermented herbal gut health supplements",
    "shop": "Gut health supplements in Singapore | Herbaferm shop",
    "drops": "Herbaferm Drops | Fermented herbal drops, Singapore",
    "fiber": "Fiber Elite | Fibre add-in for smoothies, porridge and yoghurt",
    "prefer": "Prefer HF400 | Fermented herb fibre capsules, Singapore",
    "learn": "Gut health guides and blog: microbiome, probiotics, fermented foods | Herbaferm",
    "about": "About Herbaferm | Awards, quality and the team behind the supplements",
    "partners": "Partners | Stock Herbaferm gut health supplements in your clinic or shop",
    "faq": "FAQ | Gut health supplement questions answered | Herbaferm Singapore",
    "contact": "Contact | Herbaferm Singapore",
}
DESCS = {
    "home": "Herbaferm brings fermented herbal food supplements from Hungary to Singapore: Drops, Fiber Elite and Prefer HF400. Gut health guides with sources.",
    "shop": "Shop Herbaferm gut health supplements in Singapore: Drops, Fiber Elite and Prefer HF400. Food supplements, with ingredients and usage explained.",
    "drops": "Herbaferm Drops: a fermented herbal extract of seven herbs, taken in a glass of water. A food supplement. Usage, storage and ingredients.",
    "fiber": "Fiber Elite is a fibre-rich food additive for smoothies, shakes, yoghurt and porridge. See ingredients, usage ideas and allergen information.",
    "prefer": "Prefer HF400 capsules contain fermented herb fibres and are taken alongside Herbaferm Drops. Food supplement, 14 capsules.",
    "learn": "Plain-language gut health guides: microbiome tests in Singapore, supplements, probiotics, fermented foods and microbial dysbiosis, each with named sources.",
    "about": "Who is behind Herbaferm, the awards it has received and the quality documents behind its fermented herbal food supplements.",
    "partners": "Clinics, pharmacies and retailers: how to stock Herbaferm fermented herbal food supplements in Singapore and request the partner pack.",
    "faq": "Answers on using, storing and buying Herbaferm Drops, Fiber Elite and Prefer HF400, and on how food supplements are regulated in Singapore.",
    "contact": "Contact Herbaferm Singapore for questions, orders and partner enquiries.",
}
P.PAGES = [(k, TITLES.get(k, t), h) for k, t, h in P.PAGES]

pages_html = ""
for pid, title, body in P.PAGES:
    hidden = "" if pid == "home" else " hidden"
    pages_html += '<main class="page" id="p-%s" data-title="%s" data-desc="%s"%s>%s</main>\n' % (pid, title, DESCS.get(pid, DESCS["home"]), hidden, body)

cart_svg = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 7h14l-1.3 10.2a2 2 0 0 1-2 1.8H8.3a2 2 0 0 1-2-1.8z"/><path d="M9 7a3 3 0 0 1 6 0"/></svg>'

shell = '''<meta charset="utf-8">
<title>Herbaferm Singapore</title>
<style>
__CSS__
</style>
<div class="proto">Design prototype for review. Items marked <span class="tag">To confirm</span> or <span class="tag">To supply</span> need Herbaferm's input before launch.</div>
<header class="top"><div class="wrap nav">
  <a class="brand" href="#home" aria-label="Herbaferm Singapore home"><span class="lg" role="img" aria-label="herbaferm, Vitality &amp; Balance"></span></a>
  <nav aria-label="Main">__NAV__</nav>
  <button class="icon-btn" id="search-open" type="button" aria-label="Search the site"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="6.5"/><path d="M16 16l4.5 4.5"/></svg><span class="sl">Search</span></button>
  <button class="icon-btn" id="theme" type="button">Dark</button>
  <button class="icon-btn" id="cart-open" type="button" aria-label="Open cart">__CART__<span class="cart-n" id="cart-n" hidden>0</span></button>
  <button class="icon-btn burger" id="burger" type="button" aria-label="Menu">Menu</button>
</div><div class="mnav">__MNAV__</div></header>
__PAGES__
<footer class="site"><div class="wrap">
  <div class="grid">
    <div><span class="lg lg-foot" role="img" aria-label="herbaferm, Vitality &amp; Balance"></span>Fermented herbal food supplements, available in Singapore.<br><br>Herbaferm Pte. Ltd.<br>UEN 202350449W<p class="soc"><a href="https://www.instagram.com/herbaferm_singapore_/" target="_blank" rel="noopener" aria-label="Herbaferm Singapore on Instagram (opens in a new tab)"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.3" cy="6.7" r="1" fill="currentColor" stroke="none"/></svg></a><a href="https://www.facebook.com/people/Herbaferm-Singapore/61569904427139/" target="_blank" rel="noopener" aria-label="Herbaferm Singapore on Facebook (opens in a new tab)"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M14 8.5V7c0-.8.4-1.2 1.3-1.2H17V3h-2.5C11.8 3 10.5 4.6 10.5 6.8v1.7H8V12h2.5v9H14v-9h2.6l.4-3.5z"/></svg></a></p></div>
    <div><h4>Shop</h4><a href="#drops">Herbaferm Drops</a><a href="#fiber">Fiber Elite</a><a href="#prefer">Prefer HF400</a></div>
    <div><h4>Learn</h4><a href="#learn">Guides</a><a href="#ingredients">Ingredients</a><a href="#science">Science</a><a href="#blog">Gut health blog</a><a href="learn/microbial-dysbiosis/">Microbial dysbiosis</a><a href="#about">About</a><a href="#awards">Awards</a><a href="#quality">Quality</a></div>
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
<button class="chat-fab" id="chat-fab" type="button" aria-label="Chat with Herby"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 5h14a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2h-7l-5 4v-4H5a2 2 0 0 1-2-2V7a2 2 0 0 1 2-2z"/></svg><span>Ask Herby</span></button>
<div class="chat" id="chat" role="dialog" aria-label="Herby, the Herbaferm assistant">
  <header><div class="dot">h</div><div><b>Herby</b><small>Herbaferm helper. Prototype, not medical advice.</small></div><button id="chat-big" type="button" aria-label="Expand chat window" aria-pressed="false"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path class="ex" d="M14 4h6v6M10 20H4v-6M20 4l-7 7M4 20l7-7"/><path class="co" d="M20 10h-6V4M4 14h6v6M14 10l7-7M3 21l7-7"/></svg></button><button id="chat-close" type="button" aria-label="Close chat">&times;</button></header>
  <div class="log" id="chat-log" aria-live="polite"></div>
  <div class="sugg" id="chat-sugg"></div>
  <form id="chat-form"><textarea id="chat-in" rows="1" maxlength="500" placeholder="Ask about the products" aria-label="Your question" autocomplete="off"></textarea><button id="chat-send" type="submit">Send</button></form>
</div>
<script>
__JS__
</script>
'''

out = shell
out = out.replace("__CSS__", CSS)
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
for _a in B.ARTICLES + [B.DYS]:
    idx.append({"id": _a["slug"], "t": _a["title"], "k": "Guide", "x": _txt(_a["dek"] + " " + _a["body"])[:1600], "u": "learn/%s/" % _a["slug"]})
out_js_pending = True
SEARCH_JS = "window.HFIDX=" + json.dumps(idx, ensure_ascii=False, separators=(",", ":")) + ";\n"
out = out.replace("__JS__", SEARCH_JS + ((root / "src/site.js").read_text() + "\n" + (root / "src/journey.js").read_text() + "\n" + (root / "src/reviews.js").read_text()) + "\n" + (root / "src/chat.js").read_text())
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
    css = CSS
    site_js = ((root / "src/site.js").read_text() + "\n" + (root / "src/journey.js").read_text() + "\n" + (root / "src/reviews.js").read_text())
    chat_js = (root / "src/chat.js").read_text()
    html = out_pre
    html = html.replace("<style>\n" + css + "\n</style>", '<link rel="stylesheet" href="css/site.css">')
    html = html.replace("<script>\n" + SEARCH_JS + site_js + "\n" + chat_js + "\n</script>",
                        '<script src="js/search-index.js"></script>\n<script src="js/site.js"></script>\n<script src="js/chat.js"></script>')
    assert "css/site.css" in html and "js/chat.js" in html, "shell replacement failed"
    import seo as S
    from urllib.parse import urlparse
    PREFIX = urlparse(SITE_URL).path or "/"
    # ---- routes: every page gets a real URL
    ROUTES = {"home": ""}
    for _pid, _t, _hh in ORIG_PAGES:
        ROUTES[_pid] = "guides/%s/" % _pid[2:] if _pid.startswith("a-") else "%s/" % _pid
    ROUTES["home"] = ""
    ROUTES["blog"] = "blog/"
    HOSTS = {"ingredients": "learn", "science": "learn", "blog": "learn", "quality": "about", "awards": "about"}
    T2, D2 = dict(TITLES), dict(DESCS)
    T2.update({"ingredients": "Ingredients | The seven herbs in Herbaferm Drops", "science": "Science | How fermentation works and what each study covers",
               "blog": "Gut health blog | Sourced answers to common questions | Herbaferm", "awards": "Awards | TOP 10 Winner, Longevity Breakthrough Awards 2026",
               "quality": "Quality and documents | Herbaferm Singapore", "policies": "Policies | Herbaferm Singapore", "insight": "Design evidence | Herbaferm Singapore"})
    D2.update({"ingredients": "Seven herbs, described by traditional use: chamomile, yarrow, elderflower, rosehip, propolis, oak bark and white wormwood.",
               "science": "How natural fermentation works, and what each study related to Herbaferm does and does not cover.",
               "blog": "Plain-language gut health answers: microbiome tests, supplements, probiotics, fermented foods and dysbiosis, each with named sources.",
               "awards": "Herbaferm was named a TOP 10 Winner at the TOP 10 Longevity Breakthrough Awards 2026 and received a CIM Gold Award.",
               "quality": "Registrations, lab documents and manufacturing information for the Herbaferm range, with what is still being updated.",
               "policies": "Shipping, returns, privacy and terms for Herbaferm Singapore.", "insight": "Design evidence behind the prototype."})
    for _a in X.ARTICLES:
        T2[_a[0]] = "%s | Herbaferm Journal" % _a[3]
        D2[_a[0]] = _a[4]
    META = {r: [T2.get(r, T2["home"]), D2.get(r, D2["home"])] for r in ROUTES}
    GLOBALS = ('<script>window.HF_BASE=%s;window.HF_ORIGIN=%s;window.HF_ROUTES=%s;window.HF_META=%s;</script>\n'
               % tuple(json.dumps(x, ensure_ascii=False, separators=(",", ":")) for x in (PREFIX, SITE_URL, ROUTES, META)))

    def fix_links(h, rel=r"(?:\.\./)*"):
        """#page links -> real paths; asset and learn/ links -> absolute-from-site-root paths."""
        h = re.sub(r'href="%s#([\w-]+)"' % rel, lambda m: 'href="%s%s"' % (PREFIX, ROUTES[m.group(1)]) if m.group(1) in ROUTES else m.group(0), h)
        h = re.sub(r'(href|src)="(?:\.\./)*(css|js|assets|learn|guides)/', lambda m: '%s="%s%s/' % (m.group(1), PREFIX, m.group(2)), h)
        h = re.sub(r"url\(assets/", "url(%sassets/" % PREFIX, h)
        return h

    HEAD = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            '<title>{title}</title>\n<meta name="description" content="{desc}">\n<link rel="canonical" href="{url}">\n{robots}'
            '<meta property="og:type" content="website">\n<meta property="og:site_name" content="Herbaferm Singapore">\n<meta property="og:title" content="{title}">\n'
            '<meta property="og:description" content="{desc}">\n<meta property="og:url" content="{url}">\n<meta property="og:image" content="{og_img}">\n'
            '<meta name="twitter:card" content="summary_large_image">\n'
            '<meta name="theme-color" content="#1f4d34">\n<link rel="icon" href="' + PREFIX + 'assets/logo/favicon-32.png" sizes="32x32" type="image/png">\n<link rel="icon" href="' + PREFIX + 'assets/logo/favicon-64.png" sizes="64x64" type="image/png">\n<link rel="apple-touch-icon" href="' + PREFIX + 'assets/logo/apple-touch-icon.png">\n<link rel="stylesheet" href="' + PREFIX + 'css/site.css">\n')
    rest = html.replace('<meta charset="utf-8">\n<title>Herbaferm Singapore</title>', "", 1)
    rest = rest.replace('<link rel="stylesheet" href="css/site.css">', '</head>\n<body>', 1)
    rest = rest.split("</head>\n<body>", 1)[1] + "\n</body>\n</html>\n"
    rest = re.sub(r"@@img:([a-z\-]+)@@", lambda m: "assets/images/%s.jpg" % IMGS[m.group(1)], rest)
    rest = re.sub(r'<script src="js/', '<script src="' + PREFIX + 'js/', rest)
    rest = fix_links(rest)

    def doc(route):
        host = HOSTS.get(route, route)
        def vis(m):
            attrs = m.group(2).replace(" hidden", "")
            return '<main class="page" id="p-%s"%s%s>' % (m.group(1), attrs, "" if m.group(1) == host else " hidden")
        body = re.sub(r'<main class="page" id="p-([\w-]+)"([^>]*)>', vis, rest)
        t, d = META[route]
        url = SITE_URL + ROUTES[route]
        og = SITE_URL + "assets/logo/og-logo.jpg"
        head = HEAD.format(title=_h.escape(t), desc=_h.escape(d), url=url, og_img=og,
                           robots='<meta name="robots" content="noindex">\n' if route == "insight" else "")
        return head + GLOBALS + S.route_ld(route, SITE_URL, ROUTES, P.FAQS, t) + "</head>\n<body>\n" + '<a class="skip" href="#main" onclick="var m=document.querySelector(\'main.page:not([hidden])\');if(m){m.setAttribute(\'tabindex\',\'-1\');m.focus();event.preventDefault()}">Skip to content</a>\n' + body
    for r in ROUTES:
        if r == "home":
            (dest / "index.html").write_text(doc(r))
        else:
            d = dest / ROUTES[r]
            d.mkdir(parents=True, exist_ok=True)
            (d / "index.html").write_text(doc(r))
    # --- standalone article pages + robots.txt + sitemap.xml
    hdr = re.search(r'<header class="top">.*?</header>', out_pre, re.S).group(0)
    hdr = re.sub(r'<button class="icon-btn" id="(search-open|cart-open)".*?</button>\s*', "", hdr, flags=re.S)
    hdr = '<a class="skip" href="#main">Skip to content</a>\n<div class="proto">Design prototype for review. Items marked <span class="tag">To confirm</span> or <span class="tag">To supply</span> need Herbaferm\'s input before launch.</div>\n' + fix_links(hdr)
    ftr = fix_links(re.search(r'<footer class="site">.*?</footer>', out_pre, re.S).group(0))
    ftr = ftr.replace('<button type="button" id="still" class="linkbtn" aria-pressed="false">Pause motion</button>', "")
    shead = HEAD
    allp = B.ARTICLES + [B.DYS]
    for a in allp:
        others = [o for o in allp if o is not a][(allp.index(a) % 4):(allp.index(a) % 4) + 2] if a is not B.DYS else allp[:2]
        d = dest / "learn" / a["slug"]
        d.mkdir(parents=True, exist_ok=True)
        page = S.article_html(a, others, SITE_URL, shead, hdr, ftr, ROUTES)
        (d / "index.html").write_text(fix_links(page).replace('src="../../assets/', 'src="%sassets/' % PREFIX))
    nf = (HEAD.format(title="Page not found | Herbaferm", desc="This page could not be found.", url=SITE_URL, og_img=SITE_URL + "assets/logo/og-logo.jpg",
                      robots='<meta name="robots" content="noindex">\n') + "</head>\n<body>\n" + hdr
          + '<main id="main"><div class="phero"><div class="wrap"><p class="kicker">404</p><h1>We could not find that page</h1>'
          + '<p class="lede">The link may be old or mistyped. Try the home page, the shop or the gut health guides.</p>'
          + '<p><a class="btn" href="%s">Home</a> <a class="btn" href="%s">Shop</a> <a class="btn" href="%s">Learn</a></p></div></div></main>\n' % (PREFIX, PREFIX + ROUTES["shop"], PREFIX + ROUTES["learn"])
          + ftr + "\n</body>\n</html>\n")
    (dest / "404.html").write_text(fix_links(nf))
    (dest / "robots.txt").write_text(S.robots(SITE_URL))
    (dest / "sitemap.xml").write_text(S.sitemap(SITE_URL, [r for r in ROUTES if r != "insight"], ROUTES))
    (dest / "css/site.css").write_text(css)
    (dest / "js/search-index.js").write_text(SEARCH_JS)
    (dest / "js/site.js").write_text(site_js)
    (dest / "js/chat.js").write_text(chat_js)
    _pages_txt = rest + "".join(f.read_text() for f in dest.glob("learn/*/index.html"))
    used = set(re.findall(r"assets/images/([\w\-]+\.jpg)", _pages_txt)) | {"ai-morning.jpg", "book-microbiome.jpg", "hero-bark.jpg"}
    for f in used:
        shutil.copy(root / "assets" / f, dest / "assets/images" / f)
    (dest / "assets/favicon.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="8" fill="#1f4d34"/><path d="M16 7c5 3 7 8 4 13-1 2-3 3-4 5-1-2-3-3-4-5-3-5-1-10 4-13z" fill="#eaf3ea"/></svg>')
    shutil.copytree(root / "assets" / "logo", dest / "assets/logo", dirs_exist_ok=True)
    # cache-bust: tie asset URLs to their content so browsers never mix old and new files
    import hashlib
    _ver = hashlib.md5((css + SEARCH_JS + site_js + chat_js).encode()).hexdigest()[:8]
    for _f in list(dest.rglob("*.html")):
        _t = _f.read_text()
        _n = re.sub(r'((?:css/site\.css|js/(?:site|chat|search-index)\.js))"', lambda m: m.group(1) + "?v=" + _ver + '"', _t)
        if _n != _t:
            _f.write_text(_n)
    print("site ->", dest, len(used), "images")

if "--site" in sys.argv:
    make_site(sys.argv[sys.argv.index("--site") + 1])
