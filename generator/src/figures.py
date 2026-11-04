"""Inline SVG figures for the blog (they follow the page theme, so they work in dark mode) and photo figures."""

F = 'font-family="Figtree,system-ui,sans-serif"'


def _svg(label, inner, caption, h=300):
    return ('<figure class="afig svgfig"><svg viewBox="0 0 720 %d" role="img" aria-label="%s" xmlns="http://www.w3.org/2000/svg">%s</svg>'
            '<figcaption>%s</figcaption></figure>') % (h, label, inner, caption)


def _t(x, y, s, size=17, weight=600, fill="var(--fg)", anchor="middle"):
    return '<text x="%s" y="%s" %s font-size="%s" font-weight="%s" fill="%s" text-anchor="%s">%s</text>' % (x, y, F, size, weight, fill, anchor, s)


def _arrow(x1, x2, y):
    return ('<path d="M%s %s H%s" stroke="var(--muted)" stroke-width="2.5" stroke-linecap="round"/>'
            '<path d="M%s %s l-9 -7 M%s %s l-9 7" stroke="var(--muted)" stroke-width="2.5" stroke-linecap="round"/>') % (x1, y, x2, x2, y, x2, y)


def kit():
    s = ""
    for i, (title, sub) in enumerate([("1  Collect", "Small stool sample at home"), ("2  Sequence", "Lab reads microbial DNA"), ("3  Report", "Types and proportions found")]):
        x = 20 + i * 235
        s += '<rect x="%d" y="30" width="210" height="190" rx="18" fill="var(--surface)" stroke="var(--line)" stroke-width="2"/>' % x
        cx = x + 105
        if i == 0:   # sample tube
            s += ('<rect x="%d" y="62" width="34" height="80" rx="8" fill="none" stroke="var(--leaf)" stroke-width="4"/>'
                  '<rect x="%d" y="100" width="26" height="36" rx="5" fill="var(--honey)"/><rect x="%d" y="56" width="42" height="12" rx="4" fill="var(--leaf)"/>') % (cx - 17, cx - 13, cx - 21)
        elif i == 1:  # sequence bars
            for k, (c, hh) in enumerate([("var(--leaf)", 60), ("var(--honey)", 90), ("var(--leaf)", 45), ("var(--honey)", 75), ("var(--leaf)", 100)]):
                s += '<rect x="%d" y="%d" width="14" height="%d" rx="4" fill="%s"/>' % (cx - 50 + k * 22, 140 - hh, hh, c)
        else:         # report bars
            for k, hh in enumerate([95, 60, 40, 25]):
                s += '<rect x="%d" y="%d" width="26" height="%d" rx="5" fill="var(--leaf)" opacity="%.2f"/>' % (cx - 58 + k * 32, 140 - hh, hh, 1 - k * 0.2)
        s += _t(cx, 175, title, 19, 700) + _t(cx, 198, sub, 14, 500, "var(--muted)")
        if i < 2:
            s += _arrow(x + 214, x + 232, 125)
    s += _t(360, 262, "Result: which microbes were detected in one sample. It is not a diagnosis.", 15, 600, "var(--muted)")
    return _svg("Three steps of a stool microbiome test: collect a sample, sequence the DNA, receive a report", s,
                "How a stool microbiome test works (schematic). Results can differ between providers.", 285)


def triad():
    s = ""
    items = [("Probiotic", "Live microbes", "that benefit the person taking them"), ("Prebiotic", "Food for microbes", "already living in the gut"), ("Postbiotic", "Non-living microbes", "and their components")]
    for i, (a, b, c) in enumerate(items):
        x = 20 + i * 235
        cx = x + 105
        s += '<rect x="%d" y="24" width="210" height="220" rx="18" fill="var(--surface)" stroke="var(--line)" stroke-width="2"/>' % x
        if i == 0:
            for k, (dx, dy) in enumerate([(-30, 0), (0, -18), (28, 4), (-8, 24), (20, 30)]):
                s += '<circle cx="%d" cy="%d" r="14" fill="var(--leaf)"/><circle cx="%d" cy="%d" r="5" fill="var(--surface)"/>' % (cx + dx, 92 + dy, cx + dx, 92 + dy)
        elif i == 1:
            for k in range(6):
                s += '<rect x="%d" y="%d" width="46" height="12" rx="6" fill="var(--honey)" transform="rotate(%d %d %d)"/>' % (cx - 23 + (k % 3) * 4, 66 + k * 11, -12 + k * 6, cx, 92)
        else:
            for k, (dx, dy) in enumerate([(-30, 0), (0, -18), (28, 4), (-8, 24), (20, 30)]):
                s += '<circle cx="%d" cy="%d" r="14" fill="none" stroke="var(--leaf)" stroke-width="3" stroke-dasharray="5 5"/>' % (cx + dx, 92 + dy)
        s += _t(cx, 168, a, 21, 700) + _t(cx, 194, b, 15, 600) + _t(cx, 214, c, 13, 500, "var(--muted)")
    return _svg("Probiotic, prebiotic and postbiotic compared: live microbes, food for microbes, and non-living microbes with their components", s,
                "The three ISAPP definitions in one picture (schematic).", 265)


def pillars():
    pos = [(110, 62, "Normal digestion", "and absorption"), (610, 62, "An effective", "gut barrier"), (110, 238, "A balanced", "microbial community"), (610, 238, "A well-working", "gut immune system")]
    s = "".join('<path d="M360 150 L%d %d" stroke="var(--line)" stroke-width="3"/>' % (x, y) for x, y, a, b in pos)
    s += '<circle cx="360" cy="150" r="60" fill="var(--leaf)"/>' + _t(360, 146, "Gut", 19, 700, "var(--forest-ink)") + _t(360, 168, "health", 19, 700, "var(--forest-ink)")
    for x, y, a, b in pos:
        s += '<rect x="%d" y="%d" width="200" height="64" rx="14" fill="var(--surface)" stroke="var(--line)" stroke-width="2"/>' % (x - 100, y - 32)
        s += _t(x, y - 4, a, 16, 700) + _t(x, y + 17, b, 14, 500, "var(--muted)")
    return _svg("Four elements often included in the definition of gut health: digestion and absorption, the gut barrier, the microbial community and the gut immune system", s,
                "Elements commonly included in definitions of gut health, after Bischoff (2011). There is no single agreed test.", 300)


def checklist():
    s = ""
    rows = [("Type is clear", "live microbes, fibre or fermented extract"), ("Evidence for this exact product", "same ingredient or strain and dose"), ("Independent testing", "batch certificate or lab report"),
            ("Modest, accurate claims", "no cure or detox wording, no \"HSA approved\""), ("Fits your routine", "storage, cost per day, taste")]
    for i, (a, b) in enumerate(rows):
        y = 18 + i * 52
        s += '<rect x="20" y="%d" width="680" height="44" rx="12" fill="var(--surface)" stroke="var(--line)" stroke-width="2"/>' % y
        s += '<circle cx="48" cy="%d" r="14" fill="var(--leaf)"/><path d="M41 %d l5 5 l9 -10" stroke="var(--forest-ink)" stroke-width="3.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>' % (y + 22, y + 22)
        s += _t(76, y + 28, a, 17, 700, anchor="start") + _t(690, y + 28, b, 14, 500, "var(--muted)", "end")
    return _svg("Five-point checklist for comparing gut health supplements", s, "A quick checklist for comparing gut health supplements.", 285)


def evidence():
    s = ""
    rows = [("Guidelines and systematic reviews", 330, 1.0), ("Controlled trials", 380, .8), ("Observational studies", 430, .6), ("Expert opinion", 480, .45), ("Testimonials and star ratings", 530, .3)]
    for i, (a, w, op) in enumerate(rows):
        y = 16 + i * 50
        x = 360 - w / 2
        s += '<rect x="%s" y="%d" width="%d" height="42" rx="10" fill="var(--leaf)" opacity="%s"/>' % (x, y, w, op)
        s += _t(360, y + 27, a, 15, 700, "var(--forest-ink)" if op > .55 else "var(--fg)")
    s += _t(24, 40, "Stronger", 14, 700, "var(--muted)", "start") + _t(24, 252, "Weaker", 14, 700, "var(--muted)", "start")
    return _svg("Evidence ladder from guidelines and systematic reviews at the top to testimonials and star ratings at the bottom", s,
                "Typical strength of evidence for a health claim (schematic).", 285)


def dysbiosis():
    import random
    rnd = random.Random(7)
    cols = ["var(--leaf)", "var(--honey)", "#6aa5c9", "#c9707a", "#9a82c4", "#7fb06a"]
    s = ""
    panels = [("Eubiosis", "A diverse, balanced community", [(c, rnd.choice([9, 11, 13])) for c in cols * 4]),
              ("Dysbiosis", "Fewer types; one group dominates", [(cols[1], 17)] * 6 + [(cols[0], 8)] * 3 + [(cols[3], 7)] * 2),
              ("Rebiosis", "Diversity recovering over time", [(c, rnd.choice([8, 10, 12])) for c in cols * 3])]
    for i, (a, b, dots) in enumerate(panels):
        cx = 20 + i * 235 + 105
        s += '<rect x="%d" y="20" width="210" height="260" rx="18" fill="var(--surface)" stroke="var(--line)" stroke-width="2"/>' % (cx - 105)
        s += '<circle cx="%d" cy="115" r="78" fill="var(--surface2)"/>' % cx
        for c, r in dots:
            import math
            ang = rnd.random() * 6.283
            dist = (rnd.random() ** 0.5) * (68 - r)
            s += '<circle cx="%.1f" cy="%.1f" r="%d" fill="%s" opacity=".9"/>' % (cx + dist * math.cos(ang), 115 + dist * math.sin(ang), r, c)
        s += _t(cx, 225, a, 21, 700) + _t(cx, 249, b, 13, 500, "var(--muted)")
    return _svg("Three stages: eubiosis is a diverse balanced community, dysbiosis is an imbalanced one, rebiosis is the community recovering", s,
                "Eubiosis, dysbiosis and rebiosis as an image (schematic, not to scale). Rebiosis is a term used by Herbaferm's founder, not a clinical term.", 300)


PHOTOS = {
    "ai-morning": "A glass of water and a dropper bottle on a kitchen counter",
    "ai-herbs": "Bowls of dried chamomile, elderflower, oak bark and rosehip on linen",
    "ai-porridge": "A spoon of fibre powder stirred into porridge with berries and seeds",
    "ai-jars": "Chamomile and yarrow fermenting in glass jars",
    "ai-meadow": "A flowering meadow with chamomile and yarrow at sunset",
    "ai-clinic": "A calm clinic reception with plants and warm wood panelling",
    "ai-shelf": "Glass jars of dried herbs on a rustic wooden shelf",
    "ai-chamomile": "A wooden bowl of dried chamomile and yarrow on linen",
    "ai-fridge": "Small dark bottles and a jar of fermented plants on a fridge door shelf",
    "ai-field": "A flowering field of chamomile and yarrow at sunset",
}
BANNER = {"microbiome-test-singapore": ("ai-clinic", 900), "best-supplements-for-gut-health": ("ai-shelf", 1315),
          "gut-health-supplement-reviews": ("ai-chamomile", 1300), "best-probiotics-for-gut-health": ("ai-fridge", 1400),
          "what-is-gut-health": ("ai-field", 900)}


def banner(slug):
    if slug not in BANNER:
        return ""
    n, h = BANNER[slug]
    return ('<figure class="aband"><img src="../../assets/images/%s.jpg" alt="%s" loading="eager" decoding="async">'
            '<figcaption>Illustrative image, AI-generated</figcaption></figure>') % (n, PHOTOS[n])


SVGS = {"kit": kit, "triad": triad, "pillars": pillars, "checklist": checklist, "evidence": evidence, "dysbiosis": dysbiosis}


def fig(name):
    if name in SVGS:
        return SVGS[name]()
    return ('<figure class="afig"><img src="../../assets/images/%s.jpg" alt="%s" width="1400" height="%d" loading="lazy">'
            '<figcaption>Illustrative image, AI-generated</figcaption></figure>') % (name, PHOTOS[name], 787 if name == "ai-meadow" else 1046)
