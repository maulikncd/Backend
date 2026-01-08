from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Masonry Grid - Pinterest style"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    reviews = [
        {"name": "Sarah J.", "text": "Amazing quality! Best purchase I've made.", "tall": True},
        {"name": "Mike R.", "text": "Fast shipping!", "tall": False},
        {"name": "Emily L.", "text": "Love everything about this store. The products are top-notch and customer service is excellent.", "tall": True},
        {"name": "David K.", "text": "Will buy again!", "tall": False},
        {"name": "Anna M.", "text": "Perfect gifts for everyone!", "tall": False},
        {"name": "Chris P.", "text": "Exceeded expectations. The attention to detail is incredible.", "tall": True},
    ]
    
    cards_html = ""
    for r in reviews:
        tall = "tall" if r["tall"] else ""
        cards_html += f'''<div class="masonry-card {tall}"><div class="stars">⭐⭐⭐⭐⭐</div><p>"{r['text']}"</p><span class="name">— {r['name']}</span></div>'''
    
    return f'''
    <section class="ecom-testimonials-masonry" id="testimonials">
        <div class="masonry-container">
            <div class="masonry-header"><h2>Happy Customers</h2></div>
            <div class="masonry-grid">{cards_html}</div>
        </div>
    </section>
    
    <style>
    .ecom-testimonials-masonry {{ padding: 120px 24px; background: {background}; }}
    .masonry-container {{ max-width: 1100px; margin: 0 auto; }}
    .masonry-header {{ text-align: center; margin-bottom: 60px; }}
    .masonry-header h2 {{ font-size: 2.5rem; font-weight: 800; color: {text}; }}
    .masonry-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); grid-auto-rows: 120px; gap: 20px; }}
    .masonry-card {{ background: {text}05; border-radius: 20px; padding: 28px; display: flex; flex-direction: column; }}
    .masonry-card.tall {{ grid-row: span 2; }}
    .stars {{ margin-bottom: 12px; }}
    .masonry-card p {{ color: {text}; line-height: 1.6; flex: 1; font-style: italic; }}
    .name {{ color: {primary}; font-weight: 600; margin-top: 16px; }}
    @media (max-width: 900px) {{ .masonry-grid {{ grid-template-columns: 1fr 1fr; }} }}
    </style>
    '''
