"""SEO / AIO helpers: JSON-LD, standalone article pages, robots.txt and sitemap.xml (slides 29-31 of the brand deck)."""
import html as _h, json, re
import blog as B
import figures as FG

ORG = {
    "@type": "Organization", "@id": "{base}#org", "name": "Herbaferm Pte. Ltd.", "alternateName": "Herbaferm Singapore",
    "url": "{base}", "logo": "{base}assets/logo/wordmark-green.png",
    "description": "Singapore company bringing Herbaferm's fermented herbal food supplements from Hungary to Singapore.",
    "identifier": "UEN 202350449W",
    "address": {"@type": "PostalAddress", "streetAddress": "10 Anson Road #22-02 International Plaza", "addressLocality": "Singapore", "postalCode": "079903", "addressCountry": "SG"},
    # Slide 31: link the SG and group sites so search engines see one organisation. Confirm the list with Herbaferm.
    "sameAs": ["https://herbaferm.hu/", "https://rebiotika.co.uk/", "https://rebiotika.de/"],
}
PRODUCTS = [  # id, name, description, price (SGD), image
    ("drops", "Herbaferm Drops", "Herbal extract made by natural fermentation of seven herbs, taken in a glass of water. 30 ml food supplement.", 55, "drops.jpg"),
    ("fiber", "Fiber Elite", "A fibre-rich food additive for smoothies, shakes, yoghurt and porridge. 125 g food supplement.", 55, "fiber.jpg"),
    ("prefer", "Prefer HF400", "Capsules of fermented herb fibres, taken alongside Drops. 14 capsules, food supplement.", 45, "prefer.jpg"),
]


def sub(o, base):
    if isinstance(o, str):
        return o.replace("{base}", base)
    if isinstance(o, list):
        return [sub(x, base) for x in o]
    if isinstance(o, dict):
        return {k: sub(v, base) for k, v in o.items()}
    return o


def ld(*objs):
    return "".join('<script type="application/ld+json">%s</script>\n' % json.dumps(o, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/") for o in objs)


def strip(t):
    t = re.sub(r"<[^>]+>", "", t)
    return re.sub(r"\s+", " ", _h.unescape(t)).strip()


def faq_ld(pairs):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in pairs]}


def route_ld(route, base, routes, faqs, title):
    """JSON-LD for one SPA route: Organization and WebSite everywhere, Product on shop and product pages,
    FAQPage on /faq/ (confirmed answers only), BreadcrumbList on every page except home."""
    org = sub(dict(ORG, **{"@context": "https://schema.org"}), base)
    site = {"@context": "https://schema.org", "@type": "WebSite", "name": "Herbaferm Singapore", "url": base, "publisher": {"@id": base + "#org"}}
    out = [org, site]
    for pid, name, desc, price, img in PRODUCTS:
        if route in ("shop", pid):
            out.append({"@context": "https://schema.org", "@type": "Product", "name": name, "description": desc,
                        "image": base + "assets/images/" + img, "brand": {"@type": "Brand", "name": "Herbaferm"},
                        "url": base + routes[pid],
                        # availability left out on purpose: checkout is not connected yet
                        "offers": {"@type": "Offer", "price": str(price), "priceCurrency": "SGD", "url": base + routes[pid], "seller": {"@id": base + "#org"}}})
    if route == "faq":
        out.append(faq_ld([(q, strip(a)) for _c, q, a in faqs if 'class="tag"' not in a]))
    if route != "home":
        out.append({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": base},
            {"@type": "ListItem", "position": 2, "name": title.split(" | ")[0], "item": base + routes[route]}]})
    return ld(*out)


def _cite(body_parts, used):
    def one(m):
        k = m.group(1)
        assert k in B.REFS, k
        if k not in used:
            used.append(k)
        n = used.index(k) + 1
        return '<sup class="cite"><a href="#ref-%d" aria-label="Reference %d">[%d]</a></sup>' % (n, n, n)
    return [re.sub(r"\{\{r:(\w+)\}\}", one, p) for p in body_parts]


def article_html(a, others, base, shell_head, header, footer, routes):
    """Full standalone page for one blog article (a is a dict from blog.ARTICLES or blog.DYS)."""
    used = []
    short_html, body, faq_html_ = None, None, None
    short = _cite(a["short"], used)
    body = _cite([a["body"]], used)[0]
    body = re.sub(r"\{\{fig:(\w+)\}\}", lambda m: FG.fig(m.group(1)), body)
    hero = FG.fig(B.HERO[a["slug"]])
    def _lab(m):
        t = m.group(0)
        heads = [strip(x) for x in re.findall(r"<th>(.*?)</th>", t)]
        def row(r):
            i = [0]
            def td(c):
                l = heads[i[0]] if i[0] < len(heads) else ""
                i[0] += 1
                return '<td data-l="%s">' % l
            return re.sub(r"<td>", td, r.group(0))
        return '<div class="tscroll">' + re.sub(r"<tr>.*?</tr>", row, t, flags=re.S) + "</div>"
    body = re.sub(r"<table.*?</table>", _lab, body, flags=re.S)
    refs = "".join('<li id="ref-%d">%s <a href="%s" target="_blank" rel="noopener">Source</a></li>' % (i + 1, B.REFS[k][0], B.REFS[k][1]) for i, k in enumerate(used))
    faq = "".join("<details><summary>%s</summary><p>%s</p></details>" % (q, ans) for q, ans in a["faq"])
    url = "%slearn/%s/" % (base, a["slug"])
    is_dys = a["slug"] == B.DYS["slug"]
    if is_dys:
        by = ('<p class="byline"><span>Based on <i>The Holistic Microbiome</i> by <b>Adam Bóday</b>, founder of Herbaferm Hungary</span>'
              '<span>Page drafted by the Herbaferm editorial team</span><span>Review by Adam Bóday: <span class="tag">Pending confirmation</span></span>'
              '<span>Medical reviewer: <span class="tag">Pending</span></span><span>Published %s (draft)</span></p>') % "2 Nov 2026"
    else:
        by = ('<p class="byline"><span>By <b>%s</b></span><span>Medical reviewer: <span class="tag">Pending</span></span>'
              '<span>Published %s (draft)</span></p>') % (B.AUTHOR, "2 Nov 2026")
    authbox = ""
    if is_dys:
        authbox = ('<aside class="authbox"><img src="../../assets/images/book-microbiome.jpg" alt="Cover of The Holistic Microbiome by Adam Bóday, with the herbaferm logo" width="110" height="113" loading="lazy">'
                   '<div><h3>About the author and the book</h3><p><b>Adam Bóday</b> is the founder of Herbaferm Hungary and the scientist behind its fermentation work. He is the author of <i>The Holistic Microbiome: Nature is complex but never complicated</i> (Herbaferm Ltd., 2026), written with \u00c1bel B\u00f3day, '
                   'and co-author of a 2020 paper on restoring the symbiosis of microbiome and human body.</p>'
                   '<p><a href="%s" target="_blank" rel="noopener">Read the publication on ResearchGate</a> &middot; <a href="%s" target="_blank" rel="noopener">Author profile on ResearchGate</a></p></div></aside>'
                   ) % (B.RESEARCHGATE_BOOK, B.RESEARCHGATE_PROFILE)
    nxt = "".join('<a href="../%s/"><small>%s</small>%s</a>' % (o["slug"], o["cat"], o["title"]) for o in others)
    title = "%s | Herbaferm" % B.TTL[a["slug"]]
    crumb = ('<div class="crumbs"><a href="../../#home">Home</a> / <a href="../../#learn">Learn</a> / <a href="../../#blog">Blog</a> / %s</div>' % a["cat"])
    main = ('<main id="main">\n<div class="phero"><div class="wrap">%s<p class="kicker">%s</p><h1>%s</h1><p class="lede">%s</p></div></div>\n'
            '<section><div class="wrap"><article class="article">%s<aside class="inshort"><b>In short</b><ul>%s</ul></aside>%s\n%s\n'
            '<h2>Frequently asked questions</h2><div class="faqs">%s</div>\n<h2>References</h2><ol class="refs">%s</ol>\n'
            '<p class="note">%s</p>\n<h2>Read next</h2><div class="rnext">%s</div>\n</article></div></section>\n</main>\n'
            ) % (crumb, a["cat"], a["title"], a["dek"], by, "".join("<li>%s</li>" % x for x in short), hero, body + authbox, faq, refs, B.DISCLAIM, nxt)
    # schema: Article + FAQPage + BreadcrumbList (+ Book and Person on the dysbiosis page)
    graph = []
    art = {"@context": "https://schema.org", "@type": "Article", "headline": a["title"], "description": a["desc"],
           "datePublished": B.PUBLISHED, "dateModified": B.PUBLISHED, "inLanguage": "en-SG", "mainEntityOfPage": url,
           "author": {"@type": "Organization", "name": B.AUTHOR, "url": base},
           "publisher": {"@id": base + "#org"},
           "image": base + "assets/images/" + ("book-microbiome.jpg" if is_dys else "ai-morning.jpg"),
           "about": a["kw"],
           "citation": [{"@type": "CreativeWork", "name": strip(B.REFS[k][0]), "url": B.REFS[k][1]} for k in used]}
    graph.append(art)
    if is_dys:
        person = {"@type": "Person", "@id": base + "#adam-boday", "name": "Adam Bóday", "jobTitle": "Founder, Herbaferm Hungary",
                  "worksFor": {"@id": base + "#org"}, "sameAs": [B.RESEARCHGATE_PROFILE]}
        book = {"@context": "https://schema.org", "@type": "Book", "name": "The Holistic Microbiome: Nature is complex but never complicated",
                "author": [person, {"@type": "Person", "name": "\u00c1bel B\u00f3day"}], "publisher": {"@type": "Organization", "name": "Herbaferm Ltd."}, "datePublished": "2026-04-27",
                "isbn": ["9781036960094", "978-615-02-6126-3"], "inLanguage": "en", "sameAs": [B.RESEARCHGATE_BOOK]}
        art["isBasedOn"] = {"@id": base + "#book"}
        book["@id"] = base + "#book"
        graph += [book]
    graph.append(faq_ld(a["faq"]))
    graph.append({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": base},
        {"@type": "ListItem", "position": 2, "name": "Learn", "item": base + routes["learn"]},
        {"@type": "ListItem", "position": 3, "name": a["title"], "item": url}]})
    graph.insert(0, sub(dict(ORG, **{"@context": "https://schema.org"}), base))
    head = shell_head.format(title=_h.escape(title), desc=_h.escape(a["desc"]), url=url, og_img=base + "assets/images/ai-morning.jpg", robots="") + ld(*graph)
    js = ('<script>(function(){var r=document.documentElement,t=document.getElementById("theme"),b=document.getElementById("burger");'
          'function d(){var a=r.getAttribute("data-theme");return a?a==="dark":matchMedia("(prefers-color-scheme: dark)").matches}'
          'function l(){t.textContent=d()?"Light":"Dark";t.setAttribute("aria-label",d()?"Switch to light mode":"Switch to dark mode")}'
          't.addEventListener("click",function(){r.setAttribute("data-theme",d()?"light":"dark");l()});l();'
          'b.addEventListener("click",function(){document.querySelector(".mnav").classList.toggle("on")})})();</script>')
    return "<!doctype html>\n<html lang=\"en\">\n<head>\n" + head + "</head>\n<body>\n" + header + main + footer + js + "\n</body>\n</html>\n"


def robots(base):
    return ("# Herbaferm Singapore. Bot access follows slide 31 of the brand deck.\n"
            "User-agent: *\nAllow: /\n\n"
            "# Search and AI-search bots: allowed\n"
            "User-agent: Googlebot\nAllow: /\n\nUser-agent: OAI-SearchBot\nAllow: /\n\n"
            "# AI training bots: optional. Allowed for now; uncomment to block.\n"
            "# Blocking these does not remove the site from Google or ChatGPT search.\n"
            "# User-agent: GPTBot\n# Disallow: /\n#\n# User-agent: Google-Extended\n# Disallow: /\n\n"
            "Sitemap: %ssitemap.xml\n" % base)


def sitemap(base, route_ids, routes):
    urls = [base + routes[r] for r in route_ids] + ["%slearn/%s/" % (base, a["slug"]) for a in B.ARTICLES + [B.DYS]]
    return ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            + "".join("<url><loc>%s</loc><lastmod>%s</lastmod></url>\n" % (u, B.PUBLISHED) for u in urls) + "</urlset>\n")
