from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Store Grid - Gaming merch store"""
    title = props.get("title", "Game Store")
    primary = colors.get("primary", "#FF4444")
    
    items = [
        {"name": "Hero Skin Pack", "price": "$9.99", "type": "DLC", "img": "https://images.unsplash.com/photo-1538481199705-c710c4e965fc?w=400"},
        {"name": "Starter Bundle", "price": "$19.99", "type": "Bundle", "img": "https://images.unsplash.com/photo-1511512578047-dfb367046420?w=400"},
        {"name": "Premium Pass", "price": "$29.99", "type": "Season Pass", "img": "https://images.unsplash.com/photo-1542751371-adc38448a05e?w=400"}
    ]
    
    items_html = ""
    for i in items:
        items_html += f'''<div class="store-item"><div class="item-img" style="background-image: url('{i["img"]}')"><span class="item-type">{i["type"]}</span></div><div class="item-info"><h3>{i["name"]}</h3><div class="item-footer"><span class="price">{i["price"]}</span><a href="#">Buy Now</a></div></div></div>'''
    
    return f'''
    <section class="gaming-store" id="store"><div class="container"><h2>{title}</h2><div class="store-grid">{items_html}</div></div></section>
    <style>
    .gaming-store {{ padding: 100px 40px; background: #0D0D15; }}
    .container {{ max-width: 1200px; margin: 0 auto; }}
    .gaming-store h2 {{ font-size: 2.5rem; color: #fff; font-weight: 800; text-align: center; margin-bottom: 50px; }}
    .store-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 30px; }}
    .store-item {{ background: #1a1a2e; border-radius: 16px; overflow: hidden; transition: 0.3s; }}
    .store-item:hover {{ transform: translateY(-10px); }}
    .item-img {{ height: 200px; background-size: cover; background-position: center; position: relative; }}
    .item-type {{ position: absolute; top: 15px; right: 15px; padding: 6px 15px; background: {primary}; color: #fff; font-size: 0.75rem; font-weight: 700; }}
    .item-info {{ padding: 20px; color: #fff; }}
    .item-info h3 {{ font-size: 1.2rem; margin-bottom: 15px; }}
    .item-footer {{ display: flex; justify-content: space-between; align-items: center; }}
    .price {{ font-size: 1.3rem; font-weight: 800; color: {primary}; }}
    .item-footer a {{ padding: 10px 25px; background: {primary}; color: #fff; text-decoration: none; font-weight: 600; font-size: 0.9rem; }}
    @media (max-width: 900px) {{ .store-grid {{ grid-template-columns: 1fr; }} }}
    </style>
    '''
