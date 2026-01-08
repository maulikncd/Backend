from typing import Dict, Any, List

def _normalize_item(item) -> Dict[str, Any]:
    if isinstance(item, str):
        return {"name": item, "category": "Menu", "price": "", "description": "", "image": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=400"}
    elif isinstance(item, dict):
        return item
    return {"name": str(item), "category": "Menu", "price": "", "description": "", "image": ""}

def _get_default_menu() -> List[Dict]:
    return [
        {"name": "Wagyu Tartare", "price": "$32", "description": "Hand-cut wagyu, truffle oil", "image": "https://images.unsplash.com/photo-1588168333986-5078d3ae3976?w=400"},
        {"name": "Lobster Bisque", "price": "$24", "description": "Creamy, cognac infused", "image": "https://images.unsplash.com/photo-1476124369491-e7addf5db371?w=400"},
        {"name": "Duck Magret", "price": "$48", "description": "Cherry reduction, roasted vegetables", "image": "https://images.unsplash.com/photo-1432139555190-58524dae6a55?w=400"},
        {"name": "Chocolate Soufflé", "price": "$18", "description": "Dark chocolate, crème anglaise", "image": "https://images.unsplash.com/photo-1606313564200-e75d5e30476c?w=400"},
    ]

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Horizontal Scroll - Horizontally scrolling cards"""
    title = props.get("sectionTitle", props.get("title", "Featured Dishes"))
    subtitle = props.get("subtitle", "Chef's recommendations")
    raw_items = props.get("menuItems", props.get("items", _get_default_menu()))
    menu_items = [_normalize_item(item) for item in raw_items]
    
    primary = colors.get("primary", "#D4AF37")
    bg = colors.get("background", "#0F0F0F")
    text = colors.get("text", "#FFFFFF")
    
    items_html = ""
    for item in menu_items[:8]:
        items_html += f'''
        <div class="scroll-card">
            <div class="card-image">
                <img src="{item.get('image', 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=400')}" alt="{item.get('name', 'Dish')}">
            </div>
            <div class="card-info">
                <h4>{item.get('name', 'Dish')}</h4>
                <p>{item.get('description', '')}</p>
                <span class="price">{item.get('price', '$0')}</span>
            </div>
        </div>
        '''
    
    return f'''
    <section class="menu-horizontal" id="menu">
        <div class="menu-header">
            <div class="header-content">
                <span class="label">Menu</span>
                <h2>{title}</h2>
                <p>{subtitle}</p>
            </div>
            <div class="scroll-hint">
                <span>Scroll →</span>
            </div>
        </div>
        
        <div class="scroll-container">
            <div class="scroll-track">
                {items_html}
            </div>
        </div>
    </section>
    
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500&family=Lato:wght@400&display=swap');
    
    .menu-horizontal {{
        padding: 120px 0;
        background: {bg};
        overflow: hidden;
    }}
    .menu-header {{
        display: flex;
        justify-content: space-between;
        align-items: flex-end;
        padding: 0 60px;
        margin-bottom: 60px;
    }}
    .header-content .label {{
        color: {primary};
        font-size: 0.85rem;
        letter-spacing: 4px;
        text-transform: uppercase;
        display: block;
        margin-bottom: 15px;
    }}
    .header-content h2 {{
        font-family: 'Playfair Display', serif;
        font-size: clamp(2.5rem, 5vw, 4rem);
        color: {text};
        margin-bottom: 10px;
    }}
    .header-content p {{
        color: {text}70;
        font-size: 1.1rem;
    }}
    .scroll-hint {{
        color: {text}50;
        font-size: 0.9rem;
        letter-spacing: 2px;
    }}
    .scroll-container {{
        overflow-x: auto;
        scrollbar-width: none;
        -ms-overflow-style: none;
        padding: 0 60px;
    }}
    .scroll-container::-webkit-scrollbar {{
        display: none;
    }}
    .scroll-track {{
        display: flex;
        gap: 30px;
        padding-bottom: 20px;
    }}
    .scroll-card {{
        flex: 0 0 350px;
        background: rgba(255,255,255,0.03);
        border-radius: 20px;
        overflow: hidden;
        transition: all 0.3s;
    }}
    .scroll-card:hover {{
        transform: translateY(-10px);
    }}
    .card-image {{
        height: 250px;
        overflow: hidden;
    }}
    .card-image img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.4s;
    }}
    .scroll-card:hover .card-image img {{
        transform: scale(1.05);
    }}
    .card-info {{
        padding: 25px;
    }}
    .card-info h4 {{
        font-family: 'Playfair Display', serif;
        font-size: 1.4rem;
        color: {text};
        margin-bottom: 10px;
    }}
    .card-info p {{
        color: {text}70;
        font-size: 0.9rem;
        margin-bottom: 15px;
    }}
    .card-info .price {{
        font-size: 1.3rem;
        font-weight: 600;
        color: {primary};
    }}
    @media (max-width: 768px) {{
        .menu-header {{ flex-direction: column; align-items: flex-start; gap: 20px; padding: 0 30px; }}
        .scroll-container {{ padding: 0 30px; }}
        .scroll-card {{ flex: 0 0 280px; }}
    }}
    </style>
    '''
