
/* ================= scroll journey (home) ================= */
(function(){
  var $=function(s,r){return (r||document).querySelector(s)},$$=function(s,r){return Array.prototype.slice.call((r||document).querySelectorAll(s))};
  $$("[data-journey]").forEach(function(jr){
  var still=window.matchMedia&&matchMedia("(prefers-reduced-motion:reduce)").matches;
  var chs=$$(".ch",jr),home=jr.closest("main"),rail=$(".jrail",jr);
  /* split headings into words */
  $$("[data-split]",jr).forEach(function(h){
    var words=h.textContent.trim().split(/\s+/);h.setAttribute("aria-label",words.join(" "));
    h.innerHTML=words.map(function(w,i){return '<span class="w" aria-hidden="true"><i style="--i:'+i+'">'+w+'</i></span>'}).join(" ");
  });
  $$(".jv",jr).forEach(function(el,i){var sib=Array.prototype.indexOf.call(el.parentNode.children,el);el.style.setProperty("--d",Math.min(sib,6))});
  /* rail */
  var rl=chs.filter(function(c){return c.getAttribute("data-label")&&!c.classList.contains("ch-day")||c.getAttribute("data-label")==="Morning"});
  if(rail)rl.forEach(function(c){var a=document.createElement("a");a.href="#";a.setAttribute("aria-label",c.getAttribute("data-label"));a.innerHTML="<span>"+c.getAttribute("data-label")+"</span>";
    a.addEventListener("click",function(e){e.preventDefault();c.scrollIntoView({behavior:still?"auto":"smooth",block:"start"})});rail.appendChild(a)});
  var dots=rail?$$("a",rail):[];
  $$("[data-go]",jr).forEach(function(a){a.addEventListener("click",function(e){e.preventDefault();var t=document.getElementById(a.getAttribute("href").slice(1));if(t)t.scrollIntoView({behavior:still?"auto":"smooth"})})});
  /* rotating hero line */
  var rb=$$(".rot b",jr),ri=0;
  if(rb.length&&!still)setInterval(function(){if(home.hidden)return;var o=rb[ri];o.classList.remove("on");o.classList.add("off");ri=(ri+1)%rb.length;var n=rb[ri];n.classList.remove("off");n.classList.add("on");setTimeout(function(){o.classList.remove("off")},700)},2600);
  var cur=null;
  function paint(el){
    if(!el||el===cur)return;cur=el;
    jr.style.setProperty("--jbg",el.getAttribute("data-bg"));jr.style.setProperty("--jfg",el.getAttribute("data-fg"));jr.style.setProperty("--jac",el.getAttribute("data-ac"));
  }
  var hs=$(".ch-herbs",jr),panes=$$(".hpane",jr),hnow=$("#hnow",jr),hi=-1;
  var pars=$$("[data-par]",jr),ticking=false;
  function frame(){
    ticking=false;if(home.hidden){if(rail)rail.classList.remove("show");return}
    var vh=innerHeight,mid=vh*.5,active=null,ai=0;
    if(rail)rail.classList.add("show");
    chs.forEach(function(c,i){var r=c.getBoundingClientRect();
      if(r.top<vh*.85&&r.bottom>0)c.classList.add("in");
      if(r.top<=mid&&r.bottom>mid){active=c;ai=i}});
    if(!active)active=chs[0];
    /* herbs stage picks the current herb */
    if(active===hs){
      var r=hs.getBoundingClientRect(),p=Math.max(0,Math.min(.9999,-r.top/(r.height-vh+68))),idx=Math.floor(p*panes.length);
      if(idx!==hi){hi=idx;panes.forEach(function(x,j){x.classList.toggle("on",j===idx)});if(hnow)hnow.textContent=idx+1}
      paint(panes[hi<0?0:hi]);cur=null;paintForce(panes[hi<0?0:hi]);
    }else paint(active);
    var li=chs.indexOf(active);dots.forEach(function(d,j){var c=rl[j],ci=chs.indexOf(c),nx=rl[j+1]?chs.indexOf(rl[j+1]):chs.length;d.classList.toggle("on",li>=ci&&li<nx)});
    if(!still)pars.forEach(function(el){var r=el.getBoundingClientRect();if(r.bottom<-200||r.top>vh+200)return;var off=(r.top+r.height/2-mid),f=parseFloat(el.getAttribute("data-par"));el.style.transform="translate3d(0,"+(off*f).toFixed(1)+"px,0)"});
  }
  function paintForce(el){jr.style.setProperty("--jbg",el.getAttribute("data-bg"));jr.style.setProperty("--jfg",el.getAttribute("data-fg"));jr.style.setProperty("--jac",el.getAttribute("data-ac"))}
  function tick(){if(!ticking){ticking=true;requestAnimationFrame(frame)}}
  addEventListener("scroll",tick,{passive:true});addEventListener("resize",tick);addEventListener("hashchange",function(){setTimeout(tick,60)});addEventListener("hfroute",function(){setTimeout(tick,60)});addEventListener("popstate",function(){setTimeout(tick,60)});
  tick();setTimeout(tick,300);
  });
})();

/* product pages: in-page nav */
(function(){
  var $$=function(s,r){return Array.prototype.slice.call((r||document).querySelectorAll(s))};
  document.addEventListener("click",function(e){var a=e.target.closest(".psub a");if(!a)return;e.preventDefault();
    var t=document.getElementById(a.getAttribute("data-to"));if(t){var y=t.getBoundingClientRect().top+scrollY-(a.getAttribute("data-to").slice(-3)==="top"?0:130);scrollTo({top:Math.max(0,y),behavior:"smooth"})}});
  var tick=false;
  function spy(){tick=false;var pg=document.querySelector(".page:not([hidden])");if(!pg)return;var links=$$(".psub a",pg);if(!links.length)return;
    var cur=links[0];links.forEach(function(a){var t=document.getElementById(a.getAttribute("data-to"));if(t&&t.getBoundingClientRect().top<innerHeight*.4)cur=a});
    links.forEach(function(a){a.classList.toggle("on",a===cur)})}
  addEventListener("scroll",function(){if(!tick){tick=true;requestAnimationFrame(spy)}},{passive:true});
})();
