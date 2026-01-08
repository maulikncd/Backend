from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    logo = props.get("logo_text", "CAFE")
    links = props.get("links", [
        {"text": "Home", "url": "#"},
        {"text": "Menu", "url": "#menu"},
        {"text": "About", "url": "#about"},
        {"text": "Contact", "url": "#footer"}
    ])
    
    links_html = "".join([f'<a href="{l["url"]}" class="nav-link">{l["text"]}</a>' for l in links])
    
    return f'''
    <nav class="nav-floating-pill">
        <div class="pill-container">
            <a href="#" class="nav-logo">{logo}</a>
            <div class="nav-links">
                {links_html}
            </div>
            <a href="#menu" class="nav-cta">Order Now</a>
        </div>
    </nav>
    
    <style>
    .nav-floating-pill {{
        position: fixed;
        top: 24px;
        left: 50%;
        transform: translateX(-50%);
        z-index: 1000;
        width: auto;
        min-width: 600px;
    }}
    .pill-container {{
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(15px);
        padding: 8px 32px;
        border-radius: 100px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        border: 1px solid rgba(255,255,255,0.3);
    }}
    .nav-logo {{
        font-family: 'Playfair Display', serif;
        font-size: 1.4rem;
        font-weight: 700;
        color: {colors.get("text", "#2D2013")};
        text-decoration: none;
    }}
    .nav-links {{
        display: flex;
        gap: 24px;
    }}
    .nav-link {{
        color: {colors.get("text_muted", "#8B7355")};
        text-decoration: none;
        font-weight: 500;
        font-size: 0.9rem;
        transition: color 0.3s;
    }}
    .nav-link:hover {{ color: {colors.get("primary", "#6F4E37")}; }}
    .nav-cta {{
        padding: 8px 20px;
        background: {colors.get("primary", "#6F4E37")};
        color: #fff;
        text-decoration: none;
        border-radius: 50px;
        font-weight: 600;
        font-size: 0.85rem;
    }}
    @media (max-width: 768px) {{
        .nav-floating-pill {{ min-width: 90%; top: 12px; }}
        .nav-links {{ display: none; }}
    }}
    </style>
    '''
