from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Featured Row - Featured products horizontal"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    products = [
        {"name": "Premium Headphones", "price": "$299", "badge": "New"},
        {"name": "Smart Watch Pro", "price": "$449", "badge": "Hot"},
        {"name": "Wireless Speaker", "price": "$199", "badge": ""},
        {"name": "Laptop Stand", "price": "$89", "badge": "Sale"},
    ]
    
    cards_html = ""
    for p in products:
        badge = f'<span class="badge">{p["badge"]}</span>' if p["badge"] else ""
        cards_html += f'''
        <div class="product-card">
            {badge}
            <div class="product-image"></div>
            <h3>{p['name']}</h3>
            <span class="price">{p['price']}</span>
            <button class="add-btn">Add to Cart</button>
        </div>
        '''
    
    return f'''
    <section class="ecom-products-featured" id="products">
        <div class="featured-container">
            <div class="section-header">
                <h2>Featured Products</h2>
                <a href="#" class="view-all">View All →</a>
            </div>
            <div class="products-row">{cards_html}</div>
        </div>
    </section>
    
    <style>
    .ecom-products-featured {{ padding: 120px 24px; background: {background}; }}
    .featured-container {{ max-width: 1200px; margin: 0 auto; }}
    .section-header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 48px; }}
    .section-header h2 {{ font-size: 2.5rem; font-weight: 800; color: {text}; }}
    .view-all {{ color: {primary}; text-decoration: none; font-weight: 600; }}
    .products-row {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 32px; }}
    .product-card {{ background: {text}05; border-radius: 20px; padding: 24px; position: relative; transition: all 0.4s ease; }}
    .product-card:hover {{ transform: translateY(-8px); box-shadow: 0 30px 60px {primary}15; }}
    .badge {{ position: absolute; top: 16px; right: 16px; padding: 6px 14px; background: {primary}; color: {background}; font-size: 0.75rem; font-weight: 700; border-radius: 100px; }}
    .product-image {{ aspect-ratio: 1; background: linear-gradient(135deg, {primary}20, {primary}05); border-radius: 12px; margin-bottom: 16px; }}
    .product-card h3 {{ font-size: 1.1rem; font-weight: 600; color: {text}; margin-bottom: 8px; }}
    .price {{ display: block; font-size: 1.3rem; font-weight: 800; color: {primary}; margin-bottom: 16px; }}
    .add-btn {{ width: 100%; padding: 14px; background: {primary}; color: {background}; border: none; font-weight: 700; border-radius: 10px; cursor: pointer; transition: all 0.3s ease; }}
    .add-btn:hover {{ transform: scale(1.02); }}
    @media (max-width: 900px) {{ .products-row {{ grid-template-columns: repeat(2, 1fr); }} }}
    </style>
    '''
