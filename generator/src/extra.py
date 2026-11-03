# v3 additions: photo slots, interactive blocks, journal articles, new home and learn pages.
import pages as P

CAM = P.ic('<path d="M4 8h3l1.5-2h7L17 8h3v11H4z"/><circle cx="12" cy="13.5" r="3.5"/>')


def slot(ratio, title, brief, extra=""):
    return ('<div class="slot %s %s"><span aria-hidden="true">%s</span><b>%s</b><small>%s</small>'
            '<span class="tag">Photo to supply</span><small style="opacity:.8">Click to preview one of your own photos here</small>'
            '<input type="file" accept="image/*" aria-label="Preview a photo in the slot: %s">'
            '<button class="rm" type="button">Remove</button></div>') % (ratio, extra, CAM, title, brief, title)


def slots(items, two=False):
    return '<div class="slots%s">%s</div>' % (" two" if two else "", "".join(slot(*i) for i in items))


# ---------------------------------------------------------------- articles
ARTICLES = [
    ("a-ferment", "cv1", "Science", "So what is fermentation, really?", "The old kitchen process behind every Herbaferm product, without the jargon.",
     '''<p>If you have ever eaten yoghurt, sourdough, kimchi or miso, you have already met fermentation. Tiny organisms like bacteria and yeasts feed on parts of the food and turn them into something new. That is why yoghurt is tangy and why dough rises. People have been doing this for thousands of years, long before anyone knew what a microbe was.</p>
<h2>Where the herbs come in</h2>
<p>Herbaferm takes the same idea and applies it to plants. Chamomile, yarrow, elderflower, rosehip, propolis, oak bark and white wormwood are fermented slowly with a natural community of microorganisms. The leaflet says it is mainly <i>Lactobacillus</i>, at low concentrations. What comes out the other end is a concentrated herbal extract, which is what fills the 30 ml bottle.</p>
<h2>What we can and cannot tell you</h2>
<p>We can tell you how the drops are made. We cannot give you a colony count, because there is no verified figure to quote, so we do not quote one. And we do not say the drops treat or prevent anything: they are food supplements, and our own leaflets state that no health effects can be attributed to them.</p>
<p>If you like the detail, the <a href="#science">Science page</a> lists the studies and what each one does and does not cover.</p>'''),
    ("a-month", "cv2", "Guide", "Your first month with Drops", "How to ease in, what to expect, and when to settle on your regular amount.",
     '''<figure class="afig"><img src="@@img:drops-pour@@" alt="Adding drops to a glass of water" loading="lazy"></figure>
<p>A new routine sticks best when it is small and attached to something you already do. For most people that means the glass of water at breakfast. Here is how the leaflet suggests you begin.</p>
<h2>Days one to three: keep it light</h2>
<p>Put 5 drops in a glass of water in the morning, and 5 more in the evening. That is all. The bottle lives in the fridge (5 to 12 °C), because the drops have no preservatives.</p>
<h2>Weeks one to three: go up slowly</h2>
<p>Add a drop or two every few days, up to a ceiling of 15 drops twice a day. Some people notice a bit of gas or looser stools while their body gets used to it. If that is you, stay where you are, or step back one level. There is no prize for getting there faster.</p>
<h2>From week three: your regular amount</h2>
<p>Settle at 8 drops twice a day in about 1.5 dl of water. A 30 ml bottle holds roughly 480 drops, so at that amount it lasts about a month.</p>
<h2>Before you start</h2>
<ul><li>If you take medication, are pregnant or have a diagnosed condition, talk to your doctor or pharmacist first.</li><li>Stop if you react to any ingredient.</li><li>The Singapore label may be worded a little differently, so go by the pack in your hand.</li></ul>'''),
    ("a-fiber", "cv5", "Kitchen", "Four easy ways to eat Fiber Elite", "It smells a bit like malt and survives the stove, so it goes further than a shake.",
     '''<p>Fiber Elite is a fine, flour-like powder with a malty smell, a bit like the inside of a granola bar. The everyday amount on the leaflet is 3.5 g, which is a small spoonful, taken with a meal. Because you can heat it, it is not just for cold drinks.</p>
<h2>Stirred into porridge</h2>
<p>Add it near the end of cooking so it blends in, then top with fruit and seeds.</p>
<h2>In a post-training shake</h2>
<p>People who train hard take 3.5 g two or three times a day after exercise. Blend it into a protein shake or a smoothie.</p>
<h2>In a fruit smoothie</h2>
<p>Banana, berries, your usual milk and a spoonful of Fiber Elite. Nothing fancy.</p>
<h2>On yoghurt</h2>
<p>Mix it into plain yoghurt, then add nuts and a drizzle of honey.</p>
<p class="note">Worth knowing: Fiber Elite is 75% whole barley malt and 12.5% oat flour, and it contains gluten. These are draft ideas that Herbaferm should test and approve.</p>'''),
    ("a-labels", "cv3", "Science", "Probiotic, prebiotic, postbiotic: what the words mean", "Three look-alike words on gut-health labels, sorted out in plain English.",
     '''<p>Walk down any supplement aisle and you will see all three words. They sound alike, but they mean different things. Scientists at ISAPP, the International Scientific Association for Probiotics and Prebiotics, have agreed definitions, and they are worth knowing.</p>
<h2>Probiotic: the living bugs</h2>
<p>These are live microorganisms. The definition adds that they must be given in a large enough amount to actually do something for the person taking them.</p>
<h2>Prebiotic: the food for the bugs</h2>
<p>This is something the microorganisms already living in your gut use as fuel. It is not a microbe itself.</p>
<h2>Postbiotic: what is left of the bugs</h2>
<p>These are microorganisms that are no longer alive, plus the parts and compounds they leave behind.</p>
<h2>So which is Herbaferm?</h2>
<p>Herbaferm leaflets use the words "rebiotic" and "prebiotic". Which category fits on a Singapore label has not been confirmed, so for now we do not call any product a probiotic. The exact definitions and their sources are on the <a href="#science">Science page</a>.</p>'''),
    ("a-herbs", "cv6", "Ingredients", "Meet the seven herbs", "Where each one comes from and what people have traditionally done with it.",
     '''<p>None of these seven is exotic. All of them have a place in European kitchens and herbal cabinets, and that is the point. What is described below is traditional use, not a health effect.</p>
<h2>Chamomile</h2><p>The little daisy-like flower in the tea you reach for when your stomach is unsettled. Traditionally used for gentle digestive comfort.</p>
<h2>Yarrow</h2><p>It grows at the edge of fields and paths. Herbal practice in Europe has long used it to support digestion.</p>
<h2>Elderflower</h2><p>The creamy blossoms of the elder tree, familiar from cordials and traditional preparations.</p>
<h2>Rosehip</h2><p>The bright fruit of the dog rose, a natural source of vitamin C.</p>
<h2>Propolis</h2><p>A sticky resin that bees gather from plant buds and use to seal the hive. Valued traditionally for its protective qualities.</p>
<h2>Oak bark</h2><p>Rich in tannins, which is what gives it its dry, grippy taste. It has a long history in preparations for the digestive tract.</p>
<h2>White wormwood</h2><p>A very bitter herb. Traditional European practice uses bitter herbs to support digestion.</p>
<p>The <a href="#ingredients">Ingredients page</a> lets you tap through each herb and see which products use it.</p>'''),
    ("a-gut", "cv4", "Science", "The gut microbiome in plain words", "What the word means, what scientists are still working out, and where food and herbs fit in.",
     '''<p>You may have seen the word microbiome on a label or in a headline. It means the community of microorganisms, mostly bacteria, that live in and on the human body. The biggest community is in the gut.</p>
<h2>A community, not a single thing</h2>
<p>Everyone carries their own mix, and the mix changes over time with age, food, sleep, medicines and where we live. Researchers are still working out what a healthy mix looks like, and how much any single food or supplement changes it.</p>
<h2>Why food comes up so often</h2>
<p>What we eat is one of the everyday things that feeds this community. Fibre-rich plant foods, fermented foods and a varied diet are the usual starting points in general dietary advice. Herbaferm products are food supplements that sit next to a varied diet. They do not replace it.</p>
<h2>Where Herbaferm fits</h2>
<p>Herbaferm Drops are made from seven herbs that are fermented slowly with a natural community of microorganisms, and Fiber Elite is a fibre-rich food additive. Our leaflets state that no health effects can be attributed to the products, and we do not claim that they treat or prevent any condition.</p>
<h2>Want to read more?</h2>
<p>The Herbaferm team has published a book on the subject, <i>The Holistic Microbiome</i> by Adam Boday. See the <a href="#awards">About page</a> for details. If you have a digestive condition or take medication, talk to a doctor or pharmacist first.</p>'''),
    ("a-fridge", "cv4", "Practical", "Why the bottle goes in the fridge", "No preservatives means a bit more care. Here is what that looks like day to day.",
     '''<p>Herbaferm Drops contain no preservatives. For many people that is the whole appeal. The trade-off is simple: once the bottle is yours, it lives in the fridge, at 5 to 12 °C.</p>
<h2>At home</h2>
<p>Keep it in the door shelf, next to the water you pour your morning glass from. Seeing the bottle when you reach for the water is the easiest reminder there is.</p>
<h2>If you run a clinic or a shop</h2>
<p>Drops need chilled storage, so they suit a clinic fridge or a chilled shelf better than an ambient display. Fiber Elite and Prefer HF400 are easier: they can sit on a normal shelf. We are happy to talk through storage and delivery with partners.</p>
<h2>Check the date</h2>
<p>The best-before date is printed on each pack. Typical shelf-life periods will be added here once they are confirmed.</p>'''),
]


SHORT = {}


def article_page(i):
    aid, cv, cat, title, dek, body = ARTICLES[i]
    prev = ARTICLES[i - 1]
    nxt = ARTICLES[(i + 1) % len(ARTICLES)]
    import re as _re
    words = len(_re.sub(r"<[^>]+>", " ", body).split())
    mins = max(1, round(words / 200.0))
    heads = _re.findall(r"<h2>(.*?)</h2>", body)
    n = [0]

    def idh(m):
        n[0] += 1
        return '<h2 id="%s-s%d">%s</h2>' % (aid, n[0], m.group(1))
    body = _re.sub(r"<h2>(.*?)</h2>", idh, body)
    toc = ""
    if len(heads) > 4:
        toc = '<nav class="toc" aria-label="On this page"><b>On this page</b>%s</nav>' % "".join(
            '<a href="#%s" data-jump="%s-s%d">%s</a>' % (aid, aid, k + 1, h) for k, h in enumerate(heads))
    short = SHORT.get(aid)
    box = ('<aside class="inshort"><b>In short</b><ul>%s</ul></aside>' % "".join("<li>%s</li>" % x for x in short)) if short else ""
    return (aid, title + " | Herbaferm Journal", '''
<div class="phero"><div class="wrap"><div class="crumbs"><a href="#home">Home</a> / <a href="#learn">Learn</a> / %s</div>
<p class="kicker">%s</p><h1>%s</h1><p class="lede">%s</p><p class="rt">%d min read</p></div></div>
<section><div class="wrap"><article class="article"><span class="tag draft">Draft for Herbaferm review</span>
%s%s
%s
<div class="apager"><a href="#%s"><small>Previous</small><b>%s</b></a><a href="#%s"><small>Next</small><b>%s</b></a></div>
</article></div></section>
''' % (cat, cat, title, dek, mins, box, toc, body, prev[0], prev[3], nxt[0], nxt[3]))


def jcard(a):
    return ('<a class="jcard rv" href="#%s" data-c="%s"><div class="cover %s"><span>%s</span></div><div><small>%s</small><h3>%s</h3><p>%s</p></div></a>'
            % (a[0], a[2], a[1], a[3], a[2], a[3], a[4]))


# ---------------------------------------------------------------- interactive blocks
def explorer():
    btns, panels = "", ""
    for k, h in enumerate(P.HERBS):
        sel = "true" if k == 0 else "false"
        btns += '<button type="button" role="tab" data-h="%s" aria-selected="%s">%s<span>%s</span></button>' % (h[0], sel, h[1], h[2])
        panels += ('<div class="hpanel" data-hp="%s"%s><div class="hart"><img src="@@img:herb-%s@@" alt="%s"></div><div><h3>%s</h3><span class="lat">%s</span><p>%s</p>'
                   '<div class="where"><span class="pill">Herbaferm Drops</span><span class="pill">Prefer HF400</span></div></div></div>'
                   % (h[0], "" if k == 0 else " hidden", h[0], h[3], h[1], h[2], h[4]))
    return '<div class="explorer"><div class="hlist" role="tablist" aria-label="The seven herbs">%s</div><div class="hstage">%s</div></div>' % (btns, panels)


QUIZ = '''
<div class="quiz" id="quiz">
  <div><h2>Find your starting routine</h2><p class="lede">Three quick questions about how you like to take things. It suggests a routine, not medical advice.</p></div>
  <div>
    <div class="qprog"><i class="on"></i><i></i><i></i></div>
    <div class="qstep" data-q="1"><h3>How would you rather take it?</h3><div class="opts">
      <button type="button" data-v="drops">A few drops in a glass of water</button>
      <button type="button" data-v="fiber">Stirred into food or a drink</button>
      <button type="button" data-v="prefer">A capsule with water</button></div></div>
    <div class="qstep" data-q="2" hidden><h3>What do your days look like?</h3><div class="opts">
      <button type="button" data-v="train">Regular training sessions</button>
      <button type="button" data-v="desk">Busy desk days, meals on the go</button>
      <button type="button" data-v="cook">Cooking at home most nights</button></div></div>
    <div class="qstep" data-q="3" hidden><h3>How much do you want to take on?</h3><div class="opts">
      <button type="button" data-v="one">Just one thing to start</button>
      <button type="button" data-v="two">A small routine of two</button>
      <button type="button" data-v="all">The full set</button></div></div>
    <div class="qstep qres" data-q="r" hidden><p class="rname" id="q-name"></p><p id="q-text"></p>
      <div class="btns"><button class="btn btn-honey" type="button" id="q-add">Add to cart</button><a class="btn btn-line" id="q-view" href="#shop">See the range</a></div>
      <button class="qrestart" type="button" id="q-redo">Start again</button></div>
  </div>
</div>'''

CALC_DROPS = '''
<div class="calc" data-total="480" data-unit="drops" data-name="bottle" data-dose="0">
  <div><h3>How long will a bottle last?</h3><p class="lede" style="margin-top:12px">A 30 ml bottle holds about 480 drops. Move the sliders to match how you take them.</p>
    <label>Drops per time <output class="v c-av">8</output><input class="c-a" type="range" min="3" max="15" value="8" aria-label="Drops per time"></label>
    <label>Times per day <output class="v c-bv">2</output><input class="c-b" type="range" min="1" max="3" value="2" aria-label="Times per day"></label></div>
  <div class="res"><div class="big2 c-out">30</div><small class="c-cap">days from one 30 ml bottle</small><div class="bar"><i class="c-bar"></i></div></div>
</div>'''

CALC_FIBER = '''
<div class="calc" data-total="125" data-unit="g" data-name="pouch" data-dose="3.5">
  <div><h3>How long will a pouch last?</h3><p class="lede" style="margin-top:12px">A 125 g pouch at 3.5 g per serving. Everyday use is once a day; athletes take two or three servings after training.</p>
    <label>Servings per day <output class="v c-bv">1</output><input class="c-b" type="range" min="1" max="3" value="1" aria-label="Servings per day"></label></div>
  <div class="res"><div class="big2 c-out">35</div><small class="c-cap">days from one 125 g pouch</small><div class="bar"><i class="c-bar"></i></div></div>
</div>'''

SCI_STEPS = [
    ("Select", P.LEAF, "Seven herbs are chosen for their long history in European herbal use: chamomile, yarrow, elderflower, rosehip, propolis, oak bark and white wormwood."),
    ("Ferment", P.FLASK, "The herbs are fermented gently, using a traditional method, with a natural community of microorganisms."),
    ("Mature", P.CLOCK, "Fermentation cultivates a diverse community, described in the leaflet as mainly Lactobacillus species in low concentrations."),
    ("Bottle", P.DROP, "The fermented herbal extract is filled into 30 ml bottles, with no preservatives, artificial colours or additives. It goes in the fridge."),
]


def stepper():
    b = ""
    for k, s in enumerate(SCI_STEPS):
        b += '<button type="button" role="tab" data-s="%d" aria-selected="%s"><i>%s</i><b>%s</b></button>' % (k, "true" if k == 0 else "false", s[1], s[0])
    return '<div class="stepper" role="tablist" aria-label="From herb to bottle">%s</div><p class="stepdetail" id="stepdetail" data-steps=\'%s\'>%s</p>' % (
        b, "|".join(s[2] for s in SCI_STEPS), SCI_STEPS[0][2])


# ---------------------------------------------------------------- HOME
HOME = '''
<div class="jr" data-journey>
<nav class="jrail" aria-label="Page chapters"></nav>

<section class="ch ch-hero" data-bg="#2b3a24" data-fg="#fbf4e4" data-ac="#e9b04a" data-label="Start">
  <i class="blob b1" data-par="-.12"></i><i class="blob b2" data-par=".1"></i>
  <div class="wrap herojr">
    <div class="jtxt">
      <p class="kicker jv">Fermented herbal food supplements for everyday gut health, in Singapore</p>
      <h1 class="jh1"><span class="jv" data-split>Seven herbs.</span><span class="rot" aria-live="off"><b class="on">Fermented slowly.</b><b>Born in Hungary.</b><b>Now in Singapore.</b></span></h1>
      <p class="jsub jv">A fermented herbal routine for everyday gut care. Eight drops in a glass of water, morning and evening.</p>
      <div class="btns jv"><a class="jbtn" href="#shop">Shop the range</a><a class="jbtn ghost" href="#science">How it is made</a></div>
      <ul class="jchips jv"><li>Takes about a minute a day</li><li>No preservatives or artificial colours</li><li>About S$1.83 a day</li></ul>
    </div>
    <div class="jhero-img" data-par=".08"><div class="arch"><img src="@@img:drops@@" alt="Herbaferm Drops 30 ml bottle with carton and kraft wrapper"></div></div>
  </div>
  <a class="cue" href="#jr-benefits" data-go aria-label="Scroll to the next chapter"><span></span></a>
</section>

<section class="ch ch-auto" id="jr-benefits" data-bg="#f7efdc" data-fg="#2a2417" data-ac="#b4562b" data-label="Drops">
  <div class="wrap jdrops">
    <div class="jdv jv">
      <div class="jdimg"><img src="@@img:drops@@" alt="Herbaferm Drops 30 ml bottle with carton and kraft wrapper"></div>
      <figure class="jdpour"><img src="@@img:drops-pour@@" alt="Adding drops to a glass of water (illustrative image)" loading="lazy"></figure>
    </div>
    <div class="jdt">
      <p class="kicker jv">Meet Herbaferm Drops</p>
      <h2 class="jh2 jv">A small bottle for a simple daily habit.</h2>
      <p class="jp jv">Seven herbs, fermented slowly into a drop you stir into a glass of water.</p>
      <ul class="jcheck jv"><li><i><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg></i><span><b>Supports everyday digestion</b><em>Seven herbs traditionally used in Europe for gentle digestive comfort.</em></span></li><li><i><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg></i><span><b>Fits into your day in a minute</b><em>8 drops in a glass of water, morning and evening. Nothing to prepare.</em></span></li><li><i><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg></i><span><b>Gentle and simple</b><em>No preservatives, no artificial colours or additives.</em></span></li><li><i><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg></i><span><b>Good for a whole month</b><em>One 30 ml bottle, about 480 drops, from S$1.83 a day.</em></span></li></ul>
      <div class="jbuy2 jv"><b>S$55</b><button class="jbtn" type="button" data-add="drops">Add to cart</button><a class="jlink" href="#drops">See details</a></div>
      <p class="jnote jv">Food supplement. Speak to a healthcare professional if you are pregnant or take medication.</p>
    </div>
  </div>
</section>

<section class="ch" id="jr-range" data-bg="#efdfc0" data-fg="#2f2615" data-ac="#b4562b" data-label="The range">
  <i class="blob b1" data-par=".12"></i>
  <div class="wrap">
    <p class="kicker jv">The range</p>
    <h2 class="jh2" data-split>Start with Drops. Add the rest when you want them.</h2>
    <div class="jprods">
      <article class="pcd jv"><a href="#drops" class="jimg"><img src="@@img:drops@@" alt="Herbaferm Drops bottle and carton"></a><small>Signature product</small><h3>Herbaferm Drops</h3><p>Herbal extract made by natural fermentation. 8 drops in a glass of water, twice a day.</p><div class="jbuy"><b>S$55</b><span>30 ml, about a month</span><button class="jbtn sm" type="button" data-add="drops">Add to cart</button></div></article>
      <article class="pcd jv"><a href="#fiber" class="jimg white">@@PACK_FIBER@@</a><small>Everyday add-in</small><h3>Fiber Elite</h3><p>A fibre-rich additive for smoothies, shakes, yoghurt and porridge. 3.5 g a day with a meal.</p><div class="jbuy"><b>S$55</b><span>125 g, about a month</span><button class="jbtn sm" type="button" data-add="fiber">Add to cart</button></div></article>
      <article class="pcd jv"><a href="#prefer" class="jimg white"><img src="@@img:prefer@@" alt="Prefer HF400 bottle and capsule"></a><small>Optional add-on</small><h3>Prefer HF400</h3><p>Capsules of fermented herb fibres, taken alongside Drops, morning and evening.</p><div class="jbuy"><b>S$45</b><span>14 capsules</span><button class="jbtn sm" type="button" data-add="prefer">Add to cart</button></div></article>
    </div>
    <p class="jv"><a class="jlink" href="#shop">Compare all three</a></p>
  </div>
</section>

<section class="ch" id="jr-origin" data-bg="#e9c06a" data-fg="#2b1c05" data-ac="#6b3d12" data-label="Origin">
  <i class="blob b1" data-par=".14"></i>
  <div class="wrap jsplit"><div>
    <p class="kicker jv">Where it began</p>
    <h2 class="jh2" data-split>It started in Hungary, with a scientist and a lot of herbs.</h2>
    <p class="jp jv">A Hungarian founding team, with a scientist at its centre, developed Herbaferm Drops. The Drops were registered in Hungary in 2018. Since 2023, Herbaferm has been a Singapore company.</p>
    <ul class="jstats jv">
      <li><strong><span data-count="2018">2018</span></strong><span>Drops registered in Hungary</span></li>
      <li><strong><span data-count="20">20</span>+</strong><span>years of research behind the work @@TAG_CONFIRM@@</span></li>
      <li><strong><span data-count="2023">2023</span></strong><span>Herbaferm Pte. Ltd. in Singapore</span></li>
    </ul>
    <p class="jv"><a class="jlink" href="#about">Meet the team</a></p>
  </div><div class="arch jv" data-par=".06"><img src="@@img:ai-meadow@@" alt="A flowering meadow with chamomile and yarrow at sunset (illustrative image)" loading="lazy"><span class="ill">Illustrative image</span></div></div>
</section>

<section class="ch ch-herbs" id="jr-herbs" data-label="Seven herbs" data-dyn>
  <div class="hstage">
    <div class="wrap hwrap">
      <p class="kicker">Seven herbs you probably know</p>
      <div class="hpanes">@@JHERBS@@</div>
      <div class="hcount"><span id="hnow">1</span> / 7</div>
    </div>
  </div>
</section>

<section class="ch" id="jr-ferment" data-bg="#c4683f" data-fg="#fff4e4" data-ac="#ffe2a8" data-label="Fermentation">
  <i class="blob b2" data-par="-.1"></i>
  <div class="wrap jsplit"><div>
    <p class="kicker jv">How it is made</p>
    <h2 class="jh2" data-split>Slow on purpose.</h2>
    <ol class="jsteps">
      <li class="jv"><b>01</b><div><h3>Pick the herbs</h3><p>Chamomile, yarrow, elderflower, rosehip, propolis, oak bark and white wormwood. Kitchen and herbal-tea plants from Europe.</p></div></li>
      <li class="jv"><b>02</b><div><h3>Let them ferment</h3><p>Natural fermentation, the slow, traditional way. No rush, no shortcuts.</p></div></li>
      <li class="jv"><b>03</b><div><h3>Bottle it, nothing added</h3><p>No preservatives and no artificial colours. The fridge does the job instead: keep the bottle at 5 to 12 &deg;C.</p></div></li>
    </ol>
    <p class="jv"><a class="jlink" href="#science">See the science and its limits</a></p>
  </div><div class="arch jv" data-par=".06"><img src="@@img:ai-jars@@" alt="Chamomile and yarrow fermenting in glass jars (illustrative image)" loading="lazy"><span class="ill">Illustrative image</span></div></div>
</section>


<section class="ch ch-day" data-bg="#f3dcae" data-fg="#2e1a00" data-ac="#b4562b" data-label="Morning">
  <div class="wrap jsplit">
    <div><p class="kicker jv">A day with Herbaferm</p><h2 class="jh2" data-split>Morning: a glass of water, and a few drops.</h2>
    <p class="jp jv">Fill a glass with about 1.5 dl of water and add 8 drops of Herbaferm Drops. Take the capsule alongside, if you use Prefer HF400.</p></div>
    <div class="arch jv" data-par=".06"><img src="@@img:drops-pour@@" alt="A hand adding Herbaferm Drops to a glass of water, with fruit in the background" style="object-position:55% 50%"></div>
  </div>
</section>
<section class="ch ch-day" data-bg="#d3cf9c" data-fg="#2a2a10" data-ac="#6b3d12" data-label="Midday">
  <div class="wrap jsplit rev">
    <div><h2 class="jh2" data-split>Midday: stirred into whatever you are eating.</h2>
    <p class="jp jv">Fiber Elite goes into porridge, yoghurt or a smoothie. It can be heated, so soups and warm bowls work too. Take 3.5 g a day with a meal, or on training days 3.5 g after exercise, up to three times.</p></div>
    <div class="jpack jv" data-par="-.05">@@PACK_FIBER@@</div>
  </div>
</section>
<section class="ch ch-day" data-bg="#3a2c1e" data-fg="#fbf1df" data-ac="#e9b04a" data-label="Evening">
  <i class="blob b2" data-par=".1"></i>
  <div class="wrap jcol">
    <h2 class="jh2" data-split>Evening: the same glass, the same drops.</h2>
    <p class="jp jv">Repeat the morning routine, then put the bottle back in the fridge at 5 to 12 &deg;C. A 30 ml bottle holds about 480 drops, which is about a month at the regular amount.</p>
    <p class="jv"><a class="jlink" href="#a-month">Read the first-month guide</a></p>
  </div>
</section>

<section class="ch" id="jr-loved" data-bg="#efd5bf" data-fg="#43200f" data-ac="#b4562b" data-label="For you">
  <i class="blob b1" data-par="-.12"></i>
  <div class="wrap">
    <p class="kicker jv">For you, or someone you love</p>
    <h2 class="jh2" data-split>Shopping for yourself, or a loved one?</h2>
    <p class="jp jv">Buying for a parent, a grandparent or a new mum? Pick a routine that suits them. If they are pregnant, recovering from birth or on medication, check with their healthcare professional first. These are illustrative stories, not customers.</p>
    <div class="jstories">
      <article class="pcd glass jv"><small>The new mum</small><h3>Mornings are a blur</h3><p>Between feeds and nappies she needs something she can do with one hand. Drops go into the glass of water she already pours.</p><a class="jlink" href="#drops">See Drops</a></article>
      <article class="pcd glass jv"><small>The active professional</small><h3>Meals on the move</h3><p>Early training, long desk days, lunch at the keyboard. A spoonful of Fiber Elite goes into the shake or the oats.</p><a class="jlink" href="#fiber">See Fiber Elite</a></article>
      <article class="pcd glass jv"><small>Getting back into routine</small><h3>Small, steady and gentle</h3><p>After a big change, a routine works best when it starts small. A healthcare professional should be asked first.</p><a class="jlink" href="#a-month">Read the guide</a></article>
    </div>
    <p class="jv"><a class="jbtn" href="#shop">Shop the range</a></p>
  </div>
</section>

<section class="ch" id="jr-proof" data-bg="#2b3a24" data-fg="#fbf4e4" data-ac="#e9b04a" data-label="Trust">
  <i class="blob b2" data-par=".1"></i>
  <div class="wrap">
    <p class="kicker jv">Why you can trust it</p>
    <h2 class="jh2" data-split>Awards, documents and honest limits.</h2>
    <div class="jaward">
      <img class="jv" src="@@img:award@@" alt="CIM Hong Kong Bay Area Vitality Living Brand Outstanding Award 2026, Gold Award, Herbaferm Pte Ltd" width="250" height="354">
      <div class="jv">
        <h3>Gold Award, Bay Area Vitality Living Brand Outstanding Award 2026</h3>
        <p>Presented by the Chartered Institute of Marketing Hong Kong in the Healthy Dietary (Vegetarian) category for 2025/26.</p>
        <h3 style="margin-top:20px">TOP 10 Winner, TOP 10 Longevity Breakthrough Awards 2026</h3>
        <p>Awarded to Herbaferm Pte. Ltd. by the Asia-Pacific Longevity Medicine Society, in celebration of excellence and innovation in longevity medicine.</p>
        <p style="margin-top:14px"><a class="jlink" href="#awards">All awards and accolades</a> &nbsp; <a class="jlink" href="#quality">Quality and certificates</a></p>
      </div>
    </div>
    <div class="jaward jv" style="margin-top:8px"><img src="@@img:book@@" alt="Cover of The Holistic Microbiome by Adam Boday, with the herbaferm logo" width="200" height="205" loading="lazy" style="width:min(200px,50vw);border-radius:12px"><div><h3>The Holistic Microbiome, by Adam Boday (2026)</h3><p>A plain-language book on the microbiome, published by Herbaferm. <a class="jlink" href="#a-gut">Our short guide to the gut microbiome</a></p></div></div>
    <p class="jp jv">Herbaferm products are food supplements, not medicines. They sit beside a varied diet and do not replace one. Our leaflets state that no health effects can be attributed to the products.</p>
  </div>
</section>

<div class="marq jmarq" aria-hidden="true"><div class="mq"><span>Chamomile</span><span>Yarrow</span><span>Elderflower</span><span>Rosehip</span><span>Propolis</span><span>Oak bark</span><span>White wormwood</span><span>Chamomile</span><span>Yarrow</span><span>Elderflower</span><span>Rosehip</span><span>Propolis</span><span>Oak bark</span><span>White wormwood</span></div></div>

<section class="ch ch-explore" id="jr-explore" data-bg="var(--bg)" data-fg="var(--fg)" data-ac="var(--forest)" data-label="Explore">
  <div class="wrap">
    <p class="kicker jv">Keep exploring</p>
    <h2 class="jh2" data-split>Find your starting point.</h2>
    <div class="jv" style="margin-top:28px">@@QUIZ@@</div>
    <div class="sechead" style="margin-top:56px"><div><h2>From the journal</h2><p class="lede">Guides, kitchen ideas and plain-language science.</p></div><a class="btn btn-line" href="#learn">All articles</a></div>
    <div class="jcar" data-auto="jcar"><div class="jtrack" tabindex="0" aria-label="Journal articles">@@JHOME@@</div><div class="jnav"><button type="button" data-d="-1" aria-label="Previous articles">&larr;</button><button type="button" data-d="1" aria-label="Next articles">&rarr;</button></div></div>
  </div>
</section>

<section class="ch ch-end" data-bg="#2b3a24" data-fg="#fbf4e4" data-ac="#e9b04a" data-label="Join us">
  <i class="blob b1" data-par=".1"></i>
  <div class="wrap jsplit top">
    <div><p class="kicker jv">Partners</p><h2 class="jh2" data-split>Clinic, retailer or distributor?</h2>
    <p class="jp jv">Ask for the partner evidence pack: formulation, quality, testing, shelf life and literature.</p>
    <p class="jv"><a class="jbtn" href="#partners">Become a partner</a></p></div>
    <form class="form jform jv" data-proto="Thanks. This is a prototype, so nothing was sent." novalidate><h3>Guides and news</h3><p>An occasional email with usage guides, Fiber Elite ideas and Singapore stockist news.</p><label for="nl-email">Email address<input id="nl-email" type="email" autocomplete="email" placeholder="you@example.com"></label><button class="jbtn" type="submit">Subscribe</button><p class="note fnote">We will only use your email for Herbaferm news. @@TAG_CONFIRM@@</p></form>
  </div>
</section>
</div>
'''

# ---------------------------------------------------------------- LEARN
LEARN = '''
@@PHERO_LEARN@@
<section><div class="wrap">
  <a class="jfeat rv" href="#a-month"><div class="cover cv2"><span>Your first month with Drops</span></div><div><p class="kicker" style="color:var(--leaf)">Featured guide</p><h2>Your first month with Drops</h2><p>How to ease in, what to expect, and when to settle on your regular amount.</p><p><span class="more">Read the guide</span></p></div></a>
  <div class="faqtools"><div class="chips" id="j-chips"><button type="button" data-c="all" aria-pressed="true">All</button><button type="button" data-c="Guide" aria-pressed="false">Guides</button><button type="button" data-c="Science" aria-pressed="false">Science</button><button type="button" data-c="Kitchen" aria-pressed="false">Kitchen</button><button type="button" data-c="Ingredients" aria-pressed="false">Ingredients</button><button type="button" data-c="Practical" aria-pressed="false">Practical</button></div></div>
  <div class="jgrid" id="j-grid">@@JALL@@</div>
  <p class="note" style="margin-top:36px">Articles are drafts written from the product leaflets and published research, for Herbaferm to review and extend. @@TAG_CONFIRM@@</p>
</div></section>

<section><div class="wrap split top">
  <div><h2>Get the printable starter guide</h2><p class="lede">A one-page PDF with the first-month schedule, storage tips and Fiber Elite ideas. The schedule itself is in <a href="#a-month">Your first month with Drops</a>. The PDF is produced once the content is approved. @@TAG_SUPPLY@@</p></div>
  <form class="form" data-proto="Thanks. This is a prototype, so nothing was sent." novalidate><label for="g-email">Email address<input id="g-email" type="email" autocomplete="email" placeholder="you@example.com"></label><button class="btn btn-forest" type="submit">Send me the guide</button><p class="note fnote">Prototype form.</p></form>
</div></section>
'''


# ---------------------------------------------------------------- AWARDS
AWARDS = '''
@@PHERO_AWARDS@@
<section><div class="wrap">
  <div class="award">
    <img src="@@img:award@@" alt="CIM Hong Kong Bay Area Vitality Living Brand Outstanding Award 2026, Gold Award, Herbaferm Pte Ltd" width="250" height="354">
    <div><p class="kicker" style="color:var(--leaf)">2026</p><h2 style="font-size:clamp(1.6rem,3vw,2.3rem)">Gold Award, Bay Area Vitality Living Brand Outstanding Award</h2>
    <p>Presented to Herbaferm by the Chartered Institute of Marketing Hong Kong in the Healthy Dietary (Vegetarian) category for 2025/26.</p></div>
  </div>
</div></section>

<section class="alt"><div class="wrap">
  <div class="award">
    <div style="display:grid;gap:14px;width:min(400px,100%)"><img src="@@img:awardtop@@" alt="Certificate of Recognition: TOP 10 Winner, TOP 10 Longevity Breakthrough Awards 2026, awarded to Herbaferm Pte. Ltd. by the Asia-Pacific Longevity Medicine Society" width="400" height="300" style="width:100%;height:auto;border-radius:10px"><img src="@@img:plate@@" alt="The award plate on its carved wooden stand, with a plaque reading Top 10 Longevity Breakthrough Awards 2026" width="300" height="400" loading="lazy" style="width:70%;height:auto;border-radius:10px;justify-self:center"></div>
    <div><p class="kicker" style="color:var(--leaf)">2026</p><h2 style="font-size:clamp(1.6rem,3vw,2.3rem)">TOP 10 Winner, TOP 10 Longevity Breakthrough Awards</h2>
    <p>Awarded to Herbaferm Pte. Ltd. by the Asia-Pacific Longevity Medicine Society, in celebration of excellence and innovation in longevity medicine.</p>
    <p class="note" style="margin-top:12px">This recognises the company and its work. It is not evidence that a product works or is safe for any health purpose.</p></div>
  </div>
</div></section>

<section><div class="wrap">
  <div class="sechead"><div><h2>Also on the record</h2><p class="lede">These are registrations and publications, not awards, but they are part of the same story.</p></div></div>
  <div class="three" style="margin-top:28px">
    <a class="card" href="#quality"><h3>Registered in Hungary, 2018</h3><p>Herbaferm Drops, no. 20075/2018, as a food supplement.</p><span class="more">Quality and documents</span></a>
    <a class="card" href="#science"><h3>Published research, 2024</h3><p>A study related to Fiber Elite in the Journal of the International Society of Sports Nutrition.</p><span class="more">What it covers</span></a>
    <a class="card" href="#about"><h3>Singapore company, 2023</h3><p>Herbaferm Pte. Ltd. established in Singapore.</p><span class="more">About Herbaferm</span></a>
  </div>
  <div class="award" style="margin-top:48px"><img src="@@img:book@@" alt="Cover of The Holistic Microbiome by Adam Boday, with the herbaferm logo" width="280" height="287" loading="lazy" style="width:min(280px,100%);height:auto;border-radius:14px"><div><p class="kicker" style="color:var(--leaf)">Book, 2026</p><h3 style="font-size:1.6rem">The Holistic Microbiome: Nature is complex but never complicated</h3><p>By Adam Boday, published by Herbaferm. A plain-language book on the microbiome and the natural world around it. Where to buy it in Singapore is still to be confirmed. @@TAG_CONFIRM@@</p><p><a class="more" href="#a-gut">Read our short guide to the gut microbiome</a></p></div></div>
  <p class="note" style="margin-top:20px">Awards recognise the brand. They are not health claims, and our leaflets state that no health effects can be attributed to the products.</p>
</div></section>
'''


# ---------------------------------------------------------------- INSIGHT (design evidence)
def _f(finding, change):
    return '<div class="finding rv"><div><small>What the attention data showed</small><p>%s</p></div><div><small>What changed in this prototype</small><p>%s</p></div></div>' % (finding, change)


INSIGHT = '''
<div class="phero"><div class="wrap"><div class="crumbs"><a href="#home">Home</a> / Design evidence</div>
<p class="kicker">For the project team</p><h1>How attention data shaped this prototype</h1>
<p class="lede">The team ran Attention Insight on the live Herbaferm Singapore and Rebiotika UK pages. This page lists what it found and what we changed because of it. It is for review and will not be part of the launch site.</p></div></div>

<section><div class="wrap">
  <h2>What was measured</h2>
  <p class="lede">Attention Insight predicts where people look in the first seconds. It does not measure what anyone reads, understands or buys. Pages were captured at 1512 by 742 px.</p>
  <div class="tblwrap" style="margin-top:28px"><table class="cmp">
    <thead><tr><th>Page</th><th>Clarity score</th><th>First screen text</th><th>Reading ease</th><th>Other</th></tr></thead>
    <tbody>
      <tr><td>Herbaferm home</td><td>73, optimal</td><td>0 words in the first screen</td><td>Flesch 20, grade 13</td><td>Image share of attention 3.3%, against a 17% average</td></tr>
      <tr><td>Herbaferm product</td><td>49, moderate</td><td>15 words</td><td>Flesch 20, grade 14</td><td>287 words under one heading, smallest text 10 px</td></tr>
      <tr><td>Herbaferm blog</td><td>74, optimal</td><td>0 words</td><td>Flesch 32, grade 14</td><td>1,154 words, 22 sentences over 25 words, 4 min 51 s read</td></tr>
      <tr><td>Rebiotika home</td><td>38, moderate</td><td>64 words, heavy (3.8 times the reference window)</td><td>Flesch 48, grade 9</td><td>15 of 36 first-glance lines fail contrast</td></tr>
      <tr><td>Rebiotika product</td><td>55, moderate</td><td>No text in first screen</td><td>Flesch 57, grade 8</td><td>18 of 80 first-glance lines fail contrast</td></tr>
      <tr><td>Rebiotika about (Learn)</td><td>39, moderate</td><td>61 words, heavy (3.9 times)</td><td>Flesch 45, grade 10</td><td>11 of 43 first-glance lines fail contrast. CTA share 5.1%, above the 3.4% average</td></tr>
    </tbody></table></div>
  <p class="note" style="margin-top:14px">Source: Attention Insight reports and text analysis supplied by the team. The report labelled Rebiotika Learn Page was captured on the About us page.</p>
</div></section>

<section class="alt"><div class="wrap">
  <h2>What we changed, and why</h2>
  <div class="findings">
  ''' + "".join([
    _f("Herbaferm home: the first screen was one large image. It held no headline and no button, so no text got any attention.",
       "The hero now has a headline, one line, one main button, and the Drops with price and an Add to cart button. About 25 words."),
    _f("Herbaferm home: the three products sat below the fold and drew little attention. Images took only 3.3% of attention.",
       "The range moved up to sit directly under the hero. Each card shows a large pack shot, price and a button."),
    _f("Rebiotika home: 64 words in the first screen made it heavy to read. Clarity was only 38, with four text cards and a repeated promo badge competing.",
       "Our hero stays short. The moving ticker is gone, replaced by a quiet four-fact strip. There are no floating promo badges."),
    _f("Rebiotika: between 15 and 18 first-glance text lines failed WCAG contrast on the home and product pages.",
       "Every text and button colour was checked against 4.5 to 1 (3 to 1 for large text). The accent green was darkened. Buttons use dark text on honey."),
    _f("Herbaferm product: smallest text was 10 px, with 13 lines below the target size. Rebiotika had 21.",
       "No text is under 13 px. Body copy is 16 to 17 px."),
    _f("Herbaferm product: 287 words sat under one heading, the Latin ingredient list ran 66 words, and the same pack photo was shown three times.",
       "Content is split into How to use, Ingredients and Good to know. Plain herb names lead and Latin names follow. The gallery switches between the pack, the seven herbs and an in-use photo slot."),
    _f("Herbaferm product: the Add to cart button was an outline, and the heatmap shows almost no attention on it.",
       "A solid, wide Add to cart button sits beside the quantity picker. On phones a sticky buy bar appears once you scroll past it."),
    _f("Rebiotika product was the clearest of the six pages: one title, one price, one button, then short benefit rows.",
       "Our product pages follow that order. Ledes are now one sentence. The safety note is one line, with the detail under Good to know."),
    _f("Faces and hands drew the strongest attention on Rebiotika, in the home photos and the product gallery.",
       "Photo slots now ask for people using the product, not just packs. The first one is on the home page, under the fridge story."),
    _f("Herbaferm blog: 1,154 words, grade 14 reading level, and 22 sentences over 25 words in one post.",
       "Articles open with an In short box, a read time and contents links. Sections are short, the line length is about 70 characters, and sentences stay brief."),
    _f("Herbaferm home reads at Flesch 20, grade 13. The longest sentence ran 31 words and described the product's mode of action.",
       "Home copy uses short sentences, and the long mode-of-action sentence is not reused.")]) + '''
  </div>
</div></section>

<section><div class="wrap">
  <h2>Facts added from the project files</h2>
  <p class="lede">The FSP4003 folder holds the same documents the project already had. Each fact below is on the site and tagged To confirm where the sources disagree.</p>
  <div class="tblwrap" style="margin-top:24px"><table class="cmp">
    <thead><tr><th>Fact</th><th>Where on the site</th><th>Source</th></tr></thead>
    <tbody>
      <tr><td>Cost per day: Drops S$1.83, Fiber Elite S$1.54, Prefer HF400 S$3.21 per capsule</td><td>Product pages, FAQ</td><td>Our own sums from list prices and leaflet doses</td></tr>
      <tr><td>Free from preservatives, alcohol and sugar</td><td>Drops page, FAQ</td><td>Investor deck and awards submission. Leaflets confirm only no preservatives</td></tr>
      <tr><td>Shelf life: about 6 months for Drops, 1 year for capsules</td><td>FAQ</td><td>Meeting 1 notes, 4 Aug 2026</td></tr>
      <tr><td>Company started in Budapest. Hungary and UK sites listed</td><td>About</td><td>Investor deck</td></tr>
      <tr><td>Office at 10 Anson Road #22-02, International Plaza</td><td>Contact</td><td>Singapore product range leaflet</td></tr>
      <tr><td>Six target channels in three phases: establish, test, scale</td><td>Partners, Shop</td><td>Distribution partner list and midterm plan. No store names shown</td></tr>
    </tbody></table></div>
  <p class="note" style="margin-top:14px">Not added: disease or symptom claims from the deck and leaflets, the Fiber Elite nutrient table (its ingredients differ between documents), the Vietnam and New Zealand market claims (meeting notes list different markets), and the long list of named clinics and retailers, which are targets, not confirmed stockists.</p>
</div></section>

<section><div class="wrap">
  <h2>What this prototype scores on the same checks</h2>
  <p class="lede">Attention Insight itself could not be run on this prototype from here. We measured the parts that can be checked in code: first-screen words, text size, contrast and sentence length.</p>
  <div class="tblwrap" style="margin-top:24px"><table class="cmp">
    <thead><tr><th>Check</th><th>Before</th><th>Now</th></tr></thead>
    <tbody>
      <tr><td>Text under 13 px, home</td><td>20 pieces of text</td><td>None</td></tr>
      <tr><td>Text failing contrast, home</td><td>7 pieces of text</td><td>None</td></tr>
      <tr><td>First screen words, Drops page</td><td>93</td><td>78</td></tr>
      <tr><td>First screen words, Fiber Elite page</td><td>102</td><td>87</td></tr>
      <tr><td>First screen words, Prefer HF400 page</td><td>78</td><td>67</td></tr>
      <tr><td>Reading ease, home (Flesch, our own count)</td><td>48</td><td>53</td></tr>
    </tbody></table></div>
  <p class="note" style="margin-top:14px">Counts include the breadcrumb and navigation text inside the page. To confirm the attention effect, run the Attention Insight extension on the shared link and compare it with the table above.</p>
</div></section>

<section class="alt"><div class="wrap">
  <h2>Still needed from Herbaferm</h2>
  <p class="lede">What would turn this prototype into a launch-ready site. None of it is invented here.</p>
  <ul class="plainlist" style="margin-top:20px;display:grid;gap:10px">
    <li><b>Photos:</b> Fiber Elite in use, the team, the Csömör production site, a clinic or shop shelf. English-label packs if they exist for Singapore.</li>
    <li><b>Prices and offers:</b> the prototype uses S$55, S$55 and S$45.</li>
    <li><b>Dosage and formulation:</b> final Fiber Elite composition and the Prefer HF400 dose, where documents differ.</li>
    <li><b>Quality documents:</b> a current ISO 9001 certificate (the one on file expired on 24 October 2024), a current microbiology report and a readable HACCP summary.</li>
    <li><b>Shelf life and stability data</b> for each product, and Singapore label classification.</li>
    <li><b>Policies:</b> shipping, returns, privacy and terms, plus delivery and payment details.</li>
    <li><b>Permissions:</b> to show partner and clinic names, and a real contact email and opening hours.</li>
  </ul>
</div></section>
'''


# ---------------------------------------------------------------- product page sections
PROD = {
 "drops": dict(
  more=dict(suits=["Adults who like a small, simple daily routine","People who already pour a glass of water morning and evening","Anyone shopping for a parent or loved one, once their healthcare professional is happy"],
  check=["You are pregnant or breastfeeding","You take medication or have a diagnosed condition","You are sensitive to histamine","You are thinking of giving it to a child"],
  shelf="<img class=\"pfridge\" src=\"@@img:ai-fridge@@\" alt=\"Small dark bottles and a jar on a fridge door shelf (illustrative image)\" loading=\"lazy\"><br>Keep the bottle in the fridge at 5 to 12 \u00b0C and shake before use. Herbaferm's notes give about 6 months of shelf life. @@TAG_CONFIRM@@ The best-before date is printed on the pack.",
  also=[("fiber","Fiber Elite","S$55 \u00b7 125 g"),("prefer","Prefer HF400","S$45 \u00b7 14 capsules")]),
  pt="#c4a85a",
  trust=["No preservatives", "No artificial colours", "Registered in Hungary, 2018", "Seven herbs, naturally fermented"],
  glance=[("8", "drops, twice a day"), ("480", "drops in a 30 ml bottle"), ("1 month", "from one bottle"), ("S$1.83", "a day")],
  steps=[("Fill a glass", "About 1.5 dl of water."), ("Add 8 drops", "Morning and evening. Shake the bottle first."), ("Back in the fridge", "Keep it at 5 to 12 \u00b0C. There are no preservatives.")],
  stepnote='New to it? Start with 5 drops morning and evening and build up over two to three weeks. <a href="#a-month">Read the first-month guide</a>. @@TAG_CONFIRM@@',
  img='<img src="@@img:drops-pour@@" alt="A hand adding Herbaferm Drops to a glass of water" loading="lazy" style="object-position:55% 50%">',
  inside_h="Seven herbs, fermented slowly",
  inside='<figure class="pfig"><img src="@@img:ai-herbs@@" alt="Chamomile, elderflower, oak bark and rosehip on a linen cloth (illustrative image)" loading="lazy"><span class="ill">Illustrative image</span></figure><p>Chamomile, yarrow, elderflower, rosehip, propolis, oak bark and white wormwood. Kitchen and herbal-tea plants from Europe, fermented the traditional way. No artificial additives, preservatives or colours.</p><p style="margin-top:12px"><a class="more" href="#ingredients">Meet the seven herbs</a></p>',
  faq=[0, 1, 2, 15, 11, 5, 19, 20]),
 "fiber": dict(
  more=dict(suits=["People who like to stir something into the meals they already make","Active people who want an after-training add-in","Anyone who prefers a powder to drops or capsules"],
  check=["You are coeliac or avoid gluten (it contains barley malt and oat flour)","You are pregnant or take medication","You have a diagnosed condition"],
  shelf="Store as printed on the pack. Herbaferm's notes do not give a shelf life for Fiber Elite yet. @@TAG_CONFIRM@@",
  also=[("drops","Herbaferm Drops","S$55 \u00b7 30 ml"),("prefer","Prefer HF400","S$45 \u00b7 14 capsules")]),
  pt="#e8a33a",
  trust=["Can be heated and cooked with", "Vegan and GMO-free, per the leaflet", "Contains gluten", "Fine powder, malty aroma"],
  glance=[("3.5 g", "a day, with a meal"), ("125 g", "pouch, 35 servings"), ("About a month", "from one pouch"), ("S$1.54", "a day")],
  steps=[("Measure 3.5 g", "A small spoonful of the fine powder."), ("Stir it in", "Porridge, yoghurt, a smoothie or a protein shake. It can be heated too."), ("On training days", "3.5 g two to three times a day, after exercise.")],
  stepnote='Need ideas? <a href="#a-fiber">Four easy ways to eat Fiber Elite</a>.',
  img='<img src="@@img:ai-porridge@@" alt="A spoonful of fine powder being stirred into porridge with berries (illustrative image)" loading="lazy"><span class="ill">Illustrative image</span>',
  inside_h="What is in the pouch",
  inside='<p>75% whole barley malt and 12.5% oat flour, with a characteristic malt aroma. Contains gluten. @@TAG_CONFIRM@@ The final composition is still to be confirmed with Herbaferm.</p><p style="margin-top:12px">A 31-day study in 20 elite water polo players looked at a vegan protein supplement with pre- and probiotics. Herbaferm\'s founders are among its authors and the abstract does not name Fiber Elite. <a class="more" href="#science">See the reference</a></p>',
  faq=[3, 8, 14, 5, 19, 20]),
 "prefer": dict(
  more=dict(suits=["People who prefer a capsule to drops","Anyone who already uses Herbaferm Drops","Anyone who wants to try the range for a week first"],
  check=["You are vegetarian or need halal (the shell is gelatine)","You are sensitive to histamine: use only under professional supervision","You have an immune system disorder, are pregnant or take medication"],
  shelf="Herbaferm's notes give about 1 year for the capsules. @@TAG_CONFIRM@@ The best-before date is printed on the pack.",
  also=[("drops","Herbaferm Drops","S$55 \u00b7 30 ml"),("fiber","Fiber Elite","S$55 \u00b7 125 g")]),
  pt="#c8a27c",
  trust=["Made to go with Drops", "A one-week trial pack", "Gelatine capsule", "Ask first if histamine-sensitive"],
  glance=[("2", "capsules a day"), ("14", "capsules, one week"), ("200 mg", "fermented herb fibres each"), ("S$3.21", "per capsule")],
  steps=[("Morning", "One capsule with your glass of water."), ("Evening", "One more capsule with your second glass."), ("Alongside Drops", "Prefer HF400 was developed to complement Herbaferm Drops.")],
  stepnote='A 14-capsule pack lasts 7 days, so it works well as a trial. @@TAG_CONFIRM@@ Another Herbaferm document describes a different dose.',
  img='<img src="@@img:prefer-bark@@" alt="Prefer HF400 bottle and carton on mossy bark, with a capsule in front" loading="lazy" style="object-position:30% 55%">',
  inside_h="What is in one 400 mg capsule",
  inside='<ul class="ilist"><li><b>200 mg</b> fermented herb fibres (chamomile, yarrow, rosehip, elderflower, propolis, oak bark, wormwood)</li><li><b>120 mg</b> fulvic acid</li><li><b>51 mg</b> humic acid</li><li><b>29 mg</b> vitamin C</li></ul><p style="margin-top:12px">Gelatine capsule shell, so not suitable for vegetarians. Halal status is not confirmed yet. @@TAG_CONFIRM@@</p>',
  faq=[4, 9, 5, 19, 20]),
}


def prod_sections(pid, faqs):
    d = PROD[pid]
    m = d["more"]
    trust = "".join('<li>%s</li>' % t for t in d["trust"])
    glance = "".join('<div><b>%s</b><span>%s</span></div>' % g for g in d["glance"])
    steps = "".join('<li><i>%d</i><div><h3>%s</h3><p>%s</p></div></li>' % (n + 1, s[0], s[1]) for n, s in enumerate(d["steps"]))
    faq = "".join(P.faq_item(*faqs[k]) for k in d["faq"])
    lis = lambda a: "".join("<li>%s</li>" % t for t in a)
    also = "".join('<div><span><b>%s</b><small>%s</small></span><a class="btn btn-line sm" href="#%s">View</a><button class="btn btn-honey sm" type="button" data-add="%s">Add</button></div>' % (n, p, i, i) for i, n, p in m["also"])
    deliv = ('<ul class="pdeliv"><li><b>Delivery in Singapore</b><span>Details to follow @@TAG_SUPPLY@@</span></li><li><b>Returns</b><span>Terms to follow @@TAG_SUPPLY@@</span></li>'
             '<li><b>Payment</b><span>Major cards and wallets @@TAG_CONFIRM@@</span></li><li><b>Reading</b><span><a href="learn/best-supplements-for-gut-health/">How to choose a gut health supplement</a></span></li><li><b>Questions?</b><span>Ask the Herbaferm assistant (bottom right) or see the <a href="#faq">FAQ</a></span></li></ul>'
             '<div class="pbundle"><small>Goes well with</small>%s</div>') % also
    nav = ('<nav class="psub" aria-label="On this page"><div class="wrap">%s</div></nav>' % "".join(
        '<a href="#%s" data-to="%s-%s">%s</a>' % (pid, pid, s, l) for s, l in (("top", "Overview"), ("how", "How to take it"), ("fit", "Is it for you?"), ("inside", "Inside"), ("det", "Details"), ("faq", "Questions"))))
    fit = ('<section class="pfit" id="%s-fit"><div class="wrap"><h2>Is it right for you?</h2><div class="fitgrid"><div class="fit yes"><h3>Suits you if&hellip;</h3><ul>%s</ul></div>'
           '<div class="fit chk"><h3>Check with a healthcare professional first if&hellip;</h3><ul>%s</ul></div></div></div></section>') % (pid, lis(m["suits"]), lis(m["check"]))
    extra = ('<div class="dcard"><h3>Storage and shelf life</h3><p>%s</p></div>'
             '<div class="dcard"><h3>Delivery, returns and payment</h3><p>Singapore delivery times and fees, returns terms and payment methods will be listed here. @@TAG_SUPPLY@@ Also listed on the ConnectingDNA marketplace in Singapore. @@TAG_CONFIRM@@</p></div>') % m["shelf"]
    return {
      "nav": nav, "fit": fit, "extra": extra, "deliv": deliv,
      "trust": '<ul class="ptrust">%s</ul>' % trust,
      "after": (
        '<section class="pglance"><div class="wrap"><div class="gtiles">%(glance)s</div></div></section>%(viz)s'
        '<section class="phow" id="%(p)s-how"><div class="wrap"><div class="pcols"><div><h2>How to take it</h2><ol class="psteps">%(steps)s</ol><p class="note" style="margin-top:18px">%(note)s</p></div>'
        '<div class="pimg">%(img)s</div></div></div></section>'
        '%(fit)s<section class="pinside" id="%(p)s-inside"><div class="wrap"><div class="pbox"><h2>%(ih)s</h2><div>%(inside)s</div></div></div></section>'
        '<section class="pdet" id="%(p)s-det"><div class="wrap"><h2>Details and safety</h2><div class="pgrid"><div class="tabs-wrap">') % dict(viz=VIZ[pid], glance=glance, steps=steps, note=d["stepnote"], img=d["img"], ih=d["inside_h"], inside=d["inside"], p=pid, fit=fit),
      "faq": '<section class="pfaq" id="%s-faq"><div class="wrap"><h2>Questions before you buy</h2><div class="faq" style="margin-top:22px">%s</div><p class="note" style="margin-top:16px">More answers on the <a href="#faq">FAQ page</a>, or ask the Herbaferm assistant.</p></div></section>' % (pid, faq),
      "pt": d["pt"],
    }


# ---------------------------------------------------------------- visuals (only numbers already stated on the product pages)
def bars(rows, unit, maxv=None, cls=""):
    maxv = maxv or max(r[1] for r in rows)
    out = ""
    for lab, v, txt in rows:
        out += ('<div class="brow"><span class="bl">%s</span><span class="bt"><i style="width:%.1f%%"></i></span><b>%s</b></div>' % (lab, 100.0 * v / maxv, txt))
    return '<div class="bars %s">%s</div>' % (cls, out)


VIZ_COST = ('<section class="pviz"><div class="wrap"><h2>What a day costs</h2><p class="lede">At list price and the regular amount. Prices are before any offers.</p>'
            + bars([("Fiber Elite, 3.5 g", 1.54, "S$1.54"), ("Herbaferm Drops, 16 drops", 1.83, "S$1.83"), ("Drops + Fiber Elite", 3.37, "S$3.37"),
                    ("Prefer HF400, 2 capsules", 6.43, "S$6.43"), ("All three", 9.80, "S$9.80")], "S$", 9.8)
            + '<p class="note" style="margin-top:14px">Drops: S$55 for about 30 days. Fiber Elite: S$55 for about 35 days. Prefer HF400: S$45 for 7 days at two capsules a day.</p></div></section>')

VIZ = {}
VIZ["drops"] = ('<section class="pviz"><div class="wrap"><div class="vgrid"><div><h2>How the first weeks build up</h2><p class="lede">The leaflet suggests starting small and settling at 8 drops twice a day. @@TAG_CONFIRM@@</p></div><div>'
    + bars([("Days 1 to 3", 10, "10 drops a day"), ("Weeks 1 to 3", 30, "up to 30 a day at most"), ("Regular amount", 16, "16 drops a day")], "", 30)
    + '<div class="bottle"><div class="bfill" style="--p:100%"></div><span><b>480 drops</b> in one 30 ml bottle, about one month</span></div></div></div></div></section>')
dots = "".join('<i class="%s"></i>' % ("on" if n < 35 else "half") for n in range(36))
VIZ["fiber"] = ('<section class="pviz"><div class="wrap"><div class="vgrid"><div><h2>One pouch, about 35 servings</h2><p class="lede">At 3.5 g a day, a 125 g pouch lasts about five weeks. Each dot is one day.</p>'
    '<div class="dots">%s</div></div><div><h3>Everyday and training days</h3>' % dots
    + bars([("Everyday", 3.5, "3.5 g"), ("Training day, 2 servings", 7, "7 g"), ("Training day, 3 servings", 10.5, "10.5 g")], "g", 10.5)
    + '<div class="vtiles"><div><b>31 days</b><span>study length</span></div><div><b>20</b><span>elite water polo players</span></div><div><b>2024</b><span>published</span></div></div>'
    '<p class="note">The study looked at a vegan protein supplement with pre- and probiotics. The abstract does not name Fiber Elite. <a href="#science">See the reference</a>.</p></div></div></div></section>')
parts = [("Fermented herb fibres", 200, "var(--pt)"), ("Fulvic acid", 120, "#6f8f4a"), ("Humic acid", 51, "#8a6d3b"), ("Vitamin C", 29, "#e8a33a")]
off, svg, leg = 25, "", ""
for n, v, c in parts:
    p = 100.0 * v / 400
    svg += '<circle r="15.9155" cx="21" cy="21" fill="none" stroke="%s" stroke-width="7" stroke-dasharray="%.2f %.2f" stroke-dashoffset="%.2f"></circle>' % (c, p, 100 - p, off)
    off -= p
    leg += '<li><i style="background:%s"></i><span>%s</span><b>%d mg</b></li>' % (c, n, v)
VIZ["prefer"] = ('<section class="pviz"><div class="wrap"><div class="vgrid"><div><h2>What is in one capsule</h2><p class="lede">Each 400 mg capsule, by weight.</p>'
    '<ul class="vleg">%s</ul></div><div class="donut"><svg viewBox="0 0 42 42" role="img" aria-label="Contents of one 400 mg Prefer HF400 capsule: 200 mg fermented herb fibres, 120 mg fulvic acid, 51 mg humic acid, 29 mg vitamin C">%s</svg><span><b>400 mg</b>per capsule</span></div></div></div></section>' % (leg, svg))
