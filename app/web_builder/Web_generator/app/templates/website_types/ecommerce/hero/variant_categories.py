from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Categories Hero - Category showcase"""
    title = props.get("title", "Shop by Category")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    cats = [
        {"name": "Electronics", "count": "250+"},
        {"name": "Fashion", "count": "500+"},
        {"name": "Home & Living", "count": "300+"},
    ]
    
    cats_html = ""
    for c in cats:
        cats_html += f'''
        <a href="#" class="cat-card">
            <div class="cat-image"></div>
            <div class="cat-info"><h3>{c['name']}</h3><span>{c['count']} items</span></div>
        </a>
        '''
    
    return f'''
    <section class="ecom-hero-cats" id="hero">
        <div class="cats-container">
            <div class="cats-header">
                <h1>{title}</h1>
                <p>Explore our curated collections</p>
            </div>
            <div class="cats-grid">{cats_html}</div>
        </div>
    </section>
    
    <style>
    .ecom-hero-cats {{ min-height: 100vh; background: {background}; display: flex; align-items: center; padding: 80px 24px; }}
    .cats-container {{ max-width: 1200px; margin: 0 auto; width: 100%; }}
    .cats-header {{ text-align: center; margin-bottom: 60px; }}
    .cats-header h1 {{ font-size: clamp(2.5rem, 6vw, 4.5rem); font-weight: 900; color: {text}; margin-bottom: 16px; }}
    .cats-header p {{ color: {secondary}; font-size: 1.2rem; }}
    .cats-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 32px; }}
    .cat-card {{ background: {text}05; border-radius: 24px; overflow: hidden; text-decoration: none; transition: all 0.4s ease; }}
    .cat-card:hover {{ transform: translateY(-8px); box-shadow: 0 30px 60px {primary}15; }}
    .cat-image {{ aspect-ratio: 4/3; background: linear-gradient(135deg, {primary}20, {primary}05); }}
    .cat-info {{ padding: 24px; }}
    .cat-info h3 {{ font-size: 1.5rem; font-weight: 700; color: {text}; margin-bottom: 6px; }}
    .cat-info span {{ color: {secondary}; }}
    @media (max-width: 900px) {{ .cats-grid {{ grid-template-columns: 1fr; }} }}
    </style>
    '''
