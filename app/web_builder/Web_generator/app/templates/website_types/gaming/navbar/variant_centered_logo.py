from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Centered Logo - Logo centered with links on sides"""
    brand = props.get("brand", "GameZone")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <nav class="gaming-nav-centered" id="navbar">
        <div class="nav-container">
            <div class="nav-left">
                <a href="#games">Games</a>
                <a href="#tournaments">Tournaments</a>
                <a href="#community">Community</a>
            </div>
            <a href="#" class="nav-brand-center">
                <div class="brand-logo">{brand[0]}</div>
                <span>{brand}</span>
            </a>
            <div class="nav-right">
                <a href="#store">Store</a>
                <a href="#support">Support</a>
                <a href="#signup" class="btn-join">Join Now</a>
            </div>
        </div>
    </nav>
    
    <style>
    .gaming-nav-centered {{
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 1000;
        background: {background};
        padding: 16px 40px;
        border-bottom: 1px solid {text}08;
    }}
    .nav-container {{
        max-width: 1400px;
        margin: 0 auto;
        display: grid;
        grid-template-columns: 1fr auto 1fr;
        align-items: center;
        gap: 40px;
    }}
    .nav-left {{
        display: flex;
        justify-content: flex-end;
        gap: 32px;
    }}
    .nav-right {{
        display: flex;
        align-items: center;
        gap: 32px;
    }}
    .nav-left a, .nav-right a {{
        color: {secondary};
        text-decoration: none;
        font-weight: 600;
        transition: color 0.3s ease;
    }}
    .nav-left a:hover, .nav-right a:hover {{
        color: {primary};
    }}
    .nav-brand-center {{
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 4px;
        text-decoration: none;
    }}
    .brand-logo {{
        width: 50px;
        height: 50px;
        background: linear-gradient(135deg, {primary}, {secondary});
        color: {background};
        font-family: 'Orbitron', sans-serif;
        font-size: 1.5rem;
        font-weight: 900;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 12px;
    }}
    .nav-brand-center span {{
        font-family: 'Orbitron', sans-serif;
        font-size: 0.85rem;
        font-weight: 700;
        color: {text};
        letter-spacing: 2px;
    }}
    .btn-join {{
        padding: 10px 24px;
        background: {primary};
        color: {background} !important;
        border-radius: 8px;
        font-weight: 700;
        transition: all 0.3s ease;
    }}
    .btn-join:hover {{
        transform: scale(1.05);
        box-shadow: 0 10px 30px {primary}40;
    }}
    @media (max-width: 900px) {{
        .nav-left, .nav-right {{ display: none; }}
        .nav-container {{ display: flex; justify-content: center; }}
    }}
    </style>
    '''
