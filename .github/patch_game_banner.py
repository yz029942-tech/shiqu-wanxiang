from pathlib import Path
import re

p = Path('index.html')
s = p.read_text()

card_pat = re.compile(r'(<button class="game-category-card" type="button" data-category="遊戲點數／虛寶">).*?(</button>)', re.S)
card_new = '''<button class="game-category-card" type="button" data-category="遊戲點數／虛寶">
      <img class="game-market-banner" src="game-market-banner.png" alt="遊戲專區">
    </button>'''
s, changed = card_pat.subn(card_new, s, count=1)
if changed != 1:
    raise SystemExit('Game section card not found exactly once')

old_css = '.game-category-card{width:100%;min-height:112px;border:1px solid var(--line2);background:#fff;border-radius:6px;padding:22px 24px;display:flex;align-items:center;justify-content:space-between;text-align:left;cursor:pointer;color:var(--ink2);transition:transform .18s ease,box-shadow .18s ease}'
new_css = '.game-category-card{width:100%;min-height:0;border:0;background:transparent;border-radius:6px;padding:0;display:block;overflow:hidden;text-align:left;cursor:pointer;color:var(--ink2);transition:transform .18s ease,box-shadow .18s ease}'
if old_css not in s:
    raise SystemExit('Game section CSS target not found')
s = s.replace(old_css, new_css, 1)

hover = '.game-category-card:hover{transform:translateY(-2px);box-shadow:0 10px 28px rgba(30,40,34,.07)}'
if '.game-market-banner{' not in s:
    if hover not in s:
        raise SystemExit('Game section hover CSS target not found')
    s = s.replace(hover, hover + '\n.game-market-banner{display:block;width:100%;height:auto;object-fit:contain;border-radius:6px}', 1)

mobile_old = '@media(max-width:620px){.game-section-simple{padding-bottom:26px}.game-category-card{min-height:96px;padding:18px}.game-category-copy b{font-size:16px}}'
mobile_new = '@media(max-width:620px){.game-section-simple{padding-bottom:26px}}'
if mobile_old in s:
    s = s.replace(mobile_old, mobile_new, 1)

p.write_text(s)
