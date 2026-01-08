from typing import Dict, Any, List

def _normalize_item(item) -> Dict[str, Any]:
    if isinstance(item, str):
        return {"name": item, "category": "Menu", "price": "", "description": ""}
    elif isinstance(item, dict):
        return item
    return {"name": str(item), "category": "Menu", "price": "", "description": ""}

def _get_default_menu() -> List[Dict]:
    return [
        {"name": "Filet Mignon", "category": "Mains", "price": "$62", "description": "8oz prime cut, herb crust"},
        {"name": "Lobster Thermidor", "category": "Mains", "price": "$78", "description": "Classic French preparation"},
        {"name": "Oysters Rockefeller", "category": "Starters", "price": "$28", "description": "Six pieces, spinach, gratin"},
        {"name": "Crème Brûlée", "category": "Desserts", "price": "$16", "description": "Vanilla custard, caramelized sugar"},
    ]

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Minimal Lines - Ultra minimal with dotted lines"""
    title = props.get("sectionTitle", props.get("title", "The Menu"))
    subtitle = props.get("subtitle", "Seasonal favorites")
    raw_items = props.get("menuItems", props.get("items", _get_default_menu()))
    menu_items = [_normalize_item(item) for item in raw_items]
    
    primary = colors.get("primary", "#2D3436")
    bg = colors.get("background", "#FFFFFF")
    text = colors.get("text", "#1A1A1A")
    
    items_html = ""
    for item in menu_items[:10]:
        items_html += f'''
        <div class="minimal-item">
            <div class="item-left">
                <h4 class="item-name">{item.get('name', 'Dish')}</h4>
                <span class="item-dots"></span>
                <span class="item-price">{item.get('price', '$0')}</span>
            </div>
            <p class="item-desc">{item.get('description', '')}</p>
        </div>
        '''
    
    return f'''
    <section class="menu-minimal-lines" id="menu">
        <div class="menu-container">
            <div class="menu-header">
                <h2>{title}</h2>
                <div class="header-line"></div>
                <p>{subtitle}</p>
            </div>
            
            <div class="menu-list">
                {items_html}
            </div>
            
            <div class="menu-note">
                <p>* All prices are subject to 10% service charge</p>
            </div>
        </div>
    </section>
    
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant:wght@400;500&family=Karla:wght@400&display=swap');
    
    .menu-minimal-lines {{
        padding: 150px 60px;
        background: {bg};
    }}
    .menu-container {{
        max-width: 800px;
        margin: 0 auto;
    }}
    .menu-header {{
        text-align: center;
        margin-bottom: 80px;
    }}
    .menu-header h2 {{
        font-family: 'Cormorant', serif;
        font-size: 4rem;
        font-weight: 400;
        color: {text};
        margin-bottom: 20px;
    }}
    .header-line {{
        width: 80px;
        height: 1px;
        background: {text};
        margin: 0 auto 20px;
    }}
    .menu-header p {{
        color: {text}70;
        font-size: 1rem;
        letter-spacing: 2px;
        text-transform: uppercase;
    }}
    .menu-list {{
        display: flex;
        flex-direction: column;
        gap: 35px;
    }}
    .minimal-item {{
        display: flex;
        flex-direction: column;
        gap: 8px;
    }}
    .item-left {{
        display: flex;
        align-items: baseline;
        gap: 15px;
    }}
    .item-name {{
        font-family: 'Cormorant', serif;
        font-size: 1.5rem;
        font-weight: 500;
        color: {text};
        white-space: nowrap;
    }}
    .item-dots {{
        flex: 1;
        border-bottom: 2px dotted {text}30;
        min-width: 50px;
    }}
    .item-price {{
        font-size: 1.2rem;
        font-weight: 500;
        color: {primary};
        white-space: nowrap;
    }}
    .item-desc {{
        font-family: 'Karla', sans-serif;
        font-size: 0.95rem;
        color: {text}60;
        padding-left: 20px;
    }}
    .menu-note {{
        text-align: center;
        margin-top: 60px;
        padding-top: 40px;
        border-top: 1px solid {text}10;
    }}
    .menu-note p {{
        color: {text}50;
        font-size: 0.85rem;
        font-style: italic;
    }}
    @media (max-width: 768px) {{
        .menu-minimal-lines {{ padding: 100px 30px; }}
        .menu-header h2 {{ font-size: 3rem; }}
    }}
    </style>
    '''
