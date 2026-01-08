from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Tabbed Category Menu - Filterable menu with category tabs"""
    title = props.get("sectionTitle", props.get("title", "Our Menu"))
    subtitle = props.get("sectionSubtitle", "")
    raw_items = props.get("items", [])
    categories = props.get("categories", ["All", "Coffee", "Pastries", "Brunch"])
    
    primary = colors.get("primary", "#8B7355")
    text = colors.get("text", "#2D2013")
    bg = colors.get("background", "#FAF7F4")
    
    items = []
    for item in raw_items:
        items.append({
            "name": item.get("name", "Item"),
            "desc": item.get("description", "")[:60],
            "price": item.get("price", "$0"),
            "category": item.get("category", "Coffee")
        })
    
    if not items:
        items = [
            {"name": "Espresso Shot", "desc": "Bold and rich single origin", "price": "$3.50", "category": "Coffee"},
            {"name": "Vanilla Latte", "desc": "Creamy vanilla with espresso", "price": "$5.00", "category": "Coffee"},
            {"name": "Butter Croissant", "desc": "Flaky French pastry", "price": "$4.00", "category": "Pastries"},
            {"name": "Avocado Toast", "desc": "Smashed avo on sourdough", "price": "$12.00", "category": "Brunch"}
        ]
    
    # Build category tabs
    tabs_html = '<button class="tab-btn active" data-category="all">All</button>'
    seen_cats = set()
    for item in items:
        cat = item["category"]
        if cat and cat not in seen_cats:
            tabs_html += f'<button class="tab-btn" data-category="{cat.lower().replace(" ", "-")}">{cat}</button>'
            seen_cats.add(cat)
    
    items_html = ""
    for item in items[:12]:
        cat_class = item["category"].lower().replace(" ", "-") if item["category"] else "other"
        items_html += f'''
        <div class="menu-row" data-category="{cat_class}">
            <div class="row-left">
                <h4>{item["name"]}</h4>
                <p>{item["desc"]}</p>
            </div>
            <div class="row-dots"></div>
            <span class="row-price">{item["price"]}</span>
        </div>
        '''
    
    return f'''
    <section class="menu-tabbed" id="menu">
        <div class="menu-container">
            <div class="menu-header">
                <h2>{title}</h2>
                <p>{subtitle}</p>
            </div>
            <div class="tabs-container">
                {tabs_html}
            </div>
            <div class="menu-list">
                {items_html}
            </div>
        </div>
    </section>
    
    <style>
    .menu-tabbed {{ padding: 100px 24px; background: {bg}; }}
    .menu-container {{ max-width: 900px; margin: 0 auto; }}
    .menu-header {{ text-align: center; margin-bottom: 50px; }}
    .menu-header h2 {{ font-family: 'Playfair Display', serif; font-size: 3rem; color: {text}; margin-bottom: 12px; }}
    .menu-header p {{ color: #888; font-size: 1.1rem; }}
    .tabs-container {{ display: flex; justify-content: center; gap: 10px; margin-bottom: 50px; flex-wrap: wrap; }}
    .tab-btn {{
        padding: 12px 28px;
        background: transparent;
        border: 2px solid {primary}30;
        border-radius: 50px;
        font-weight: 600;
        color: {text};
        cursor: pointer;
        transition: all 0.3s;
    }}
    .tab-btn:hover, .tab-btn.active {{ background: {primary}; color: #fff; border-color: {primary}; }}
    .menu-list {{ display: flex; flex-direction: column; gap: 24px; }}
    .menu-row {{
        display: flex;
        align-items: center;
        gap: 20px;
        padding: 20px 0;
        border-bottom: 1px solid #eee;
    }}
    .row-left h4 {{ font-family: 'Playfair Display', serif; font-size: 1.3rem; margin-bottom: 6px; color: {text}; }}
    .row-left p {{ color: #888; font-size: 0.95rem; }}
    .row-dots {{ flex: 1; border-bottom: 2px dotted #ddd; }}
    .row-price {{ font-size: 1.3rem; font-weight: 700; color: {primary}; }}
    </style>
    '''
