from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Minimal Strip - Compact strip"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    features = [
        {"icon": "🚚", "text": "Free Shipping"},
        {"icon": "🔄", "text": "Easy Returns"},
        {"icon": "🔒", "text": "Secure Payment"},
        {"icon": "💬", "text": "24/7 Support"},
    ]
    
    items_html = ""
    for f in features:
        items_html += f'''<span class="strip-item">{f['icon']} {f['text']}</span>'''
    
    return f'''
    <section class="ecom-features-strip" id="features">
        <div class="strip-container">{items_html}</div>
    </section>
    
    <style>
    .ecom-features-strip {{ padding: 16px 24px; background: {primary}; }}
    .strip-container {{ max-width: 1200px; margin: 0 auto; display: flex; justify-content: center; gap: 60px; flex-wrap: wrap; }}
    .strip-item {{ color: {background}; font-weight: 600; white-space: nowrap; }}
    </style>
    '''
