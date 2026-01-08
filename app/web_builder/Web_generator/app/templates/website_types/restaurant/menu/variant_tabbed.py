from typing import Dict, Any, List

def _normalize_item(item) -> Dict[str, Any]:
    if isinstance(item, str):
        return {"name": item, "category": "Menu", "price": "", "description": ""}
    elif isinstance(item, dict):
        return item
    return {"name": str(item), "category": "Menu", "price": "", "description": ""}

def _get_default_menu() -> List[Dict]:
    return [
        {"name": "Signature Steak", "category": "Mains", "price": "$58", "description": "Dry-aged ribeye, herb butter"},
        {"name": "Seafood Tower", "category": "Starters", "price": "$75", "description": "Oysters, shrimp, lobster"},
        {"name": "Pasta Truffle", "category": "Mains", "price": "$38", "description": "Fresh tagliatelle, black truffle"},
        {"name": "Tiramisu", "category": "Desserts", "price": "$14", "description": "Classic Italian dessert"},
    ]

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Tabbed Categories - Tabs for different menu categories"""
    title = props.get("sectionTitle", props.get("title", "Menu"))
    subtitle = props.get("subtitle", "Select a category")
    raw_items = props.get("menuItems", props.get("items", _get_default_menu()))
    menu_items = [_normalize_item(item) for item in raw_items]
    
    primary = colors.get("primary", "#1E3A5F")
    bg = colors.get("background", "#FAFAFA")
    text = colors.get("text", "#1A1A1A")
    
    # Group by category
    categories = {}
    for item in menu_items:
        cat = item.get("category", "Menu")
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(item)
    
    if not categories:
        categories = {"Menu": menu_items}
    
    # Build tabs
    tabs_html = ""
    panels_html = ""
    for i, (cat, items) in enumerate(categories.items()):
        active = "active" if i == 0 else ""
        tabs_html += f'<button class="tab-btn {active}" data-tab="{cat}">{cat}</button>'
        
        items_html = ""
        for item in items:
            items_html += f'''
            <div class="menu-item">
                <div class="item-info">
                    <h4>{item.get('name', 'Dish')}</h4>
                    <p>{item.get('description', '')}</p>
                </div>
                <div class="item-price">{item.get('price', '$0')}</div>
            </div>
            '''
        
        panels_html += f'<div class="tab-panel {active}" data-tab="{cat}">{items_html}</div>'
    
    return f'''
    <section class="menu-tabbed" id="menu">
        <div class="menu-container">
            <div class="menu-header">
                <h2>{title}</h2>
                <p>{subtitle}</p>
            </div>
            
            <div class="tabs-wrapper">
                <div class="tabs-nav">
                    {tabs_html}
                </div>
                
                <div class="tabs-content">
                    {panels_html}
                </div>
            </div>
        </div>
    </section>
    
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Libre+Baskerville:wght@400;700&family=Source+Sans+Pro:wght@400;600&display=swap');
    
    .menu-tabbed {{
        padding: 120px 60px;
        background: {bg};
    }}
    .menu-container {{
        max-width: 900px;
        margin: 0 auto;
    }}
    .menu-header {{
        text-align: center;
        margin-bottom: 60px;
    }}
    .menu-header h2 {{
        font-family: 'Libre Baskerville', serif;
        font-size: clamp(2.5rem, 5vw, 4rem);
        color: {text};
        margin-bottom: 15px;
    }}
    .menu-header p {{
        color: {text}70;
        font-size: 1.1rem;
    }}
    .tabs-nav {{
        display: flex;
        justify-content: center;
        gap: 10px;
        margin-bottom: 50px;
        flex-wrap: wrap;
    }}
    .tab-btn {{
        padding: 14px 30px;
        background: transparent;
        border: 2px solid {text}20;
        color: {text}80;
        font-size: 0.9rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s;
        border-radius: 50px;
    }}
    .tab-btn:hover {{
        border-color: {primary};
        color: {primary};
    }}
    .tab-btn.active {{
        background: {primary};
        border-color: {primary};
        color: white;
    }}
    .tab-panel {{
        display: none;
    }}
    .tab-panel.active {{
        display: block;
    }}
    .menu-item {{
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        padding: 25px 0;
        border-bottom: 1px solid {text}10;
    }}
    .menu-item:last-child {{
        border-bottom: none;
    }}
    .item-info h4 {{
        font-family: 'Libre Baskerville', serif;
        font-size: 1.3rem;
        color: {text};
        margin-bottom: 8px;
    }}
    .item-info p {{
        color: {text}70;
        font-size: 0.95rem;
    }}
    .item-price {{
        font-size: 1.3rem;
        font-weight: 600;
        color: {primary};
        white-space: nowrap;
        margin-left: 20px;
    }}
    @media (max-width: 768px) {{
        .menu-tabbed {{ padding: 80px 30px; }}
    }}
    </style>
    
    <script>
    document.querySelectorAll('.tab-btn').forEach(btn => {{
        btn.addEventListener('click', () => {{
            document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
            document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
            btn.classList.add('active');
            document.querySelector(`.tab-panel[data-tab="${{btn.dataset.tab}}"]`).classList.add('active');
        }});
    }});
    </script>
    '''
