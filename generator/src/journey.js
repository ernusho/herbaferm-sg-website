
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
  var DK={"#2b3a24":["#1a241a","#f3ead6","#e9b04a"],"#f7efdc":["#231d14","#f3e8d2","#e08a52"],"#efdfc0":["#2b2217","#f3e8d2","#e08a52"],"#e9c06a":["#3a2a12","#f6e6c4","#e9b04a"],"#c4683f":["#4a2418","#ffe9d0","#ffcf8a"],"#f3dcae":["#33261a","#f6e8cf","#e9b04a"],"#d3cf9c":["#2a2d1a","#ecebcf","#cdd68a"],"#3a2c1e":["#1c1610","#f6e8d2","#e9b04a"],"#efd5bf":["#36221a","#f6e2d4","#e0875a"],"#e8c45e":["#3d3414","#f6e9b8","#e8c45e"],"#e9bdb0":["#3d2420","#f3d9d2","#e9a090"],"#efe6cc":["#2f2d1b","#efe9cf","#cfc47a"],"#b8473f":["#3d1a1a","#ffe3dc","#ff9a8a"],"#b9772a":["#3a2610","#ffe6bf","#e9a040"],"#5b3d24":["#241810","#f6ead9","#e9b04a"],"#aebb8c":["#222b17","#e3ebd0","#b5c98a"]};
  function isDark(){var t=document.documentElement.getAttribute("data-theme");return t?t==="dark":matchMedia("(prefers-color-scheme: dark)").matches}
  function cols(el){var b=el.getAttribute("data-bg"),f=el.getAttribute("data-fg"),a=el.getAttribute("data-ac");if(isDark()&&DK[b.toLowerCase()]){var d=DK[b.toLowerCase()];return[d[0],d[1],d[2]]}return[b,f,a]}
  function paint(el){
    if(!el||el===cur)return;cur=el;
    var c=cols(el);jr.style.setProperty("--jbg",c[0]);jr.style.setProperty("--jfg",c[1]);jr.style.setProperty("--jac",c[2]);
  }
  new MutationObserver(function(){var e=cur;cur=null;if(e)paint(e)}).observe(document.documentElement,{attributes:true,attributeFilter:["data-theme"]});
  var hs=$(".ch-herbs",jr),panes=$$(".hslide",jr),hnow=$("#hnow",jr),hi=0,hsOn=false,htrack=$("#hpanes",jr),hprev=$("#hprev",jr),hnext=$("#hnext",jr),hdots=$$(".hdot",jr);

  /* seven herbs carousel */
  function hgo(i,instant){i=Math.max(0,Math.min(panes.length-1,i));if(!htrack)return;htrack.scrollTo({left:i*htrack.clientWidth,behavior:(still||instant)?"auto":"smooth"})}
  function hset(i){
    if(i===hi&&panes[i].classList.contains("on"))return;hi=i;
    panes.forEach(function(x,k){x.classList.toggle("on",k===i)});
    hdots.forEach(function(d,k){d.classList.toggle("on",k===i);d.setAttribute("aria-selected",k===i?"true":"false")});
    if(hnow)hnow.textContent=i+1;if(hprev)hprev.disabled=i===0;if(hnext)hnext.disabled=i===panes.length-1;
    if(hsOn)paintForce(panes[i]);
  }
  if(htrack&&panes.length){
    var hraf=0;htrack.addEventListener("scroll",function(){if(hraf)return;hraf=requestAnimationFrame(function(){hraf=0;hset(Math.round(htrack.scrollLeft/Math.max(1,htrack.clientWidth)))})},{passive:true});
    if(hprev)hprev.addEventListener("click",function(){hgo(hi-1)});
    if(hnext)hnext.addEventListener("click",function(){hgo(hi+1)});
    hdots.forEach(function(d){d.addEventListener("click",function(){hgo(+d.getAttribute("data-i"))})});
    htrack.addEventListener("keydown",function(e){if(e.key==="ArrowRight"){e.preventDefault();hgo(hi+1)}else if(e.key==="ArrowLeft"){e.preventDefault();hgo(hi-1)}else if(e.key==="Home"){e.preventDefault();hgo(0)}else if(e.key==="End"){e.preventDefault();hgo(panes.length-1)}});
    addEventListener("resize",function(){hgo(hi,true)});
    if(hprev)hprev.disabled=true;
  }
  var pars=$$("[data-par]",jr),ticking=false;
  function frame(){
    ticking=false;if(home.hidden){if(rail)rail.classList.remove("show");return}
    var vh=innerHeight,mid=vh*.5,active=null,ai=0;
    if(rail)rail.classList.add("show");
    chs.forEach(function(c,i){var r=c.getBoundingClientRect();
      if(r.top<vh*.85&&r.bottom>0)c.classList.add("in");
      if(r.top<=mid&&r.bottom>mid){active=c;ai=i}});
    if(!active)active=chs[0];
    /* herbs carousel: the chapter takes the colours of the herb on show */
    if(active===hs){hsOn=true;paintForce(panes[hi]);cur=null;
    }else{hsOn=false;paint(active)}
    var li=chs.indexOf(active);dots.forEach(function(d,j){var c=rl[j],ci=chs.indexOf(c),nx=rl[j+1]?chs.indexOf(rl[j+1]):chs.length;d.classList.toggle("on",li>=ci&&li<nx)});
    if(!still)pars.forEach(function(el){var r=el.getBoundingClientRect();if(r.bottom<-200||r.top>vh+200)return;var off=(r.top+r.height/2-mid),f=parseFloat(el.getAttribute("data-par"));el.style.transform="translate3d(0,"+(off*f).toFixed(1)+"px,0)"});
  }
  function paintForce(el){var c=cols(el);jr.style.setProperty("--jbg",c[0]);jr.style.setProperty("--jfg",c[1]);jr.style.setProperty("--jac",c[2])}
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
