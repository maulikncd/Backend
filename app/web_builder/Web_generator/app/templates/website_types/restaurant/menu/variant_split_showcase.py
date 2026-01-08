from typing import Dict, Any, List

def _normalize_item(item) -> Dict[str, Any]:
    if isinstance(item, str):
        return {"name": item, "category": "Menu", "price": "", "description": ""}
    elif isinstance(item, dict):
        return item
    return {"name": str(item), "category": "Menu", "price": "", "description": ""}

def _get_default_menu() -> List[Dict]:
    return [
        {"name": "Tomahawk Steak", "category": "Signatures", "price": "$95", "description": "32oz bone-in ribeye, aged 45 days"},
        {"name": "Seared Scallops", "category": "Ocean", "price": "$42", "description": "Diver scallops, cauliflower purée"},
        {"name": "Truffle Pasta", "category": "Signatures", "price": "$48", "description": "Fresh tagliatelle, black truffle"},
        {"name": "Hamachi Crudo", "category": "Ocean", "price": "$28", "description": "Yellowtail, citrus, olive oil"},
    ]

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Split Showcase - Large image with menu list"""
    title = props.get("sectionTitle", props.get("title", "Our Menu"))
    subtitle = props.get("subtitle", "Crafted with passion")
    raw_items = props.get("menuItems", props.get("items", _get_default_menu()))
    menu_items = [_normalize_item(item) for item in raw_items]
    
    primary = colors.get("primary", "#8B7355")
    bg = colors.get("background", "#FDFAF6")
    text = colors.get("text", "#2D2013")
    
    items_html = ""
    for item in menu_items[:6]:
        items_html += f'''
        <div class="split-menu-item">
            <div class="item-header">
                <h4>{item.get('name', 'Dish')}</h4>
                <span class="dots"></span>
                <span class="price">{item.get('price', '$0')}</span>
            </div>
            <p class="item-desc">{item.get('description', '')}</p>
        </div>
        '''
    
    return f'''
    <section class="menu-split-showcase" id="menu">
        <div class="split-grid">
            <div class="split-image">
                <img src="https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=1200" alt="Food">
                <div class="image-overlay">
                    <span class="overlay-text">Farm to Table</span>
                </div>
            </div>
            
            <div class="split-content">
                <div class="content-inner">
                    <span class="label">Our Menu</span>
                    <h2>{title}</h2>
                    <p class="subtitle">{subtitle}</p>
                    
                    <div class="menu-list">
                        {items_html}
                    </div>
                    
                    <a href="#" class="btn-full-menu">View Complete Menu</a>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600&family=Lora:wght@400&display=swap');
    
    .menu-split-showcase {{
        background: {bg};
    }}
    .split-grid {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        min-height: 100vh;
    }}
    .split-image {{
        position: relative;
        overflow: hidden;
    }}
    .split-image img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
    }}
    .image-overlay {{
        position: absolute;
        inset: 0;
        background: rgba(0,0,0,0.3);
        display: flex;
        align-items: center;
        justify-content: center;
    }}
    .overlay-text {{
        color: white;
        font-family: 'Playfair Display', serif;
        font-size: 3rem;
        font-style: italic;
        text-align: center;
        padding: 30px 50px;
        border: 2px solid white;
    }}
    .split-content {{
        display: flex;
        align-items: center;
        padding: 80px;
    }}
    .content-inner {{
        max-width: 550px;
    }}
    .content-inner .label {{
        color: {primary};
        font-size: 0.85rem;
        letter-spacing: 4px;
        text-transform: uppercase;
        display: block;
        margin-bottom: 15px;
    }}
    .content-inner h2 {{
        font-family: 'Playfair Display', serif;
        font-size: clamp(2.5rem, 5vw, 4rem);
        color: {text};
        margin-bottom: 15px;
    }}
    .content-inner .subtitle {{
        color: {text}80;
        font-size: 1.1rem;
        margin-bottom: 50px;
    }}
    .menu-list {{
        display: flex;
        flex-direction: column;
        gap: 25px;
        margin-bottom: 50px;
    }}
    .split-menu-item {{}}
    .item-header {{
        display: flex;
        align-items: baseline;
        gap: 15px;
        margin-bottom: 8px;
    }}
    .item-header h4 {{
        font-family: 'Playfair Display', serif;
        font-size: 1.3rem;
        color: {text};
        white-space: nowrap;
    }}
    .item-header .dots {{
        flex: 1;
        border-bottom: 2px dotted {text}30;
    }}
    .item-header .price {{
        font-size: 1.2rem;
        font-weight: 600;
        color: {primary};
    }}
    .item-desc {{
        font-family: 'Lora', serif;
        font-size: 0.9rem;
        color: {text}70;
        padding-left: 5px;
    }}
    .btn-full-menu {{
        display: inline-block;
        padding: 18px 45px;
        background: {primary};
        color: white;
        text-decoration: none;
        border-radius: 50px;
        font-weight: 500;
        transition: all 0.3s;
    }}
    .btn-full-menu:hover {{
        transform: translateY(-3px);
        box-shadow: 0 15px 40px {primary}40;
    }}
    @media (max-width: 968px) {{
        .split-grid {{ grid-template-columns: 1fr; }}
        .split-image {{ height: 50vh; }}
        .split-content {{ padding: 60px 30px; }}
    }}
    </style>
    '''
