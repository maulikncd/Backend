from typing import Dict, Any, List

def _normalize_item(item) -> Dict[str, Any]:
    if isinstance(item, str):
        return {"name": item, "category": "Menu", "price": "", "description": ""}
    elif isinstance(item, dict):
        return item
    return {"name": str(item), "category": "Menu", "price": "", "description": ""}

def _get_default_menu() -> List[Dict]:
    return [
        {"name": "Beef Wellington", "category": "Mains", "price": "$72", "description": "Tenderloin wrapped in puff pastry"},
        {"name": "Pan-Seared Foie Gras", "category": "Starters", "price": "$38", "description": "Apple compote, brioche"},
        {"name": "Mediterranean Sea Bass", "category": "Mains", "price": "$48", "description": "Lemon herb crust, vegetables"},
    ]

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Dark Luxury - Dark premium style"""
    title = props.get("sectionTitle", props.get("title", "The Menu"))
    subtitle = props.get("subtitle", "Culinary Excellence")
    raw_items = props.get("menuItems", props.get("items", _get_default_menu()))
    menu_items = [_normalize_item(item) for item in raw_items]
    
    primary = colors.get("primary", "#C9A962")
    bg = colors.get("background", "#0A0A0A")
    text = colors.get("text", "#FFFFFF")
    
    # Group by category
    categories = {}
    for item in menu_items:
        cat = item.get("category", "Menu")
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(item)
    
    sections_html = ""
    for cat, items in categories.items():
        items_html = ""
        for item in items:
            items_html += f'''
            <div class="luxury-item">
                <div class="item-top">
                    <h4>{item.get('name', 'Dish')}</h4>
                    <div class="item-line"></div>
                    <span class="item-price">{item.get('price', '$0')}</span>
                </div>
                <p>{item.get('description', '')}</p>
            </div>
            '''
        sections_html += f'''
        <div class="menu-category">
            <h3 class="category-title">{cat}</h3>
            <div class="category-items">{items_html}</div>
        </div>
        '''
    
    return f'''
    <section class="menu-dark-luxury" id="menu">
        <div class="luxury-bg">
            <div class="bg-pattern"></div>
        </div>
        
        <div class="menu-container">
            <div class="menu-header">
                <div class="decorative-line"></div>
                <span class="label">Curated Selection</span>
                <h2>{title}</h2>
                <p>{subtitle}</p>
                <div class="decorative-line"></div>
            </div>
            
            <div class="menu-sections">
                {sections_html}
            </div>
        </div>
    </section>
    
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600&family=Montserrat:wght@300;400&display=swap');
    
    .menu-dark-luxury {{
        position: relative;
        padding: 150px 60px;
        background: {bg};
        overflow: hidden;
    }}
    .luxury-bg {{
        position: absolute;
        inset: 0;
        opacity: 0.03;
    }}
    .bg-pattern {{
        width: 100%;
        height: 100%;
        background-image: repeating-linear-gradient(
            45deg,
            transparent,
            transparent 50px,
            {primary} 50px,
            {primary} 51px
        );
    }}
    .menu-container {{
        position: relative;
        max-width: 1000px;
        margin: 0 auto;
    }}
    .menu-header {{
        text-align: center;
        margin-bottom: 80px;
    }}
    .decorative-line {{
        width: 150px;
        height: 1px;
        background: linear-gradient(90deg, transparent, {primary}, transparent);
        margin: 20px auto;
    }}
    .menu-header .label {{
        color: {primary};
        font-size: 0.85rem;
        letter-spacing: 5px;
        text-transform: uppercase;
        display: block;
        margin-bottom: 20px;
    }}
    .menu-header h2 {{
        font-family: 'Cormorant Garamond', serif;
        font-size: clamp(3rem, 8vw, 5rem);
        color: {text};
        margin-bottom: 15px;
        font-weight: 400;
    }}
    .menu-header p {{
        font-family: 'Montserrat', sans-serif;
        color: {text}60;
        font-size: 1rem;
        letter-spacing: 2px;
    }}
    .menu-sections {{
        display: flex;
        flex-direction: column;
        gap: 60px;
    }}
    .menu-category {{}}
    .category-title {{
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.8rem;
        color: {primary};
        margin-bottom: 30px;
        padding-bottom: 15px;
        border-bottom: 1px solid {text}15;
    }}
    .category-items {{
        display: flex;
        flex-direction: column;
        gap: 30px;
    }}
    .luxury-item {{}}
    .item-top {{
        display: flex;
        align-items: center;
        gap: 20px;
        margin-bottom: 10px;
    }}
    .item-top h4 {{
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.4rem;
        color: {text};
        white-space: nowrap;
    }}
    .item-line {{
        flex: 1;
        height: 1px;
        background: {text}20;
    }}
    .item-price {{
        font-size: 1.2rem;
        color: {primary};
        font-weight: 500;
    }}
    .luxury-item p {{
        font-family: 'Montserrat', sans-serif;
        color: {text}60;
        font-size: 0.9rem;
        padding-left: 10px;
    }}
    @media (max-width: 768px) {{
        .menu-dark-luxury {{ padding: 100px 30px; }}
    }}
    </style>
    '''
