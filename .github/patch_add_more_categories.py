from pathlib import Path

p = Path('index.html')
s = p.read_text()

old_form = '<label>分類<select id="pCategory"><option>衣服鞋子</option><option>3C</option><option>釣魚用具</option><option>露營裝備</option><option>遊戲點數／虛寶</option></select></label>'
new_form = '<label>分類<select id="pCategory"><option>衣服鞋子</option><option>3C</option><option>釣魚用具</option><option>露營裝備</option><option>寵物用品</option><option>嬰幼兒用品</option><option>書籍／收藏／娛樂</option><option>居家家具／生活美學</option><option>廚房／餐具</option><option>汽機車用品／配件</option><option>教材／商業用品</option><option>婚禮／派對用品</option><option>旅行／外派用品</option><option>居家照護／保健器材</option><option>遊戲點數／虛寶</option></select></label>'
if old_form not in s:
    raise SystemExit('pCategory target not found')
s = s.replace(old_form, new_form, 1)

old_filter = '''          <option value="衣服鞋子">衣服鞋子</option>\n          <option value="3C">3C</option>\n          <option value="釣魚用具">釣魚用具</option>\n          <option value="露營裝備">露營裝備</option>'''
new_filter = '''          <option value="衣服鞋子">衣服鞋子</option>\n          <option value="3C">3C</option>\n          <option value="釣魚用具">釣魚用具</option>\n          <option value="露營裝備">露營裝備</option>\n          <option value="寵物用品">寵物用品</option>\n          <option value="嬰幼兒用品">嬰幼兒用品</option>\n          <option value="書籍／收藏／娛樂">書籍／收藏／娛樂</option>\n          <option value="居家家具／生活美學">居家家具／生活美學</option>\n          <option value="廚房／餐具">廚房／餐具</option>\n          <option value="汽機車用品／配件">汽機車用品／配件</option>\n          <option value="教材／商業用品">教材／商業用品</option>\n          <option value="婚禮／派對用品">婚禮／派對用品</option>\n          <option value="旅行／外派用品">旅行／外派用品</option>\n          <option value="居家照護／保健器材">居家照護／保健器材</option>'''
if old_filter not in s:
    raise SystemExit('categoryFilter target not found')
s = s.replace(old_filter, new_filter, 1)

p.write_text(s)
