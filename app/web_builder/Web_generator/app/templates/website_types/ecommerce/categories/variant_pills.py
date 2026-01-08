from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Tag Pills - Category pills/tags"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    cats = ["Electronics", "Fashion", "Home & Living", "Sports", "Beauty", "Kids", "Automotive", "Books", "Toys", "Garden"]
    
    pills_html = ""
    for c in cats:
        pills_html += f'''<a href="#" class="cat-pill">{c}</a>'''
    
    return f'''
    <section class="ecom-categories-pills" id="categories">
        <div class="pills-container">
            <h2>Browse Categories</h2>
            <div class="pills-wrap">{pills_html}</div>
        </div>
    </section>
    
    <style>
    .ecom-categories-pills {{ padding: 80px 24px; background: {text}03; }}
    .pills-container {{ max-width: 900px; margin: 0 auto; text-align: center; }}
    .pills-container h2 {{ font-size: 2rem; font-weight: 800; color: {text}; margin-bottom: 40px; }}
    .pills-wrap {{ display: flex; flex-wrap: wrap; justify-content: center; gap: 12px; }}
    .cat-pill {{ padding: 14px 28px; background: {background}; border: 1px solid {text}15; color: {text}; text-decoration: none; font-weight: 500; border-radius: 100px; transition: all 0.3s ease; }}
    .cat-pill:hover {{ background: {primary}; border-color: {primary}; color: {background}; }}
    </style>
    '''
