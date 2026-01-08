from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    # Support blueprint keys
    title = props.get("sectionTitle", props.get("title", "Our Menu"))
    subtitle = props.get("sectionSubtitle", props.get("subtitle", "Carefully curated for the coffee connoisseur"))
    
    # Blueprint uses 'items' key with name, description, price structure
    raw_items = props.get("items", props.get("menuItems", []))
    
    # Transform blueprint items to template format
    items = []
    for item in raw_items:
        items.append({
            "name": item.get("name", "Item"),
            "desc": item.get("description", ""),
            "price": item.get("price", "$0.00"),
            "category": item.get("category", "")
        })
    
    # Fallback if no items provided
    if not items:
        items = [
            {"name": "Espresso", "price": "$3.00", "desc": "Rich, concentrated shot of coffee"},
            {"name": "Cappuccino", "price": "$4.50", "desc": "Double espresso with steamed milk foam"},
            {"name": "Croissant", "price": "$3.50", "desc": "Flaky, buttery French pastry"}
        ]
    
    items_html = ""
    for item in items:
        desc_short = item["desc"][:80] + "..." if len(item["desc"]) > 80 else item["desc"]
        items_html += f'''
        <div class="menu-item-elegant">
            <div class="item-header">
                <h4 class="item-name">{item["name"]}</h4>
                <div class="item-line"></div>
                <span class="item-price">{item["price"]}</span>
            </div>
            <p class="item-desc">{desc_short}</p>
        </div>
        '''
    
    return f'''
    <section class="cafe-menu-elegant" id="menu">
        <div class="menu-container">
            <div class="menu-info">
                <h2 class="menu-title">{title}</h2>
                <div class="title-divider"></div>
                <p class="menu-subtitle">{subtitle}</p>
            </div>
            <div class="menu-grid">
                {items_html}
            </div>
        </div>
    </section>
    
    <style>
    .cafe-menu-elegant {{
        padding: 100px 24px;
        background: {colors.get("background", "#FFF8F0")};
    }}
    .menu-container {{ max-width: 1000px; margin: 0 auto; }}
    .menu-info {{ text-align: center; margin-bottom: 60px; }}
    .menu-title {{
        font-family: 'Playfair Display', serif;
        font-size: 3rem;
        color: {colors.get("text", "#2D2013")};
        margin-bottom: 16px;
    }}
    .menu-subtitle {{
        color: {colors.get("text_muted", "#888")};
        font-size: 1.1rem;
    }}
    .title-divider {{
        width: 60px;
        height: 2px;
        background: {colors.get("primary", "#6F4E37")};
        margin: 0 auto 24px;
    }}
    .menu-grid {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 40px;
    }}
    .menu-item-elegant {{ margin-bottom: 30px; }}
    .item-header {{ display: flex; align-items: baseline; gap: 12px; margin-bottom: 8px; }}
    .item-name {{ font-family: 'Playfair Display', serif; font-size: 1.3rem; font-weight: 600; white-space: nowrap; color: {colors.get("text", "#2D2013")}; }}
    .item-line {{ flex: 1; border-bottom: 1px dotted {colors.get("text_muted", "#8B7355")}50; }}
    .item-price {{ font-weight: 700; color: {colors.get("primary", "#6F4E37")}; font-size: 1.1rem; }}
    .item-desc {{ font-size: 0.95rem; color: {colors.get("text_muted", "#8B7355")}; line-height: 1.5; }}
    @media (max-width: 768px) {{ .menu-grid {{ grid-template-columns: 1fr; }} }}
    </style>
    '''
