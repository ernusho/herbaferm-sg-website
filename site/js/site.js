(function(){
  var $=function(s,r){return (r||document).querySelector(s)};
  var $$=function(s,r){return Array.prototype.slice.call((r||document).querySelectorAll(s))};
  var PRODUCTS={drops:{name:"Herbaferm Drops",size:"30 ml",price:55},fiber:{name:"Fiber Elite",size:"125 g",price:55},prefer:{name:"Prefer HF400",size:"14 capsules",price:45}};
  var root=document.documentElement;

  /* ---------- router ---------- */
  var pages=$$(".page"),names=pages.map(function(p){return p.id.slice(2)});
  var parents={drops:"shop",fiber:"shop",prefer:"shop",ingredients:"learn",science:"learn",quality:"about",awards:"about"};
  var hosts={ingredients:"learn",science:"learn",quality:"about",awards:"about"};
  function route(first){
    var h=(location.hash||"").replace("#","");
    var host=hosts[h]||h;
    if(names.indexOf(host)<0){host="home";h="home"}
    pages.forEach(function(p){var on=p.id==="p-"+host;p.hidden=!on;p.classList.remove("in");if(on){void p.offsetWidth;p.classList.add("in")}});
    var cur=$("#p-"+host);document.title=cur.getAttribute("data-title")||"Herbaferm Singapore";
    var key=parents[h]||(h.indexOf("a-")===0?"learn":h);
    $$(".nav nav a, .mnav a").forEach(function(a){a.classList.toggle("on",a.getAttribute("data-r")===key)});
    $(".mnav").classList.remove("on");
    var sec=hosts[h]?$("#sec-"+h,cur):null;
    if(sec){var go=function(){window.scrollTo({top:sec.getBoundingClientRect().top+window.scrollY-120,behavior:"auto"})};go();setTimeout(go,60)}
    else if(!first)window.scrollTo(0,0);
    spy();
  }
  /* sub-tabs on merged pages follow the scroll position */
  function spy(){
    var cur=$(".page:not([hidden])");if(!cur)return;var tabs=$$(".subnav a",cur);if(!tabs.length)return;
    var on=tabs[0];tabs.forEach(function(t){var s=document.getElementById(t.getAttribute("data-sec"));if(s&&s.getBoundingClientRect().top<180)on=t});
    tabs.forEach(function(t){t.classList.toggle("on",t===on)});
    var wrap=on.parentNode;if(wrap&&wrap.scrollWidth>wrap.clientWidth){wrap.scrollLeft=on.offsetLeft-16}
  }
  addEventListener("scroll",spy,{passive:true});
  document.addEventListener("click",function(e){var a=e.target.closest(".subnav a");if(a&&a.getAttribute("href")==="#"+(location.hash||"").replace("#","")){e.preventDefault();var s=document.getElementById(a.getAttribute("data-sec"));if(s)window.scrollTo({top:s.getBoundingClientRect().top+window.scrollY-120,behavior:"smooth"})}});
  window.addEventListener("hashchange",function(){route(false)});
  route(true);
  window.addEventListener("scroll",function(){var rb=$("#readbar");if(!rb)return;var on=(location.hash||"").indexOf("#a-")===0;if(!on){rb.style.width=0;return}var h=document.documentElement;var m=h.scrollHeight-h.clientHeight;rb.style.width=(m>0?Math.min(100,h.scrollTop/m*100):0)+"%"},{passive:true});

  /* ---------- theme ---------- */
  var tb=$("#theme");
  function isDark(){var t=root.getAttribute("data-theme");return t?t==="dark":window.matchMedia("(prefers-color-scheme: dark)").matches}
  function tl(){tb.setAttribute("aria-label",isDark()?"Switch to light mode":"Switch to dark mode");tb.textContent=isDark()?"Light":"Dark"}
  tb.addEventListener("click",function(){root.setAttribute("data-theme",isDark()?"light":"dark");tl()});tl();
  $("#burger").addEventListener("click",function(){$(".mnav").classList.toggle("on")});

  /* ---------- cart ---------- */
  var cart={};
  try{cart=JSON.parse(localStorage.getItem("hf-cart")||"{}")||{}}catch(e){cart={}}
  function save(){try{localStorage.setItem("hf-cart",JSON.stringify(cart))}catch(e){}}
  function fmt(n){return "S$"+n.toFixed(2)}
  function thumb(id){
    var im=$('img[data-thumb="'+id+'"]');
    return im?'<img alt="" src="'+im.src+'">':'<span>'+(id==="fiber"?"FIBER":"")+'</span>';
  }
  function render(){
    var ids=Object.keys(cart).filter(function(k){return cart[k]>0&&PRODUCTS[k]}),n=0,tot=0,h="";
    ids.forEach(function(k){var p=PRODUCTS[k];n+=cart[k];tot+=cart[k]*p.price;
      h+='<div class="line"><div class="th">'+thumb(k)+'</div><div><b>'+p.name+'</b><br><small>'+p.size+' · '+fmt(p.price)+'</small><div class="qty" style="margin-top:6px"><button type="button" data-d="-1" data-id="'+k+'" aria-label="Decrease">&minus;</button><output>'+cart[k]+'</output><button type="button" data-d="1" data-id="'+k+'" aria-label="Increase">+</button></div></div><b>'+fmt(cart[k]*p.price)+'</b></div>'});
    $("#cart-items").innerHTML=h||'<p class="empty">Your cart is empty.</p>';
    $("#cart-total").textContent=fmt(tot);$("#cart-n").textContent=n;$("#cart-n").hidden=!n;
    $("#cart-go").disabled=!n;
  }
  /* v7: spring engine. Critically damped by default, velocity carried across hand-offs, always started from the live value. */
  var RM=matchMedia("(prefers-reduced-motion: reduce)");
  function buzz(n){try{if(navigator.vibrate&&!RM.matches)navigator.vibrate(n||8)}catch(e){}}
  function spring(o){ /* o: from,to,v (px/s),response (s),damping,step(x),done() */
    var w=2*Math.PI/(o.response||.4),k=w*w,c=2*(o.damping==null?1:o.damping)*w,x=o.from,v=o.v||0,last=performance.now(),dead=false;
    if(RM.matches){o.step(o.to);if(o.done)o.done();return {stop:function(){},get:function(){return o.to}}}
    function tick(t){if(dead)return;var dt=Math.min((t-last)/1000,.05);last=t;
      for(var i=0;i<4;i++){var h=dt/4,a=-k*(x-o.to)-c*v;v+=a*h;x+=v*h}
      o.step(x);
      if(Math.abs(v)<.5&&Math.abs(x-o.to)<.25){o.step(o.to);dead=true;if(o.done)o.done();return}
      requestAnimationFrame(tick)}
    requestAnimationFrame(tick);
    return {stop:function(){dead=true},get:function(){return x},vel:function(){return v}};
  }
  function project(v,r){r=r||.998;return (v/1000)*r/(1-r)}
  function rubber(over,dim){var c=.55;return (over*dim*c)/(dim+c*Math.abs(over))}
  function tracker(){var h=[];return {add:function(x){var t=performance.now();h.push([t,x]);while(h.length>1&&t-h[0][0]>100)h.shift()},v:function(){if(h.length<2)return 0;var a=h[0],b=h[h.length-1],dt=(b[0]-a[0])/1000;return dt>0?(b[1]-a[1])/dt:0},clear:function(){h=[]}}}
  window.HFX={spring:spring,project:project,rubber:rubber,tracker:tracker,buzz:buzz,RM:RM};
  /* cart drawer: follows the finger, flick to dismiss, springs in from the right */
  var dr=$("#drawer"),scr=$("#scrim"),dx=0,dsp=null,dopen=false;
  function dset(x){dx=x;var w=dr.offsetWidth||420;dr.style.transform="translate3d("+x+"px,0,0)";scr.style.opacity=Math.max(0,Math.min(1,1-x/w))}
  function openCart(on,vel){
    if(on===dopen&&!dr.classList.contains("moving"))return;
    dopen=on;var w=dr.offsetWidth||420;
    if(dsp)dsp.stop();
    if(on){dr.classList.add("on","moving");scr.classList.add("on");if(!dr.style.transform)dset(w)}
    scr.classList.toggle("on",on);
    dsp=spring({from:dx,to:on?0:w,v:vel||0,response:on?.42:.34,damping:on?.86:1,step:dset,done:function(){dr.classList.remove("moving");if(!on){dr.classList.remove("on");dr.style.transform="";scr.style.opacity="";scr.classList.remove("on");dx=0}else{dr.style.transform="";scr.style.opacity=""}}});
  }
  (function(){var tr=tracker(),sx=0,drag=false,id=null;
    dr.addEventListener("pointerdown",function(e){if(e.target.closest("button,input,a"))return;sx=e.clientX;id=e.pointerId;drag=false;tr.clear();tr.add(e.clientX)});
    dr.addEventListener("pointermove",function(e){if(id!==e.pointerId)return;var d=e.clientX-sx;
      if(!drag){if(d<10)return;drag=true;if(dsp)dsp.stop();dr.classList.add("moving");try{dr.setPointerCapture(id)}catch(_){}}
      tr.add(e.clientX);dset(Math.max(0,d))});
    function end(e){if(id!==e.pointerId)return;id=null;if(!drag)return;drag=false;var v=tr.v(),w=dr.offsetWidth,proj=dx+project(v);dopen=false;openCart(proj<w*.5,v)}
    dr.addEventListener("pointerup",end);dr.addEventListener("pointercancel",end)})();
  var tt;function toast(m){var t=$("#toast");t.textContent=m;t.classList.add("on");clearTimeout(tt);tt=setTimeout(function(){t.classList.remove("on")},2200)}
  function add(id,q){cart[id]=(cart[id]||0)+q;save();render();buzz(8);toast(PRODUCTS[id].name+" added to cart")}
  $("#cart-open").addEventListener("click",function(){openCart(true)});
  $("#cart-close").addEventListener("click",function(){openCart(false)});
  $("#scrim").addEventListener("click",function(){openCart(false)});
  $("#cart-items").addEventListener("click",function(e){var b=e.target.closest("button[data-id]");if(!b)return;var id=b.getAttribute("data-id");cart[id]=Math.max(0,(cart[id]||0)+parseInt(b.getAttribute("data-d"),10));save();render()});
  $("#cart-go").addEventListener("click",function(){var n=$("#cart-note");n.hidden=false});
  document.addEventListener("keydown",function(e){if(e.key==="Escape")openCart(false)});
  document.addEventListener("click",function(e){
    var a=e.target.closest("[data-add]");
    if(a){var id=a.getAttribute("data-add"),q=1,box=a.closest(".buy");if(box){q=parseInt($("output",box).textContent,10)||1}add(id,q);return}
    var m=e.target.closest(".qty button[data-q]");
    if(m){var o=$("output",m.parentNode);o.textContent=Math.max(1,Math.min(20,(parseInt(o.textContent,10)||1)+parseInt(m.getAttribute("data-q"),10)))}
  });
  render();

  /* ---------- tabs ---------- */
  $$(".tabs").forEach(function(tabs){
    var panels=$$(".tabpanel",tabs.parentNode);
    $$("button",tabs).forEach(function(b){b.addEventListener("click",function(){
      $$("button",tabs).forEach(function(x){x.setAttribute("aria-selected",x===b?"true":"false")});
      panels.forEach(function(p){p.hidden=p.id!==b.getAttribute("aria-controls")});
    })});
  });

  /* ---------- faq filter + search ---------- */
  var fq=$("#faq-q"),cat="all";
  function faqFilter(){
    var q=(fq.value||"").toLowerCase().trim(),shown=0;
    $$("#faq-list details").forEach(function(d){
      var ok=(cat==="all"||d.getAttribute("data-c")===cat)&&(!q||d.textContent.toLowerCase().indexOf(q)>-1);
      d.hidden=!ok;if(ok)shown++;
    });
    $("#faq-none").hidden=shown>0;
  }
  if(fq){fq.addEventListener("input",faqFilter);
    $$("#faq-chips button").forEach(function(b){b.addEventListener("click",function(){cat=b.getAttribute("data-c");$$("#faq-chips button").forEach(function(x){x.setAttribute("aria-pressed",x===b?"true":"false")});faqFilter()})})}

  /* ---------- forms (prototype: nothing is sent) ---------- */
  $$("form[data-proto]").forEach(function(f){f.addEventListener("submit",function(e){
    e.preventDefault();
    var n=$(".fnote",f);if(n){n.className="sent fnote";n.textContent=f.getAttribute("data-proto")}
  })});

  /* ---------- v3 interactions ---------- */
  function tabset(sel,panelFn){
    $$(sel).forEach(function(group){
      $$("button",group).forEach(function(b){b.addEventListener("click",function(){
        $$("button",group).forEach(function(x){x.setAttribute("aria-selected",x===b?"true":"false")});panelFn(b,group)})});
    });
  }
  /* day tabs */
  tabset(".daytabs",function(b,g){var wrap=g.parentNode;$$(".daypanel",wrap).forEach(function(p){p.hidden=p.id!==b.getAttribute("aria-controls")})});
  /* herb explorer */
  $$(".explorer").forEach(function(ex){
    var btns=$$(".hlist button",ex);
    function pick(id){btns.forEach(function(x){x.setAttribute("aria-selected",x.getAttribute("data-h")===id?"true":"false")});$$(".hpanel",ex).forEach(function(p){p.hidden=p.getAttribute("data-hp")!==id})}
    btns.forEach(function(b){b.addEventListener("click",function(){pick(b.getAttribute("data-h"))});b.addEventListener("mouseenter",function(){if(window.matchMedia("(hover:hover)").matches)pick(b.getAttribute("data-h"))})});
  });
  /* journal filter */
  $$("#j-chips button").forEach(function(b){b.addEventListener("click",function(){
    $$("#j-chips button").forEach(function(x){x.setAttribute("aria-pressed",x===b?"true":"false")});
    var c=b.getAttribute("data-c");$$("#j-grid .jcard").forEach(function(a){a.hidden=!(c==="all"||a.getAttribute("data-c")===c)});
  })});
  /* calculators */
  $$(".calc").forEach(function(c){
    var total=parseFloat(c.getAttribute("data-total")),unit=c.getAttribute("data-unit"),fixed=parseFloat(c.getAttribute("data-dose"))||0;
    var a=$(".c-a",c),b=$(".c-b",c);
    function upd(){
      var d=fixed||(a?parseFloat(a.value):1),n=parseFloat(b.value);
      if(a)$(".c-av",c).textContent=a.value;$(".c-bv",c).textContent=b.value;
      var days=Math.max(1,Math.floor(total/(d*n)));
      $(".c-out",c).textContent=days;
      $(".c-cap",c).textContent="days from one "+(unit==="g"?"125 g pouch":"30 ml bottle");
      $(".c-bar",c).style.width=Math.min(100,days/40*100)+"%";
    }
    if(a)a.addEventListener("input",upd);b.addEventListener("input",upd);upd();
  });
  /* science stepper */
  var st=$(".stepper");
  if(st){
    var det=$("#stepdetail"),texts=det.getAttribute("data-steps").split("|"),bs=$$("button",st),cur=0,timer=null;
    function go(i){cur=i;bs.forEach(function(x,k){x.setAttribute("aria-selected",k===i?"true":"false")});det.textContent=texts[i]}
    bs.forEach(function(x,k){x.addEventListener("click",function(){clearInterval(timer);go(k)})});
    if(!window.matchMedia("(prefers-reduced-motion: reduce)").matches){timer=setInterval(function(){if(!st.offsetParent)return;go((cur+1)%bs.length)},4200)}
  }
  /* routine finder */
  var qz=$("#quiz");
  if(qz){
    var ans={},steps=$$(".qstep",qz),prog=$$(".qprog i",qz);
    var NAME={drops:"Herbaferm Drops",fiber:"Fiber Elite",prefer:"Prefer HF400"};
    var HOW={drops:"8 drops in 1.5 dl of water, morning and evening, built up gradually from 5.",fiber:"3.5 g a day with a meal, stirred into food or a drink.",prefer:"1 capsule in the morning and 1 in the evening."};
    function show(n){steps.forEach(function(s){s.hidden=s.getAttribute("data-q")!==String(n)});prog.forEach(function(p,i){p.classList.toggle("on",i<(n==="r"?3:n))})}
    function result(){
      var base=ans[1],list=[base];
      if(ans[3]==="two"){list.push(base==="drops"?(ans[2]==="desk"?"prefer":"fiber"):"drops")}
      if(ans[3]==="all"){list=["drops","fiber","prefer"]}
      $("#q-name").textContent=list.map(function(k){return NAME[k]}).join(" + ");
      $("#q-text").innerHTML=list.map(function(k){return "<b>"+NAME[k]+":</b> "+HOW[k]}).join("<br>")+"<br><br><small>A suggestion based on how you like to take things, not health advice. Speak to a professional if you take medication or have a condition.</small>";
      var t=list.reduce(function(a,k){return a+PRODUCTS[k].price},0);
      $("#q-add").textContent="Add to cart, S$"+t;$("#q-add").setAttribute("data-list",list.join(","));
      $("#q-view").setAttribute("href","#"+(list.length===1?list[0]:"shop"));
      show("r");
    }
    $$(".opts button",qz).forEach(function(b){b.addEventListener("click",function(){
      var q=parseInt(b.closest(".qstep").getAttribute("data-q"),10);ans[q]=b.getAttribute("data-v");
      if(q<3)show(q+1);else result();
    })});
    $("#q-redo").addEventListener("click",function(){ans={};show(1)});
    $("#q-add").addEventListener("click",function(){($("#q-add").getAttribute("data-list")||"").split(",").forEach(function(k){if(PRODUCTS[k]){cart[k]=(cart[k]||0)+1}});save();render();toast("Routine added to cart");openCart(true)});
  }
  /* photo slots: preview your own photo */
  $$(".slot").forEach(function(s){
    var f=$("input",s),rm=$(".rm",s);
    f.addEventListener("change",function(){var file=f.files&&f.files[0];if(!file||!/^image\//.test(file.type))return;
      var r=new FileReader();r.onload=function(){s.style.backgroundImage="url("+r.result+")";s.classList.add("has")};r.readAsDataURL(file)});
    rm.addEventListener("click",function(e){e.preventDefault();e.stopPropagation();s.style.backgroundImage="";s.classList.remove("has");f.value=""});
  });

  /* v4: product gallery views, sticky buy bar, article contents links */
  $$("[data-gal]").forEach(function(g){
    var bar=g.parentNode.querySelector(".gthumbs");if(!bar)return;
    $$("button",bar).forEach(function(b){b.addEventListener("click",function(){
      var i=b.getAttribute("data-gi");
      $$("[data-g]",g).forEach(function(v){v.hidden=v.getAttribute("data-g")!==i});
      $$("button",bar).forEach(function(x){x.setAttribute("aria-selected",x===b?"true":"false")});
    })});
  });
  $$(".pd").forEach(function(pd){
    var buy=$(".buy",pd),btn=buy&&$("[data-add]",buy),pr=$(".price b",pd),h1=$("h1",pd);if(!btn||!pr||!h1)return;
    var bar=document.createElement("div");bar.className="stickybuy";bar.setAttribute("aria-hidden","true");
    bar.innerHTML='<div><b>'+h1.textContent+'</b><span>'+pr.textContent+'</span></div><button class="btn btn-honey" type="button" tabindex="-1" data-add="'+btn.getAttribute("data-add")+'">Add to cart</button>';
    pd.closest("main").appendChild(bar);
    if("IntersectionObserver" in window){
      new IntersectionObserver(function(es){es.forEach(function(e){var past=!e.isIntersecting&&e.boundingClientRect.bottom<0;bar.classList.toggle("on",past);document.body.classList.toggle("sb",past&&!pd.closest("main").hidden)})}).observe(buy);
    }
  });
  window.addEventListener("hashchange",function(){document.body.classList.remove("sb");$$(".stickybuy").forEach(function(b){b.classList.remove("on")})});
  document.addEventListener("click",function(e){
    var a=e.target.closest("[data-jump]");if(!a)return;e.preventDefault();
    var t=document.getElementById(a.getAttribute("data-jump"));if(t)t.scrollIntoView({behavior:window.matchMedia("(prefers-reduced-motion: reduce)").matches?"auto":"smooth",block:"start"});
  });

  /* v5: calm motion. Everything below pauses on hover or focus, outside the viewport, and with "Pause motion" or reduced-motion. */
  var still=window.matchMedia("(prefers-reduced-motion: reduce)").matches,html=document.documentElement;
  function inView(el){var r=el.getBoundingClientRect();return r.bottom>0&&r.top<window.innerHeight&&el.offsetParent!==null}
  function auto(el,ms,step,stopOnUser){
    if(!el)return;var held=false,done=false;
    ["mouseenter","focusin","touchstart"].forEach(function(t){el.addEventListener(t,function(){held=true},{passive:true})});
    ["mouseleave","focusout"].forEach(function(t){el.addEventListener(t,function(){held=false})});
    if(stopOnUser)el.addEventListener("click",function(e){if(e.isTrusted)done=true});
    setInterval(function(){if(done||held||still||html.classList.contains("still")||document.hidden||!inView(el))return;step()},ms);
  }
  var st=$("#still");if(st)st.addEventListener("click",function(){var on=html.classList.toggle("still");st.setAttribute("aria-pressed",on?"true":"false");st.textContent=on?"Play motion":"Pause motion"});
  /* hero: swipeable product stage. 1:1 drag, momentum projection, rubber band, spring settle */
  var hp=$(".heroprod");if(hp){
    var trk=$(".hslides",hp),hs=$$(".hs",hp),hd=$$(".hdots button",hp),hi=0,hx=0,hsp=null,htr=tracker();
    function hw(){return hp.clientWidth}
    function hset(x){hx=x;trk.style.transform="translate3d("+x+"px,0,0)"}
    function hmark(i){hi=i;hs.forEach(function(x,k){x.classList.toggle("on",k===i);$$("a,button",x).forEach(function(c){c.tabIndex=k===i?0:-1})});hd.forEach(function(x,k){x.classList.toggle("on",k===i);x.setAttribute("aria-selected",k===i?"true":"false")})}
    function hshow(i,v,quiet){hmark(i);if(hsp)hsp.stop();hsp=spring({from:hx,to:-i*hw(),v:v||0,response:.5,damping:v?.8:1,step:hset});if(!quiet&&v)buzz(6)}
    window.addEventListener("resize",function(){hset(-hi*hw())});
    hd.forEach(function(b,k){b.addEventListener("click",function(){hshow(k)})});
    var hdn=false,hsx=0,hbase=0,hmoved=false,hid=null;
    trk.addEventListener("pointerdown",function(e){if(e.button>0)return;hid=e.pointerId;hsx=e.clientX;hbase=hx;hdn=true;hmoved=false;htr.clear();htr.add(e.clientX);if(hsp)hsp.stop()});
    trk.addEventListener("pointermove",function(e){if(!hdn||e.pointerId!==hid)return;var d=e.clientX-hsx;
      if(!hmoved){if(Math.abs(d)<8)return;hmoved=true;trk.classList.add("drag");try{trk.setPointerCapture(hid)}catch(_){}}
      htr.add(e.clientX);var x=hbase+d,mn=-(hs.length-1)*hw();
      if(x>0)x=rubber(x,hw());else if(x<mn)x=mn-rubber(mn-x,hw());hset(x)});
    function hend(e){if(!hdn||e.pointerId!==hid)return;hdn=false;trk.classList.remove("drag");if(!hmoved)return;
      var v=htr.v(),to=hx+project(v),i=Math.max(0,Math.min(hs.length-1,Math.round(-to/hw())));hshow(i,v)}
    trk.addEventListener("pointerup",hend);trk.addEventListener("pointercancel",hend);
    trk.addEventListener("click",function(e){if(hmoved){e.preventDefault();e.stopPropagation();hmoved=false}},true);
    trk.addEventListener("dragstart",function(e){e.preventDefault()});
    hp.addEventListener("keydown",function(e){if(e.key==="ArrowRight")hshow(Math.min(hs.length-1,hi+1));if(e.key==="ArrowLeft")hshow(Math.max(0,hi-1))});
    auto(hp,4500,function(){if(hdn)return;hshow((hi+1)%hs.length,0,true)},false);
  }
  /* header gains its edge once content slides beneath it */
  var htop=$("header.top");if(htop){var sc=function(){htop.classList.toggle("sc",window.scrollY>8)};addEventListener("scroll",sc,{passive:true});sc()}
  /* iOS only shows :active when a touch listener exists */
  document.addEventListener("touchstart",function(){},{passive:true});
  /* journal strip: mouse drag with momentum (touch uses native scroll) */
  $$(".jtrack").forEach(function(t){var d=false,sx=0,sl=0,tr=tracker(),mv=false,raf=0;
    t.addEventListener("pointerdown",function(e){if(e.pointerType!=="mouse")return;d=true;mv=false;sx=e.clientX;sl=t.scrollLeft;tr.clear();tr.add(e.clientX);cancelAnimationFrame(raf)});
    window.addEventListener("pointermove",function(e){if(!d)return;var dx=e.clientX-sx;if(!mv&&Math.abs(dx)>6){mv=true;t.style.scrollSnapType="none";t.style.cursor="grabbing"}if(mv){t.scrollLeft=sl-dx;tr.add(e.clientX)}});
    window.addEventListener("pointerup",function(){if(!d)return;d=false;t.style.cursor="";if(!mv)return;var v=-tr.v(),x=t.scrollLeft,to=x+project(v,.995);
      var cards=$$(".jcard",t),best=to,bd=1e9;cards.forEach(function(c){var p=c.offsetLeft-t.offsetLeft-parseInt(getComputedStyle(t).paddingLeft||0,10);if(Math.abs(p-to)<bd){bd=Math.abs(p-to);best=p}});
      best=Math.max(0,Math.min(best,t.scrollWidth-t.clientWidth));
      spring({from:x,to:best,v:v,response:.5,damping:.85,step:function(s){t.scrollLeft=s},done:function(){t.style.scrollSnapType=""}})});
    t.addEventListener("click",function(e){if(mv){e.preventDefault();mv=false}},true)});
  /* herb explorer and day tabs rotate until you take over */
  var exl=$(".explorer");if(exl){var hb=$$(".hlist button",exl),hk=0;
    exl.classList.add("auto");
    hb.forEach(function(b,k){b.addEventListener("click",function(e){if(e.isTrusted)exl.classList.remove("auto");hk=k})});
    auto(exl,5000,function(){if(!exl.classList.contains("auto"))return;hk=(hk+1)%hb.length;hb[hk].click()},true);
  }
  var dt=$(".daytabs");if(dt){var db=$$("button",dt),dk=0,dw=dt.parentNode;
    db.forEach(function(b,k){b.addEventListener("click",function(){dk=k})});
    auto(dw,6000,function(){dk=(dk+1)%db.length;db[dk].click()},true);
  }
  /* journal strip */
  var jc=$(".jcar");if(jc){var tr=$(".jtrack",jc),jn=$$(".jnav button",jc);
    function jgo(d){var w=(tr.firstElementChild?tr.firstElementChild.getBoundingClientRect().width+24:320);
      if(d>0&&tr.scrollLeft+tr.clientWidth>=tr.scrollWidth-4)tr.scrollTo({left:0,behavior:"smooth"});
      else tr.scrollBy({left:d*w,behavior:"smooth"})}
    jn.forEach(function(b){b.addEventListener("click",function(){jgo(parseInt(b.getAttribute("data-d"),10))})});
    auto(jc,3800,function(){jgo(1)},false);
  }
  /* numbers count up once */
  var cn=$$("[data-count]");
  if(cn.length&&"IntersectionObserver" in window&&!still){
    var co=new IntersectionObserver(function(es){es.forEach(function(e){if(!e.isIntersecting)return;co.unobserve(e.target);
      var el=e.target,to=parseInt(el.getAttribute("data-count"),10),t0=null;
      function f(t){if(t0===null)t0=t;var p=Math.min(1,(t-t0)/1100),v=Math.round(to*(1-Math.pow(1-p,3)));el.textContent=v;if(p<1)requestAnimationFrame(f)}
      el.textContent="0";requestAnimationFrame(f)})},{threshold:.6});
    cn.forEach(function(el){co.observe(el)});
  }
  /* soft parallax on arched photos */
  if(!still){var par=$$(".arch img");
    if(par.length){var tick=false;
      function pp(){tick=false;if(html.classList.contains("still"))return;par.forEach(function(im){var r=im.parentNode.getBoundingClientRect();if(r.bottom<0||r.top>window.innerHeight)return;var c=(r.top+r.height/2-window.innerHeight/2)/window.innerHeight;im.style.transform="translateY("+(c*-28).toFixed(1)+"px) scale(1.1)"})}
      window.addEventListener("scroll",function(){if(!tick){tick=true;requestAnimationFrame(pp)}},{passive:true});pp();
    }
  }

  /* v6: site search, back to top */
  (function(){
    var ov=$("#srch"),qi=$("#srch-q"),res=$("#srch-res"),idx=window.HFIDX||[],sel=-1,items=[];
    var POP=[["drops","Herbaferm Drops"],["fiber","Fiber Elite"],["prefer","Prefer HF400"],["a-month","Your first month with Drops"],["faq","Questions and answers"],["partners","Partner with us"]];
    function esc(t){return String(t).replace(/[&<>"]/g,function(c){return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]})}
    function hi(t,ws){var o=esc(t);ws.forEach(function(w){if(w.length>1)o=o.replace(new RegExp("("+w.replace(/[.*+?^${}()|[\]\\]/g,"\\$&")+")","ig"),"<mark>$1</mark>")});return o}
    function snip(x,ws){var l=x.toLowerCase(),p=-1;for(var i=0;i<ws.length;i++){p=l.indexOf(ws[i]);if(p>-1)break}if(p<0)p=0;var a=Math.max(0,p-40);return (a>0?"\u2026":"")+x.slice(a,a+110)+"\u2026"}
    function render(list,ws){
      items=list;sel=list.length?0:-1;
      if(!list.length){res.innerHTML='<p class="none">Nothing found. Try another word, or <a href="#faq" data-close>browse the questions</a>.</p>';return}
      res.innerHTML=list.map(function(r,i){return '<a href="#'+r.id+'" role="option" data-i="'+i+'"'+(i===0?' class="on"':'')+'><span class="kd">'+esc(r.k)+'</span><b>'+hi(r.t,ws)+'</b>'+(r.x&&ws.length?'<small>'+hi(snip(r.x,ws),ws)+'</small>':'')+'</a>'}).join("");
    }
    function search(q){
      var ws=q.toLowerCase().split(/\s+/).filter(Boolean);
      if(!ws.length){render(POP.map(function(p){return {id:p[0],t:p[1],k:"Popular",x:""}}),[]);return}
      var sc=[];idx.forEach(function(r){var t=r.t.toLowerCase(),x=r.x.toLowerCase(),s=0,ok=true;
        ws.forEach(function(w){var a=t.indexOf(w)>-1,b=x.indexOf(w)>-1;if(!a&&!b){ok=false}else{s+=(a?5:0)+(b?1:0)+(t.indexOf(w)===0?2:0)}});
        if(ok)sc.push([s+(r.k==="Product"?2:0),r])});
      sc.sort(function(a,b){return b[0]-a[0]});render(sc.slice(0,8).map(function(z){return z[1]}),ws);
    }
    function open_(){ov.hidden=false;document.body.style.overflow="hidden";qi.value="";search("");setTimeout(function(){qi.focus()},30)}
    function close_(){ov.hidden=true;document.body.style.overflow=""}
    function go(i){var r=items[i];if(!r)return;close_();
      if(r.q){location.hash="#faq";setTimeout(function(){var f=$("#faq-q");if(f){f.value=r.q.split(" ").slice(0,4).join(" ");f.dispatchEvent(new Event("input",{bubbles:true}))}},60)}
      else location.hash="#"+r.id}
    $("#search-open").addEventListener("click",open_);
    $("#srch-x").addEventListener("click",close_);
    ov.addEventListener("click",function(e){if(e.target===ov)close_();if(e.target.closest("[data-close]"))close_()});
    qi.addEventListener("input",function(){search(qi.value)});
    res.addEventListener("click",function(e){var a=e.target.closest("a[data-i]");if(a){e.preventDefault();go(parseInt(a.getAttribute("data-i"),10))}});
    qi.addEventListener("keydown",function(e){
      if(e.key==="ArrowDown"||e.key==="ArrowUp"){e.preventDefault();if(!items.length)return;sel=(sel+(e.key==="ArrowDown"?1:-1)+items.length)%items.length;$$("a[data-i]",res).forEach(function(a,i){a.classList.toggle("on",i===sel)});var cur=$("a.on",res);if(cur)cur.scrollIntoView({block:"nearest"})}
      else if(e.key==="Enter"){e.preventDefault();go(Math.max(sel,0))}});
    document.addEventListener("keydown",function(e){
      if(e.key==="Escape"&&!ov.hidden)close_();
      if((e.key==="/"||(e.key==="k"&&(e.metaKey||e.ctrlKey)))&&ov.hidden&&!/INPUT|TEXTAREA|SELECT/.test((document.activeElement||{}).tagName||"")){e.preventDefault();open_()}});
    var tt=$("#totop");
    window.addEventListener("scroll",function(){tt.hidden=window.scrollY<900},{passive:true});
    tt.addEventListener("click",function(){window.scrollTo({top:0,behavior:"smooth"})});
  })();
  /* gentle reveal: content is always visible, it only lifts into place */
  if("IntersectionObserver" in window&&!window.matchMedia("(prefers-reduced-motion: reduce)").matches){
    var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.remove("pre");io.unobserve(e.target)}})},{rootMargin:"0px 0px -8% 0px"});
    $$("section .wrap > *, .rv").forEach(function(el){el.classList.add("rv");var r=el.getBoundingClientRect();if(r.top>window.innerHeight){el.classList.add("pre")}io.observe(el)});
  }
})();


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
  addEventListener("scroll",tick,{passive:true});addEventListener("resize",tick);addEventListener("hashchange",function(){setTimeout(tick,60)});
  tick();setTimeout(tick,300);
  });
})();
