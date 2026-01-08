from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """
    Aura Premium Menu - Card-based menu with categories, 
    hover effects, and premium styling
    """
    title = props.get("sectionTitle", props.get("title", "Our Menu"))
    subtitle = props.get("sectionSubtitle", props.get("subtitle", "Curated selections for the discerning palate"))
    
    # Get items from blueprint
    raw_items = props.get("items", props.get("menuItems", []))
    categories = props.get("categories", ["Coffee", "Pastries", "Light Bites"])
    
    # Transform items
    items = []
    for item in raw_items:
        items.append({
            "name": item.get("name", "Item"),
            "desc": item.get("description", ""),
            "price": item.get("price", "$0"),
            "category": item.get("category", "Coffee"),
            "image": f"https://source.unsplash.com/300x300/?{item.get('name', 'coffee').replace(' ', ',')}"
        })
    
    if not items:
        items = [
            {"name": "Signature Espresso", "desc": "Rich, bold, and perfectly balanced", "price": "$4.50", "category": "Coffee", "image": "https://images.unsplash.com/photo-1510707577719-ae7c14805e3a?w=300"},
            {"name": "Creamy Cappuccino", "desc": "Velvety foam meets robust espresso", "price": "$5.50", "category": "Coffee", "image": "https://images.unsplash.com/photo-1572442388796-11668a67e53d?w=300"},
            {"name": "Butter Croissant", "desc": "Flaky, golden, freshly baked", "price": "$4.00", "category": "Pastries", "image": "https://images.unsplash.com/photo-1555507036-ab1f4038808a?w=300"},
            {"name": "Avocado Toast", "desc": "Smashed avocado on artisan bread", "price": "$12.00", "category": "Light Bites", "image": "https://images.unsplash.com/photo-1525351484163-7529414344d8?w=300"}
        ]
    
    primary = colors.get("primary", "#8B7355")
    bg = colors.get("background", "#FAF7F4")
    text = colors.get("text", "#2D2013")
    
    # Build menu items by category
    items_html = ""
    for item in items[:8]:
        desc_short = item["desc"][:60] + "..." if len(item["desc"]) > 60 else item["desc"]
        items_html += f'''
        <div class="menu-card animate-on-scroll">
            <div class="card-image">
                <img src="{item['image']}" alt="{item['name']}" loading="lazy">
                <div class="card-overlay">
                    <span class="price-tag">{item['price']}</span>
                </div>
            </div>
            <div class="card-content">
                <span class="card-category">{item['category']}</span>
                <h4 class="card-title">{item['name']}</h4>
                <p class="card-desc">{desc_short}</p>
            </div>
        </div>
        '''
    
    return f'''
    <section class="aura-menu" id="menu">
        <div class="menu-container">
            <div class="menu-header">
                <span class="section-badge">Menu</span>
                <h2 class="section-title">{title}</h2>
                <p class="section-subtitle">{subtitle}</p>
            </div>
            <div class="menu-grid">
                {items_html}
            </div>
            <div class="menu-cta">
                <a href="#contact" class="btn-view-full">View Full Menu</a>
            </div>
        </div>
    </section>
    
    <style>
    .aura-menu {{
        padding: 120px 24px;
        background: {bg};
    }}
    .menu-container {{ max-width: 1200px; margin: 0 auto; }}
    .menu-header {{ text-align: center; margin-bottom: 60px; }}
    .section-badge {{
        display: inline-block;
        padding: 8px 20px;
        background: {primary}15;
        color: {primary};
        border-radius: 50px;
        font-size: 0.85rem;
        font-weight: 600;
        margin-bottom: 20px;
    }}
    .aura-menu .section-title {{
        font-family: 'Playfair Display', serif;
        font-size: clamp(2.5rem, 4vw, 3.5rem);
        color: {text};
        margin-bottom: 16px;
    }}
    .aura-menu .section-subtitle {{
        color: #888;
        font-size: 1.1rem;
        max-width: 500px;
        margin: 0 auto;
    }}
    .menu-grid {{
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
        gap: 30px;
    }}
    .menu-card {{
        background: #fff;
        border-radius: 20px;
        overflow: hidden;
        transition: all 0.4s;
        box-shadow: 0 5px 20px rgba(0,0,0,0.05);
    }}
    .menu-card:hover {{
        transform: translateY(-10px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
    }}
    .card-image {{
        position: relative;
        height: 200px;
        overflow: hidden;
    }}
    .card-image img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.5s;
    }}
    .menu-card:hover .card-image img {{ transform: scale(1.1); }}
    .card-overlay {{
        position: absolute;
        inset: 0;
        background: linear-gradient(to top, rgba(0,0,0,0.6), transparent);
        display: flex;
        align-items: flex-end;
        padding: 20px;
    }}
    .price-tag {{
        background: {primary};
        color: #fff;
        padding: 8px 16px;
        border-radius: 50px;
        font-weight: 700;
    }}
    .card-content {{ padding: 24px; }}
    .card-category {{
        font-size: 0.8rem;
        color: {primary};
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
    }}
    .card-title {{
        font-family: 'Playfair Display', serif;
        font-size: 1.4rem;
        color: {text};
        margin: 10px 0;
    }}
    .card-desc {{
        color: #888;
        font-size: 0.95rem;
        line-height: 1.5;
    }}
    .menu-cta {{ text-align: center; margin-top: 50px; }}
    .btn-view-full {{
        display: inline-block;
        padding: 16px 40px;
        background: {text};
        color: #fff;
        text-decoration: none;
        border-radius: 50px;
        font-weight: 600;
        transition: all 0.3s;
    }}
    .btn-view-full:hover {{
        background: {primary};
        transform: translateY(-2px);
    }}
    </style>
    '''
