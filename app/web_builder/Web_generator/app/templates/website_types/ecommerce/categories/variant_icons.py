from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Icon Cards - Categories with icons"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    cats = [
        {"icon": "📱", "name": "Electronics"},
        {"icon": "👔", "name": "Fashion"},
        {"icon": "🏠", "name": "Home"},
        {"icon": "⚽", "name": "Sports"},
        {"icon": "💄", "name": "Beauty"},
        {"icon": "🧸", "name": "Kids"},
    ]
    
    cards_html = ""
    for c in cats:
        cards_html += f'''<a href="#" class="icon-cat"><span class="icon">{c['icon']}</span><span class="name">{c['name']}</span></a>'''
    
    return f'''
    <section class="ecom-categories-icons" id="categories">
        <div class="icons-container">
            <h2>Categories</h2>
            <div class="icons-grid">{cards_html}</div>
        </div>
    </section>
    
    <style>
    .ecom-categories-icons {{ padding: 100px 24px; background: {background}; }}
    .icons-container {{ max-width: 1000px; margin: 0 auto; text-align: center; }}
    .icons-container h2 {{ font-size: 2.5rem; font-weight: 800; color: {text}; margin-bottom: 48px; }}
    .icons-grid {{ display: grid; grid-template-columns: repeat(6, 1fr); gap: 24px; }}
    .icon-cat {{ background: {text}05; border-radius: 20px; padding: 32px 16px; text-decoration: none; transition: all 0.4s ease; }}
    .icon-cat:hover {{ background: {primary}15; transform: translateY(-8px); }}
    .icon {{ display: block; font-size: 3rem; margin-bottom: 12px; }}
    .name {{ display: block; color: {text}; font-weight: 600; }}
    @media (max-width: 900px) {{ .icons-grid {{ grid-template-columns: repeat(3, 1fr); }} }}
    </style>
    '''
