from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    # Support both title formats from blueprint
    title = props.get("sectionTitle", props.get("title", "Our Menu"))
    subtitle = props.get("sectionSubtitle", "")
    
    # Blueprint uses 'items' key with name, description, price structure
    raw_items = props.get("items", props.get("menuItems", []))
    
    # Transform blueprint items to template format
    items = []
    for item in raw_items:
        items.append({
            "name": item.get("name", "Item"),
            "description": item.get("description", ""),
            "price": item.get("price", "$0.00"),
            "category": item.get("category", ""),
            # Generate a food image based on item name
            "image": f"https://source.unsplash.com/400x300/?{item.get('name', 'food').replace(' ', ',')},food"
        })
    
    # Fallback if no items provided
    if not items:
        items = [
            {"name": "Signature Coffee", "price": "$4.50", "description": "Our house blend", "image": "https://images.unsplash.com/photo-1461023058943-07fcbe16d735?w=400"},
            {"name": "Fresh Pastry", "price": "$5.00", "description": "Baked daily", "image": "https://images.unsplash.com/photo-1509440159596-0249088772ff?w=400"},
            {"name": "Artisan Toast", "price": "$8.00", "description": "With premium toppings", "image": "https://images.unsplash.com/photo-1525351484163-7529414344d8?w=400"}
        ]
    
    items_html = ""
    for item in items:
        items_html += f'''
        <div class="visual-item">
            <div class="item-img" style="background-image: url('{item["image"]}')">
                <span class="img-price">{item["price"]}</span>
            </div>
            <div class="item-info">
                <div class="item-text">
                    <h4>{item["name"]}</h4>
                    <p class="item-desc">{item.get("description", "")[:60]}...</p>
                </div>
                <a href="#" class="btn-add">+</a>
            </div>
        </div>
        '''
    
    return f'''
    <section class="cafe-menu-visual" id="menu">
        <div class="container">
            <h2 class="section-title text-center">{title}</h2>
            <div class="visual-grid">
                {items_html}
            </div>
        </div>
    </section>
    
    <style>
    .cafe-menu-visual {{ padding: 100px 24px; background: #fff; }}
    .visual-grid {{
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
        gap: 32px;
        max-width: 1200px;
        margin: 0 auto;
    }}
    .visual-item {{
        background: {colors.get("background", "#FFF8F0")};
        border-radius: 20px;
        overflow: hidden;
        transition: transform 0.3s;
    }}
    .visual-item:hover {{ transform: scale(1.02); }}
    .item-img {{ height: 250px; background-size: cover; background-position: center; position: relative; }}
    .img-price {{ position: absolute; bottom: 20px; right: 20px; background: #fff; padding: 6px 16px; border-radius: 50px; font-weight: 700; color: {colors.get("text", "#2D2013")}; }}
    .item-info {{ padding: 24px; display: flex; justify-content: space-between; align-items: center; }}
    .item-info h4 {{ font-family: 'Playfair Display', serif; font-size: 1.25rem; margin: 0; }}
    .btn-add {{ background: {colors.get("primary", "#6F4E37")}; color: #fff; width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center; text-decoration: none; font-size: 1.5rem; }}
    </style>
    '''
