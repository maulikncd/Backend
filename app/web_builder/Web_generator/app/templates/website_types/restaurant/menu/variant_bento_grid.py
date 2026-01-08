from typing import Dict, Any, List

def _normalize_item(item) -> Dict[str, Any]:
    if isinstance(item, str):
        return {"name": item, "category": "Menu", "price": "", "description": "", "image": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=400"}
    elif isinstance(item, dict):
        return item
    return {"name": str(item), "category": "Menu", "price": "", "description": "", "image": ""}

def _get_default_menu() -> List[Dict]:
    return [
        {"name": "Prime Ribeye", "price": "$58", "description": "28-day aged, herb butter", "image": "https://images.unsplash.com/photo-1544025162-d76694265947?w=400"},
        {"name": "King Crab", "price": "$85", "description": "Grilled legs, drawn butter", "image": "https://images.unsplash.com/photo-1553247407-23251ce81f59?w=400"},
        {"name": "Wagyu Slider", "price": "$45", "description": "A5 wagyu trio, truffle aioli", "image": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=400"},
        {"name": "Burrata", "price": "$22", "description": "Fresh, heirloom tomatoes, basil", "image": "https://images.unsplash.com/photo-1608897013039-887f21d8c804?w=400"},
    ]

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Bento Grid - Asymmetric bento-box style layout"""
    title = props.get("sectionTitle", props.get("title", "Menu"))
    subtitle = props.get("subtitle", "Today's selections")
    raw_items = props.get("menuItems", props.get("items", _get_default_menu()))
    menu_items = [_normalize_item(item) for item in raw_items]
    
    primary = colors.get("primary", "#E63946")
    bg = colors.get("background", "#FFFFFF")
    text = colors.get("text", "#1A1A1A")
    
    return f'''
    <section class="menu-bento" id="menu">
        <div class="bento-container">
            <div class="bento-header">
                <span class="label">Menu</span>
                <h2>{title}</h2>
            </div>
            
            <div class="bento-grid">
                <div class="bento-item large">
                    <img src="{menu_items[0].get('image', '')}" alt="">
                    <div class="item-overlay">
                        <span class="price">{menu_items[0].get('price', '$0')}</span>
                        <h3>{menu_items[0].get('name', 'Dish')}</h3>
                        <p>{menu_items[0].get('description', '')}</p>
                    </div>
                </div>
                
                <div class="bento-item">
                    <img src="{menu_items[1].get('image', '') if len(menu_items) > 1 else ''}" alt="">
                    <div class="item-overlay">
                        <span class="price">{menu_items[1].get('price', '$0') if len(menu_items) > 1 else ''}</span>
                        <h3>{menu_items[1].get('name', 'Dish') if len(menu_items) > 1 else ''}</h3>
                    </div>
                </div>
                
                <div class="bento-item">
                    <img src="{menu_items[2].get('image', '') if len(menu_items) > 2 else ''}" alt="">
                    <div class="item-overlay">
                        <span class="price">{menu_items[2].get('price', '$0') if len(menu_items) > 2 else ''}</span>
                        <h3>{menu_items[2].get('name', 'Dish') if len(menu_items) > 2 else ''}</h3>
                    </div>
                </div>
                
                <div class="bento-item wide">
                    <img src="{menu_items[3].get('image', '') if len(menu_items) > 3 else ''}" alt="">
                    <div class="item-overlay">
                        <span class="price">{menu_items[3].get('price', '$0') if len(menu_items) > 3 else ''}</span>
                        <h3>{menu_items[3].get('name', 'Dish') if len(menu_items) > 3 else ''}</h3>
                        <p>{menu_items[3].get('description', '') if len(menu_items) > 3 else ''}</p>
                    </div>
                </div>
            </div>
            
            <div class="bento-footer">
                <a href="#" class="btn-view">View Complete Menu</a>
            </div>
        </div>
    </section>
    
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');
    
    .menu-bento {{
        padding: 120px 60px;
        background: {bg};
    }}
    .bento-container {{
        max-width: 1200px;
        margin: 0 auto;
    }}
    .bento-header {{
        text-align: center;
        margin-bottom: 60px;
    }}
    .bento-header .label {{
        color: {primary};
        font-size: 0.85rem;
        letter-spacing: 3px;
        text-transform: uppercase;
        display: block;
        margin-bottom: 15px;
    }}
    .bento-header h2 {{
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-size: clamp(2.5rem, 5vw, 4rem);
        font-weight: 700;
        color: {text};
    }}
    .bento-grid {{
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        grid-template-rows: repeat(2, 300px);
        gap: 20px;
    }}
    .bento-item {{
        position: relative;
        overflow: hidden;
        border-radius: 20px;
    }}
    .bento-item img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.5s;
    }}
    .bento-item:hover img {{
        transform: scale(1.1);
    }}
    .bento-item.large {{
        grid-row: span 2;
    }}
    .bento-item.wide {{
        grid-column: span 2;
    }}
    .item-overlay {{
        position: absolute;
        inset: 0;
        background: linear-gradient(to top, rgba(0,0,0,0.8), transparent 60%);
        padding: 30px;
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
        color: white;
    }}
    .item-overlay .price {{
        display: inline-block;
        padding: 6px 15px;
        background: {primary};
        border-radius: 50px;
        font-size: 0.85rem;
        font-weight: 600;
        margin-bottom: 10px;
        align-self: flex-start;
    }}
    .item-overlay h3 {{
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 8px;
    }}
    .item-overlay p {{
        font-size: 0.9rem;
        opacity: 0.8;
    }}
    .bento-footer {{
        text-align: center;
        margin-top: 50px;
    }}
    .btn-view {{
        display: inline-block;
        padding: 18px 45px;
        background: {primary};
        color: white;
        text-decoration: none;
        border-radius: 12px;
        font-weight: 600;
        transition: all 0.3s;
    }}
    .btn-view:hover {{
        transform: translateY(-3px);
        box-shadow: 0 15px 40px {primary}40;
    }}
    @media (max-width: 968px) {{
        .bento-grid {{ grid-template-columns: 1fr 1fr; }}
        .bento-item.large {{ grid-row: auto; }}
    }}
    @media (max-width: 600px) {{
        .menu-bento {{ padding: 80px 30px; }}
        .bento-grid {{ grid-template-columns: 1fr; grid-template-rows: auto; }}
        .bento-item {{ height: 300px; }}
        .bento-item.wide {{ grid-column: auto; }}
    }}
    </style>
    '''
