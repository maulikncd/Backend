from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Luxury Dark Menu - Premium dark theme with gold accents"""
    title = props.get("sectionTitle", props.get("title", "The Menu"))
    subtitle = props.get("sectionSubtitle", "Curated with passion")
    raw_items = props.get("items", [])
    
    primary = colors.get("primary", "#C8A97E")
    
    items = []
    for item in raw_items:
        items.append({
            "name": item.get("name", "Item"),
            "desc": item.get("description", "")[:80],
            "price": item.get("price", "$0")
        })
    
    if not items:
        items = [
            {"name": "Signature Espresso", "desc": "Single origin arabica, roasted to perfection", "price": "$4.50"},
            {"name": "Golden Latte", "desc": "Turmeric, ginger, and oat milk", "price": "$6.00"},
            {"name": "Pain au Chocolat", "desc": "Flaky pastry with Belgian chocolate", "price": "$5.50"},
            {"name": "Smoked Salmon Benedict", "desc": "Poached eggs, hollandaise, artisan bread", "price": "$18.00"},
            {"name": "Matcha Ceremony", "desc": "Ceremonial grade Japanese matcha", "price": "$7.00"},
            {"name": "French Toast", "desc": "Brioche, berries, maple syrup", "price": "$14.00"}
        ]
    
    items_html = ""
    for item in items[:8]:
        items_html += f'''
        <div class="dark-menu-item">
            <div class="item-top">
                <h4>{item["name"]}</h4>
                <span class="item-price">{item["price"]}</span>
            </div>
            <p>{item["desc"]}</p>
        </div>
        '''
    
    return f'''
    <section class="menu-dark-luxury" id="menu">
        <div class="dark-pattern"></div>
        <div class="menu-content">
            <div class="menu-intro">
                <span class="intro-line"></span>
                <span class="intro-text">Menu</span>
                <span class="intro-line"></span>
            </div>
            <h2>{title}</h2>
            <p class="menu-subtitle">{subtitle}</p>
            <div class="menu-columns">
                {items_html}
            </div>
        </div>
    </section>
    
    <style>
    .menu-dark-luxury {{ padding: 120px 24px; background: #0D0D0D; position: relative; overflow: hidden; }}
    .dark-pattern {{ position: absolute; inset: 0; background-image: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23C8A97E' fill-opacity='0.05'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E"); }}
    .menu-content {{ position: relative; z-index: 2; max-width: 1000px; margin: 0 auto; text-align: center; color: #fff; }}
    .menu-intro {{ display: flex; align-items: center; justify-content: center; gap: 20px; margin-bottom: 20px; }}
    .intro-line {{ width: 60px; height: 1px; background: {primary}; }}
    .intro-text {{ color: {primary}; text-transform: uppercase; letter-spacing: 4px; font-size: 0.9rem; }}
    .menu-dark-luxury h2 {{ font-family: 'Playfair Display', serif; font-size: 4rem; margin-bottom: 16px; }}
    .menu-subtitle {{ color: rgba(255,255,255,0.6); font-size: 1.1rem; margin-bottom: 60px; }}
    .menu-columns {{ display: grid; grid-template-columns: repeat(2, 1fr); gap: 40px; text-align: left; }}
    .dark-menu-item {{ padding: 30px; border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; transition: 0.3s; }}
    .dark-menu-item:hover {{ border-color: {primary}; background: rgba(200,169,126,0.05); }}
    .item-top {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; }}
    .dark-menu-item h4 {{ font-family: 'Playfair Display', serif; font-size: 1.4rem; }}
    .item-price {{ color: {primary}; font-weight: 700; font-size: 1.2rem; }}
    .dark-menu-item p {{ color: rgba(255,255,255,0.5); font-size: 0.95rem; line-height: 1.6; }}
    @media (max-width: 768px) {{ .menu-columns {{ grid-template-columns: 1fr; }} }}
    </style>
    '''
