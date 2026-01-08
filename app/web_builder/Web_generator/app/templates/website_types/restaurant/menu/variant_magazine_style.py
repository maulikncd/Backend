from typing import Dict, Any, List

def _normalize_item(item) -> Dict[str, Any]:
    if isinstance(item, str):
        return {"name": item, "category": "Menu", "price": "", "description": "", "image": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=400"}
    elif isinstance(item, dict):
        return item
    return {"name": str(item), "category": "Menu", "price": "", "description": "", "image": ""}

def _get_default_menu() -> List[Dict]:
    return [
        {"name": "Grilled Octopus", "price": "$34", "description": "Charred tentacles, olive tapenade", "image": "https://images.unsplash.com/photo-1519708227418-c8fd9a32b7a2?w=400"},
        {"name": "Lamb Rack", "price": "$52", "description": "Herb crusted, mint pesto", "image": "https://images.unsplash.com/photo-1544025162-d76694265947?w=400"},
        {"name": "Tuna Tataki", "price": "$28", "description": "Seared rare, ponzu sauce", "image": "https://images.unsplash.com/photo-1579871494447-9811cf80d66c?w=400"},
    ]

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Magazine Style - Editorial magazine look"""
    title = props.get("sectionTitle", props.get("title", "The Menu"))
    subtitle = props.get("subtitle", "Our carefully curated selection")
    raw_items = props.get("menuItems", props.get("items", _get_default_menu()))
    menu_items = [_normalize_item(item) for item in raw_items]
    
    primary = colors.get("primary", "#2D3436")
    bg = colors.get("background", "#F8F6F3")
    text = colors.get("text", "#1A1A1A")
    
    items_html = ""
    for i, item in enumerate(menu_items[:4]):
        reverse = "reverse" if i % 2 == 1 else ""
        items_html += f'''
        <div class="magazine-item {reverse}">
            <div class="item-image">
                <img src="{item.get('image', 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=600')}" alt="{item.get('name', 'Dish')}">
                <span class="item-number">0{i+1}</span>
            </div>
            <div class="item-content">
                <span class="price-tag">{item.get('price', '$0')}</span>
                <h3>{item.get('name', 'Dish')}</h3>
                <p>{item.get('description', '')}</p>
            </div>
        </div>
        '''
    
    return f'''
    <section class="menu-magazine" id="menu">
        <div class="magazine-container">
            <div class="magazine-header">
                <div class="header-accent"></div>
                <span class="issue">Issue 12 • Menu</span>
                <h2>{title}</h2>
                <p>{subtitle}</p>
            </div>
            
            <div class="magazine-items">
                {items_html}
            </div>
        </div>
    </section>
    
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Bodoni+Moda:opsz,wght@6..96,400;6..96,600&family=Source+Sans+Pro:wght@300;400&display=swap');
    
    .menu-magazine {{
        padding: 120px 60px;
        background: {bg};
    }}
    .magazine-container {{
        max-width: 1100px;
        margin: 0 auto;
    }}
    .magazine-header {{
        margin-bottom: 80px;
    }}
    .header-accent {{
        width: 60px;
        height: 4px;
        background: {primary};
        margin-bottom: 30px;
    }}
    .magazine-header .issue {{
        font-size: 0.85rem;
        color: {text}60;
        letter-spacing: 3px;
        text-transform: uppercase;
        display: block;
        margin-bottom: 20px;
    }}
    .magazine-header h2 {{
        font-family: 'Bodoni Moda', serif;
        font-size: clamp(4rem, 10vw, 7rem);
        color: {text};
        line-height: 1;
        margin-bottom: 20px;
    }}
    .magazine-header p {{
        font-family: 'Source Sans Pro', sans-serif;
        font-size: 1.2rem;
        color: {text}70;
        max-width: 500px;
    }}
    .magazine-items {{
        display: flex;
        flex-direction: column;
        gap: 100px;
    }}
    .magazine-item {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 80px;
        align-items: center;
    }}
    .magazine-item.reverse {{
        direction: rtl;
    }}
    .magazine-item.reverse > * {{
        direction: ltr;
    }}
    .item-image {{
        position: relative;
    }}
    .item-image img {{
        width: 100%;
        height: 450px;
        object-fit: cover;
    }}
    .item-number {{
        position: absolute;
        top: 30px;
        left: 30px;
        font-family: 'Bodoni Moda', serif;
        font-size: 4rem;
        color: white;
        opacity: 0.8;
    }}
    .item-content {{}}
    .price-tag {{
        display: inline-block;
        padding: 8px 20px;
        background: {primary};
        color: white;
        font-size: 0.9rem;
        border-radius: 50px;
        margin-bottom: 25px;
    }}
    .item-content h3 {{
        font-family: 'Bodoni Moda', serif;
        font-size: 2.5rem;
        color: {text};
        margin-bottom: 20px;
    }}
    .item-content p {{
        font-family: 'Source Sans Pro', sans-serif;
        font-size: 1.1rem;
        color: {text}70;
        line-height: 1.8;
    }}
    @media (max-width: 968px) {{
        .menu-magazine {{ padding: 80px 30px; }}
        .magazine-item {{ grid-template-columns: 1fr; gap: 30px; }}
        .magazine-item.reverse {{ direction: ltr; }}
        .item-image img {{ height: 300px; }}
        .magazine-items {{ gap: 60px; }}
    }}
    </style>
    '''
