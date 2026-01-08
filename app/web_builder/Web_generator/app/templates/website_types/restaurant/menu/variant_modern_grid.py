from typing import Dict, Any, List

def _normalize_item(item) -> Dict[str, Any]:
    """Normalize menu item to dict format"""
    if isinstance(item, str):
        return {"name": item, "category": "Menu", "price": "", "description": ""}
    elif isinstance(item, dict):
        return item
    return {"name": str(item), "category": "Menu", "price": "", "description": ""}

def _get_default_menu() -> List[Dict]:
    return [
        {"name": "Wagyu Beef", "category": "Mains", "price": "$68", "description": "Prime wagyu, truffle butter"},
        {"name": "Salmon", "category": "Mains", "price": "$42", "description": "Atlantic salmon, lemon herb"},
        {"name": "Caesar Salad", "category": "Starters", "price": "$18", "description": "Romaine, parmesan, croutons"},
        {"name": "Chocolate Fondant", "category": "Desserts", "price": "$16", "description": "Warm chocolate, vanilla ice cream"},
    ]

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Modern Grid - Clean grid layout with hover effects"""
    title = props.get("sectionTitle", props.get("title", "Our Menu"))
    subtitle = props.get("subtitle", "Carefully crafted dishes")
    raw_items = props.get("menuItems", props.get("items", _get_default_menu()))
    menu_items = [_normalize_item(item) for item in raw_items]
    
    primary = colors.get("primary", "#E63946")
    bg = colors.get("background", "#FFFFFF")
    text = colors.get("text", "#1A1A1A")
    
    items_html = ""
    for item in menu_items[:8]:
        items_html += f'''
        <div class="menu-card">
            <div class="card-header">
                <h3 class="item-name">{item.get('name', 'Dish')}</h3>
                <span class="item-price">{item.get('price', '$0')}</span>
            </div>
            <p class="item-desc">{item.get('description', '')}</p>
            <span class="item-category">{item.get('category', 'Menu')}</span>
        </div>
        '''
    
    return f'''
    <section class="menu-grid-modern" id="menu">
        <div class="menu-container">
            <div class="menu-header">
                <span class="label">Menu</span>
                <h2>{title}</h2>
                <p>{subtitle}</p>
            </div>
            
            <div class="menu-grid">
                {items_html}
            </div>
            
            <div class="menu-footer">
                <a href="#" class="btn-menu">View Full Menu</a>
            </div>
        </div>
    </section>
    
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500&family=Inter:wght@400;500&display=swap');
    
    .menu-grid-modern {{
        padding: 120px 60px;
        background: {bg};
    }}
    .menu-container {{
        max-width: 1200px;
        margin: 0 auto;
    }}
    .menu-header {{
        text-align: center;
        margin-bottom: 70px;
    }}
    .menu-header .label {{
        color: {primary};
        font-size: 0.85rem;
        letter-spacing: 3px;
        text-transform: uppercase;
        display: block;
        margin-bottom: 15px;
    }}
    .menu-header h2 {{
        font-family: 'Playfair Display', serif;
        font-size: clamp(2.5rem, 5vw, 4rem);
        color: {text};
        margin-bottom: 15px;
    }}
    .menu-header p {{
        color: {text}80;
        font-size: 1.1rem;
    }}
    .menu-grid {{
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 30px;
    }}
    .menu-card {{
        background: {bg};
        padding: 35px;
        border-radius: 16px;
        border: 1px solid {text}10;
        transition: all 0.3s;
    }}
    .menu-card:hover {{
        transform: translateY(-5px);
        box-shadow: 0 20px 50px rgba(0,0,0,0.08);
        border-color: {primary}30;
    }}
    .card-header {{
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        margin-bottom: 12px;
    }}
    .item-name {{
        font-family: 'Playfair Display', serif;
        font-size: 1.4rem;
        color: {text};
    }}
    .item-price {{
        font-size: 1.3rem;
        font-weight: 600;
        color: {primary};
    }}
    .item-desc {{
        font-size: 0.95rem;
        color: {text}70;
        line-height: 1.6;
        margin-bottom: 15px;
    }}
    .item-category {{
        display: inline-block;
        padding: 6px 15px;
        background: {primary}15;
        color: {primary};
        font-size: 0.75rem;
        border-radius: 50px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }}
    .menu-footer {{
        text-align: center;
        margin-top: 60px;
    }}
    .btn-menu {{
        display: inline-block;
        padding: 18px 50px;
        background: {primary};
        color: white;
        text-decoration: none;
        border-radius: 50px;
        font-weight: 500;
        transition: all 0.3s;
    }}
    .btn-menu:hover {{
        transform: translateY(-3px);
        box-shadow: 0 15px 40px {primary}40;
    }}
    @media (max-width: 768px) {{
        .menu-grid-modern {{ padding: 80px 30px; }}
        .menu-grid {{ grid-template-columns: 1fr; }}
    }}
    </style>
    '''
