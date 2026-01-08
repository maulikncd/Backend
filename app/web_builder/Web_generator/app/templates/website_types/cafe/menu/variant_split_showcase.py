from typing import Dict, Any

def _normalize_item(item) -> Dict[str, Any]:
    """Normalize menu item to dict format - handles string or dict input"""
    if isinstance(item, str):
        return {"name": item, "description": "", "price": "$0"}
    elif isinstance(item, dict):
        return item
    else:
        return {"name": str(item), "description": "", "price": "$0"}

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Split Image Menu - Half image, half menu items"""
    title = props.get("sectionTitle", props.get("title", "Our Selection"))
    raw_items = props.get("items", [])
    
    primary = colors.get("primary", "#8B7355")
    text = colors.get("text", "#2D2013")
    
    items = []
    for raw_item in raw_items:
        item = _normalize_item(raw_item)
        items.append({
            "name": item.get("name", "Item"),
            "desc": item.get("description", "")[:60],
            "price": item.get("price", "$0")
        })
    
    if not items:
        items = [
            {"name": "House Blend", "desc": "Medium roast, notes of chocolate", "price": "$4.00"},
            {"name": "Cold Brew", "desc": "20-hour steep, smooth finish", "price": "$5.50"},
            {"name": "Affogato", "desc": "Espresso over vanilla gelato", "price": "$7.00"},
            {"name": "Almond Croissant", "desc": "Filled with frangipane", "price": "$5.00"}
        ]
    
    items_html = ""
    for item in items[:6]:
        items_html += f'''
        <div class="split-item">
            <div class="split-top">
                <h4>{item["name"]}</h4>
                <span class="split-dots"></span>
                <span class="split-price">{item["price"]}</span>
            </div>
            <p>{item["desc"]}</p>
        </div>
        '''
    
    return f'''
    <section class="menu-split" id="menu">
        <div class="split-image">
            <img src="https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=1200" alt="Coffee">
            <div class="image-overlay"></div>
            <div class="image-text">
                <span>Crafted</span>
                <span>With</span>
                <span>Love</span>
            </div>
        </div>
        <div class="split-content">
            <h2>{title}</h2>
            <div class="menu-items">
                {items_html}
            </div>
            <a href="#" class="view-full">View Full Menu</a>
        </div>
    </section>
    
    <style>
    .menu-split {{ display: grid; grid-template-columns: 1fr 1fr; min-height: 100vh; }}
    .split-image {{ position: relative; }}
    .split-image img {{ width: 100%; height: 100%; object-fit: cover; }}
    .image-overlay {{ position: absolute; inset: 0; background: rgba(0,0,0,0.4); }}
    .image-text {{ position: absolute; inset: 0; display: flex; flex-direction: column; justify-content: center; align-items: center; color: #fff; font-family: 'Playfair Display', serif; font-size: 4rem; line-height: 1.2; }}
    .split-content {{ padding: 80px 60px; display: flex; flex-direction: column; justify-content: center; background: #fff; }}
    .split-content h2 {{ font-family: 'Playfair Display', serif; font-size: 3rem; color: {text}; margin-bottom: 50px; }}
    .menu-items {{ display: flex; flex-direction: column; gap: 30px; margin-bottom: 50px; }}
    .split-item {{ padding-bottom: 30px; border-bottom: 1px solid #eee; }}
    .split-top {{ display: flex; align-items: center; gap: 15px; margin-bottom: 10px; }}
    .split-item h4 {{ font-family: 'Playfair Display', serif; font-size: 1.4rem; color: {text}; white-space: nowrap; }}
    .split-dots {{ flex: 1; border-bottom: 2px dotted #ddd; }}
    .split-price {{ font-weight: 700; color: {primary}; font-size: 1.2rem; }}
    .split-item p {{ color: #888; font-size: 0.95rem; }}
    .view-full {{ display: inline-block; padding: 16px 40px; background: {primary}; color: #fff; text-decoration: none; border-radius: 50px; font-weight: 600; align-self: flex-start; transition: 0.3s; }}
    .view-full:hover {{ transform: translateY(-3px); box-shadow: 0 10px 30px {primary}40; }}
    @media (max-width: 968px) {{ .menu-split {{ grid-template-columns: 1fr; }} .split-image {{ height: 50vh; }} }}
    </style>
    '''
