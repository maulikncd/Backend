from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Mega Style - Large hero categories"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="ecom-categories-mega" id="categories">
        <div class="mega-container">
            <div class="mega-grid">
                <a href="#" class="mega-cat main"><div class="overlay"><h2>Electronics</h2><span>Shop Now →</span></div></a>
                <a href="#" class="mega-cat"><div class="overlay"><h3>Fashion</h3></div></a>
                <a href="#" class="mega-cat"><div class="overlay"><h3>Home</h3></div></a>
            </div>
        </div>
    </section>
    
    <style>
    .ecom-categories-mega {{ padding: 60px 24px; background: {background}; }}
    .mega-container {{ max-width: 1400px; margin: 0 auto; }}
    .mega-grid {{ display: grid; grid-template-columns: 2fr 1fr 1fr; gap: 20px; height: 500px; }}
    .mega-cat {{ position: relative; background: linear-gradient(135deg, {primary}25, {primary}10); border-radius: 24px; overflow: hidden; text-decoration: none; }}
    .mega-cat.main {{ }}
    .overlay {{ position: absolute; inset: 0; background: linear-gradient(to top, {text}E6, transparent 60%); display: flex; flex-direction: column; justify-content: flex-end; padding: 32px; }}
    .overlay h2 {{ font-size: 2.5rem; font-weight: 800; color: {background}; margin-bottom: 8px; }}
    .overlay h3 {{ font-size: 1.5rem; font-weight: 700; color: {background}; }}
    .overlay span {{ color: {primary}; font-weight: 600; }}
    @media (max-width: 900px) {{ .mega-grid {{ grid-template-columns: 1fr; height: auto; }} .mega-cat {{ min-height: 250px; }} }}
    </style>
    '''
