# SEO / AIO content: keyword blog articles and the microbial dysbiosis page.
# Source: Brand and Social Media deck slides 24-32 (keyword list on slide 29, E-E-A-T on slide 30, structure on slide 31).
# Guardrails: food-supplement wording only, no disease or treatment claims, no unverified numbers about Herbaferm products,
# and every factual claim about the microbiome carries a numbered citation. {{r:key}} inserts a citation marker.

PUBLISHED = "2026-11-02"
AUTHOR = "Herbaferm editorial team"
RESEARCHGATE_BOOK = "https://www.researchgate.net/publication/404728994_The_Holistic_microbiome"
RESEARCHGATE_PROFILE = "https://www.researchgate.net/profile/Adam-Boday"

# key -> (citation text, url)
REFS = {
    "hill2014": ("Hill C, et al. The International Scientific Association for Probiotics and Prebiotics consensus statement on the scope and appropriate use of the term probiotic. <i>Nat Rev Gastroenterol Hepatol</i> 2014;11:506-514.", "https://doi.org/10.1038/nrgastro.2014.66"),
    "gibson2017": ("Gibson GR, et al. Expert consensus document: the ISAPP consensus statement on the definition and scope of prebiotics. <i>Nat Rev Gastroenterol Hepatol</i> 2017;14:491-502.", "https://doi.org/10.1038/nrgastro.2017.75"),
    "salminen2021": ("Salminen S, et al. The ISAPP consensus statement on the definition and scope of postbiotics. <i>Nat Rev Gastroenterol Hepatol</i> 2021;18:649-667.", "https://doi.org/10.1038/s41575-021-00440-6"),
    "marco2021": ("Marco ML, et al. The ISAPP consensus statement on the definition and scope of fermented foods. <i>Nat Rev Gastroenterol Hepatol</i> 2021;18:196-208.", "https://doi.org/10.1038/s41575-020-00390-5"),
    "wastyk2021": ("Wastyk HC, et al. Gut-microbiota-targeted diets modulate human immune status. <i>Cell</i> 2021;184:4137-4153.", "https://doi.org/10.1016/j.cell.2021.06.019"),
    "su2020": ("Su GL, et al. AGA clinical practice guidelines on the role of probiotics in the management of gastrointestinal disorders. <i>Gastroenterology</i> 2020;159:697-705.", "https://doi.org/10.1053/j.gastro.2020.05.059"),
    "lynch2016": ("Lynch SV, Pedersen O. The human intestinal microbiome in health and disease. <i>N Engl J Med</i> 2016;375:2369-2379.", "https://doi.org/10.1056/NEJMra1600266"),
    "sender2016": ("Sender R, Fuchs S, Milo R. Revised estimates for the number of human and bacteria cells in the body. <i>PLoS Biol</i> 2016;14:e1002533.", "https://doi.org/10.1371/journal.pbio.1002533"),
    "levy2017": ("Levy M, Kolodziejczyk AA, Thaiss CA, Elinav E. Dysbiosis and the immune system. <i>Nat Rev Immunol</i> 2017;17:219-232.", "https://doi.org/10.1038/nri.2017.7"),
    "hrncir2022": ("Hrncir T. Gut microbiota dysbiosis: triggers, consequences, diagnostic and therapeutic options. <i>Microorganisms</i> 2022;10:578.", "https://doi.org/10.3390/microorganisms10030578"),
    "dethlefsen2011": ("Dethlefsen L, Relman DA. Incomplete recovery and individualized responses of the human distal gut microbiota to repeated antibiotic perturbation. <i>Proc Natl Acad Sci USA</i> 2011;108(Suppl 1):4554-4561.", "https://doi.org/10.1073/pnas.1000087107"),
    "david2014": ("David LA, et al. Diet rapidly and reproducibly alters the human gut microbiome. <i>Nature</i> 2014;505:559-563.", "https://doi.org/10.1038/nature12820"),
    "bischoff2011": ("Bischoff SC. 'Gut health': a new objective in medicine? <i>BMC Med</i> 2011;9:24.", "https://doi.org/10.1186/1741-7015-9-24"),
    "reynolds2019": ("Reynolds A, et al. Carbohydrate quality and human health: a series of systematic reviews and meta-analyses. <i>Lancet</i> 2019;393:434-445.", "https://doi.org/10.1016/S0140-6736(18)31809-9"),
    "zmora2019": ("Zmora N, Suez J, Elinav E. You are what you eat: diet, health and the gut microbiota. <i>Nat Rev Gastroenterol Hepatol</i> 2019;16:35-56.", "https://doi.org/10.1038/s41575-018-0061-2"),
    "servetas2024": ("Servetas SL, Jackson S, Hoffmann D, Ravel J. Evaluating the analytical performance of direct-to-consumer gut microbiome testing services. bioRxiv preprint, 2024 (not peer reviewed at the time of writing).", "https://www.biorxiv.org/content/10.1101/2024.06.05.596628"),
    "amili_na": ("Lim GY. WATCH: AMILI on South East Asia's 'first' gut microbiome test with personalised nutrition recommendations. NutraIngredients, 9 March 2021.", "https://www.nutraingredients.com/Article/2021/03/09/WATCH-AMiLi-on-South-East-Asia-s-first-gut-microbiome-test-with-personalised-nutrition-recommendations/"),
    "amili_astar": ("A*STAR. Testing gut health with no humans required (AMILI case study).", "https://www.a-star.edu.sg/industries/stories/testing-gut-health-with-no-humans-required"),
    "hsa": ("Health Sciences Authority, Singapore. Health supplements.", "https://www.hsa.gov.sg/health-supplements"),
    "fritz2020": ("Fritz P, Bóday Á. The role and restoration of the symbiosis of microbiome and human body. <i>recreation</i> 2020;10(3):10-13.", "https://doi.org/10.21486/recreation.2020.10.3.1"),
    "mao_franke": ("Mao L, Franke J. Symbiosis, dysbiosis and rebiosis: the value of metaproteomics in human microbiome monitoring. <i>Proteomics</i> (doi 10.1002/pmic.201400329).", "https://doi.org/10.1002/pmic.201400329"),
    "boday_book": ("B\u00f3day AJ (ed.), B\u00f3day AJ, B\u00f3day \u00c1B. <i>The Holistic Microbiome: Nature is complex but never complicated.</i> Herbaferm Ltd., 2026 (textbook and methodological guide; chapter titles and opening chapter read from the publisher's sample).", RESEARCHGATE_BOOK),
    "boday_pres": ("Bóday A. The natural way to restore symbiosis in the digestion and microbiota (Herbaferm R&amp;D presentation, 2 February 2022). Company material, cites no sources.", "https://herbaferm.hu/img/cms/doc/AdamBoday-Presentation_2022_02_02.pdf"),
}

DISCLAIM = ("This article is general information, not medical advice. Herbaferm products are food supplements and are not intended to "
            "diagnose, treat, cure or prevent any disease. Speak to a doctor or pharmacist if you have a medical condition, are pregnant or take medication.")

# slug, keyword, h1, meta description, dek, in-short bullets, body, faq [(q, a)], tag, cover
ARTICLES = [
    dict(slug="microbiome-test-singapore", kw="microbiome test singapore", cat="Microbiome",
         title="Microbiome test in Singapore: what it measures and what it cannot tell you",
         desc="What a gut microbiome test in Singapore involves, what the report shows, and where the science is still limited. Plain-language guide with sources.",
         dek="A stool-based gut microbiome test counts which microbes are present. It does not diagnose anything. Here is how to read one.",
         short=["A microbiome test reads microbial DNA from a small stool sample and reports which bacteria are present and in what proportions.{{r:amili_na}}",
                "It is not a medical diagnosis. Independent testing found large differences between commercial services given the same sample.{{r:servetas2024}}",
                "Use a report as a conversation starter with a dietitian or doctor, not as a reason to start or stop a treatment."],
         body='''<h2>What is a microbiome test?</h2>
<p>A gut microbiome test looks at the community of microbes in your digestive tract. You collect a small stool sample at home and post it to a laboratory. The lab extracts bacterial DNA, sequences it and compares the result with reference databases.{{r:amili_na}} The report typically lists the types of bacteria found, their relative amounts and a diversity score.</p>
<h2>Who offers a microbiome test in Singapore?</h2>
<p>Singapore has a home-grown option. AMILI, a Singapore start-up founded in 2019, built an Asian gut microbiome database from stool samples of healthy local residents and launched what it described in 2021 as South East Asia's first gut microbiome test with personalised nutrition recommendations.{{r:amili_na}}{{r:amili_astar}} AMILI's own website (amili.asia) describes its current services. Overseas kits can also be posted to Singapore. Herbaferm does not sell or endorse any test, and this page is not a review of one.</p>
<h2>What does a microbiome report actually show?</h2>
<table class="atable"><thead><tr><th>Part of the report</th><th>What it tells you</th><th>What it does not tell you</th></tr></thead><tbody>
<tr><td>Bacterial types and proportions</td><td>Which groups were detected in that one sample</td><td>Whether your mix is "good" or "bad": researchers are still working out what a healthy mix looks like{{r:lynch2016}}</td></tr>
<tr><td>Diversity score</td><td>How varied the detected community is</td><td>A single number cannot show whether a symptom has a microbial cause</td></tr>
<tr><td>Food suggestions</td><td>General, diet-based ideas such as eating more plant fibre</td><td>That a particular food will change your results; diet does shift the microbiome, but individual responses vary{{r:david2014}}</td></tr>
</tbody></table>
<h2>How reliable is a consumer microbiome test?</h2>
<p>This is the main caution. In a 2024 preprint, researchers sent the same standardised human stool material to seven commercial direct-to-consumer services. The results differed widely within and between companies, by roughly as much as the biological differences between donors, and the authors called for quality standards and regulatory oversight.{{r:servetas2024}} A preprint has not completed peer review, but it is a useful reminder that two tests on the same sample can read differently.</p>
<p>Herbaferm founder Adam B\u00f3day's textbook <i>The Holistic Microbiome</i> includes a supplementary chapter on interpreting stool microbiome reports. Its section titles flag the same issues: relative abundance versus absolute quantity (the "snapshot fallacy"), correlation versus causation, reproducibility, and the need for standardisation.{{r:boday_book}}</p>
<h2>When is a microbiome test worth considering?</h2>
<p>If you are curious, a test can be a starting point for a discussion about food and routine. If you have persistent digestive symptoms, blood in the stool, unexplained weight loss or pain, see a doctor first: a stool microbiome report is not the right tool to investigate these.</p>
<h2>Does a microbiome test relate to Herbaferm products?</h2>
<p>No test result is needed to use a food supplement. Herbaferm Drops, Fiber Elite and Prefer HF400 are sold as food supplements that sit alongside a varied diet, and our leaflets state that no health effects can be attributed to them. Singapore does not pre-approve health supplements, so no supplement can be called "HSA approved".{{r:hsa}}</p>''',
         faq=[("Does a microbiome test diagnose a condition?", "No. It describes which microbes were detected in a stool sample. It cannot diagnose a disease, and independent testing shows that results can vary between commercial services."),
              ("How is a gut microbiome test done?", "You collect a small stool sample at home, post it to a laboratory, and the lab sequences the microbial DNA and compiles a report."),
              ("Is there a microbiome test made in Singapore?", "Yes. AMILI, a Singapore company, launched a stool-based test in 2021. Herbaferm is not affiliated with AMILI and does not endorse any test.")],
         refs=["amili_na", "amili_astar", "servetas2024", "lynch2016", "david2014", "hsa", "boday_book"]),

    dict(slug="best-supplements-for-gut-health", kw="best supplements for gut health", cat="Supplements",
         title="Best supplements for gut health: how to choose, and what the evidence says",
         desc="How to choose a gut health supplement in Singapore: the types, what the research supports, a checklist to compare brands, and when to see a professional.",
         dek="There is no single best supplement. There are better questions to ask. This guide gives you a checklist.",
         short=["'Gut health supplement' covers very different things: probiotics, prebiotics, postbiotics, fibre and fermented products.{{r:hill2014}}{{r:gibson2017}}{{r:salminen2021}}",
                "Evidence is specific to the strain or ingredient and the condition studied. A product that helps one group may do nothing for another.{{r:su2020}}",
                "Compare brands on clarity of ingredients, evidence for that exact product, testing and honest claims, not on star ratings or superlatives."],
         body='''<h2>What counts as a gut health supplement?</h2>
<p>The label covers several different categories. Scientists have agreed definitions for most of them:</p>
<table class="atable"><thead><tr><th>Type</th><th>Plain meaning</th></tr></thead><tbody>
<tr><td>Probiotic</td><td>Live microorganisms that, given in adequate amounts, may give a health benefit to the person taking them{{r:hill2014}}</td></tr>
<tr><td>Prebiotic</td><td>A substrate that microorganisms already in the host use selectively, giving a health benefit{{r:gibson2017}}</td></tr>
<tr><td>Postbiotic</td><td>A preparation of inanimate (not living) microorganisms and/or their components{{r:salminen2021}}</td></tr>
<tr><td>Dietary fibre</td><td>Plant carbohydrates that are not digested in the small intestine; higher intakes are associated with better health outcomes in large reviews{{r:reynolds2019}}</td></tr>
</tbody></table>
<h2>Which supplements for gut health have the best evidence?</h2>
<p>It depends on who you are and what the question is. The American Gastroenterological Association reviewed probiotics for a range of digestive conditions in 2020 and recommended them for only a few specific situations, while advising against routine use for others. The evidence was often of low quality and specific to particular strains.{{r:su2020}} In other words, "probiotic" is not one treatment. The same caution applies to every other category on the label.</p>
<h2>How do I compare gut health supplements?</h2>
<ol><li><b>Is the type clear?</b> A label should say whether it contains live organisms, fibre, fermented extracts or something else.</li>
<li><b>Is there evidence for this exact product?</b> Look for studies on the same ingredient or strain at a similar dose, not just on the category.</li>
<li><b>Is it tested?</b> Ask for a certificate of analysis or batch testing.</li>
<li><b>Are the claims modest and accurate?</b> In Singapore, health supplements are not pre-approved by the Health Sciences Authority, so "HSA approved" should be a red flag.{{r:hsa}} Be wary of words like "cure", "detox" or "treats".</li>
<li><b>Does it fit your routine?</b> Storage, taste, cost per day and whether you will actually take it for weeks.</li></ol>
<h2>Do food and routine matter more than supplements?</h2>
<p>Long-term diet shapes the gut microbiome, and a short change in diet can shift it within days.{{r:david2014}}{{r:zmora2019}} Plant variety, whole grains, legumes, vegetables and fermented foods are the usual starting points. A supplement is an add-on, not a replacement. See our guides on <a href="../how-to-improve-gut-health/">how to improve gut health</a> and <a href="../fermented-foods-gut-health/">fermented foods</a>.</p>
<h2>Where do Herbaferm products fit?</h2>
<p>Herbaferm Drops are a fermented herbal extract, Fiber Elite is a fibre-rich food additive and Prefer HF400 is a capsule of fermented herb fibres. We do not call Drops a probiotic and do not publish a live-organism count, because we do not have a verified figure. Our leaflets state that no health effects can be attributed to the products. The <a href="../../#shop">Shop page</a> lists what is in each.</p>''',
         faq=[("What is the best supplement for gut health?", "There is no single best supplement. Evidence depends on the specific ingredient or strain and on the person. Compare products on clear labelling, evidence for that exact product, testing and honest claims."),
              ("Are gut health supplements approved by the HSA in Singapore?", "No. Singapore does not pre-approve health supplements, so no supplement can be described as HSA approved."),
              ("Should I take a supplement or change my diet first?", "Diet is the usual starting point: plant variety, fibre and fermented foods. A supplement is an add-on, and anyone with persistent symptoms should see a doctor.")],
         refs=["hill2014", "gibson2017", "salminen2021", "reynolds2019", "su2020", "david2014", "zmora2019", "hsa"]),

    dict(slug="natural-supplements-for-gut-health", kw="natural supplements for gut health", cat="Supplements",
         title="Natural supplements for gut health: fibre, fermented and herbal options explained",
         desc="What 'natural' means on a gut health supplement label, and how fibre, fermented and herbal products differ. Plain-language guide with sources.",
         dek="'Natural' is a marketing word, not a safety guarantee. Here is what the main natural options are and how to read the label.",
         short=["'Natural' has no fixed legal meaning on a supplement label. Natural does not mean safe or proven.",
                "The common natural options are fibre, fermented foods or extracts, and herbs used traditionally. Each has a different kind of evidence.{{r:gibson2017}}{{r:marco2021}}",
                "Herbs can interact with medicines. Check with a doctor or pharmacist before starting."],
         body='''<h2>What does "natural" mean for a gut health supplement?</h2>
<p>There is no single definition. A product can call itself natural if it uses plant or fermented ingredients, yet still vary a great deal in quality, dose and evidence. Judge a product by its ingredient list and the evidence for it, not by the word on the front.</p>
<h2>Which natural options are there?</h2>
<h3>Fibre</h3>
<p>Fibre is food for the microbes already in your gut, and some fibres meet the scientific definition of a prebiotic.{{r:gibson2017}} Higher intakes of fibre from whole foods are linked with better health outcomes in large reviews of observational studies and trials.{{r:reynolds2019}} Food comes first; a fibre supplement can top it up. Increase slowly, with water.</p>
<h3>Fermented foods and extracts</h3>
<p>The international consensus definition of fermented foods is foods made through desired microbial growth and conversion of food components.{{r:marco2021}} That covers yoghurt, kimchi, tempeh and many more. A fermented herbal extract such as Herbaferm Drops is made by fermenting herbs, but it is a supplement, not a fermented food in the everyday sense.</p>
<h3>Herbs</h3>
<p>Chamomile, yarrow, elderflower, rosehip, propolis, oak bark and white wormwood each have a long history of traditional use in Europe. Traditional use is not the same as clinical evidence, and herbs can interact with medicines or be unsuitable in pregnancy. Our <a href="../../#ingredients">Ingredients page</a> describes each herb as traditionally used, without health claims.</p>
<h2>How do I use natural supplements safely?</h2>
<ul><li>Start with one product at a time so you can tell what is working or causing a reaction.</li><li>Read storage instructions. Products without preservatives, including Herbaferm Drops, are kept in the fridge.</li><li>Stop and speak to a professional if you have unusual or severe digestive symptoms.</li><li>Tell your doctor or pharmacist about any supplement if you take medication.</li></ul>
<h2>Are Herbaferm products natural supplements?</h2>
<p>They are plant-based food supplements made with natural fermentation, with no preservatives or artificial colours. We do not claim they treat or prevent any condition, and our leaflets state that no health effects can be attributed to them. See <a href="../best-supplements-for-gut-health/">how to choose a gut health supplement</a> for a comparison checklist.</p>''',
         faq=[("Are natural supplements for gut health safer than other supplements?", "Not automatically. Natural products can still cause side effects or interact with medicines. Check with a doctor or pharmacist."),
              ("Is fibre a natural gut health supplement?", "Fibre feeds the microbes already in the gut and some fibres meet the definition of a prebiotic. Whole foods are the first source, and a supplement can add to them.")],
         refs=["gibson2017", "marco2021", "reynolds2019"]),

    dict(slug="gut-health-supplement-reviews", kw="gut health supplement reviews", cat="Supplements",
         title="Gut health supplement reviews: how to read them and what to check first",
         desc="How to judge gut health supplement reviews and ratings in Singapore: what a review can and cannot tell you, red flags, and a short checklist.",
         dek="Star ratings are a poor guide to whether a supplement does anything. Here is how to read reviews critically.",
         short=["A positive review shows that someone liked a product, not that it worked, because gut symptoms change on their own and many things change at once.",
                "Look for evidence on the exact product, independent testing and plain claims instead of ratings.{{r:su2020}}",
                "Herbaferm does not yet have customer reviews to show, and we do not publish or rank competing products."],
         body='''<h2>Can you trust gut health supplement reviews?</h2>
<p>Reviews are useful for practical things: taste, how easy a product is to take, delivery and customer service. They are weak evidence for whether a supplement works. Digestive symptoms rise and fall naturally, people often change several things at once, and expectation alone affects how we feel. That is why researchers use controlled trials rather than testimonials.{{r:su2020}}</p>
<h2>What should you look for in a review?</h2>
<table class="atable"><thead><tr><th>Check</th><th>Good sign</th><th>Red flag</th></tr></thead><tbody>
<tr><td>Who wrote it?</td><td>Named reviewer who disclosed any free product or payment</td><td>Anonymous, repetitive or all five-star</td></tr>
<tr><td>What does it claim?</td><td>Practical experience ("easy to take", "tasted fine")</td><td>Cure or disease claims</td></tr>
<tr><td>Does it cite evidence?</td><td>Links to the studies and says what they covered</td><td>"Clinically proven" with no source</td></tr>
<tr><td>Is it independent?</td><td>Lab or consumer-group testing</td><td>Review site that earns commission on every sale</td></tr>
</tbody></table>
<h2>Which evidence beats a review?</h2>
<p>Guidelines written by expert panels that reviewed the trials carry more weight than ratings. For probiotics, the AGA's 2020 guideline is one example: it recommended them only for specific uses and found much of the evidence to be low quality.{{r:su2020}} Even then, results depend on the exact strain.</p>
<h2>Does Herbaferm have reviews?</h2>
<p>Herbaferm Singapore is at an early stage and has no verified customer reviews to publish yet, and we do not publish invented ones. When real reviews exist they will appear on the product pages with the reviewer's consent and without health claims. We also do not rate other brands. To compare options yourself, use the checklist in <a href="../best-supplements-for-gut-health/">best supplements for gut health</a>.</p>''',
         faq=[("Are online gut health supplement reviews reliable?", "They are useful for practical details like taste and delivery but weak evidence of effect. Gut symptoms vary naturally and expectation influences how people feel."),
              ("Does Herbaferm have customer reviews?", "Not yet. Herbaferm does not publish invented reviews. Verified reviews will be added to product pages once they exist.")],
         refs=["su2020"]),

    dict(slug="best-probiotics-for-gut-health", kw="best probiotics for gut health", cat="Supplements",
         title="Best probiotics for gut health: what to look for before you buy",
         desc="How to choose a probiotic for gut health: what the word means, why strain matters, what the guidelines say, and how it differs from prebiotics and postbiotics.",
         dek="The best probiotic depends on the strain and the reason for taking it. A short guide to the questions that matter.",
         short=["A probiotic is a live microorganism given in an adequate amount that benefits the person taking it.{{r:hill2014}}",
                "Benefits are strain-specific and condition-specific; the AGA found evidence for only some uses.{{r:su2020}}",
                "Herbaferm does not market its products as probiotics."],
         body='''<h2>What is a probiotic?</h2>
<p>The scientific definition is live microorganisms that, when administered in adequate amounts, confer a health benefit on the host.{{r:hill2014}} Yoghurt with live cultures is not automatically a probiotic by this definition unless the organisms and amount are shown to benefit people.</p>
<h2>Why does the strain matter?</h2>
<p>Two bacteria with the same species name can behave differently. Evidence is tied to a named strain at a studied dose for a studied purpose. So "contains <i>Lactobacillus</i>" is not enough: look for the full strain name (for example, species plus a strain code) and whether it was tested for what you want it for.{{r:hill2014}}</p>
<h2>What do the guidelines say?</h2>
<p>In 2020, the American Gastroenterological Association assessed probiotics across several digestive conditions. It recommended them in a small number of specific situations, suggested not using them routinely in others, and described the evidence in many areas as low quality.{{r:su2020}} If you have a medical condition, ask your doctor which, if any, applies to you.</p>
<h2>How is a probiotic different from a prebiotic or postbiotic?</h2>
<table class="atable"><thead><tr><th>Word</th><th>What it is</th></tr></thead><tbody>
<tr><td>Probiotic</td><td>Live microbes{{r:hill2014}}</td></tr>
<tr><td>Prebiotic</td><td>Food for microbes already in your gut{{r:gibson2017}}</td></tr>
<tr><td>Postbiotic</td><td>Non-living microbes and their components{{r:salminen2021}}</td></tr>
</tbody></table>
<h2>Is Herbaferm a probiotic?</h2>
<p>No. Herbaferm leaflets describe the products with the words "rebiotic" and "prebiotic", and which regulatory category fits in Singapore is still being confirmed. Until it is, we do not call any Herbaferm product a probiotic and we do not publish a live-organism count. The <a href="../../#a-labels">probiotic, prebiotic, postbiotic guide</a> explains the terms further.</p>''',
         faq=[("What is the best probiotic for gut health?", "It depends on the strain, the dose and the purpose. Evidence is strain-specific, and guidelines support probiotics only for certain uses."),
              ("Is Herbaferm Drops a probiotic?", "Herbaferm does not market its products as probiotics. Its leaflets use the terms rebiotic and prebiotic, and the Singapore category is being confirmed.")],
         refs=["hill2014", "gibson2017", "salminen2021", "su2020"]),

    dict(slug="best-supplements-for-gut-health-and-weight-loss", kw="best supplements for gut health and weight loss", cat="Supplements",
         title="Best supplements for gut health and weight loss: what is known, and what is not",
         desc="Do gut health supplements help with weight loss? What the research on the microbiome and body weight does and does not show, and safer first steps.",
         dek="The microbiome and body weight are linked in research. That does not mean a supplement will change your weight.",
         short=["Studies link the gut microbiome with body weight, but links are not proof that a supplement causes weight loss.{{r:lynch2016}}",
                "Herbaferm does not claim any product helps with weight loss.",
                "Fibre-rich whole foods have the most consistent evidence behind them.{{r:reynolds2019}}"],
         body='''<h2>Is there a link between the gut microbiome and weight?</h2>
<p>Researchers have found differences in gut microbial communities between people with and without obesity, and animal experiments show the microbiome can influence energy balance. Human findings are more mixed, and association does not show cause.{{r:lynch2016}}</p>
<h2>Do supplements for gut health help with weight loss?</h2>
<p>Showing that a particular product changes weight in people requires well-designed trials of that product. Marketing that pairs "gut health" with "weight loss" usually goes further than the research supports. Herbaferm does not make any weight-loss claim for its products, and under Singapore's rules, supplement claims must stay within what can be substantiated.{{r:hsa}}</p>
<h2>What has the most consistent evidence?</h2>
<p>Food. A series of reviews for the World Health Organization found that higher intake of dietary fibre and whole grains was associated with lower body weight and better health outcomes.{{r:reynolds2019}} Diet also shifts the gut microbiome within days.{{r:david2014}} Practical steps: more vegetables, legumes and whole grains, fewer ultra-processed foods, regular activity and sleep. If weight is a health concern, see a doctor or dietitian.</p>
<h2>Where could Fiber Elite fit?</h2>
<p>Fiber Elite is a fibre-rich food additive that can be stirred into porridge, smoothies or yoghurt. It adds fibre to a meal; it is not a weight-loss product, and it contains gluten. See <a href="../how-to-improve-gut-health/">how to improve gut health</a> for a food-first plan.</p>''',
         faq=[("Can gut health supplements help me lose weight?", "There is no reliable evidence that a gut health supplement on its own leads to weight loss. Herbaferm makes no weight-loss claims."),
              ("What helps gut health and weight at the same time?", "Fibre-rich whole foods, regular activity and sleep are the best-supported places to start. See a doctor or dietitian for personal advice.")],
         refs=["lynch2016", "reynolds2019", "david2014", "hsa"]),

    dict(slug="what-is-gut-health", kw="what is gut health", cat="Basics",
         title="What is gut health? A plain-language explanation",
         desc="What gut health means, what the gut microbiome is, what scientists still do not know, and when to see a doctor. Clear answers with sources.",
         dek="Gut health is a popular phrase with a loose definition. Here is what it usually means and what is still being researched.",
         short=["Gut health generally refers to the normal working of the digestive tract, including digestion, absorption, the gut barrier and the microbial community that lives there.{{r:bischoff2011}}",
                "The community is made of trillions of microbes. The best estimate is that human and bacterial cells in the body are about equal in number.{{r:sender2016}}",
                "There is no agreed test or score for gut health, and what a healthy mix looks like is still under study.{{r:lynch2016}}"],
         body='''<h2>What does gut health mean?</h2>
<p>There is no single definition. A commonly cited one describes gut health as the absence of gastrointestinal complaints together with normal digestion and absorption, an effective barrier, a balanced microbiome and a well-functioning immune system in the gut.{{r:bischoff2011}} The word is also used loosely in marketing, which is why it is worth asking what a source means by it.</p>
<h2>What is the gut microbiome?</h2>
<p>It is the community of microorganisms, mostly bacteria, that live in the digestive tract. A widely quoted older ratio of ten bacterial cells to every human cell was revised in 2016 to roughly one to one.{{r:sender2016}} Everyone carries their own mix, and it changes with age, diet, medicines and where we live.{{r:lynch2016}}</p>
<h2>Why do people talk about gut health so much?</h2>
<p>Research links the microbiome with digestion, the immune system and metabolism, and interest has grown quickly.{{r:lynch2016}} Many of these findings are associations, and scientists are still working out which are causes. That is a reason for interest and for caution.</p>
<h2>What are signs I should see a doctor?</h2>
<p>Blood in the stool, black stool, persistent diarrhoea or constipation, unexplained weight loss, severe or ongoing pain, or trouble swallowing need medical assessment. Supplements are not a substitute.</p>
<h2>What can I do for everyday gut health?</h2>
<p>Start with food and routine: a variety of plant foods, fibre, fermented foods you enjoy, enough water, sleep and activity. Our guide on <a href="../how-to-improve-gut-health/">how to improve gut health</a> goes into detail, and <a href="../microbial-dysbiosis/">microbial dysbiosis</a> explains what researchers mean by an imbalanced microbiome.</p>''',
         faq=[("What is gut health in simple terms?", "It generally means that the digestive tract works normally, including digestion, absorption, the gut barrier and the community of microbes living there."),
              ("How many bacteria are in the gut?", "Estimates are in the tens of trillions. A 2016 analysis found that bacterial and human cells in the body are roughly equal in number.")],
         refs=["bischoff2011", "sender2016", "lynch2016"]),

    dict(slug="how-to-improve-gut-health", kw="how to improve gut health", cat="Basics",
         title="How to improve gut health: six evidence-informed habits",
         desc="Six everyday habits that research links to a healthier gut microbiome: plant variety, fibre, fermented foods, sleep and more. With sources.",
         dek="No quick fix, but plenty of simple habits that research supports. Start with food.",
         short=["Diet is the strongest everyday lever on the gut microbiome that researchers have identified.{{r:david2014}}{{r:zmora2019}}",
                "A diet high in fermented foods increased microbiome diversity in a 10-week trial, while a high-fibre diet had more mixed effects.{{r:wastyk2021}}",
                "Persistent symptoms need a doctor, not a supplement."],
         body='''<h2>1. Eat a wide range of plant foods</h2>
<p>Vegetables, fruit, legumes, whole grains, nuts and seeds feed different microbes. Dietary fibre intake is consistently linked with better health outcomes in large reviews.{{r:reynolds2019}} Add new foods gradually and drink water as you raise fibre.</p>
<h2>2. Include fermented foods you enjoy</h2>
<p>In a 10-week Stanford trial, healthy adults who ate more fermented foods such as yoghurt, kefir, kimchi and kombucha showed greater microbiome diversity and lower markers of inflammation than a comparison group.{{r:wastyk2021}} It was a small study and not a treatment trial, but it supports the food-first advice. More in <a href="../fermented-foods-gut-health/">fermented foods and gut health</a>.</p>
<h2>3. Notice how fast diet can change things</h2>
<p>In a controlled study, switching to a diet of either mostly animal or mostly plant foods altered gut microbial communities within days.{{r:david2014}} Small, steady changes are enough to try; extreme diets are not needed.</p>
<h2>4. Be thoughtful about antibiotics</h2>
<p>Antibiotics can disrupt the gut microbial community, and in a study of repeated courses the community did not fully return to its starting state.{{r:dethlefsen2011}} Take antibiotics only when prescribed and as directed, and ask your doctor about any questions on diet afterwards.</p>
<h2>5. Sleep, stress and activity</h2>
<p>These are part of general health advice and are discussed in reviews of diet and lifestyle on the microbiome.{{r:zmora2019}} They are worth keeping in mind even though the exact effects on the microbiome are still being studied.</p>
<h2>6. Consider supplements last</h2>
<p>Supplements can be an add-on once food and routine are in place. Use our <a href="../best-supplements-for-gut-health/">checklist for choosing one</a>. Herbaferm Drops, Fiber Elite and Prefer HF400 are food supplements that sit beside a varied diet. Our leaflets state that no health effects can be attributed to them.</p>''',
         faq=[("What is the fastest way to improve gut health?", "There is no instant fix. Research shows diet can shift the gut microbiome within days, and the usual advice is a wide variety of plant foods, fibre and fermented foods."),
              ("Do fermented foods improve gut health?", "In one 10-week trial, a high fermented-food diet increased microbiome diversity in healthy adults. It was a small study, and results in other groups may differ.")],
         refs=["david2014", "zmora2019", "wastyk2021", "reynolds2019", "dethlefsen2011"]),

    dict(slug="fermented-foods-gut-health", kw="fermented foods", cat="Basics",
         title="Fermented foods and gut health: what counts, and what the research shows",
         desc="What counts as a fermented food, how it differs from probiotics, examples common in Singapore, and what trials show about gut health.",
         dek="Fermented foods are not all probiotics, and not all fermented products are the same. Here is the difference.",
         short=["Fermented foods are made through desired microbial growth and conversion of food components.{{r:marco2021}}",
                "Only some fermented foods contain live microbes at the time of eating, and a fermented food is not automatically a probiotic.{{r:marco2021}}{{r:hill2014}}",
                "One 10-week trial found a high fermented-food diet increased microbiome diversity in healthy adults.{{r:wastyk2021}}"],
         body='''<h2>What are fermented foods?</h2>
<p>The ISAPP consensus definition is "foods made through desired microbial growth and enzymatic conversions of food components".{{r:marco2021}} Yoghurt, kefir, kimchi, sauerkraut, tempeh, miso, natto and sourdough bread are all examples.</p>
<h2>Are fermented foods the same as probiotics?</h2>
<p>No. Some fermented foods contain live microbes when you eat them, and some are heated, filtered or baked after fermenting so the microbes are gone. A probiotic must have a shown benefit for the person taking it.{{r:hill2014}} The consensus statement says that a fermented food is not a probiotic unless it meets that bar.{{r:marco2021}}</p>
<h2>Which fermented foods are easy to find in Singapore?</h2>
<p>Yoghurt and kefir, kimchi, tempeh, miso, natto and fermented bean pastes are widely available in supermarkets and Asian groceries. Check labels for live cultures if that matters to you, and for salt and sugar content.</p>
<h2>What does the research say?</h2>
<p>In a 2021 Stanford trial of healthy adults over ten weeks, a diet high in fermented foods increased microbiome diversity and lowered several markers of inflammation, while the high-fibre group responded more differently from person to person.{{r:wastyk2021}} The study was small and does not show effects on disease, and results may differ in other groups.</p>
<h2>Is a fermented herbal extract the same thing?</h2>
<p>Herbaferm Drops are made by fermenting seven herbs with a natural community of microorganisms, then bottled as a food supplement. They are a different product from yoghurt or kimchi, and we do not claim any health effect for them. For more on the process, read <a href="../../#a-ferment">So what is fermentation, really?</a></p>''',
         faq=[("What counts as a fermented food?", "Foods made through desired microbial growth and conversion of food components, such as yoghurt, kefir, kimchi, tempeh, miso and sourdough."),
              ("Are fermented foods probiotics?", "Not automatically. Some contain live microbes and some do not, and a probiotic needs a shown benefit for the person taking it.")],
         refs=["marco2021", "hill2014", "wastyk2021"]),
]

# ------------------------------------------------------------------ dysbiosis page
DYS = dict(
    slug="microbial-dysbiosis", kw="microbial dysbiosis", cat="Microbiome",
    title="Microbial dysbiosis and rebiosis: what they mean and how the gut community recovers",
    desc="What microbial dysbiosis is, what researchers know about its causes and links to health, and what the term rebiosis means in the work of Herbaferm founder Adam Boday.",
    dek="An explainer based on the Herbaferm founder's book The Holistic Microbiome, set beside what independent research says.",
    short=["Dysbiosis means an imbalance in the microbial community of the body, usually the gut. It is a description, not a diagnosis.{{r:hrncir2022}}",
           "Researchers link dysbiosis with many conditions, but whether it is a cause or a result is still debated in most cases.{{r:levy2017}}",
           "Rebiosis is a term used by Herbaferm's founder for the restoration of a healthy host-microbe relationship; it is not a medical treatment and is not an established clinical term.{{r:fritz2020}}"],
    body='''<h2>What is microbial dysbiosis?</h2>
<p>Dysbiosis is an imbalance of the microbial community of the body, most often the gut. The changes can involve fewer types of microbes, a shift in which groups dominate, or a change in what the community does.{{r:hrncir2022}} The word describes a pattern, and researchers use it in different ways, so on its own it is not a diagnosis.{{r:lynch2016}}</p>
<h2>What causes dysbiosis?</h2>
<p>Reviews list several triggers: antibiotics and other medicines, infections, changes in diet, and ageing.{{r:hrncir2022}} In a study of repeated antibiotic courses, the gut community did not fully return to its starting state in the weeks that followed.{{r:dethlefsen2011}} Diet can also shift the community within days.{{r:david2014}} The founder's book and Herbaferm's materials add a wider argument that modern life, industrial food, treated water and chemical exposure are contributing factors. That argument is Herbaferm's perspective, and the sources cited here do not establish it.{{r:boday_pres}}</p>
<h2>How is dysbiosis linked to health?</h2>
<p>Studies have found altered gut microbial communities in people with a wide range of conditions, including inflammatory bowel disease, obesity and type 2 diabetes. In most cases it remains unclear whether the change helps cause the condition, results from it, or both.{{r:levy2017}}{{r:lynch2016}} Herbaferm does not claim that any product treats, prevents or reverses any of these conditions.</p>
<h2>What is rebiosis?</h2>
<p>Rebiosis is a term used by Herbaferm's founder, Adam Bóday, for an eco-physiological process of regeneration, rebalance or re-establishment of the symbiosis between the human host and its microbes after a disturbed state.{{r:boday_pres}}{{r:fritz2020}} It is not a standard clinical term. The word has also appeared in the research literature, for example in a review of metaproteomics for monitoring the human microbiome.{{r:mao_franke}} We use it here to describe the idea of recovery, not to promise an outcome.</p>
<h2>What does <i>The Holistic Microbiome</i> say about dysbiosis and rebiosis?</h2>
<p>The book is a 2026 textbook and methodological guide by Adam B\u00f3day and \u00c1bel B\u00f3day. Its sixth chapter is titled "Eubiosis, dysbiosis, rebiosis: dynamic equilibrium and regeneration", with sections on a functioning ecology, patterns of dysbiosis and "natural regeneration and clear-cutting-free stewardship".{{r:boday_book}} We read that last title as a forestry-style image: support the ecosystem so it can regrow, rather than wipe it out and start again. We have only seen the book's opening chapter and contents list, so this page summarises its framing, not the chapter's detail.</p>
<p>The author's note says the book is "a synthesis of currently available literature on the microbiome and a decade of dedicated research", not "a collection of absolute truths or dogmatic assertions", and that it is not a substitute for medical advice.{{r:boday_book}} We have tried to keep to that spirit.</p>
<h2>What does the founder say supports recovery?</h2>
<p>In his writing and talks, Bóday argues that a recovering community needs diverse natural microbial input, unprocessed plant foods, activity and rest, and that the aim is to supply the natural diversity that is missing from modern diets and water rather than to find a single "best" microbe.{{r:boday_pres}}{{r:boday_book}} This overlaps with general dietary advice: a variety of plant foods, fibre and fermented foods.{{r:zmora2019}}{{r:marco2021}} Where these ideas go beyond published evidence, we say so.</p>
<h2>Where do Herbaferm products fit?</h2>
<p>Herbaferm Drops are a fermented herbal extract that the company describes as rebiotic, and Fiber Elite is a fibre-rich food additive. They are food supplements. Our leaflets state that no health effects can be attributed to them, and we make no claim that they correct dysbiosis. See also <a href="../what-is-gut-health/">what is gut health</a>, <a href="../how-to-improve-gut-health/">how to improve gut health</a> and <a href="../microbiome-test-singapore/">microbiome tests</a>.</p>''',
    faq=[("What is microbial dysbiosis?", "An imbalance in the microbial community of the body, usually the gut. It is a description of a pattern, not a diagnosis."),
         ("What is rebiosis?", "A term used by Herbaferm's founder, Adam Bóday, for the restoration of a healthy symbiosis between the host and its microbes. It is not a standard clinical term and is not a treatment."),
         ("Can dysbiosis be tested?", "Microbiome tests can describe which microbes are present, but there is no agreed clinical test for dysbiosis, and consumer tests can vary between providers.")],
    refs=["hrncir2022", "levy2017", "lynch2016", "dethlefsen2011", "david2014", "fritz2020", "mao_franke", "boday_pres", "boday_book", "zmora2019", "marco2021"],
)

TTL = {
    "microbiome-test-singapore": "Microbiome test in Singapore: what it can and cannot tell you",
    "best-supplements-for-gut-health": "Best supplements for gut health: how to choose",
    "natural-supplements-for-gut-health": "Natural supplements for gut health explained",
    "gut-health-supplement-reviews": "Gut health supplement reviews: how to read them",
    "best-probiotics-for-gut-health": "Best probiotics for gut health: what to look for",
    "best-supplements-for-gut-health-and-weight-loss": "Supplements for gut health and weight loss: the facts",
    "what-is-gut-health": "What is gut health? A plain-language guide",
    "how-to-improve-gut-health": "How to improve gut health: six evidence-informed habits",
    "fermented-foods-gut-health": "Fermented foods and gut health: what counts",
    "microbial-dysbiosis": "Microbial dysbiosis and rebiosis explained",
}
DYS["desc"] = "What microbial dysbiosis is, what research links it to, and what rebiosis means in Herbaferm founder Adam B\u00f3day's book The Holistic Microbiome."

HERO = {"microbiome-test-singapore": "kit", "best-supplements-for-gut-health": "checklist", "natural-supplements-for-gut-health": "ai-herbs",
        "gut-health-supplement-reviews": "evidence", "best-probiotics-for-gut-health": "triad", "best-supplements-for-gut-health-and-weight-loss": "ai-porridge",
        "what-is-gut-health": "pillars", "how-to-improve-gut-health": "ai-morning", "fermented-foods-gut-health": "ai-jars", "microbial-dysbiosis": "ai-meadow"}
DYS["body"] = DYS["body"].replace("<h2>What causes dysbiosis?</h2>", "{{fig:dysbiosis}}\n<h2>What causes dysbiosis?</h2>", 1)
