from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Magazine Style Menu - Editorial layout with large images"""
    title = props.get("sectionTitle", props.get("title", "The Menu"))
    raw_items = props.get("items", [])
    
    primary = colors.get("primary", "#8B7355")
    text = colors.get("text", "#2D2013")
    
    items = []
    for item in raw_items:
        items.append({
            "name": item.get("name", "Item"),
            "desc": item.get("description", ""),
            "price": item.get("price", "$0"),
            "image": f"https://source.unsplash.com/400x500/?{item.get('name', 'coffee').replace(' ', ',')}"
        })
    
    if not items:
        items = [
            {"name": "Signature Blend", "desc": "Our house roasted specialty", "price": "$4.50", "image": "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=400"},
            {"name": "Artisan Pastries", "desc": "Baked fresh every morning", "price": "$5.00", "image": "https://images.unsplash.com/photo-1509440159596-0249088772ff?w=400"},
            {"name": "Brunch Special", "desc": "Eggs benedict with hollandaise", "price": "$16.00", "image": "https://images.unsplash.com/photo-1525351484163-7529414344d8?w=400"}
        ]
    
    items_html = ""
    for i, item in enumerate(items[:6]):
        layout_class = "left" if i % 2 == 0 else "right"
        desc_short = item["desc"][:100] if item["desc"] else ""
        items_html += f'''
        <div class="magazine-item {layout_class}">
            <div class="item-image">
                <img src="{item['image']}" alt="{item['name']}" loading="lazy">
                <span class="item-number">0{i+1}</span>
            </div>
            <div class="item-content">
                <span class="item-price">{item['price']}</span>
                <h3>{item['name']}</h3>
                <p>{desc_short}</p>
                <a href="#order" class="order-link">Order Now →</a>
            </div>
        </div>
        '''
    
    return f'''
    <section class="menu-magazine" id="menu">
        <div class="magazine-header">
            <span class="header-line"></span>
            <h2>{title}</h2>
            <span class="header-line"></span>
        </div>
        <div class="magazine-grid">
            {items_html}
        </div>
    </section>
    
    <style>
    .menu-magazine {{ padding: 120px 40px; background: #fff; }}
    .magazine-header {{ display: flex; align-items: center; justify-content: center; gap: 40px; margin-bottom: 80px; }}
    .header-line {{ width: 100px; height: 1px; background: {primary}; }}
    .magazine-header h2 {{ font-family: 'Playfair Display', serif; font-size: 3.5rem; color: {text}; white-space: nowrap; }}
    .magazine-grid {{ max-width: 1200px; margin: 0 auto; display: flex; flex-direction: column; gap: 100px; }}
    .magazine-item {{ display: grid; grid-template-columns: 1fr 1fr; gap: 80px; align-items: center; }}
    .magazine-item.right {{ direction: rtl; }}
    .magazine-item.right > * {{ direction: ltr; }}
    .item-image {{ position: relative; }}
    .item-image img {{ width: 100%; aspect-ratio: 4/5; object-fit: cover; border-radius: 20px; }}
    .item-number {{ position: absolute; top: -20px; left: -20px; font-size: 5rem; font-weight: 900; color: {primary}20; font-family: 'Playfair Display', serif; }}
    .item-content {{ padding: 40px 0; }}
    .item-price {{ display: inline-block; padding: 8px 20px; background: {primary}; color: #fff; border-radius: 50px; font-weight: 700; margin-bottom: 20px; }}
    .item-content h3 {{ font-family: 'Playfair Display', serif; font-size: 2.5rem; color: {text}; margin-bottom: 20px; }}
    .item-content p {{ color: #666; font-size: 1.1rem; line-height: 1.8; margin-bottom: 30px; }}
    .order-link {{ color: {primary}; font-weight: 600; text-decoration: none; font-size: 1.1rem; transition: 0.3s; }}
    .order-link:hover {{ letter-spacing: 2px; }}
    @media (max-width: 900px) {{ .magazine-item {{ grid-template-columns: 1fr; gap: 40px; }} .magazine-item.right {{ direction: ltr; }} }}
    </style>
    '''
