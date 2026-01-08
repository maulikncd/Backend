from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Horizontal Scroll - Scrollable products"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    products = [
        {"name": "Wireless Earbuds", "price": "$149", "cat": "Audio"},
        {"name": "Smart Watch", "price": "$299", "cat": "Wearables"},
        {"name": "Laptop Pro", "price": "$1299", "cat": "Computers"},
        {"name": "Gaming Mouse", "price": "$79", "cat": "Accessories"},
        {"name": "Keyboard", "price": "$129", "cat": "Accessories"},
        {"name": "Monitor 4K", "price": "$599", "cat": "Displays"},
    ]
    
    cards_html = ""
    for p in products:
        cards_html += f'''
        <div class="scroll-card">
            <div class="card-image"></div>
            <span class="cat">{p['cat']}</span>
            <h3>{p['name']}</h3>
            <span class="price">{p['price']}</span>
        </div>
        '''
    
    return f'''
    <section class="ecom-products-scroll" id="products">
        <div class="scroll-header">
            <h2>New Arrivals</h2>
            <div class="arrows"><button>←</button><button>→</button></div>
        </div>
        <div class="scroll-track">{cards_html}</div>
    </section>
    
    <style>
    .ecom-products-scroll {{ padding: 120px 0; background: {background}; }}
    .scroll-header {{ max-width: 1400px; margin: 0 auto 40px; padding: 0 24px; display: flex; justify-content: space-between; align-items: center; }}
    .scroll-header h2 {{ font-size: 2.5rem; font-weight: 800; color: {text}; }}
    .arrows {{ display: flex; gap: 12px; }}
    .arrows button {{ width: 50px; height: 50px; background: {text}08; border: none; border-radius: 50%; color: {text}; font-size: 1.2rem; cursor: pointer; transition: all 0.3s ease; }}
    .arrows button:hover {{ background: {primary}; color: {background}; }}
    .scroll-track {{ display: flex; gap: 24px; overflow-x: auto; padding: 0 24px 20px; scroll-snap-type: x mandatory; scrollbar-width: none; }}
    .scroll-track::-webkit-scrollbar {{ display: none; }}
    .scroll-card {{ flex-shrink: 0; width: 280px; background: {text}05; border-radius: 20px; padding: 20px; scroll-snap-align: start; transition: all 0.4s ease; cursor: pointer; }}
    .scroll-card:hover {{ transform: translateY(-8px); }}
    .card-image {{ aspect-ratio: 1; background: linear-gradient(135deg, {primary}20, {primary}05); border-radius: 12px; margin-bottom: 16px; }}
    .cat {{ display: inline-block; padding: 4px 12px; background: {primary}20; color: {primary}; font-size: 0.75rem; font-weight: 600; border-radius: 100px; margin-bottom: 8px; }}
    .scroll-card h3 {{ font-size: 1.1rem; font-weight: 600; color: {text}; margin-bottom: 6px; }}
    .price {{ font-size: 1.2rem; font-weight: 800; color: {primary}; }}
    </style>
    '''
