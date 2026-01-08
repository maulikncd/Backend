from typing import Dict, Any, List

def _normalize_item(item) -> Dict[str, Any]:
    """Normalize menu item to dict format - handles string or dict input"""
    if isinstance(item, str):
        return {"name": item, "category": "Menu", "price": "", "description": "", "image": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=400"}
    elif isinstance(item, dict):
        return item
    else:
        return {"name": str(item), "category": "Menu", "price": "", "description": "", "image": ""}

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """
    Elegant Cards - Menu with elegant card layout,
    prices and descriptions
    """
    title = props.get("sectionTitle", props.get("title", "Our Menu"))
    subtitle = props.get("subtitle", "Carefully crafted dishes using the finest ingredients")
    raw_items = props.get("menuItems", props.get("items", _get_default_menu()))
    
    # Normalize all items to dict format
    menu_items = [_normalize_item(item) for item in raw_items]
    
    primary = colors.get("primary", "#C9A962")
    bg = colors.get("background", "#0A0A0A")
    text = colors.get("text", "#FFFFFF")
    
    categories = {}
    for item in menu_items:
        cat = item.get("category", "Mains")
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(item)
    
    tabs_html = ""
    content_html = ""
    for i, (cat, items) in enumerate(categories.items()):
        active = "active" if i == 0 else ""
        tabs_html += f'<button class="menu-tab {active}" data-category="{cat}">{cat}</button>'
        
        items_html = ""
        for item in items:
            items_html += f'''
            <div class="menu-item">
                <div class="item-image">
                    <img src="{item.get('image', 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=400')}" alt="{item.get('name', 'Dish')}">
                </div>
                <div class="item-content">
                    <div class="item-header">
                        <h3 class="item-name">{item.get('name', 'Dish Name')}</h3>
                        <span class="item-price">${item.get('price', '24')}</span>
                    </div>
                    <p class="item-desc">{item.get('description', 'Delicious dish prepared with care')}</p>
                </div>
            </div>
            '''
        
        content_html += f'<div class="menu-category {active}" data-category="{cat}">{items_html}</div>'
    
    return f'''
    <section class="menu-section" id="menu">
        <div class="container">
            <div class="section-header">
                <span class="section-label">Menu</span>
                <h2 class="section-title">{title}</h2>
                <p class="section-subtitle">{subtitle}</p>
            </div>
            
            <div class="menu-tabs">
                {tabs_html}
            </div>
            
            <div class="menu-content">
                {content_html}
            </div>
            
            <div class="menu-footer">
                <a href="#" class="download-menu">View Full Menu (PDF)</a>
            </div>
        </div>
    </section>
    
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Lato:wght@400;500&display=swap');
    
    .menu-section {{
        padding: 120px 0;
        background: {bg};
    }}
    .menu-section .container {{
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 40px;
    }}
    .section-header {{
        text-align: center;
        margin-bottom: 60px;
    }}
    .section-label {{
        display: inline-block;
        font-size: 0.85rem;
        color: {primary};
        text-transform: uppercase;
        letter-spacing: 4px;
        margin-bottom: 20px;
    }}
    .section-title {{
        font-family: 'Cormorant Garamond', serif;
        font-size: clamp(2.5rem, 5vw, 4rem);
        color: {text};
        margin-bottom: 16px;
    }}
    .section-subtitle {{
        font-family: 'Lato', sans-serif;
        font-size: 1.1rem;
        color: {text}60;
    }}
    .menu-tabs {{
        display: flex;
        justify-content: center;
        gap: 12px;
        margin-bottom: 60px;
        flex-wrap: wrap;
    }}
    .menu-tab {{
        padding: 14px 32px;
        background: transparent;
        border: 1px solid {text}20;
        color: {text}80;
        font-family: 'Lato', sans-serif;
        font-size: 0.95rem;
        cursor: pointer;
        transition: all 0.3s;
    }}
    .menu-tab:hover {{
        border-color: {primary};
        color: {primary};
    }}
    .menu-tab.active {{
        background: {primary};
        border-color: {primary};
        color: #0A0A0A;
    }}
    .menu-category {{
        display: none;
        grid-template-columns: repeat(2, 1fr);
        gap: 30px;
    }}
    .menu-category.active {{
        display: grid;
    }}
    .menu-item {{
        display: flex;
        gap: 24px;
        padding: 24px;
        background: rgba(255,255,255,0.03);
        border: 1px solid rgba(255,255,255,0.05);
        border-radius: 16px;
        transition: all 0.3s;
    }}
    .menu-item:hover {{
        background: rgba(255,255,255,0.06);
        transform: translateY(-5px);
    }}
    .item-image {{
        width: 100px;
        height: 100px;
        border-radius: 12px;
        overflow: hidden;
        flex-shrink: 0;
    }}
    .item-image img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
    }}
    .item-content {{
        flex: 1;
    }}
    .item-header {{
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        margin-bottom: 10px;
    }}
    .item-name {{
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.4rem;
        color: {text};
        margin: 0;
    }}
    .item-price {{
        font-size: 1.2rem;
        font-weight: 600;
        color: {primary};
    }}
    .item-desc {{
        font-size: 0.95rem;
        color: {text}60;
        line-height: 1.6;
        margin: 0;
    }}
    .menu-footer {{
        text-align: center;
        margin-top: 60px;
    }}
    .download-menu {{
        color: {primary};
        text-decoration: none;
        font-size: 0.95rem;
        border-bottom: 1px solid {primary}50;
        padding-bottom: 4px;
        transition: all 0.3s;
    }}
    .download-menu:hover {{
        border-color: {primary};
    }}
    @media (max-width: 768px) {{
        .menu-category {{ grid-template-columns: 1fr; }}
        .menu-item {{ flex-direction: column; }}
        .item-image {{ width: 100%; height: 200px; }}
    }}
    </style>
    
    <script>
    document.querySelectorAll('.menu-tab').forEach(tab => {{
        tab.addEventListener('click', () => {{
            document.querySelectorAll('.menu-tab').forEach(t => t.classList.remove('active'));
            document.querySelectorAll('.menu-category').forEach(c => c.classList.remove('active'));
            tab.classList.add('active');
            document.querySelector(`.menu-category[data-category="${{tab.dataset.category}}"]`).classList.add('active');
        }});
    }});
    </script>
    '''


def _get_default_menu() -> List[Dict]:
    return [
        {"name": "Wagyu Beef Steak", "category": "Mains", "price": "68", "description": "Prime wagyu beef, truffle butter, seasonal vegetables", "image": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=400"},
        {"name": "Pan-Seared Salmon", "category": "Mains", "price": "42", "description": "Atlantic salmon, lemon herb sauce, asparagus", "image": "https://images.unsplash.com/photo-1467003909585-2f8a72700288?w=400"},
        {"name": "Lobster Risotto", "category": "Mains", "price": "56", "description": "Maine lobster, arborio rice, parmesan, white wine", "image": "https://images.unsplash.com/photo-1473093295043-cdd812d0e601?w=400"},
        {"name": "Caesar Salad", "category": "Starters", "price": "18", "description": "Romaine lettuce, parmesan, croutons, caesar dressing", "image": "https://images.unsplash.com/photo-1546793665-c74683f339c1?w=400"},
        {"name": "French Onion Soup", "category": "Starters", "price": "16", "description": "Caramelized onions, gruyère cheese, crusty bread", "image": "https://images.unsplash.com/photo-1476718406336-bb5a9690ee2a?w=400"},
        {"name": "Chocolate Fondant", "category": "Desserts", "price": "16", "description": "Warm chocolate cake, vanilla ice cream", "image": "https://images.unsplash.com/photo-1606313564200-e75d5e30476c?w=400"},
        {"name": "Crème Brûlée", "category": "Desserts", "price": "14", "description": "Classic vanilla custard, caramelized sugar", "image": "https://images.unsplash.com/photo-1470324161839-ce2bb6fa6bc3?w=400"},
    ]
