from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Sticky Transparent - Transparent that becomes solid on scroll"""
    brand = props.get("brand", "GameZone")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <nav class="gaming-nav-sticky" id="navbar">
        <div class="nav-container">
            <a href="#" class="nav-brand">{brand}</a>
            <div class="nav-links">
                <a href="#games">Games</a>
                <a href="#tournaments">Tournaments</a>
                <a href="#community">Community</a>
                <a href="#store">Store</a>
            </div>
            <div class="nav-actions">
                <a href="#login" class="btn-ghost">Sign In</a>
                <a href="#signup" class="btn-primary">Play Free</a>
            </div>
        </div>
    </nav>
    
    <style>
    .gaming-nav-sticky {{
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 1000;
        padding: 20px 40px;
        background: transparent;
        transition: all 0.3s ease;
    }}
    .gaming-nav-sticky.scrolled {{
        background: {background}F2;
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-bottom: 1px solid {text}10;
        padding: 16px 40px;
    }}
    .nav-container {{
        max-width: 1400px;
        margin: 0 auto;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }}
    .nav-brand {{
        font-family: 'Orbitron', sans-serif;
        font-size: 1.8rem;
        font-weight: 900;
        color: {primary};
        text-decoration: none;
    }}
    .nav-links {{
        display: flex;
        gap: 40px;
    }}
    .nav-links a {{
        color: {text};
        text-decoration: none;
        font-weight: 600;
        position: relative;
        transition: color 0.3s ease;
    }}
    .nav-links a::after {{
        content: '';
        position: absolute;
        bottom: -4px;
        left: 0;
        width: 0;
        height: 2px;
        background: {primary};
        transition: width 0.3s ease;
    }}
    .nav-links a:hover {{
        color: {primary};
    }}
    .nav-links a:hover::after {{
        width: 100%;
    }}
    .nav-actions {{
        display: flex;
        gap: 16px;
        align-items: center;
    }}
    .btn-ghost {{
        color: {text};
        text-decoration: none;
        font-weight: 600;
        transition: color 0.3s ease;
    }}
    .btn-ghost:hover {{
        color: {primary};
    }}
    .btn-primary {{
        padding: 12px 28px;
        background: {primary};
        color: {background};
        text-decoration: none;
        font-weight: 700;
        border-radius: 8px;
        transition: all 0.3s ease;
    }}
    .btn-primary:hover {{
        transform: scale(1.05);
        box-shadow: 0 10px 30px {primary}40;
    }}
    @media (max-width: 900px) {{
        .nav-links {{ display: none; }}
    }}
    </style>
    '''
