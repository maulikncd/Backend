from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Sale Grid - Products on sale"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    products = [
        {"name": "Premium Headphones", "price": "$199", "old": "$299", "off": "33%"},
        {"name": "Smart Watch", "price": "$279", "old": "$399", "off": "30%"},
        {"name": "Laptop Stand", "price": "$49", "old": "$79", "off": "38%"},
        {"name": "Wireless Mouse", "price": "$39", "old": "$59", "off": "34%"},
    ]
    
    cards_html = ""
    for p in products:
        cards_html += f'''
        <div class="sale-card">
            <span class="off-badge">-{p['off']}</span>
            <div class="card-image"></div>
            <h3>{p['name']}</h3>
            <div class="prices"><span class="new">{p['price']}</span><span class="old">{p['old']}</span></div>
            <button class="add-btn">Add to Cart</button>
        </div>
        '''
    
    return f'''
    <section class="ecom-products-sale" id="products">
        <div class="sale-container">
            <div class="sale-header">
                <div class="header-text"><span class="tag">🔥 Hot Deals</span><h2>On Sale Now</h2></div>
                <a href="#" class="view-all">View All Deals →</a>
            </div>
            <div class="sale-grid">{cards_html}</div>
        </div>
    </section>
    
    <style>
    .ecom-products-sale {{ padding: 120px 24px; background: linear-gradient(135deg, {primary}08, {background}); }}
    .sale-container {{ max-width: 1200px; margin: 0 auto; }}
    .sale-header {{ display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 48px; }}
    .tag {{ display: inline-block; padding: 8px 18px; background: #ff3b3b; color: white; font-weight: 700; font-size: 0.85rem; border-radius: 100px; margin-bottom: 12px; }}
    .header-text h2 {{ font-size: 2.5rem; font-weight: 800; color: {text}; }}
    .view-all {{ color: {primary}; text-decoration: none; font-weight: 600; }}
    .sale-grid {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 28px; }}
    .sale-card {{ background: {background}; border-radius: 20px; padding: 20px; position: relative; transition: all 0.4s ease; }}
    .sale-card:hover {{ transform: translateY(-8px); box-shadow: 0 30px 60px {primary}15; }}
    .off-badge {{ position: absolute; top: 16px; right: 16px; padding: 8px 14px; background: #ff3b3b; color: white; font-weight: 700; font-size: 0.85rem; border-radius: 8px; }}
    .card-image {{ aspect-ratio: 1; background: linear-gradient(135deg, {primary}15, {primary}05); border-radius: 12px; margin-bottom: 16px; }}
    .sale-card h3 {{ font-size: 1rem; font-weight: 600; color: {text}; margin-bottom: 10px; }}
    .prices {{ display: flex; gap: 12px; align-items: center; margin-bottom: 16px; }}
    .new {{ font-size: 1.3rem; font-weight: 800; color: {primary}; }}
    .old {{ text-decoration: line-through; color: {secondary}; }}
    .add-btn {{ width: 100%; padding: 12px; background: {primary}; color: {background}; border: none; font-weight: 700; border-radius: 10px; cursor: pointer; }}
    @media (max-width: 900px) {{ .sale-grid {{ grid-template-columns: repeat(2, 1fr); }} }}
    </style>
    '''
