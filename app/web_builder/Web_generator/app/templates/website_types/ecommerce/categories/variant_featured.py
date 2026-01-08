from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Featured Row - Large featured categories"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    cats = [
        {"name": "Electronics", "count": "250+"},
        {"name": "Fashion", "count": "500+"},
        {"name": "Home & Living", "count": "300+"},
        {"name": "Sports", "count": "180+"},
    ]
    
    cards_html = ""
    for c in cats:
        cards_html += f'''<a href="#" class="cat-card"><div class="cat-image"></div><div class="cat-info"><h3>{c['name']}</h3><span>{c['count']} items</span></div></a>'''
    
    return f'''
    <section class="ecom-categories-featured" id="categories">
        <div class="cat-container">
            <div class="cat-header"><h2>Shop by Category</h2><a href="#" class="view-all">View All →</a></div>
            <div class="cats-grid">{cards_html}</div>
        </div>
    </section>
    
    <style>
    .ecom-categories-featured {{ padding: 100px 24px; background: {background}; }}
    .cat-container {{ max-width: 1200px; margin: 0 auto; }}
    .cat-header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 48px; }}
    .cat-header h2 {{ font-size: 2.5rem; font-weight: 800; color: {text}; }}
    .view-all {{ color: {primary}; text-decoration: none; font-weight: 600; }}
    .cats-grid {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 28px; }}
    .cat-card {{ text-decoration: none; transition: all 0.4s ease; }}
    .cat-card:hover {{ transform: translateY(-8px); }}
    .cat-image {{ aspect-ratio: 1; background: linear-gradient(135deg, {primary}20, {primary}05); border-radius: 20px; margin-bottom: 16px; }}
    .cat-info h3 {{ font-size: 1.3rem; font-weight: 700; color: {text}; margin-bottom: 4px; }}
    .cat-info span {{ color: {secondary}; }}
    @media (max-width: 900px) {{ .cats-grid {{ grid-template-columns: 1fr 1fr; }} }}
    </style>
    '''
