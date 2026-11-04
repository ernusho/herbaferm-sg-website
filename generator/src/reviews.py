"""Review, rating and comment blocks. No reviews exist yet, so every block starts empty and nothing is invented.
Product pages get a rating summary and a review form. Articles get a helpful vote and a question or comment form.
The forms are front end only. Set window.HF_REVIEW_ENDPOINT in the page to send submissions to a real backend later."""

STAR = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.8l2.9 6 6.6.9-4.8 4.6 1.2 6.5L12 17.7 6.1 20.8l1.2-6.5L2.5 9.7l6.6-.9z"/></svg>'

RULES = ('<p class="rv-rules"><b>Before you write.</b> Tell us how you use it and what you thought of the taste, texture and routine. '
         'Please do not share medical conditions, and do not say the product treats, cures or prevents anything. Reviews that do cannot be published. '
         'All reviews are read by our team before they appear.</p>')


def _stars(n=5):
    return "".join('<span class="rv-s">%s</span>' % STAR for _ in range(n))


def product(key, name):
    radios = "".join(
        '<input type="radio" name="rating-%s" id="rt-%s-%d" value="%d" required><label for="rt-%s-%d" title="%d out of 5"><span class="rv-s">%s</span><span class="vh">%d star%s</span></label>'
        % (key, key, i, i, key, i, i, STAR, i, "" if i == 1 else "s") for i in (5, 4, 3, 2, 1))
    bars = "".join('<li><span>%d</span><i><b style="width:0"></b></i><em>0</em></li>' % i for i in (5, 4, 3, 2, 1))
    return '''
<section class="rvs" id="%(k)s-reviews" data-rv="%(k)s" data-rv-kind="review" data-rv-name="%(n)s"><div class="wrap">
  <div class="rv-head"><div><p class="kicker">Reviews</p><h2>What customers say about %(n)s</h2></div>
  <button type="button" class="rv-open btn btn-honey" aria-expanded="false" aria-controls="%(k)s-rvform">Write a review</button></div>
  <div class="rv-grid">
    <div class="rv-sum">
      <div class="rv-score"><b>&ndash;</b><span class="rv-stars" aria-hidden="true">%(st)s</span></div>
      <p class="rv-none"><b>No reviews yet.</b> Be the first to share how %(n)s fits into your day.</p>
      <ul class="rv-bars" aria-label="Rating breakdown, no reviews yet">%(bars)s</ul>
    </div>
    <div class="rv-main">
      <div class="rv-list" aria-live="polite"><div class="rv-empty"><span>%(st1)s</span><p>Reviews will appear here once customers have shared them. We only show real reviews.</p></div></div>
      <form class="rv-form" id="%(k)s-rvform" hidden novalidate>
        <h3>Share your experience</h3>
        %(rules)s
        <fieldset class="rv-rate"><legend>Your rating <em>(required)</em></legend><div class="rv-radios">%(radios)s</div></fieldset>
        <div class="rv-row"><label>Headline<input name="title" maxlength="80" placeholder="A few words that sum it up" required></label>
        <label>First name or initial<input name="name" maxlength="30" autocomplete="given-name" placeholder="Shown with your review" required></label></div>
        <label>Your review<textarea name="body" rows="5" maxlength="600" placeholder="How do you take it, and what did you like or not like?" required></textarea><span class="rv-count">0 / 600</span></label>
        <div class="rv-row"><label>How long have you used it?<select name="used"><option value="">Choose one</option><option>Not yet, first order</option><option>Less than a week</option><option>1 to 4 weeks</option><option>1 to 3 months</option><option>Over 3 months</option></select></label>
        <label>Email <em>(private, optional)</em><input name="email" type="email" maxlength="80" autocomplete="email" placeholder="So we can reply if needed"></label></div>
        <label class="rv-check"><input type="checkbox" name="ok" required> I agree that my review can be shown with my first name once the team has checked it.</label>
        <p class="rv-err" role="alert" hidden></p>
        <div class="rv-actions"><button type="submit" class="btn btn-honey">Submit review</button><button type="button" class="rv-cancel btn btn-line">Cancel</button></div>
        <p class="rv-proto">Prototype: this form does not send anything yet. Your review stays in this browser as a private preview.</p>
      </form>
    </div>
  </div>
</div></section>
''' % {"k": key, "n": name, "st": _stars(), "st1": STAR * 1, "bars": bars, "radios": radios, "rules": RULES}


def article():
    return '''
<section class="rvs rv-art" data-rv="article" data-rv-kind="comment"><div>
  <h2>Was this article helpful?</h2>
  <div class="rv-vote" role="group" aria-label="Was this article helpful?"><button type="button" data-v="yes">Yes, it helped</button><button type="button" data-v="no">Not really</button><span class="rv-thanks" aria-live="polite" hidden>Thank you, that helps us improve it.</span></div>
  <h3>Questions or comments</h3>
  <p class="rv-hint">Ask us something or tell us what is missing. Please do not share personal health details. Comments are read by our team before they appear.</p>
  <div class="rv-list" aria-live="polite"><div class="rv-empty"><p>No comments yet. Be the first to ask a question.</p></div></div>
  <form class="rv-form rv-open-form" novalidate>
    <div class="rv-row"><label>First name or initial<input name="name" maxlength="30" required></label><label>Email <em>(private, optional)</em><input name="email" type="email" maxlength="80"></label></div>
    <label>Your question or comment<textarea name="body" rows="4" maxlength="500" required></textarea><span class="rv-count">0 / 500</span></label>
    <p class="rv-err" role="alert" hidden></p>
    <div class="rv-actions"><button type="submit" class="btn btn-honey">Post comment</button></div>
    <p class="rv-proto">Prototype: nothing is sent yet. Your comment stays in this browser as a private preview.</p>
  </form>
</div></section>
'''
