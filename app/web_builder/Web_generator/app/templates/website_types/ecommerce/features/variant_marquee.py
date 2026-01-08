from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Marquee Style - Scrolling features"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    features = ["🚚 Free Shipping", "🔄 Easy Returns", "🔒 Secure Payment", "💬 24/7 Support", "⭐ 5-Star Rated", "✈️ Worldwide Delivery"]
    
    marquee_html = ""
    for f in features:
        marquee_html += f'''<span class="marquee-item">{f}</span><span class="dot">•</span>'''
    
    return f'''
    <section class="ecom-features-marquee" id="features">
        <div class="marquee-track"><div class="marquee-content">{marquee_html}{marquee_html}</div></div>
    </section>
    
    <style>
    .ecom-features-marquee {{ background: {primary}; overflow: hidden; padding: 16px 0; }}
    .marquee-track {{ overflow: hidden; }}
    .marquee-content {{ display: flex; gap: 32px; animation: marquee 25s linear infinite; width: max-content; }}
    @keyframes marquee {{ from {{ transform: translateX(0); }} to {{ transform: translateX(-50%); }} }}
    .marquee-item {{ color: {background}; font-weight: 600; white-space: nowrap; }}
    .dot {{ color: {background}50; }}
    </style>
    '''
