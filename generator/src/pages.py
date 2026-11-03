# Page content for the Herbaferm Singapore prototype. Image tokens look like @@img:name@@ and are inlined by build.py.

def ic(path):
    return ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" '
            'stroke-linejoin="round" aria-hidden="true">' + path + '</svg>')

LEAF = ic('<path d="M5 19c0-8 5-13 15-14 0 10-5 15-13 15"/><path d="M5 19c3-5 6-8 10-10"/>')
DROP = ic('<path d="M12 3c4 5 6 8 6 11a6 6 0 0 1-12 0c0-3 2-6 6-11z"/><path d="M9.5 14.5a2.5 2.5 0 0 0 2.5 2.5"/>')
FLASK = ic('<path d="M9 3h6M10 3v6l-5 9a2 2 0 0 0 1.8 3h10.4a2 2 0 0 0 1.8-3l-5-9V3"/><path d="M7.5 15h9"/>')
SHIELD = ic('<path d="M12 3l7 3v5c0 4.5-3 8-7 10-4-2-7-5.5-7-10V6z"/><path d="M9 12l2 2 4-4"/>')
WHEAT = ic('<path d="M12 21V8"/><path d="M12 8c-2-1-3-3-3-5 2 0 3 2 3 5zM12 8c2-1 3-3 3-5-2 0-3 2-3 5z"/><path d="M12 14c-2-1-3-3-3-5M12 14c2-1 3-3 3-5M12 19c-2-1-3-3-3-5M12 19c2-1 3-3 3-5"/>')
CAPS = ic('<rect x="3" y="9" width="18" height="7" rx="3.5" transform="rotate(-35 12 12.5)"/><path d="M9.5 8.2l5 7.6"/>')
DOC = ic('<path d="M7 3h7l4 4v14H7z"/><path d="M14 3v4h4M10 12h5M10 16h5"/>')
MAIL = ic('<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>')
GLOBE = ic('<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"/>')
USERS = ic('<circle cx="9" cy="8" r="3"/><path d="M3 20c0-3.5 3-6 6-6s6 2.5 6 6M17 11a3 3 0 1 0 0-6M21 20c0-2.5-1.5-4.5-4-5.3"/>')
BOOK = ic('<path d="M4 5c3-1 6-1 8 1 2-2 5-2 8-1v13c-3-1-6-1-8 1-2-2-5-2-8-1z"/><path d="M12 6v13"/>')
SNOW = ic('<path d="M12 3v18M4.2 7.5l15.6 9M19.8 7.5l-15.6 9"/>')
CLOCK = ic('<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>')

TC = '<span class="tag">To confirm</span>'


def tag(t):
    return '<span class="tag">%s</span>' % t


HERBS = [
    ("chamomile", "Chamomile", "Matricaria chamomilla", "Chamomile flower",
     "A familiar herb in European kitchens and herbal teas, traditionally used for gentle digestive comfort."),
    ("yarrow", "Yarrow", "Achillea millefolium", "Yarrow flowering herb",
     "A wayside flowering herb used in traditional European herbal practice to support digestion and normal gut function."),
    ("elderflower", "Elderflower", "Sambucus nigra", "Elderflower",
     "The creamy blossoms of the elder tree, a classic ingredient in traditional European preparations."),
    ("rosehip", "Rosehip", "Rosa canina", "Rosehip",
     "The fruit of the dog rose, a natural source of vitamin C and long valued in traditional herbal use."),
    ("propolis", "Propolis", "Apis mellifera propolis", "Propolis",
     "A resinous substance collected by bees from plant buds, traditionally used for its natural, protective qualities."),
    ("oak-bark", "Oak bark", "Quercus robur", "Oak bark",
     "Contains tannins and has a long tradition of use in herbal preparations for the digestive tract."),
    ("wormwood", "White wormwood", "Artemisia absinthium", "White wormwood flowering herb",
     "A bitter herb used in traditional European practice to support digestion and maintain a healthy balance."),
]


def herb_card(h):
    return ('<div class="herb"><div class="im"><img src="@@img:herb-%s@@" alt="%s"></div>'
            '<div class="t"><b>%s</b><i>%s</i></div></div>') % (h[0], h[3], h[1], h[2])


def herb_row(h):
    return ('<div class="herb-row"><div class="im"><img src="@@img:herb-%s@@" alt="%s"></div>'
            '<div><h3>%s</h3><span class="lat">%s</span><p>%s</p></div></div>') % (h[0], h[3], h[1], h[2], h[4])


def pcard(pid, page, role, name, blurb, price, size, img_html, white=False, extra=""):
    return ('<article class="pcard"><a class="shot%s" href="#%s" aria-label="%s">%s</a><div class="body">'
            '<span class="role">%s</span><h3>%s</h3><p>%s</p>%s<div class="row"><b>S$%d</b><span>%s</span></div>'
            '<div class="btns"><a class="btn btn-forest btn-sm" href="#%s">View product</a>'
            '<button class="btn btn-line btn-sm" type="button" data-add="%s">Add to cart</button></div></div></article>'
            ) % (" white" if white else "", page, name, img_html, role, name, blurb, extra, price, size, page, pid)


PACK_FIBER = '<img src="@@img:fiber@@" alt="Fiber Elite 125 g pouch, 35 servings" data-thumb="fiber">'
IMG_DROPS = '<img src="@@img:drops@@" alt="Herbaferm Drops 30 ml bottle with carton and kraft wrapper" data-thumb="drops">'
IMG_PREFER = '<img src="@@img:prefer@@" alt="Prefer HF400 bottle with a capsule" data-thumb="prefer">'


HERO = {"Shop": ("ai-morning", "#e8b04a"), "Learn": ("ai-herbs", "#7fc79a"), "About": ("hero-bark", "#8fb86a"), "Partners": ("ai-clinic", "#d9a27a"),
        "FAQ": ("ai-fridge", "#a9d3c8"), "Contact": ("ai-field", "#cfe0b8"), "Awards": ("ai-propolis", "#f2b73d"), "Ingredients": ("ai-chamomile", "#7fc79a"),
        "Science": ("ai-shelf", "#a9d3c8"), "Quality": (None, "#8fb86a"), "Policies": (None, "#d8c7a5")}


def phero(crumb, eyebrow, title, lede, trail=""):
    img, pt = HERO.get(crumb, (None, "#7fc79a"))
    bg = '<img class="phbg" src="@@img:%s@@" alt="" loading="lazy">' % img if img else ""
    return ('<div class="phero phx" style="--pt:%s">%s<div class="wrap"><div class="crumbs"><a href="#home">Home</a> / %s</div>'
            '<p class="eyebrow">%s</p><h1>%s</h1><p class="lede">%s</p>%s</div></div>') % (pt, bg, crumb, eyebrow, title, lede, trail)


def faq_item(cat, q, a):
    return '<details data-c="%s"><summary>%s</summary><p>%s</p></details>' % (cat, q, a)


FAQS = [
    ("use", "How long does one bottle of Drops last?",
     "A 30 ml bottle holds about 480 drops. At 8 drops twice a day, that is about one month. The leaflet suggests a slower build-up over the first weeks."),
    ("use", "How do I start with Drops?",
     "The leaflet suggests starting with 5 drops in the morning and 5 in the evening, then increasing gradually to up to 15 drops twice a day over two to three weeks. After that, 8 drops twice a day is the regular amount. Always take the drops in water. " + TC),
    ("use", "Will I notice anything in the first days?",
     "Some people notice temporary digestive changes such as gas or looser stools when they start. This is why we suggest building up gradually. If you are uncomfortable, reduce the amount or pause. " + TC),
    ("use", "How do I use Fiber Elite?",
     "The everyday amount is 3.5 g a day with a meal. Athletes take 3.5 g two to three times a day, after training, ideally in a smoothie or protein shake. You can also stir it into yoghurt or porridge, or heat it into food."),
    ("use", "Can I take the capsules and the drops together?",
     "Yes. Prefer HF400 was developed to be taken together with Herbaferm Drops. The capsule leaflet suggests one capsule in the morning and one in the evening."),
    ("safety", "Who should speak to a professional first?",
     "Anyone with a diagnosed health condition, anyone taking medication, and anyone who is pregnant. The leaflets also advise stopping the product if you notice hypersensitivity to an ingredient, and using Prefer HF400 only under professional supervision if you have histamine sensitivity."),
    ("safety", "Are Herbaferm products medicines?",
     "No. They are food supplements. Our leaflets state that no health effects can be attributed to them. They are not intended to diagnose, treat, cure or prevent any disease."),
    ("safety", "Can children use these products?",
     "Speak to a healthcare professional before giving any supplement to a child. " + TC),
    ("products", "Is Fiber Elite gluten-free?",
     "No. The current leaflet lists 75% whole barley malt and 12.5% oat flour and states that Fiber Elite contains gluten."),
    ("products", "Are the capsules vegetarian or halal?",
     "The capsule shell is gelatine, so the capsules are not suitable for vegetarians. Halal status has not been confirmed. " + TC),
    ("products", "How long do the products keep?",
     "Herbaferm's notes give about 6 months for Drops and about 1 year for the capsules. The best-before date is printed on each pack. " + TC),
    ("products", "Are Drops free from alcohol and sugar?",
     "Herbaferm describes the Drops as free from preservatives, alcohol and sugar. The leaflets confirm no preservatives. " + TC),
    ("products", "Is Herbaferm sold in Singapore yet?",
     "Yes, early on. All three products are listed on the ConnectingDNA marketplace in Singapore, with first sales (12+, 17+ and 20+ units shown at the time of checking). Clinic and retail stockists are still being built. " + TC),
    ("products", "What are the products free from?",
     "The ConnectingDNA listings show a free-from icon set (gluten, sugar, alcohol and lactose free, vegetarian) on all three products. That conflicts with the leaflet, which says Fiber Elite contains gluten, so please rely on the pack label. " + TC),
    ("products", "What does a day cost?",
     "At list price, Drops at the regular amount are about S$1.83 a day (S$55 for about 30 days). Fiber Elite at 3.5 g a day is about S$1.54 a day. Prefer HF400 is S$3.21 per capsule. Prices are before any offers."),
    ("products", "How should I store Herbaferm Drops?",
     "Keep the bottle in the fridge at 5 to 12 °C. The drops contain no preservatives. Check the best-before date printed on the pack."),
    ("products", "Where are the products made?",
     "Herbaferm Kft. develops and produces the range at Csömör, Hungary. Drops are registered in Hungary under number 20075/2018 as a food supplement."),
    ("about", "Is Herbaferm approved by the HSA?",
     "In Singapore, health supplements do not need pre-market approval from the Health Sciences Authority, so no supplement can be described as \"HSA approved\". Herbaferm products are marketed as food supplements. " + TC),
    ("ordering", "Where can I buy Herbaferm in Singapore?",
     "Today the range is sold through this website and on the ConnectingDNA marketplace. Clinic, pharmacy and retail stockists are being built, and the Shop page has a sign-up for stockist news. " + TC),
    ("ordering", "How much does delivery cost, and how long does it take?",
     "Delivery details for Singapore will be listed here. " + tag("To supply")),
    ("ordering", "What is your returns policy?",
     "Returns and refund terms will be listed here. " + tag("To supply")),
    ("ordering", "Which payment methods do you accept?",
     "The current store accepts major cards and wallets. The live list will be shown here. " + TC),
    ("partners", "How can my clinic or shop stock Herbaferm?",
     "Send us an enquiry on the Partners page. We reply with the partner evidence pack: formulation, quality and safety information, testing, shelf life and available literature."),
    ("partners", "Do you offer samples for practitioners?",
     "Sample availability for practitioners and retail buyers will be confirmed. " + TC),
]

NAV = [("shop", "Shop"), ("learn", "Learn"), ("about", "About"), ("partners", "Partners")]

PAGES = []  # list of (id, title, html)

# ------------------------------------------------------------------ HOME
PAGES.append(("home", "Herbaferm Singapore", '''
<div class="hero"><div class="bg" style="background-image:url(@@img:hero-bark@@)"></div><div class="wrap">
  <p class="eyebrow" style="color:var(--honey)">Fermented herbal food supplements</p>
  <h1>Seven herbs. Natural fermentation. <em>One simple routine.</em></h1>
  <p class="sub">Herbaferm brings a fermented herbal formula from Hungary to Singapore, to support everyday digestive wellbeing.</p>
  <div class="btns"><a class="btn btn-honey" href="#shop">Shop the range</a><a class="btn btn-line" href="#science">Explore the science</a></div>
  <div class="meta"><span>Registered in Hungary since 2018</span><span>No preservatives or artificial colours</span><span>Free from artificial additives</span></div>
</div></div>

<div class="facts"><div class="wrap"><ul>
  <li><strong>7 traditional herbs</strong><span>Chamomile, yarrow, elderflower, rosehip, propolis, oak bark, wormwood</span></li>
  <li><strong>Natural fermentation</strong><span>A gentle, traditional process</span></li>
  <li><strong>Made in Hungary</strong><span>Developed and produced by Herbaferm Kft.</span></li>
  <li><strong>Gold award 2026</strong><span>CIM Hong Kong, Healthy Dietary (Vegetarian)</span></li>
</ul></div></div>

<section><div class="wrap split">
  <div class="stack">
    <p class="eyebrow">Our approach</p>
    <h2>Herbs, fermented the way they have been for generations</h2>
    <p class="lede">Herbaferm Drops are a herbal extract made by natural fermentation. A blend of seven plants is fermented with a natural community of microorganisms, so the drops carry both the herbs and what fermentation adds.</p>
    <p class="lede">The range is built to sit beside a varied, mostly natural diet. It does not replace one.</p>
    <p><a class="more" href="#science">How fermentation works</a></p>
  </div>
  <div><img src="@@img:drops@@" alt="Herbaferm Drops with carton and kraft wrapper" style="border-radius:28px;width:100%;background:#f4efe3;padding:18px"></div>
</div></section>

<section class="alt"><div class="wrap">
  <div class="sechead"><div><p class="eyebrow">The range</p><h2>Three products, one routine</h2><p class="lede">Start with Drops, add Fiber Elite to your meals, and use Prefer HF400 if you like a capsule routine.</p></div><a class="btn btn-line" href="#shop">See all products</a></div>
  <div class="three">
    @@PC_DROPS@@
    @@PC_FIBER@@
    @@PC_PREFER@@
  </div>
</div></section>

<section class="dark"><div class="wrap">
  <p class="eyebrow">How to begin</p>
  <h2>Three steps to a daily habit</h2>
  <div class="three" style="margin-top:36px">
    <div class="step"><span class="n">1</span><h3>Start gently</h3><p>Begin with a few drops and build up over the first weeks, as the leaflet describes.</p></div>
    <div class="step"><span class="n">2</span><h3>Pair it with something you already do</h3><p>Take Drops in a glass of water with breakfast and in the evening. Stir Fiber Elite into your usual smoothie or porridge.</p></div>
    <div class="step"><span class="n">3</span><h3>Stay consistent</h3><p>Keep opened Drops in the fridge at 5 to 12 °C. Read the starter guide for the full schedule.</p></div>
  </div>
  <p style="margin-top:30px"><a class="btn btn-honey" href="#learn">Read the starter guide</a></p>
</div></section>

<section><div class="wrap">
  <div class="sechead"><div><p class="eyebrow">Ingredients</p><h2>Seven herbs from the Carpathian Basin tradition</h2><p class="lede">The same seven ingredients are in Herbaferm Drops and in the fermented herb fibres of Prefer HF400.</p></div><a class="btn btn-line" href="#ingredients">Meet the herbs</a></div>
  <div class="herb-grid">@@HERBS@@</div>
</div></section>

<section class="dark"><div class="wrap">
  <p class="eyebrow">By the numbers</p>
  <h2>What is in the bottle, and behind it</h2>
  <div class="four" style="margin-top:34px">
    <div><div class="big">7</div><p class="m" style="margin-top:8px">herbal ingredients in every drop</p></div>
    <div><div class="big">480</div><p class="m" style="margin-top:8px">drops in a 30 ml bottle, about one month</p></div>
    <div><div class="big">2018</div><p class="m" style="margin-top:8px">year Drops were registered in Hungary</p></div>
    <div><div class="big">31</div><p class="m" style="margin-top:8px">days in the published Fiber Elite related study</p></div>
  </div>
</div></section>

<section><div class="wrap">
  <div class="sechead"><div><p class="eyebrow">Trust</p><h2>Evidence you can check</h2><p class="lede">We publish what we have, say what it covers, and flag what is still being updated.</p></div><a class="btn btn-line" href="#quality">Quality and certificates</a></div>
  <div class="three">
    <a class="card" href="#science"><div class="ic">@@FLASK@@</div><h3>Published research</h3><p>A peer-reviewed study linked to Fiber Elite, with the authors, journal and DOI.</p><span class="more">Read the summary</span></a>
    <a class="card" href="#quality"><div class="ic">@@SHIELD@@</div><h3>Registration and testing</h3><p>Hungarian registration for Drops, lab documents and manufacturing information.</p><span class="more">View documents</span></a>
    <a class="card" href="#about"><div class="ic">@@USERS@@</div><h3>The people behind it</h3><p>A Hungarian founding team with a scientist at the centre, now working in Singapore.</p><span class="more">Our story</span></a>
  </div>
</div></section>

<section class="alt"><div class="wrap">
  <div class="award">
    <img src="@@img:award@@" alt="CIM Hong Kong Bay Area Vitality Living Brand Outstanding Award 2026, Gold Award, Herbaferm Pte Ltd" width="250" height="354">
    <div><p class="eyebrow">Recognition</p><h2 style="font-size:clamp(1.5rem,3vw,2.1rem)">Gold Award, Bay Area Vitality Living Brand Outstanding Award 2026</h2>
    <p>Presented to Herbaferm by the Chartered Institute of Marketing Hong Kong in the Healthy Dietary (Vegetarian) category for 2025/26.</p></div>
  </div>
</div></section>

<section><div class="wrap">
  <div class="sechead"><div><p class="eyebrow">Voices</p><h2>What customers say</h2></div></div>
  <div class="ph"><b>Reviews area</b><p style="margin-top:6px">Verified Singapore customer reviews and practitioner quotes appear here once collected. No placeholder quotes are shown. @@TAG_SUPPLY@@</p></div>
</div></section>

<section class="alt"><div class="wrap">
  <div class="cta"><div><h2>Clinic, retailer or distributor?</h2><p>Request the partner evidence pack: formulation, quality, testing, shelf life and literature.</p></div><a class="btn btn-honey" href="#partners">Become a partner</a></div>
</div></section>

<section><div class="wrap split top">
  <div><p class="eyebrow">Stay in touch</p><h2>Guides and news, no noise</h2><p class="lede">Occasional emails with usage guides, Fiber Elite ideas and Singapore stockist news.</p></div>
  <form class="form" data-proto="Thanks. This is a prototype, so nothing was sent." novalidate><label for="nl-email">Email address<input id="nl-email" type="email" autocomplete="email" placeholder="you@example.com"></label><button class="btn btn-forest" type="submit">Subscribe</button><p class="note fnote">We will only use your email for Herbaferm news. @@TAG_CONFIRM@@</p></form>
</div></section>
'''))

# ------------------------------------------------------------------ SHOP
PAGES.append(("shop", "Shop | Herbaferm Singapore", '''
@@PHERO_SHOP@@
<section><div class="wrap">
  <div class="three">
    @@PC_DROPS@@
    @@PC_FIBER@@
    @@PC_PREFER@@
  </div>
  <figure class="rangeshot"><img src="@@img:range@@" alt="Prefer HF400, Fiber Elite and Herbaferm Drops together" loading="lazy"><figcaption><b>The whole range</b><span>Drops, Fiber Elite and Prefer HF400 are made to be used together.</span></figcaption></figure>
  <p class="note" style="margin-top:18px">Prices in Singapore dollars. Delivery, returns and checkout are connected in the live build. @@TAG_SUPPLY@@</p>
</div></section>

<section class="alt" style="padding-block:44px"><div class="wrap">
  <div class="where">
    <div><h3>Buy online now</h3><p>The whole range ships from this store. It is also listed on the ConnectingDNA marketplace in Singapore.</p></div>
    <div><h3>Clinics and stockists</h3><p>Being built. Leave your email for stockist news.</p></div>
    <form class="form inline" data-proto="Thanks. This is a prototype, so nothing was sent." novalidate><label for="st-email">Email address<input id="st-email" type="email" autocomplete="email" placeholder="you@example.com"></label><button class="btn btn-forest" type="submit">Tell me</button></form>
  </div>
</div></section>

<section class="alt"><div class="wrap">
  <p class="eyebrow">Not sure where to start?</p><h2>Pick the way you would like to use it</h2>
  <div class="three" style="margin-top:34px">
    <a class="card" href="#drops"><div class="ic">@@DROP@@</div><h3>"I want a simple daily routine"</h3><p>Herbaferm Drops go into a glass of water, morning and evening. The core of the range.</p><span class="more">Herbaferm Drops</span></a>
    <a class="card" href="#fiber"><div class="ic">@@WHEAT@@</div><h3>"I would rather add it to meals"</h3><p>Fiber Elite stirs into smoothies, shakes, yoghurt or porridge, and can be heated.</p><span class="more">Fiber Elite</span></a>
    <a class="card" href="#prefer"><div class="ic">@@CAPS@@</div><h3>"I like capsules"</h3><p>Prefer HF400 pairs fermented herb fibres with fulvic acid, humic acid and vitamin C.</p><span class="more">Prefer HF400</span></a>
  </div>
</div></section>

@@VIZ_COST@@
<section><div class="wrap">
  <p class="eyebrow">Compare</p><h2>The range side by side</h2>
  <div class="tblwrap" style="margin-top:30px"><table>
    <thead><tr><th></th><th>Herbaferm Drops</th><th>Fiber Elite</th><th>Prefer HF400</th></tr></thead>
    <tbody>
      <tr><td>Format</td><td>Liquid drops, 30 ml</td><td>Powder, 125 g</td><td>14 capsules</td></tr>
      <tr><td>Price</td><td>S$55</td><td>S$55</td><td>S$45</td></tr>
      <tr><td>How you use it</td><td>8 drops in 1.5 dl of water, twice a day</td><td>3.5 g a day with a meal, stirred into food or drinks</td><td>1 capsule morning and evening</td></tr>
      <tr><td>One pack lasts</td><td>About 30 days at 8 drops twice a day</td><td>About 35 days at 3.5 g a day</td><td>7 days at 2 capsules a day</td></tr>
      <tr><td>Main ingredients</td><td>Fermented extract of 7 herbs</td><td>75% whole barley malt, 12.5% oat flour</td><td>Fermented herb fibres, fulvic acid, humic acid, vitamin C</td></tr>
      <tr><td>Cost per day</td><td>About S$1.83</td><td>About S$1.54</td><td>About S$6.43</td></tr>
      <tr><td>Storage</td><td>Fridge, 5 to 12 °C</td><td>Cool and dry @@TAG_CONFIRM@@</td><td>Cool and dry @@TAG_CONFIRM@@</td></tr>
      <tr><td>Good to know</td><td>No preservatives</td><td>Vegan. Contains gluten</td><td>Gelatine capsule</td></tr>
    </tbody>
  </table></div>
</div></section>
'''))

# ------------------------------------------------------------------ PRODUCT: DROPS
PAGES.append(("drops", "Herbaferm Drops | Herbaferm Singapore", '''
<section style="padding-block:40px 70px"><div class="wrap">
  <div class="crumbs" style="color:var(--muted);margin-bottom:22px"><a href="#home">Home</a> / <a href="#shop">Shop</a> / Herbaferm Drops</div>
  <div class="pd">
    <div class="gallery"><div class="main" data-gal><div data-g="0"><img src="@@img:drops@@" alt="Herbaferm Drops 30 ml bottle with carton and kraft wrapper" data-thumb="drops"></div><div data-g="1" hidden><img src="@@img:flatlay@@" alt="The seven herbs in Herbaferm Drops, laid out flat"></div><div data-g="2" hidden><img class="pour" src="@@img:drops-pour@@" alt="A hand adding Herbaferm Drops to a glass of water, with Prefer HF400 and a bowl of fruit behind" loading="lazy"></div></div>
      <div class="gthumbs" role="tablist" aria-label="Product views"><button type="button" role="tab" aria-selected="true" data-gi="0">The pack</button><button type="button" role="tab" aria-selected="false" data-gi="1">Seven herbs</button><button type="button" role="tab" aria-selected="false" data-gi="2">In use</button></div></div>
    <div>
      <p class="eyebrow">Signature product</p>
      <h1>Herbaferm Drops</h1>
      <p class="lede" style="margin-top:12px">A herbal extract made by natural fermentation. Take it in a glass of water, morning and evening.</p>
      <div class="price"><b>S$55</b><span>30 ml, about one month</span></div>
      <div class="buy"><div class="qty"><button type="button" data-q="-1" aria-label="Decrease quantity">&minus;</button><output>1</output><button type="button" data-q="1" aria-label="Increase quantity">+</button></div><button class="btn btn-honey" type="button" data-add="drops">Add to cart</button></div>
      <div class="keyfacts">
        <div><small>Per bottle</small><b>About 480 drops, S$1.83 a day</b></div>
        <div><small>Regular amount</small><b>8 drops, twice a day</b></div>
        <div><small>Storage</small><b>Fridge, 5 to 12 °C</b></div>
        <div><small>Free from</small><b>Preservatives</b></div>
      </div>
      <p class="note">Food supplement. Speak to a healthcare professional if you are pregnant or take medication.</p>
    </div>
  </div>

  <div class="tabs-wrap"><div class="tabs" role="tablist">
    <button role="tab" aria-selected="true" aria-controls="d-use">How to use</button><button role="tab" aria-selected="false" aria-controls="d-ing">Ingredients</button><button role="tab" aria-selected="false" aria-controls="d-info">Good to know</button>
  </div>
  <div class="tabpanel" id="d-use"><dl class="spec">
    <dt>Regular use</dt><dd>8 drops in 1.5 dl of water, twice a day. An occasional range of 5 to 15 drops is acceptable depending on body weight and age.</dd>
    <dt>Getting started</dt><dd>Start with 5 drops in the morning and 5 in the evening, then increase gradually to up to 15 drops twice a day over two to three weeks. After that, return to 8 drops twice a day. @@TAG_CONFIRM@@</dd>
    <dt>Storage</dt><dd>Keep in the fridge at 5 to 12 °C. The product contains no preservatives.</dd>
    <dt>Bottle size</dt><dd>30 ml contains the regular monthly amount for an average consumer: 480 drops, which is 8 x 2 x 30.</dd></dl></div>
  <div class="tabpanel" id="d-ing" hidden><p>Herbal extract made by natural fermentation of seven plant ingredients:</p><ul><li>Chamomile flower (<i>Matricaria chamomilla</i>)</li><li>Yarrow flowering herb (<i>Achillea millefolium</i>)</li><li>Elderflower (<i>Sambucus nigra</i>)</li><li>Rosehip (<i>Rosa canina</i>)</li><li>Propolis</li><li>Oak bark (<i>Quercus robur</i>)</li><li>White wormwood flowering herb (<i>Artemisia absinthium</i>)</li></ul><p>No artificial additives, preservatives or colours. @@TAG_CONFIRM@@ the full label for Singapore.</p></div>
  <div class="tabpanel" id="d-info" hidden><ul><li>Some people notice temporary digestive changes when they start. Build up gradually.</li><li>Stop and speak to a professional if you notice hypersensitivity to any ingredient.</li><li>Histamine sensitivity, immune system disorders and severe gut inflammation need professional advice before use.</li><li>Registered in Hungary, no. 20075/2018. Alcohol-free and sugar-free, according to Herbaferm. @@TAG_CONFIRM@@</li><li>As a dietary supplement, no health effects can be attributed to the product, according to the leaflet.</li></ul></div>
  </div>
</div></section>

<section class="alt"><div class="wrap"><div class="sechead"><div><p class="eyebrow">Pairs well with</p><h2>Complete the routine</h2></div></div>
  <div class="two">
    <a class="card" href="#fiber"><h3>Fiber Elite</h3><p>Stir it into the shake or porridge you already make. S$55, 125 g.</p><span class="more">View product</span></a>
    <a class="card" href="#prefer"><h3>Prefer HF400</h3><p>Developed to be taken together with Herbaferm Drops. S$45, 14 capsules.</p><span class="more">View product</span></a>
  </div></div></section>
'''))

# ------------------------------------------------------------------ PRODUCT: FIBER
PAGES.append(("fiber", "Fiber Elite | Herbaferm Singapore", '''
<section style="padding-block:40px 70px"><div class="wrap">
  <div class="crumbs" style="color:var(--muted);margin-bottom:22px"><a href="#home">Home</a> / <a href="#shop">Shop</a> / Fiber Elite</div>
  <div class="pd">
    <div class="gallery"><div class="main white" data-gal><div data-g="0">@@PACK_FIBER@@</div></div>
      </div>
    <div>
      <p class="eyebrow">Everyday add-in</p>
      <h1>Fiber Elite</h1>
      <p class="lede" style="margin-top:12px">A fibre-rich add-in with a malt aroma. Stir it into food and drinks, or heat it.</p>
      <div class="price"><b>S$55</b><span>125 g, about one month</span></div>
      <div class="buy"><div class="qty"><button type="button" data-q="-1" aria-label="Decrease quantity">&minus;</button><output>1</output><button type="button" data-q="1" aria-label="Increase quantity">+</button></div><button class="btn btn-honey" type="button" data-add="fiber">Add to cart</button></div>
      <div class="keyfacts">
        <div><small>Everyday amount</small><b>3.5 g a day, about S$1.54</b></div>
        <div><small>Athletes</small><b>3.5 g, 2 to 3 times a day</b></div>
        <div><small>Made from</small><b>75% barley malt, 12.5% oat flour</b></div>
        <div><small>Allergens</small><b>Contains gluten</b></div>
      </div>
      <p class="note">Food supplement. Vegan and GMO-free, according to the leaflet.</p>
    </div>
  </div>
  <div class="tabs-wrap"><div class="tabs" role="tablist">
    <button role="tab" aria-selected="true" aria-controls="f-use">How to use</button><button role="tab" aria-selected="false" aria-controls="f-ing">Ingredients</button><button role="tab" aria-selected="false" aria-controls="f-study">The study</button>
  </div>
  <div class="tabpanel" id="f-use"><dl class="spec">
    <dt>Everyday</dt><dd>3.5 g a day, with a meal.</dd>
    <dt>After training</dt><dd>3.5 g two to three times a day, preferably stirred into a smoothie or protein shake.</dd>
    <dt>Ideas</dt><dd>Yoghurt, porridge, smoothies and shakes. Fiber Elite can also be heated, which makes it the one product in the range suited to cooking. See <a href="#a-fiber">four easy ways to eat it</a>.</dd>
    <dt>Pack size</dt><dd>125 g, about a month at the everyday amount.</dd></dl></div>
  <div class="tabpanel" id="f-ing" hidden><p>75% whole barley malt and 12.5% oat flour, with a characteristic malt aroma and flour-like texture. Contains gluten. @@TAG_CONFIRM@@ A newer Herbaferm note describes dark-germinated barley with naturally occurring enzymes, which does not match this leaflet, so the final composition is still to be confirmed. Another Herbaferm document describes a different formulation, so the final label must be confirmed.</p></div>
  <div class="tabpanel" id="f-study" hidden><p>A 31-day study in 20 elite male water polo players compared a vegan protein supplement with and without pre- and probiotics. It was published in the Journal of the International Society of Sports Nutrition in 2024. Herbaferm's founders are among the authors, and the abstract does not name Fiber Elite.</p><p><a class="more" href="#science">See the full reference</a></p></div>
  </div>
</div></section>
<section class="alt"><div class="wrap"><div class="sechead"><div><p class="eyebrow">Pairs well with</p><h2>Complete the routine</h2></div></div>
  <div class="two">
    <a class="card" href="#drops"><h3>Herbaferm Drops</h3><p>The signature product. S$55, 30 ml.</p><span class="more">View product</span></a>
    <a class="card" href="#learn"><h3>Fiber Elite ideas</h3><p>Four simple ways to use it in your week.</p><span class="more">Read ideas</span></a>
  </div></div></section>
'''))

# ------------------------------------------------------------------ PRODUCT: PREFER
PAGES.append(("prefer", "Prefer HF400 | Herbaferm Singapore", '''
<section style="padding-block:40px 70px"><div class="wrap">
  <div class="crumbs" style="color:var(--muted);margin-bottom:22px"><a href="#home">Home</a> / <a href="#shop">Shop</a> / Prefer HF400</div>
  <div class="pd">
    <div class="gallery"><div class="main white" data-gal><div data-g="0"><img src="@@img:prefer@@" alt="Prefer HF400 bottle with a capsule" data-thumb="prefer"></div><div data-g="1" hidden><img src="@@img:prefer-bark@@" alt="Prefer HF400 bottle and carton on a mossy bark, with a capsule in front" loading="lazy"></div></div>
      <div class="gthumbs" role="tablist" aria-label="Product views"><button type="button" role="tab" aria-selected="true" data-gi="0">The pack</button><button type="button" role="tab" aria-selected="false" data-gi="1">Close up</button></div></div>
    <div>
      <p class="eyebrow">Optional add-on</p>
      <h1>Prefer HF400</h1>
      <p class="lede" style="margin-top:12px">Fermented herb fibre capsules, developed to be taken with Herbaferm Drops.</p>
      <div class="price"><b>S$45</b><span>14 capsules, 400 mg each</span></div>
      <div class="buy"><div class="qty"><button type="button" data-q="-1" aria-label="Decrease quantity">&minus;</button><output>1</output><button type="button" data-q="1" aria-label="Increase quantity">+</button></div><button class="btn btn-honey" type="button" data-add="prefer">Add to cart</button></div>
      <div class="keyfacts">
        <div><small>How to take</small><b>1 capsule morning and evening</b></div>
        <div><small>Fermented herb fibres</small><b>200 mg per capsule</b></div>
        <div><small>Capsule shell</small><b>Gelatine</b></div>
        <div><small>Price per capsule</small><b>S$3.21</b></div>
      </div>
      <p class="note">One 14-capsule pack lasts 7 days at two capsules a day, so it works as a trial pack. Food supplement. Histamine sensitivity: ask a healthcare professional first.</p>
    </div>
  </div>
  <div class="tabs-wrap"><div class="tabs" role="tablist">
    <button role="tab" aria-selected="true" aria-controls="p-use">How to use</button><button role="tab" aria-selected="false" aria-controls="p-ing">Ingredients</button><button role="tab" aria-selected="false" aria-controls="p-info">Good to know</button>
  </div>
  <div class="tabpanel" id="p-use"><dl class="spec"><dt>Dose</dt><dd>2 capsules a day, one in the morning and one in the evening.</dd><dt>With Drops</dt><dd>Prefer HF400 was developed to complement Herbaferm Drops, taken morning and evening.</dd><dt>Pack</dt><dd>14 capsules is one week at two a day. @@TAG_CONFIRM@@ Another Herbaferm document describes a different dose.</dd></dl></div>
  <div class="tabpanel" id="p-ing" hidden><p>Per 400 mg capsule:</p><ul><li>200 mg fermented herb fibres (chamomile, yarrow, rosehip, elderflower, propolis, oak bark, wormwood)</li><li>120 mg fulvic acid</li><li>51 mg humic acid</li><li>29 mg vitamin C</li></ul><p>Gelatine capsule shell. Hungarian registration number on the leaflet is truncated. @@TAG_CONFIRM@@</p></div>
  <div class="tabpanel" id="p-info" hidden><ul><li>Histamine sensitivity: use only with professional supervision.</li><li>Stop if you notice hypersensitivity to any ingredient or have an immune system disorder.</li><li>The capsule shell is gelatine, so not suitable for vegetarians. Halal status unconfirmed. @@TAG_CONFIRM@@</li></ul></div>
  </div>
</div></section>
<section class="alt"><div class="wrap"><div class="sechead"><div><p class="eyebrow">Pairs well with</p><h2>Complete the routine</h2></div></div>
  <div class="two">
    <a class="card" href="#drops"><h3>Herbaferm Drops</h3><p>The product Prefer HF400 was developed to accompany. S$55, 30 ml.</p><span class="more">View product</span></a>
    <a class="card" href="#fiber"><h3>Fiber Elite</h3><p>Add to meals and shakes. S$55, 125 g.</p><span class="more">View product</span></a>
  </div></div></section>
'''))

# ------------------------------------------------------------------ INGREDIENTS
PAGES.append(("ingredients", "Ingredients | Herbaferm Singapore", '''
@@PHERO_ING@@
<section><div class="wrap">
  <div>@@EXPLORER@@</div>
</div></section>

<section class="alt"><div class="wrap">
  <p class="eyebrow">Product by product</p><h2>What is in each one</h2>
  <div class="three" style="margin-top:30px">
    <div class="card"><h3>Herbaferm Drops</h3><p>A fermented extract of all seven herbs, in a 30 ml bottle. No preservatives, no artificial colours.</p></div>
    <div class="card"><h3>Fiber Elite</h3><p>75% whole barley malt and 12.5% oat flour, a fine powder with a malt aroma. Contains gluten. @@TAG_CONFIRM@@</p></div>
    <div class="card"><h3>Prefer HF400</h3><p>Fermented herb fibres (200 mg per capsule) with fulvic acid, humic acid and vitamin C, in a gelatine capsule.</p></div>
  </div>
  <p class="note" style="margin-top:18px">Curious how the herbs become a drop? See <a href="#science">how fermentation works</a>, or read the plain-English version in the <a href="#a-ferment">journal</a>.</p>
</div></section>

<section><div class="wrap">
  <p class="eyebrow">Clean formula</p><h2>What is not in it</h2>
  <div class="four" style="margin-top:30px">
    <div class="card"><h3>No preservatives</h3><p>Which is why Drops live in the fridge.</p></div>
    <div class="card"><h3>No artificial colours</h3><p>The colour comes from the herbs.</p></div>
    <div class="card"><h3>No artificial additives</h3><p>A short list of plant ingredients.</p></div>
    <div class="card"><h3>Vegan Fiber Elite</h3><p>Fiber Elite is vegan and GMO-free, but contains gluten.</p></div>
  </div>
  <p class="note" style="margin-top:18px">Prefer HF400 uses a gelatine capsule shell. Allergen and dietary statements must match the final Singapore label. @@TAG_CONFIRM@@</p>
</div></section>
'''))

# ------------------------------------------------------------------ SCIENCE
PAGES.append(("science", "Science | Herbaferm Singapore", '''
@@PHERO_SCI@@
<section><div class="wrap split top">
  <div class="stack"><p class="eyebrow">The idea</p><h2>Why fermentation</h2>
    <p class="lede">Fermentation is one of the oldest food technologies. Herbaferm ferments a blend of herbs with a natural community of microorganisms, so the result carries the plants and the compounds produced during fermentation.</p>
    <p class="lede">The leaflet describes the drops as containing a diverse natural microbiota in low concentrations. No colony count is published, so we do not quote one.</p></div>
  <div class="honest"><b>What we say, and what we don't</b><p>Herbaferm products are dietary supplements. Our own leaflets state that no health effects can be attributed to them. They are not medicines, and they do not diagnose, treat or prevent any condition.</p></div>
</div></section>

<section class="alt"><div class="wrap">
  <p class="eyebrow">Plain-language glossary</p><h2>Terms you will see on gut-health labels</h2>
  <p class="lede">Definitions follow the international scientific consensus statements from ISAPP, the International Scientific Association for Probiotics and Prebiotics.</p>
  <div class="two" style="margin-top:30px">
    <div class="card"><h3>Microbiome</h3><p>The community of microorganisms living in a particular environment, here the human gut.</p></div>
    <div class="card"><h3>Probiotic</h3><p>Live microorganisms that, when given in adequate amounts, confer a health benefit on the host (Hill et al., 2014).</p></div>
    <div class="card"><h3>Prebiotic</h3><p>A substrate that is selectively used by host microorganisms to confer a health benefit (Gibson et al., 2017).</p></div>
    <div class="card"><h3>Postbiotic</h3><p>A preparation of inanimate microorganisms and/or their components that confers a health benefit (Salminen et al., 2021).</p></div>
  </div>
  <p class="note" style="margin-top:16px">Herbaferm's leaflets use "rebiotic" and "prebiotic" for the products. The label category for Singapore is to be confirmed. @@TAG_CONFIRM@@</p>
</div></section>

<section><div class="wrap">
  <p class="eyebrow">Research</p><h2>The studies, and what each one covers</h2>
  <ul class="refs" style="margin-top:30px">
    <li><b>Fiber Elite related study, JISSN 2024</b><span>Fritz P., Fritz R., Bóday P., Bóday Á. et al. <i>Journal of the International Society of Sports Nutrition</i>, 2024, 21(1). 20 elite male water polo players, 10 vs 10, 31 days, vegan protein with or without pre- and probiotics. Herbaferm's founders are co-authors, and the abstract does not name Fiber Elite.</span> <a href="https://doi.org/10.1080/15502783.2023.2297992" target="_blank" rel="noopener">doi.org/10.1080/15502783.2023.2297992</a></li>
    <li><b>Fermented foods and the human microbiome, Cell 2021</b><span>Wastyk H.C. et al. <i>Cell</i>, 2021, 184(16):4137-4153. A 10-week trial in healthy adults comparing a high-fermented-food diet with a high-fibre diet. It studied fermented foods in general. It is not a study of Herbaferm products.</span> <a href="https://doi.org/10.1016/j.cell.2021.06.019" target="_blank" rel="noopener">doi.org/10.1016/j.cell.2021.06.019</a></li>
    <li><b>Probiotic definition, 2014</b><span>Hill C. et al. <i>Nature Reviews Gastroenterology &amp; Hepatology</i>, 2014, 11:506-514.</span> <a href="https://doi.org/10.1038/nrgastro.2014.66" target="_blank" rel="noopener">doi.org/10.1038/nrgastro.2014.66</a></li>
    <li><b>Prebiotic definition, 2017</b><span>Gibson G.R. et al. <i>Nature Reviews Gastroenterology &amp; Hepatology</i>, 2017, 14:491-502.</span> <a href="https://doi.org/10.1038/nrgastro.2017.75" target="_blank" rel="noopener">doi.org/10.1038/nrgastro.2017.75</a></li>
    <li><b>Postbiotic definition, 2021</b><span>Salminen S. et al. <i>Nature Reviews Gastroenterology &amp; Hepatology</i>, 2021, 18:649-667.</span> <a href="https://doi.org/10.1038/s41575-021-00440-6" target="_blank" rel="noopener">doi.org/10.1038/s41575-021-00440-6</a></li>
  </ul>
  <p class="note" style="margin-top:14px">Please verify each reference against the original article before launch. Herbaferm's own microbiome publications and the university textbook will be added when the client approves the set. @@TAG_CONFIRM@@</p>
</div></section>

<section class="dark"><div class="wrap">
  <div class="three">
    <div class="card"><div class="ic">@@BOOK@@</div><h3>Education</h3><p>Herbaferm's scientific team contributes to microbiome education and publication. Details to be supplied. @@TAG_CONFIRM@@</p></div>
    <div class="card"><div class="ic">@@FLASK@@</div><h3>Testing partners</h3><p>Microbiome testing is offered through partners and clinics in Singapore. Partner names are listed on the Partners page. @@TAG_CONFIRM@@</p></div>
    <div class="card"><div class="ic">@@USERS@@</div><h3>Real-world feedback</h3><p>Clinics ask for user feedback. We will publish verified Singapore feedback when we have it. @@TAG_SUPPLY@@</p></div>
  </div>
</div></section>
'''))

# ------------------------------------------------------------------ LEARN
PAGES.append(("learn", "Learn | Herbaferm Singapore", '''
@@PHERO_LEARN@@
<section><div class="wrap">
  <div class="sechead"><div><p class="eyebrow">Guide 1</p><h2>The Herbaferm Drops starter guide</h2><p class="lede">A gentle build-up, based on the product leaflet.</p></div></div>
  <ul class="timeline">
    <li><b>Days 1 to 3</b><p>5 drops in the morning and 5 in the evening, in a glass of water.</p></li>
    <li><b>Weeks 1 to 3</b><p>Increase gradually, up to 15 drops twice a day. Some people notice temporary digestive changes at this stage. If so, hold at the current amount or reduce.</p></li>
    <li><b>From week 3</b><p>Settle at 8 drops twice a day, which is the regular amount. A bottle then lasts about a month.</p></li>
    <li><b>Always</b><p>Keep the bottle in the fridge at 5 to 12 °C. Take drops in water. Speak to a professional if you take medication or have a medical condition.</p></li>
  </ul>
  <p class="note" style="margin-top:18px">Schedule taken from the English Drops leaflet. Other Herbaferm materials give a slightly different schedule, so the Singapore label must be confirmed. @@TAG_CONFIRM@@</p>
</div></section>

<section class="alt"><div class="wrap">
  <p class="eyebrow">Guide 2</p><h2>Four ways to use Fiber Elite</h2>
  <p class="lede">Idea cards for the one product in the range that can be cooked with. Use the 3.5 g everyday amount. Recipes are drafts for Herbaferm to test and approve. @@TAG_CONFIRM@@</p>
  <div class="four" style="margin-top:30px">
    <div class="card"><div class="ic">@@WHEAT@@</div><h3>Morning porridge</h3><p>Stir into warm oats at the end of cooking, then top with fruit and seeds.</p></div>
    <div class="card"><div class="ic">@@DROP@@</div><h3>Post-training shake</h3><p>Blend with your usual protein shake. Athletes take 3.5 g after exercise.</p></div>
    <div class="card"><div class="ic">@@LEAF@@</div><h3>Fruit smoothie</h3><p>Add to a smoothie of banana, berries and your preferred milk.</p></div>
    <div class="card"><div class="ic">@@BOOK@@</div><h3>Yoghurt bowl</h3><p>Mix into plain yoghurt and finish with nuts and a little honey.</p></div>
  </div>
</div></section>

<section><div class="wrap">
  <p class="eyebrow">Guide 3</p><h2>A balanced approach</h2>
  <div class="three" style="margin-top:30px">
    <div class="step"><span class="n">Diet</span><h3>Keep it varied</h3><p>Herbaferm products sit beside a varied, mostly natural diet. The leaflets encourage food from natural sources and fewer refined and processed foods.</p></div>
    <div class="step"><span class="n">Routine</span><h3>Link it to a habit</h3><p>Take drops with your morning water and again in the evening, so the routine is easy to keep.</p></div>
    <div class="step"><span class="n">Advice</span><h3>Ask a professional</h3><p>If you have a condition, take medication or are pregnant, speak to a doctor or pharmacist first.</p></div>
  </div>
</div></section>

<section class="alt"><div class="wrap split top">
  <div><p class="eyebrow">Free guide</p><h2>Get the printable starter guide</h2><p class="lede">A one-page PDF with the schedule, storage tips and Fiber Elite ideas. The PDF is produced once the content is approved. @@TAG_SUPPLY@@</p></div>
  <form class="form" data-proto="Thanks. This is a prototype, so nothing was sent." novalidate><label for="g-email">Email address<input id="g-email" type="email" autocomplete="email" placeholder="you@example.com"></label><button class="btn btn-forest" type="submit">Send me the guide</button><p class="note fnote">Prototype form.</p></form>
</div></section>
'''))

# ------------------------------------------------------------------ ABOUT
PAGES.append(("about", "About | Herbaferm Singapore", '''
@@PHERO_ABOUT@@
<section><div class="wrap split top">
  <div class="stack"><p class="eyebrow">Our story</p><span class="lgi" role="img" aria-label="Herbaferm leaf-in-circle emblem"></span><h2>A Hungarian formula, now in Singapore</h2>
    <p class="lede">Herbaferm develops food supplements by fermenting medicinal herbs with a natural community of microorganisms. The Drops were registered in Hungary in 2018, and the team set up Herbaferm Pte. Ltd. in Singapore in 2023.</p>
    <p class="lede">The founders come from food science, medicine and finance, and the company still works closely with the scientists behind the formula. @@TAG_CONFIRM@@</p></div>
  <div><img src="@@img:flatlay@@" alt="Propolis, oak bark, elderflower and wormwood arranged around a Herbaferm Drops bottle" style="border-radius:26px;width:100%"></div>
</div></section>

<section class="alt"><div class="wrap">
  <p class="eyebrow">Milestones</p><h2>From the first registration to Singapore</h2>
  <ul class="timeline" style="margin-top:34px">
    <li><b>Budapest</b><p>The company starts in Budapest, Hungary. The investor deck says about eight years before November 2025. @@TAG_CONFIRM@@</p></li>
    <li><b>2018</b><p>Herbaferm Drops registered in Hungary, no. 20075/2018.</p></li>
    <li><b>2023</b><p>Herbaferm Pte. Ltd. established in Singapore.</p></li>
    <li><b>2024</b><p>Study related to Fiber Elite published in the Journal of the International Society of Sports Nutrition.</p></li>
    <li><b>2026</b><p>Gold Award at the CIM Hong Kong Bay Area Vitality Living Brand Outstanding Awards.</p></li>
  </ul>
  <p class="note" style="margin-top:16px">Additional milestones (formula development, UK launch as ReBiotika, first Singapore partners) can be added once confirmed. @@TAG_CONFIRM@@</p>
</div></section>

<section><div class="wrap">
  <p class="eyebrow">The team</p><h2>People behind Herbaferm</h2>
  <div class="four" style="margin-top:30px">
    <div class="card"><div class="avatar">TV</div><h3>Thomas Vargoczky</h3><p>Co-founder and CEO</p></div>
    <div class="card"><div class="avatar">ÁB</div><h3>Ádám Bóday</h3><p>Co-founder, scientist</p></div>
    <div class="card"><div class="avatar">DB</div><h3>Dániel Bóday</h3><p>Co-founder, finance</p></div>
    <div class="card"><div class="avatar">SK</div><h3>Szabina Kodela</h3><p>Singapore contact</p></div>
  </div>
  <p class="lede" style="margin-top:28px">Herbaferm also runs sites for <a href="https://herbaferm.hu/" target="_blank" rel="noopener" style="color:var(--leaf)">Hungary</a> and the <a href="https://herbaferm.co.uk/" target="_blank" rel="noopener" style="color:var(--leaf)">UK</a>. This site is for Singapore.</p>
  <p class="note" style="margin-top:16px">Names and titles are taken from the investor deck. Photos, short bios and confirmation of roles are needed. @@TAG_SUPPLY@@</p>
</div></section>

<section class="dark"><div class="wrap">
  <p class="eyebrow">What guides us</p><h2>Principles</h2>
  <div class="three" style="margin-top:30px">
    <div class="card"><h3>Natural process</h3><p>Plant ingredients and traditional fermentation, with no artificial additives, preservatives or colours.</p></div>
    <div class="card"><h3>Honest communication</h3><p>We describe what the products are and what the research covers. We do not promise outcomes.</p></div>
    <div class="card"><h3>Practitioner partnership</h3><p>We work with clinics and specialists who guide customers, and supply the evidence they ask for.</p></div>
  </div>
</div></section>
'''))

# ------------------------------------------------------------------ QUALITY
PAGES.append(("quality", "Quality and certificates | Herbaferm Singapore", '''
@@PHERO_QUALITY@@
<section><div class="wrap">
  <p class="eyebrow">Documents</p><h2>Paperwork you can check</h2>
  <p class="lede">Asian buyers and clinic partners look at documents first, so they live here. Each item becomes a downloadable file once supplied. Items marked as needing an update are not yet ready for public use.</p>
  <div class="docs" style="margin-top:30px">
    <div class="doc"><span class="ok">On file</span><h3>Product registration</h3><p>Herbaferm Drops, Hungarian National Institute of Pharmacy and Nutrition, no. 20075/2018.</p></div>
    <div class="doc"><span class="ok">On file</span><h3>Capsule certificate of analysis</h3><p>Capsule shell supplier document for Prefer HF400.</p></div>
    <div class="doc"><span class="ok">On file</span><h3>Product leaflets</h3><p>English leaflets for Drops and Prefer HF400, and the Fiber Elite leaflet.</p></div>
    <div class="doc"><span class="tag" style="align-self:flex-start">Update needed</span><h3>Microbiology declaration</h3><p>A current lab report is being prepared. Ask us for the latest declaration.</p></div>
    <div class="doc"><span class="tag" style="align-self:flex-start">Update needed</span><h3>ISO 9001:2015</h3><p>Renewal in progress. The current certificate will be added here once issued.</p></div>
    <div class="doc"><span class="tag" style="align-self:flex-start">To supply</span><h3>HACCP plan summary</h3><p>The HACCP file received is a scan. A readable summary is needed.</p></div>
    <div class="doc"><span class="tag" style="align-self:flex-start">To confirm</span><h3>Singapore classification</h3><p>How the products are classified and labelled in Singapore, as confirmed by Herbaferm.</p></div>
    <div class="doc"><span class="tag" style="align-self:flex-start">To supply</span><h3>Stability and shelf life</h3><p>Stability data and best-before periods for each product.</p></div>
  </div>
</div></section>

<section class="alt"><div class="wrap">
  <p class="eyebrow">Made in Hungary</p><h2>Developed and produced by Herbaferm Kft.</h2>
  <div class="three" style="margin-top:30px">
    <div class="card"><div class="ic">@@FLASK@@</div><h3>Own production</h3><p>The company develops and produces its dietary supplement family at Csömör, Hungary.</p></div>
    <div class="card"><div class="ic">@@SNOW@@</div><h3>Cold storage</h3><p>Drops contain no preservatives and need refrigeration at 5 to 12 °C. We plan the supply chain around this.</p></div>
    <div class="card"><div class="ic">@@CLOCK@@</div><h3>Shelf life</h3><p>Best-before dates are printed on every pack. Typical periods will be listed once confirmed. @@TAG_CONFIRM@@</p></div>
  </div>
</div></section>

<section><div class="wrap">
  <div class="sechead"><div><h2>Recognition</h2><p class="lede">Gold Award at the CIM Hong Kong Bay Area Vitality Living Brand Outstanding Awards 2026, and more on the awards page.</p></div><a class="btn btn-line" href="#awards">See awards</a></div>
</div></section>
'''))

# ------------------------------------------------------------------ PARTNERS
PAGES.append(("partners", "Partners | Herbaferm Singapore", '''
@@PHERO_PARTNERS@@
<section><div class="wrap">
  <p class="eyebrow">Who we work with</p><h2>Three kinds of partner</h2>
  <div class="three" style="margin-top:30px">
    <div class="card"><div class="ic">@@USERS@@</div><h3>Clinics and practitioners</h3><p>Longevity clinics and GPs who offer microbiome testing, personalised nutrition or structured protocols, and recommend supplements to their patients.</p></div>
    <div class="card"><div class="ic">@@GLOBE@@</div><h3>Retailers</h3><p>Specialist health stores and premium retail. Drops need chilled shelves. Fiber Elite and Prefer HF400 suit ambient shelves.</p></div>
    <div class="card"><div class="ic">@@DOC@@</div><h3>Distributors</h3><p>Bulk and regional partners, and marketplace sellers for the ambient products.</p></div>
  </div>
</div></section>

<section class="alt"><div class="wrap split top">
  <div>
    <p class="eyebrow">The evidence pack</p><h2>What partners usually ask for</h2>
    <p class="lede">Eight items, in the order partners tend to ask. We assemble them for you on request.</p>
    <ol style="margin:22px 0 0;padding-left:1.2em;display:grid;gap:8px"><li>Formulation and ingredient documentation</li><li>Safety and quality-control information</li><li>Manufacturing standards and batch testing</li><li>Stability and shelf-life data</li><li>Microbiological and contaminant testing</li><li>Regulatory and product classification</li><li>Available scientific literature</li><li>Clinical or real-world evidence, where available</li></ol>
    <p class="note" style="margin-top:16px">Medically oriented partners expect more evidence. Items still being updated are listed on the Quality page.</p>
  </div>
  <div class="formbox"><h3>Request the evidence pack</h3>
    <form class="form" style="margin-top:16px" data-proto="Thanks. This is a prototype, so nothing was sent. In the live site this goes to Herbaferm's partner inbox." novalidate>
      <label for="pf-name">Your name<input id="pf-name" autocomplete="name"></label>
      <label for="pf-org">Organisation<input id="pf-org" autocomplete="organization"></label>
      <label for="pf-email">Email<input id="pf-email" type="email" autocomplete="email"></label>
      <label for="pf-type">I am a<select id="pf-type"><option>Clinic or practitioner</option><option>Retailer</option><option>Distributor</option><option>Other</option></select></label>
      <label for="pf-msg">Message<textarea id="pf-msg"></textarea></label>
      <button class="btn btn-forest" type="submit">Request the evidence pack</button>
      <p class="note fnote">Prototype form: nothing is sent yet. Live contact: szabina@herbafermsg.com @@TAG_CONFIRM@@</p>
    </form></div>
</div></section>

<section><div class="wrap">
  <p class="eyebrow">How it works</p><h2>From enquiry to first order</h2>
  <div class="proc" style="margin-top:30px">
    <div>@@MAIL@@<h3>Enquire</h3><p>Tell us what you do and who you serve.</p></div>
    <div>@@DOC@@<h3>Review the pack</h3><p>We send the evidence pack and answer questions.</p></div>
    <div>@@FLASK@@<h3>Try the range</h3><p>Samples or a trial order. @@TAG_CONFIRM@@</p></div>
    <div>@@USERS@@<h3>Onboard</h3><p>Training material, customer guides and a named contact.</p></div>
  </div>
</div></section>

<section><div class="wrap">
  <p class="eyebrow">Where we are heading</p><h2>Six places to find Herbaferm</h2>
  <p class="lede">The Singapore plan starts with practitioners, then widens. These are target channels, not confirmed stockists.</p>
  <div class="chan" style="margin-top:30px">
    <div class="card"><b class="ph1">1</b><h3>Longevity and preventive clinics</h3><p>Start here: practitioner-led and evidence-minded.</p></div>
    <div class="card"><b class="ph1">1</b><h3>Specialist and gastro clinics</h3><p>Digestive, wellness and sports practices.</p></div>
    <div class="card"><b class="ph1">2</b><h3>TCM clinics</h3><p>A natural fit for fermented herbal products. Classification to confirm.</p></div>
    <div class="card"><b class="ph1">2</b><h3>Pharmacies and health retail</h3><p>Chilled shelves are needed for Drops.</p></div>
    <div class="card"><b class="ph1">3</b><h3>Premium and supplement retail</h3><p>Specialist and department stores.</p></div>
    <div class="card"><b class="ph1">3</b><h3>Online marketplaces</h3><p>Better for the ambient products than for chilled Drops.</p></div>
  </div>
  <p class="note" style="margin-top:14px">Numbers show the suggested order: 1 establish, 2 test, 3 scale. Taken from the project's distribution list and midterm plan. @@TAG_CONFIRM@@</p>
</div></section>

<section><div class="wrap">
  <p class="eyebrow">Already in Singapore</p><h2>First listings on a Singapore marketplace</h2>
  <p class="lede">All three products are listed on ConnectingDNA, a Singapore wellness marketplace, with next-business-day delivery shown. Early traction, not proof of demand.</p>
  <div class="tblwrap" style="margin-top:28px"><table>
    <thead><tr><th></th><th>Herbaferm Drops</th><th>Fiber Elite</th><th>Prefer HF400</th></tr></thead>
    <tbody>
      <tr><td>Pack</td><td>30 ml bottle</td><td>125 g pouch</td><td>14 capsules</td></tr>
      <tr><td>Units sold when checked</td><td>12+</td><td>17+</td><td>20+</td></tr>
      <tr><td>Reviews</td><td>None yet</td><td>None yet</td><td>None yet</td></tr>
    </tbody></table></div>
  <p class="note" style="margin-top:14px">Checked on 18 October 2026. The marketplace's own wording on benefits is marketing copy and is not used here.</p>
</div></section>

<section class="alt"><div class="wrap">
  <p class="eyebrow">Partners</p><h2>Practitioners and specialists we already work with</h2>
  <div class="allies" style="margin-top:24px"><span>Biotier Longevity</span><span>TSquared Health</span><span>ConnectingDNA</span></div>
  <p class="note" style="margin-top:16px">Listed from the client's own partner list. Herbaferm should confirm permission to show each name and add links. @@TAG_CONFIRM@@</p>
  <div class="cta" style="margin-top:40px"><div><h2>Prefer to talk first?</h2><p>Send a message and we will arrange a call.</p></div><a class="btn btn-honey" href="#contact">Contact us</a></div>
</div></section>
'''))

# ------------------------------------------------------------------ FAQ
PAGES.append(("faq", "FAQ | Herbaferm Singapore", '''
@@PHERO_FAQ@@
<section><div class="wrap">
  <div class="faqtools"><input id="faq-q" type="search" placeholder="Search questions" aria-label="Search questions">
    <div class="chips" id="faq-chips"><button type="button" data-c="all" aria-pressed="true">All</button><button type="button" data-c="use" aria-pressed="false">Using</button><button type="button" data-c="safety" aria-pressed="false">Safety</button><button type="button" data-c="products" aria-pressed="false">Products</button><button type="button" data-c="ordering" aria-pressed="false">Ordering</button><button type="button" data-c="about" aria-pressed="false">About</button><button type="button" data-c="partners" aria-pressed="false">Partners</button></div></div>
  <div class="faq" id="faq-list">@@FAQ_ITEMS@@</div>
  <p class="nores" id="faq-none" hidden>No questions match. Try another word, or <a href="#contact" style="color:var(--leaf)">contact us</a>.</p>
</div></section>
'''))

# ------------------------------------------------------------------ CONTACT
PAGES.append(("contact", "Contact | Herbaferm Singapore", '''
@@PHERO_CONTACT@@
<section><div class="wrap split top">
  <div class="stack">
    <div class="card"><div class="ic">@@MAIL@@</div><h3>Email</h3><p>szabina@herbafermsg.com @@TAG_CONFIRM@@</p></div>
    <div class="card"><div class="ic">@@GLOBE@@</div><h3>Company</h3><p>Herbaferm Pte. Ltd., Singapore. UEN 202350449W. Office: 10 Anson Road #22-02, International Plaza, Singapore 079903, as shown on the Singapore leaflet. @@TAG_CONFIRM@@ Opening hours @@TAG_SUPPLY@@</p></div>
    <div class="card"><div class="ic">@@USERS@@</div><h3>Practitioners and retailers</h3><p>Use the <a href="#partners" style="color:var(--leaf)">Partners page</a> to request the evidence pack.</p></div>
  </div>
  <div class="formbox"><h3>Send us a message</h3>
    <form class="form" style="margin-top:16px" data-proto="Thanks. This is a prototype, so nothing was sent." novalidate>
      <label for="c-name">Your name<input id="c-name" autocomplete="name"></label>
      <label for="c-email">Email<input id="c-email" type="email" autocomplete="email"></label>
      <label for="c-topic">Topic<select id="c-topic"><option>A question about a product</option><option>An order</option><option>Becoming a partner</option><option>Something else</option></select></label>
      <label for="c-msg">Message<textarea id="c-msg"></textarea></label>
      <button class="btn btn-forest" type="submit">Send message</button>
      <p class="note fnote">Prototype form: nothing is sent yet.</p>
    </form></div>
</div></section>
'''))

# ------------------------------------------------------------------ POLICIES
PAGES.append(("policies", "Policies | Herbaferm Singapore", '''
@@PHERO_POLICIES@@
<section><div class="wrap policy">
  <h3 style="margin-top:0">Shipping</h3><p>Delivery areas, fees, timings and chilled delivery for Drops will be set out here. @@TAG_SUPPLY@@</p>
  <h3>Returns and refunds</h3><p>Return windows and conditions for opened and unopened products will be set out here. @@TAG_SUPPLY@@</p>
  <h3>Privacy</h3><p>How personal data is collected and used, in line with Singapore's Personal Data Protection Act. @@TAG_SUPPLY@@</p>
  <h3>Terms of service</h3><p>The terms for using this site and ordering from it. @@TAG_SUPPLY@@</p>
  <h3>Health information</h3><p>Herbaferm products are food supplements. They are not intended to diagnose, treat, cure or prevent any disease, and are not a substitute for a varied diet or medical advice. Speak to a healthcare professional if you are pregnant, breastfeeding, have a medical condition or take medication.</p>
</div></section>
'''))

PHEROS = {
    "AWARDS": phero("Awards", "Recognition", "Awards and accolades", "What Herbaferm has been recognised for, and what is still to be confirmed."),
    "SHOP": phero("Shop", "The range", "Shop Herbaferm", "Three fermented herbal food supplements. Prices in Singapore dollars."),
    "ING": phero("Ingredients", "Ingredients", "Seven herbs, one fermentation", "What goes into each product, and what is left out."),
    "SCI": phero("Science", "Science", "The science, stated plainly", "How fermentation works, the terms explained, and the research behind the range, including what each study does and does not cover."),
    "LEARN": phero("Learn", "Learn", "Guides and ideas", "Starter schedules, Fiber Elite ideas and a balanced approach to everyday use."),
    "ABOUT": phero("About", "About Herbaferm", "A Hungarian formula, in Singapore", "Who we are, where the range comes from and what we stand for."),
    "QUALITY": phero("Quality", "Quality and certificates", "Quality you can check", "Registrations, lab documents and manufacturing information, with what is still being updated."),
    "PARTNERS": phero("Partners", "For clinics, retailers and distributors", "Carry Herbaferm in Singapore", "Tell us how you would stock or recommend the range, and we will send the evidence pack."),
    "FAQ": phero("FAQ", "Help", "Questions, answered", "Using the products, safety, ordering and partnering. Search or filter by topic."),
    "CONTACT": phero("Contact", "Contact", "Get in touch", "Questions about the range, an order or a partnership."),
    "POLICIES": phero("Policies", "Legal", "Policies and health information", "Shipping, returns, privacy and terms."),
}
