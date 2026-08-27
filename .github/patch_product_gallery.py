from pathlib import Path

p = Path('index.html')
s = p.read_text()

old_css = '.gallery{display:grid;grid-template-columns:2fr 1fr 1fr;gap:8px}.gallery img{width:100%;height:130px;object-fit:cover;border-radius:12px}.gallery img:first-child{height:268px;grid-row:span 2}.detail-grid{display:grid;grid-template-columns:1fr 1fr;gap:22px}'
new_css = '.gallery{position:relative;min-height:420px;display:flex;align-items:center;justify-content:center;background:#f6f2eb;border-radius:18px;overflow:hidden}.gallery-main{display:block;width:100%;height:420px;object-fit:contain}.gallery-nav{position:absolute;top:50%;transform:translateY(-50%);width:42px;height:42px;border:0;border-radius:50%;background:rgba(255,255,255,.92);color:#1d211d;font-size:28px;line-height:1;display:flex;align-items:center;justify-content:center;cursor:pointer;box-shadow:0 4px 16px rgba(0,0,0,.12);z-index:2}.gallery-nav.prev{left:12px}.gallery-nav.next{right:12px}.gallery-nav:hover{background:#fff}.gallery-counter{position:absolute;left:50%;bottom:12px;transform:translateX(-50%);background:rgba(29,33,29,.72);color:#fff;border-radius:999px;padding:5px 9px;font-size:11px;z-index:2}.detail-grid{display:grid;grid-template-columns:1fr 1fr;gap:22px}'
if old_css not in s:
    raise SystemExit('gallery css target not found')
s = s.replace(old_css, new_css, 1)

old_mobile = '@media(max-width:600px){.nav{padding:12px 0;align-items:flex-start}.nav-actions{justify-content:flex-end}.brand{font-size:20px}.hero{padding-top:46px}h1{font-size:37px}.categories,.product-grid{grid-template-columns:1fr 1fr}.product-img{height:165px}.form-grid{grid-template-columns:1fr}.span-2{grid-column:auto}.section-head{align-items:flex-start;flex-direction:column}.list-row{grid-template-columns:1fr}.thumb{width:100%;height:210px}.gallery{grid-template-columns:1fr 1fr}.gallery img,.gallery img:first-child{height:180px;grid-row:auto}}'
new_mobile = '@media(max-width:600px){.nav{padding:12px 0;align-items:flex-start}.nav-actions{justify-content:flex-end}.brand{font-size:20px}.hero{padding-top:46px}h1{font-size:37px}.categories,.product-grid{grid-template-columns:1fr 1fr}.product-img{height:165px}.form-grid{grid-template-columns:1fr}.span-2{grid-column:auto}.section-head{align-items:flex-start;flex-direction:column}.list-row{grid-template-columns:1fr}.thumb{width:100%;height:210px}.gallery{min-height:320px}.gallery-main{height:320px}.gallery-nav{width:38px;height:38px;font-size:24px}}'
if old_mobile not in s:
    raise SystemExit('mobile gallery css target not found')
s = s.replace(old_mobile, new_mobile, 1)

old_js = '''async function openDetail(id){
  const {data,error}=await supabase.rpc("get_public_product",{p_id:id});
  const p=Array.isArray(data)?data[0]:data;
  if(error||!p)return toast("商品不存在或已下架");
  const gallery=(p.image_urls||[]).map(u=>`<img src="${u}" alt="">`).join("")||"<div class='empty'>沒有照片</div>";
  const meta=parseProductMeta(p);
  const specHtml=[meta.size?`<div class="detail-spec"><small>尺寸</small><b>${esc(meta.size)}</b></div>`:"",meta.color?`<div class="detail-spec"><small>顏色</small><b>${esc(meta.color)}</b></div>`:"",meta.quantity?`<div class="detail-spec"><small>數量</small><b>${esc(meta.quantity)}</b></div>`:""] .filter(Boolean).join("");
  $("detailContent").innerHTML=`<div class="detail-grid"><div class="gallery">${gallery}</div><div class="detail-info"><span class="badge">${esc(p.condition)}</span><h2>${esc(p.name)}</h2><div class="muted">${esc(p.category)}</div><div class="price" style="font-size:32px;margin:12px 0">${money(p.price)}</div>${specHtml?`<div class="detail-spec-grid">${specHtml}</div>`:""}${meta.description?`<div class="detail-description">${esc(meta.description)}</div>`:""}<div class="detail-actions"><button class="btn primary large" id="askProductBtn">我有興趣／詢問此商品</button></div><p class="muted" style="margin-top:10px">為保護賣家隱私，聯絡資訊不會直接公開，由平台協助聯繫。</p></div></div>`;
  const askBtn=$("askProductBtn");
  if(askBtn) askBtn.addEventListener("click",()=>window.askAboutProduct(p.id,p.name));
  openModal("detailModal");
}'''
new_js = '''async function openDetail(id){
  const {data,error}=await supabase.rpc("get_public_product",{p_id:id});
  const p=Array.isArray(data)?data[0]:data;
  if(error||!p)return toast("商品不存在或已下架");
  const images=(p.image_urls||[]).filter(Boolean);
  const gallery=images.length
    ? `<img id="detailGalleryImage" class="gallery-main" src="${images[0]}" alt="${esc(p.name)}">${images.length>1?`<button class="gallery-nav prev" id="detailGalleryPrev" type="button" aria-label="上一張">‹</button><button class="gallery-nav next" id="detailGalleryNext" type="button" aria-label="下一張">›</button><span class="gallery-counter" id="detailGalleryCounter">1 / ${images.length}</span>`:""}`
    : "<div class='empty'>沒有照片</div>";
  const meta=parseProductMeta(p);
  const specHtml=[meta.size?`<div class="detail-spec"><small>尺寸</small><b>${esc(meta.size)}</b></div>`:"",meta.color?`<div class="detail-spec"><small>顏色</small><b>${esc(meta.color)}</b></div>`:"",meta.quantity?`<div class="detail-spec"><small>數量</small><b>${esc(meta.quantity)}</b></div>`:""] .filter(Boolean).join("");
  $("detailContent").innerHTML=`<div class="detail-grid"><div class="gallery">${gallery}</div><div class="detail-info"><span class="badge">${esc(p.condition)}</span><h2>${esc(p.name)}</h2><div class="muted">${esc(p.category)}</div><div class="price" style="font-size:32px;margin:12px 0">${money(p.price)}</div>${specHtml?`<div class="detail-spec-grid">${specHtml}</div>`:""}${meta.description?`<div class="detail-description">${esc(meta.description)}</div>`:""}<div class="detail-actions"><button class="btn primary large" id="askProductBtn">我有興趣／詢問此商品</button></div><p class="muted" style="margin-top:10px">為保護賣家隱私，聯絡資訊不會直接公開，由平台協助聯繫。</p></div></div>`;
  if(images.length>1){
    let galleryIndex=0;
    const galleryImg=$("detailGalleryImage");
    const galleryCounter=$("detailGalleryCounter");
    const showImage=index=>{
      galleryIndex=(index+images.length)%images.length;
      galleryImg.src=images[galleryIndex];
      if(galleryCounter) galleryCounter.textContent=`${galleryIndex+1} / ${images.length}`;
    };
    $("detailGalleryPrev")?.addEventListener("click",()=>showImage(galleryIndex-1));
    $("detailGalleryNext")?.addEventListener("click",()=>showImage(galleryIndex+1));
  }
  const askBtn=$("askProductBtn");
  if(askBtn) askBtn.addEventListener("click",()=>window.askAboutProduct(p.id,p.name));
  openModal("detailModal");
}'''
if old_js not in s:
    raise SystemExit('openDetail target not found')
s = s.replace(old_js, new_js, 1)

p.write_text(s)
