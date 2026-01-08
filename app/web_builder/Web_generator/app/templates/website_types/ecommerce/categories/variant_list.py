from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Minimal List - Clean list style"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    cats = [
        {"name": "Electronics", "count": "250"},
        {"name": "Fashion", "count": "500"},
        {"name": "Home & Living", "count": "300"},
        {"name": "Sports & Outdoors", "count": "180"},
        {"name": "Beauty & Personal Care", "count": "220"},
    ]
    
    list_html = ""
    for c in cats:
        list_html += f'''<a href="#" class="cat-row"><span class="name">{c['name']}</span><span class="count">{c['count']} items</span><span class="arrow">→</span></a>'''
    
    return f'''
    <section class="ecom-categories-list" id="categories">
        <div class="list-container">
            <h2>Browse Categories</h2>
            <div class="cats-list">{list_html}</div>
        </div>
    </section>
    
    <style>
    .ecom-categories-list {{ padding: 100px 24px; background: {background}; }}
    .list-container {{ max-width: 800px; margin: 0 auto; }}
    .list-container h2 {{ font-size: 2.5rem; font-weight: 800; color: {text}; margin-bottom: 48px; }}
    .cats-list {{ display: flex; flex-direction: column; }}
    .cat-row {{ display: flex; align-items: center; gap: 20px; padding: 24px 0; border-bottom: 1px solid {text}10; text-decoration: none; transition: all 0.3s ease; }}
    .cat-row:hover {{ padding-left: 16px; background: {primary}05; }}
    .name {{ flex: 1; font-size: 1.2rem; font-weight: 600; color: {text}; }}
    .count {{ color: {secondary}; }}
    .arrow {{ color: {primary}; font-size: 1.2rem; }}
    </style>
    '''
