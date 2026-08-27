from pathlib import Path
import re

p = Path('index.html')
s = p.read_text()

marker = '<!-- hero-carousel-a-v1 -->'
if marker in s:
    raise SystemExit('hero carousel already exists')

pattern = re.compile(r'''(?P<indent>\s*)<div class="hero-photo-wrap">\s*(?P<img><img[^>]+alt="精選二手相機商品"[^>]*>)\s*(?P<card><div class="hero-photo-card">.*?</div>)\s*</div>''', re.S)
m = pattern.search(s)
if not m:
    raise SystemExit('hero photo block not found')

indent = m.group('indent')
img = m.group('img')
card = m.group('card')
replacement = f'''{indent}<!-- hero-carousel-a-v1 -->
{indent}<div class="hero-photo-wrap hero-carousel" id="heroCarousel">
{indent}  <div class="hero-slide active" data-slide="0">
{indent}    {img}
{indent}    {card}
{indent}  </div>
{indent}  <div class="hero-slide hero-placeholder hero-placeholder-1" data-slide="1" aria-label="預留輪播圖片"></div>
{indent}  <div class="hero-slide hero-placeholder hero-placeholder-2" data-slide="2" aria-label="預留輪播圖片"></div>
{indent}  <div class="hero-slide hero-placeholder hero-placeholder-3" data-slide="3" aria-label="預留輪播圖片"></div>
{indent}  <div class="hero-carousel-dots" aria-label="首頁圖片輪播位置">
{indent}    <button type="button" class="hero-dot active" aria-label="第 1 張" data-index="0"></button>
{indent}    <button type="button" class="hero-dot" aria-label="第 2 張" data-index="1"></button>
{indent}    <button type="button" class="hero-dot" aria-label="第 3 張" data-index="2"></button>
{indent}    <button type="button" class="hero-dot" aria-label="第 4 張" data-index="3"></button>
{indent}  </div>
{indent}</div>'''
s = s[:m.start()] + replacement + s[m.end():]

css = '''
<style id="hero-carousel-a-style">
.hero-carousel{isolation:isolate}
.hero-slide{position:absolute;inset:0;opacity:0;pointer-events:none;transition:opacity .7s ease}
.hero-slide.active{opacity:1;pointer-events:auto;z-index:1}
.hero-slide>img{width:100%;height:100%;object-fit:cover;object-position:center 46%;display:block}
.hero-placeholder{background:#ece6dd}
.hero-placeholder-1{background:linear-gradient(135deg,#f0ece5 0%,#e7e0d6 52%,#ded6ca 100%)}
.hero-placeholder-2{background:linear-gradient(145deg,#ebe7df 0%,#e2ddd4 48%,#d7d0c5 100%)}
.hero-placeholder-3{background:linear-gradient(125deg,#f2eee7 0%,#e8e1d7 55%,#ddd5ca 100%)}
.hero-placeholder:after{content:'';position:absolute;inset:0;background:radial-gradient(circle at 30% 28%,rgba(255,255,255,.58),transparent 34%),radial-gradient(circle at 75% 68%,rgba(255,255,255,.28),transparent 38%);opacity:.72}
.hero-carousel-dots{position:absolute;right:14px;bottom:14px;z-index:6;display:flex;gap:7px;align-items:center;padding:6px 8px;border-radius:999px;background:rgba(255,255,255,.62);backdrop-filter:blur(6px)}
.hero-dot{width:7px;height:7px;padding:0;border:0;border-radius:50%;background:rgba(38,53,47,.28);cursor:pointer;transition:transform .18s ease,background .18s ease}
.hero-dot.active{background:#284d40;transform:scale(1.22)}
@media(max-width:620px){.hero-carousel-dots{right:10px;bottom:10px;gap:6px;padding:5px 7px}.hero-dot{width:6px;height:6px}}
@media(prefers-reduced-motion:reduce){.hero-slide{transition:none}}
</style>
'''
if '</head>' not in s:
    raise SystemExit('head end not found')
s = s.replace('</head>', css + '</head>', 1)

js = '''
<script id="hero-carousel-a-script">
(function(){
  const root=document.getElementById('heroCarousel');
  if(!root) return;
  const slides=Array.from(root.querySelectorAll('.hero-slide'));
  const dots=Array.from(root.querySelectorAll('.hero-dot'));
  if(slides.length<2 || dots.length!==slides.length) return;
  let index=0;
  let timer=null;
  function show(next){
    index=(next+slides.length)%slides.length;
    slides.forEach((slide,i)=>slide.classList.toggle('active',i===index));
    dots.forEach((dot,i)=>dot.classList.toggle('active',i===index));
  }
  function start(){
    if(timer) clearInterval(timer);
    timer=setInterval(()=>show(index+1),3500);
  }
  dots.forEach((dot,i)=>dot.addEventListener('click',()=>{show(i);start();}));
  document.addEventListener('visibilitychange',()=>{
    if(document.hidden){if(timer) clearInterval(timer);timer=null;}
    else start();
  });
  start();
})();
</script>
'''
if '</body>' not in s:
    raise SystemExit('body end not found')
s = s.replace('</body>', js + '</body>', 1)

p.write_text(s)
