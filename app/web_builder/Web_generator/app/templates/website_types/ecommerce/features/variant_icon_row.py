from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Icon Row - Simple icon row"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    features = [
        {"icon": "🚚", "title": "Free Shipping", "desc": "On orders over $50"},
        {"icon": "🔄", "title": "Easy Returns", "desc": "30-day return policy"},
        {"icon": "🔒", "title": "Secure Payment", "desc": "100% protected"},
        {"icon": "💬", "title": "24/7 Support", "desc": "Always here to help"},
    ]
    
    items_html = ""
    for f in features:
        items_html += f'''<div class="feature-item"><span class="icon">{f['icon']}</span><h4>{f['title']}</h4><p>{f['desc']}</p></div>'''
    
    return f'''
    <section class="ecom-features-row" id="features">
        <div class="features-container">{items_html}</div>
    </section>
    
    <style>
    .ecom-features-row {{ padding: 60px 24px; background: {text}03; border-top: 1px solid {text}10; border-bottom: 1px solid {text}10; }}
    .features-container {{ max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: repeat(4, 1fr); gap: 40px; }}
    .feature-item {{ text-align: center; }}
    .icon {{ display: block; font-size: 2.5rem; margin-bottom: 12px; }}
    .feature-item h4 {{ font-size: 1.1rem; font-weight: 700; color: {text}; margin-bottom: 4px; }}
    .feature-item p {{ color: {secondary}; font-size: 0.9rem; }}
    @media (max-width: 900px) {{ .features-container {{ grid-template-columns: 1fr 1fr; }} }}
    </style>
    '''
