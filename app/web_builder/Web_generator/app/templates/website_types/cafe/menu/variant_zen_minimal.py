from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Minimalist Japanese Menu - Clean lines and zen aesthetic"""
    title = props.get("sectionTitle", props.get("title", "メニュー"))
    subtitle = props.get("sectionSubtitle", "Our Offerings")
    raw_items = props.get("items", [])
    
    primary = colors.get("primary", "#8B7355")
    text = colors.get("text", "#2D2013")
    
    items = []
    for item in raw_items:
        items.append({
            "name": item.get("name", "Item"),
            "desc": item.get("description", "")[:60],
            "price": item.get("price", "$0")
        })
    
    if not items:
        items = [
            {"name": "Matcha Latte", "desc": "Ceremonial grade", "price": "¥650"},
            {"name": "Pour Over", "desc": "Single origin", "price": "¥550"},
            {"name": "Hojicha", "desc": "Roasted green tea", "price": "¥480"},
            {"name": "Rice Bowl", "desc": "Seasonal toppings", "price": "¥980"}
        ]
    
    items_html = ""
    for i, item in enumerate(items[:8]):
        items_html += f'''
        <div class="zen-item">
            <span class="item-num">{str(i+1).zfill(2)}</span>
            <div class="item-details">
                <h4>{item["name"]}</h4>
                <p>{item["desc"]}</p>
            </div>
            <span class="item-price">{item["price"]}</span>
        </div>
        '''
    
    return f'''
    <section class="menu-zen" id="menu">
        <div class="zen-container">
            <div class="zen-header">
                <span class="jp-title">{title}</span>
                <h2>{subtitle}</h2>
                <div class="zen-line"></div>
            </div>
            <div class="zen-grid">
                {items_html}
            </div>
        </div>
    </section>
    
    <style>
    .menu-zen {{ padding: 120px 24px; background: #FAFAF8; }}
    .zen-container {{ max-width: 800px; margin: 0 auto; }}
    .zen-header {{ text-align: center; margin-bottom: 80px; }}
    .jp-title {{ display: block; font-size: 3rem; color: {primary}20; font-weight: 300; margin-bottom: 10px; }}
    .zen-header h2 {{ font-family: 'Playfair Display', serif; font-size: 2.5rem; color: {text}; font-weight: 400; letter-spacing: 4px; }}
    .zen-line {{ width: 40px; height: 1px; background: {primary}; margin: 30px auto; }}
    .zen-grid {{ display: flex; flex-direction: column; }}
    .zen-item {{ display: flex; align-items: center; gap: 30px; padding: 30px 0; border-bottom: 1px solid #eee; transition: 0.3s; }}
    .zen-item:hover {{ padding-left: 20px; background: #fff; }}
    .item-num {{ font-size: 0.8rem; color: {primary}; font-weight: 600; min-width: 30px; }}
    .item-details {{ flex: 1; }}
    .zen-item h4 {{ font-family: 'Playfair Display', serif; font-size: 1.3rem; color: {text}; margin-bottom: 6px; font-weight: 400; }}
    .zen-item p {{ color: #999; font-size: 0.9rem; }}
    .zen-item .item-price {{ font-size: 1.1rem; color: {text}; font-weight: 500; }}
    </style>
    '''
