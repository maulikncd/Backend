from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Cards Grid - Feature cards"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    features = [
        {"icon": "🚚", "title": "Free Shipping", "desc": "Free shipping on all orders over $50"},
        {"icon": "🔄", "title": "Easy Returns", "desc": "30-day hassle-free return policy"},
        {"icon": "🔒", "title": "Secure Checkout", "desc": "Your payments are 100% secure"},
        {"icon": "💬", "title": "24/7 Support", "desc": "Get help anytime you need it"},
    ]
    
    cards_html = ""
    for f in features:
        cards_html += f'''<div class="feature-card"><span class="icon">{f['icon']}</span><h4>{f['title']}</h4><p>{f['desc']}</p></div>'''
    
    return f'''
    <section class="ecom-features-cards" id="features">
        <div class="cards-container">
            <h2>Why Shop With Us</h2>
            <div class="cards-grid">{cards_html}</div>
        </div>
    </section>
    
    <style>
    .ecom-features-cards {{ padding: 100px 24px; background: {background}; }}
    .cards-container {{ max-width: 1100px; margin: 0 auto; }}
    .cards-container h2 {{ font-size: 2.5rem; font-weight: 800; color: {text}; text-align: center; margin-bottom: 60px; }}
    .cards-grid {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px; }}
    .feature-card {{ background: {text}05; border-radius: 20px; padding: 32px; text-align: center; transition: all 0.4s ease; }}
    .feature-card:hover {{ transform: translateY(-8px); box-shadow: 0 20px 40px {primary}10; }}
    .icon {{ display: block; font-size: 3rem; margin-bottom: 16px; }}
    .feature-card h4 {{ font-size: 1.1rem; font-weight: 700; color: {text}; margin-bottom: 8px; }}
    .feature-card p {{ color: {secondary}; font-size: 0.9rem; line-height: 1.5; }}
    @media (max-width: 900px) {{ .cards-grid {{ grid-template-columns: 1fr 1fr; }} }}
    </style>
    '''
