from pathlib import Path

p = Path('index.html')
s = p.read_text()
old = 'src="game-market-banner.png"'
new = 'src="game-market-banner-v2.png"'
count = s.count(old)
if count != 1:
    raise SystemExit(f'expected exactly 1 old banner reference, found {count}')
s = s.replace(old, new, 1)
p.write_text(s)
