/* reviews and comments: front end only, drafts live in this browser. Set window.HF_REVIEW_ENDPOINT to post to a backend. */
(function(){
  var STAR='<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.8l2.9 6 6.6.9-4.8 4.6 1.2 6.5L12 17.7 6.1 20.8l1.2-6.5L2.5 9.7l6.6-.9z"/></svg>';
  var CLAIM=/\b(cure[sd]?|curing|heal(s|ed|ing)?|treat(s|ed|ing|ment)?|prevent(s|ed|ing)?|diagnos\w*|disease|cancer|diabet\w*|ibs|crohn\w*|colitis|infection|medicat\w*|prescri\w*|anxiety|depress\w*)\b/i;
  function $(s,r){return (r||document).querySelector(s)}
  function esc(t){return String(t).replace(/[&<>"']/g,function(c){return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]})}
  function load(k){try{return JSON.parse(localStorage.getItem("hf-rv-"+k)||"[]")}catch(e){return[]}}
  function save(k,v){try{localStorage.setItem("hf-rv-"+k,JSON.stringify(v))}catch(e){}}
  function stars(n){var h="";for(var i=1;i<=5;i++)h+='<span class="rv-s'+(i<=n?" on":"")+'">'+STAR+'</span>';return '<span class="rv-stars" role="img" aria-label="'+n+' out of 5 stars">'+h+'</span>'}
  function render(box){
    var k=box.getAttribute("data-rv"),kind=box.getAttribute("data-rv-kind"),items=load(k),list=$(".rv-list",box);
    if(!list)return;
    var empty=list.getAttribute("data-empty");if(empty===null){list.setAttribute("data-empty",list.innerHTML);empty=list.innerHTML}
    if(!items.length){list.innerHTML=empty}
    else list.innerHTML=items.map(function(r,i){
      return '<article class="rv-item"><div class="rv-badge">Your private preview, not published</div>'+
        (kind==="review"?'<div class="rv-top">'+stars(r.rating)+'<b>'+esc(r.title)+'</b></div>':'')+
        '<p>'+esc(r.body)+'</p><p class="rv-by">'+esc(r.name)+(r.used?' &middot; used '+esc(r.used.toLowerCase()):'')+' &middot; '+esc(r.date)+
        ' <button type="button" class="rv-del" data-i="'+i+'">Delete</button></p></article>'}).join("");
  }
  function msg(f,t){var e=$(".rv-err",f);if(!e)return;e.textContent=t||"";e.hidden=!t}
  function field(f,n){var e=f.elements[n];return e?(e.value||"").trim():""}
  function submit(f){
    var box=f.closest(".rvs"),k=box.getAttribute("data-rv"),kind=box.getAttribute("data-rv-kind");
    var r={name:field(f,"name"),body:field(f,"body"),title:field(f,"title"),used:field(f,"used"),email:field(f,"email"),date:new Date().toLocaleDateString("en-GB",{day:"numeric",month:"short",year:"numeric"})};
    if(kind==="review"){var c=f.querySelector("input[type=radio]:checked");r.rating=c?+c.value:0;if(!r.rating)return msg(f,"Please choose a star rating."),void 0}
    if(kind==="review"&&!r.title)return msg(f,"Please add a short headline."),void 0;
    if(!r.name)return msg(f,"Please add your first name or initial."),void 0;
    if(r.body.length<(kind==="review"?20:8))return msg(f,"Please write a little more so others can learn from it."),void 0;
    if(CLAIM.test(r.title+" "+r.body))return msg(f,"Please remove wording about treating, curing, preventing or medical conditions. We cannot publish those. Describe your routine and what you liked instead."),void 0;
    if(r.email&&!/^\S+@\S+\.\S+$/.test(r.email))return msg(f,"That email does not look right, or leave it empty."),void 0;
    if(f.elements.ok&&!f.elements.ok.checked)return msg(f,"Please tick the box to agree."),void 0;
    msg(f,"");
    if(window.HF_REVIEW_ENDPOINT){try{fetch(window.HF_REVIEW_ENDPOINT,{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({page:k,kind:kind,review:r,url:location.href})})}catch(e){}}
    var all=load(k);all.unshift(r);save(k,all);
    f.reset();var cnt=$(".rv-count",f);if(cnt)cnt.textContent="0 / "+f.elements.body.maxLength;
    if(kind==="review"){f.hidden=true;var b=$(".rv-open",box);if(b)b.setAttribute("aria-expanded","false")}
    render(box);var first=$(".rv-item",box);if(first){first.scrollIntoView({block:"center",behavior:"smooth"})}
  }
  document.addEventListener("click",function(e){
    var t=e.target;if(!t.closest)return;
    var g=t.closest("[data-rv-go]");if(g){e.preventDefault();var s=document.getElementById(g.getAttribute("data-rv-go"));if(s){window.scrollTo({top:s.getBoundingClientRect().top+window.scrollY-110,behavior:"smooth"});var ob=s.querySelector(".rv-open");if(ob&&ob.getAttribute("aria-expanded")!=="true")setTimeout(function(){ob.click()},450)}return}
    var o=t.closest(".rv-open");if(o){var box=o.closest(".rvs"),f=$(".rv-form",box),show=f.hidden;f.hidden=!show;o.setAttribute("aria-expanded",show?"true":"false");if(show){f.scrollIntoView({block:"center",behavior:"smooth"});var i=f.querySelector("input[type=radio]");}return}
    var c=t.closest(".rv-cancel");if(c){var f2=c.closest("form");f2.hidden=true;msg(f2,"");var b2=$(".rv-open",f2.closest(".rvs"));if(b2)b2.setAttribute("aria-expanded","false");return}
    var d=t.closest(".rv-del");if(d){var bx=d.closest(".rvs"),k=bx.getAttribute("data-rv"),a=load(k);a.splice(+d.getAttribute("data-i"),1);save(k,a);render(bx);return}
    var v=t.closest(".rv-vote button");if(v){var g=v.parentNode;[].forEach.call(g.querySelectorAll("button"),function(x){x.setAttribute("aria-pressed",x===v?"true":"false")});var th=$(".rv-thanks",g);if(th)th.hidden=false;try{localStorage.setItem("hf-vote-"+location.pathname,v.getAttribute("data-v"))}catch(er){}}
  });
  document.addEventListener("submit",function(e){var f=e.target;if(f.classList&&f.classList.contains("rv-form")){e.preventDefault();submit(f)}});
  document.addEventListener("input",function(e){var t=e.target;if(t.tagName==="TEXTAREA"&&t.closest(".rv-form")){var c=$(".rv-count",t.parentNode);if(c)c.textContent=t.value.length+" / "+t.maxLength}});
  function init(){[].forEach.call(document.querySelectorAll(".rvs[data-rv]"),function(b){render(b);
    if(b.getAttribute("data-rv")==="article"){try{var s=localStorage.getItem("hf-vote-"+location.pathname);if(s){var bt=b.querySelector('.rv-vote button[data-v="'+s+'"]');if(bt){bt.setAttribute("aria-pressed","true");var th=$(".rv-thanks",b);if(th)th.hidden=false}}}catch(er){}}})}
  if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",init);else init();
})();
