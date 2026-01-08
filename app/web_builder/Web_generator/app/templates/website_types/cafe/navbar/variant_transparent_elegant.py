from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    logo = props.get("logo_text", "CAFE")
    links = props.get("links", [
        {"text": "Home", "url": "#"},
        {"text": "Menu", "url": "#menu"},
        {"text": "About", "url": "#about"},
        {"text": "Gallery", "url": "#gallery"},
        {"text": "Contact", "url": "#footer"}
    ])
    
    links_html = "".join([f'<a href="{l["url"]}" class="nav-link">{l["text"]}</a>' for l in links])
    
    return f'''
    <nav class="cafe-nav nav-transparent" id="navbar">
        <div class="nav-container">
            <a href="#" class="nav-logo">{logo}</a>
            <div class="nav-links">
                {links_html}
            </div>
            <a href="#menu" class="nav-cta">Reserve</a>
        </div>
    </nav>
    
    <style>
    .nav-transparent {{
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 1000;
        padding: 24px;
        transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        background: transparent;
    }}
    .nav-transparent.scrolled {{
        padding: 16px 24px;
        background: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(20px);
        box-shadow: 0 4px 30px rgba(0,0,0,0.05);
    }}
    .nav-container {{
        max-width: 1200px;
        margin: 0 auto;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }}
    .nav-logo {{
        font-family: 'Playfair Display', serif;
        font-size: 1.8rem;
        font-weight: 700;
        color: #fff;
        text-decoration: none;
        letter-spacing: 1px;
    }}
    .scrolled .nav-logo {{ color: {colors.get("text", "#2D2013")}; }}
    .nav-links {{
        display: flex;
        gap: 32px;
    }}
    .nav-link {{
        color: rgba(255,255,255,0.8);
        text-decoration: none;
        font-weight: 500;
        font-size: 0.95rem;
        transition: color 0.3s;
    }}
    .scrolled .nav-link {{ color: {colors.get("text_muted", "#8B7355")}; }}
    .nav-link:hover {{ color: #fff; }}
    .scrolled .nav-link:hover {{ color: {colors.get("primary", "#6F4E37")}; }}
    .nav-cta {{
        padding: 10px 24px;
        background: {colors.get("primary", "#6F4E37")};
        color: #fff;
        text-decoration: none;
        border-radius: 50px;
        font-weight: 600;
        font-size: 0.9rem;
        transition: transform 0.3s;
    }}
    .nav-cta:hover {{ transform: scale(1.05); }}
    </style>
    
    <script>
    window.addEventListener('scroll', () => {{
        const nav = document.getElementById('navbar');
        if (window.scrollY > 50) {{
            nav.classList.add('scrolled');
        }} else {{
            nav.classList.remove('scrolled');
        }}
    }});
    </script>
    '''
