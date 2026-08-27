from pathlib import Path

p = Path('index.html')
s = p.read_text()

marker = '<!-- more-category-section-stage2 -->'
if marker in s:
    raise SystemExit('more category section already exists')

anchor = '''    </div>\n  </div>\n</section>\n<section class="game-section-simple">'''
if anchor not in s:
    raise SystemExit('category section anchor not found')

block = '''    </div>\n\n    <!-- more-category-section-stage2 -->\n    <div class="more-category-wrap">\n      <div class="more-category-head">\n        <small>MORE CATEGORIES</small>\n        <h3>更多商品分類</h3>\n      </div>\n      <div class="more-category-grid">\n        <button class="more-category-btn" type="button" data-category="寵物用品"><b>寵物用品</b><span>飼料・玩具・外出・清潔</span></button>\n        <button class="more-category-btn" type="button" data-category="嬰幼兒用品"><b>嬰幼兒用品</b><span>童裝・玩具・推車・育兒用品</span></button>\n        <button class="more-category-btn" type="button" data-category="書籍／收藏／娛樂"><b>書籍／收藏／娛樂</b><span>書籍・公仔・收藏・影音娛樂</span></button>\n        <button class="more-category-btn" type="button" data-category="居家家具／生活美學"><b>居家家具／生活美學</b><span>家具・家飾・收納・生活選物</span></button>\n        <button class="more-category-btn" type="button" data-category="廚房／餐具"><b>廚房／餐具</b><span>廚具・餐具・杯壺・餐瓷</span></button>\n        <button class="more-category-btn" type="button" data-category="汽機車用品／配件"><b>汽機車用品／配件</b><span>汽車・機車・美容・改裝配件</span></button>\n        <button class="more-category-btn" type="button" data-category="教材／商業用品"><b>教材／商業用品</b><span>教材・文具・辦公・商業設備</span></button>\n        <button class="more-category-btn" type="button" data-category="婚禮／派對用品"><b>婚禮／派對用品</b><span>婚禮・派對・佈置・活動用品</span></button>\n        <button class="more-category-btn" type="button" data-category="旅行／外派用品"><b>旅行／外派用品</b><span>行李・旅行用品・外派生活</span></button>\n        <button class="more-category-btn" type="button" data-category="居家照護／保健器材"><b>居家照護／保健器材</b><span>照護・輔具・保健・居家設備</span></button>\n      </div>\n    </div>\n  </div>\n</section>\n<section class="game-section-simple">'''

s = s.replace(anchor, block, 1)

css = '''\n<style id="more-category-section-style">\n.more-category-wrap{margin-top:34px;padding-top:28px;border-top:1px solid var(--line2,#e6e0d6)}\n.more-category-head{margin-bottom:15px}\n.more-category-head small{display:block;color:#888b85;font-size:10px;letter-spacing:.18em;margin-bottom:6px}\n.more-category-head h3{margin:0;font-size:22px;letter-spacing:.01em}\n.more-category-grid{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:10px}\n.more-category-btn{min-width:0;text-align:left;background:#fff;border:1px solid var(--line2,#e6e0d6);border-radius:14px;padding:14px 15px;cursor:pointer;color:var(--ink2,#1d211d);transition:border-color .15s ease,transform .15s ease}\n.more-category-btn:hover{border-color:#aeb9b3;transform:translateY(-1px)}\n.more-category-btn b,.more-category-btn span{display:block}\n.more-category-btn b{font-size:14px;margin-bottom:5px}\n.more-category-btn span{font-size:11px;color:#7b7d78;line-height:1.45}\n@media(max-width:1000px){.more-category-grid{grid-template-columns:repeat(2,minmax(0,1fr))}}\n@media(max-width:600px){.more-category-wrap{margin-top:26px;padding-top:22px}.more-category-grid{grid-template-columns:1fr 1fr;gap:8px}.more-category-btn{padding:12px}.more-category-btn b{font-size:13px}.more-category-btn span{font-size:10px}}\n</style>\n'''

if '</head>' not in s:
    raise SystemExit('head end not found')
s = s.replace('</head>', css + '</head>', 1)

p.write_text(s)
