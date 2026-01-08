from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Horizontal Scroll - Scrollable categories"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    cats = ["Electronics", "Fashion", "Home", "Sports", "Beauty", "Kids", "Automotive"]
    
    cards_html = ""
    for c in cats:
        cards_html += f'''<a href="#" class="scroll-cat"><div class="cat-icon">{c[0]}</div><span>{c}</span></a>'''
    
    return f'''
    <section class="ecom-categories-scroll" id="categories">
        <div class="scroll-track">{cards_html}</div>
    </section>
    
    <style>
    .ecom-categories-scroll {{ padding: 60px 0; background: {text}03; overflow: hidden; }}
    .scroll-track {{ display: flex; gap: 24px; overflow-x: auto; padding: 20px 24px; scroll-snap-type: x mandatory; scrollbar-width: none; }}
    .scroll-track::-webkit-scrollbar {{ display: none; }}
    .scroll-cat {{ flex-shrink: 0; display: flex; flex-direction: column; align-items: center; gap: 12px; text-decoration: none; scroll-snap-align: start; }}
    .cat-icon {{ width: 100px; height: 100px; background: {primary}15; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 2rem; font-weight: 700; color: {primary}; transition: all 0.3s ease; }}
    .scroll-cat:hover .cat-icon {{ background: {primary}; color: {background}; transform: scale(1.1); }}
    .scroll-cat span {{ color: {text}; font-weight: 600; }}
    </style>
    '''
