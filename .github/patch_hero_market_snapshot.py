from pathlib import Path

p = Path('index.html')
s = p.read_text()

marker = '<!-- hero-market-snapshot-v1 -->'
if marker in s:
    raise SystemExit('hero market snapshot already exists')

anchor = '''      <div class="hero-actions2"><button class="btn primary hero-btn" id="heroSellBtn">開始刊登</button><button class="btn ghost hero-btn" id="heroQueryBtn">查詢我的商品</button></div>\n      <div class="trust-inline"><span>✓ 人工審核</span><span>✓ 免註冊刊登</span><span>✓ 聯絡資訊保護</span></div>'''
if anchor not in s:
    raise SystemExit('hero actions anchor not found')

replacement = '''      <div class="hero-actions2"><button class="btn primary hero-btn" id="heroSellBtn">開始刊登</button><button class="btn ghost hero-btn" id="heroQueryBtn">查詢我的商品</button></div>\n      <!-- hero-market-snapshot-v1 -->\n      <div class="hero-market-snapshot" aria-label="平台資訊">\n        <span><b>本週持續更新</b><small>精選好物陸續上架</small></span>\n        <span><b>熱門分類</b><small>3C・露營・釣具</small></span>\n        <span><b>人工審核</b><small>上架前逐件確認</small></span>\n      </div>\n      <div class="trust-inline"><span>✓ 人工審核</span><span>✓ 免註冊刊登</span><span>✓ 聯絡資訊保護</span></div>'''
s = s.replace(anchor, replacement, 1)

css = '''\n<style id="hero-market-snapshot-style">\n.hero-market-snapshot{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));margin-top:18px;padding:13px 0;border-top:1px solid var(--v3-line,#e7e2d9);border-bottom:1px solid var(--v3-line,#e7e2d9)}\n.hero-market-snapshot>span{min-width:0;padding:0 13px}\n.hero-market-snapshot>span:first-child{padding-left:0}\n.hero-market-snapshot>span+span{border-left:1px solid var(--v3-line,#e7e2d9)}\n.hero-market-snapshot b,.hero-market-snapshot small{display:block}\n.hero-market-snapshot b{font-size:12px;line-height:1.35;color:var(--v3-black,#20231f);margin-bottom:4px}\n.hero-market-snapshot small{font-size:10px;line-height:1.45;color:var(--v3-sub,#71756f);white-space:nowrap}\n@media(max-width:620px){.hero-market-snapshot{margin-top:16px;padding:11px 0}.hero-market-snapshot>span{padding:0 8px}.hero-market-snapshot b{font-size:11px}.hero-market-snapshot small{font-size:9px;white-space:normal}.trust-inline{margin-top:14px}}\n</style>\n'''
if '</head>' not in s:
    raise SystemExit('head end not found')
s = s.replace('</head>', css + '</head>', 1)

p.write_text(s)
