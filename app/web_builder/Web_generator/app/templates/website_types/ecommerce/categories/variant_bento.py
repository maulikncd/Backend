from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Bento Style - Modern bento grid"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="ecom-categories-bento" id="categories">
        <div class="bento-container">
            <div class="bento-grid">
                <a href="#" class="bento-cat main"><span class="label">Electronics</span><span class="count">250+ items</span></a>
                <a href="#" class="bento-cat"><span class="label">Fashion</span></a>
                <a href="#" class="bento-cat"><span class="label">Sports</span></a>
                <a href="#" class="bento-cat wide"><span class="label">Home & Living</span><span class="count">300+ items</span></a>
                <a href="#" class="bento-cat"><span class="label">Beauty</span></a>
            </div>
        </div>
    </section>
    
    <style>
    .ecom-categories-bento {{ padding: 100px 24px; background: {background}; }}
    .bento-container {{ max-width: 1100px; margin: 0 auto; }}
    .bento-grid {{ display: grid; grid-template-columns: repeat(4, 1fr); grid-template-rows: repeat(2, 200px); gap: 16px; }}
    .bento-cat {{ background: linear-gradient(135deg, {primary}20, {primary}05); border-radius: 20px; padding: 24px; display: flex; flex-direction: column; justify-content: flex-end; text-decoration: none; transition: all 0.4s ease; }}
    .bento-cat:hover {{ transform: scale(1.02); }}
    .bento-cat.main {{ grid-column: span 2; grid-row: span 2; }}
    .bento-cat.wide {{ grid-column: span 2; }}
    .label {{ font-size: 1.3rem; font-weight: 700; color: {text}; }}
    .bento-cat.main .label {{ font-size: 2rem; }}
    .count {{ color: {secondary}; font-size: 0.9rem; margin-top: 4px; }}
    @media (max-width: 900px) {{ .bento-grid {{ grid-template-columns: 1fr 1fr; }} .bento-cat.main {{ grid-column: span 2; grid-row: span 1; }} }}
    </style>
    '''
