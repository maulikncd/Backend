from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Quick View Cards - Products with quick view"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    products = [
        {"name": "Wireless Earbuds Pro", "price": "$179", "rating": "4.8"},
        {"name": "Smart Watch Elite", "price": "$399", "rating": "4.9"},
        {"name": "Bluetooth Speaker", "price": "$129", "rating": "4.7"},
        {"name": "USB-C Hub", "price": "$59", "rating": "4.6"},
        {"name": "Ergonomic Mouse", "price": "$89", "rating": "4.8"},
        {"name": "Mechanical Keyboard", "price": "$149", "rating": "4.9"},
    ]
    
    cards_html = ""
    for p in products:
        cards_html += f'''
        <div class="qv-card">
            <div class="card-image"><button class="quick-view">Quick View</button></div>
            <div class="card-body">
                <div class="rating">⭐ {p['rating']}</div>
                <h3>{p['name']}</h3>
                <div class="card-footer">
                    <span class="price">{p['price']}</span>
                    <button class="cart-btn">+</button>
                </div>
            </div>
        </div>
        '''
    
    return f'''
    <section class="ecom-products-qv" id="products">
        <div class="qv-container">
            <div class="section-header"><h2>Shop Our Collection</h2></div>
            <div class="products-grid">{cards_html}</div>
        </div>
    </section>
    
    <style>
    .ecom-products-qv {{ padding: 120px 24px; background: {background}; }}
    .qv-container {{ max-width: 1200px; margin: 0 auto; }}
    .section-header {{ text-align: center; margin-bottom: 60px; }}
    .section-header h2 {{ font-size: 2.5rem; font-weight: 800; color: {text}; }}
    .products-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 32px; }}
    .qv-card {{ background: {text}05; border-radius: 20px; overflow: hidden; transition: all 0.4s ease; }}
    .qv-card:hover {{ transform: translateY(-8px); box-shadow: 0 30px 60px {primary}15; }}
    .card-image {{ aspect-ratio: 1; background: linear-gradient(135deg, {primary}20, {primary}05); position: relative; }}
    .quick-view {{ position: absolute; bottom: 16px; left: 50%; transform: translateX(-50%) translateY(20px); padding: 12px 28px; background: {background}; color: {text}; border: none; font-weight: 600; border-radius: 100px; cursor: pointer; opacity: 0; transition: all 0.3s ease; }}
    .qv-card:hover .quick-view {{ opacity: 1; transform: translateX(-50%) translateY(0); }}
    .card-body {{ padding: 20px; }}
    .rating {{ color: {secondary}; font-size: 0.9rem; margin-bottom: 8px; }}
    .qv-card h3 {{ font-size: 1.1rem; font-weight: 600; color: {text}; margin-bottom: 12px; }}
    .card-footer {{ display: flex; justify-content: space-between; align-items: center; }}
    .price {{ font-size: 1.3rem; font-weight: 800; color: {primary}; }}
    .cart-btn {{ width: 44px; height: 44px; background: {primary}; color: {background}; border: none; border-radius: 50%; font-size: 1.5rem; cursor: pointer; transition: all 0.3s ease; }}
    .cart-btn:hover {{ transform: scale(1.1); }}
    @media (max-width: 900px) {{ .products-grid {{ grid-template-columns: repeat(2, 1fr); }} }}
    </style>
    '''
