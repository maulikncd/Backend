from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Animated Pills - Pill-style links with animations"""
    brand = props.get("brand", "GameZone")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <nav class="gaming-nav-pills" id="navbar">
        <div class="nav-container">
            <a href="#" class="nav-brand">
                <div class="brand-hex">{brand[0]}</div>
                <span>{brand}</span>
            </a>
            <div class="nav-pills">
                <a href="#games" class="pill active">Games</a>
                <a href="#tournaments" class="pill">Tournaments</a>
                <a href="#community" class="pill">Community</a>
                <a href="#store" class="pill">Store</a>
            </div>
            <div class="nav-actions">
                <a href="#" class="user-btn">👤</a>
                <a href="#signup" class="btn-glow">Play Now</a>
            </div>
        </div>
    </nav>
    
    <style>
    .gaming-nav-pills {{
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 1000;
        padding: 16px 40px;
        background: {background}F2;
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
    }}
    .nav-container {{
        max-width: 1400px;
        margin: 0 auto;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }}
    .nav-brand {{
        display: flex;
        align-items: center;
        gap: 12px;
        text-decoration: none;
    }}
    .brand-hex {{
        width: 45px;
        height: 45px;
        background: {primary};
        color: {background};
        font-family: 'Orbitron', sans-serif;
        font-size: 1.3rem;
        font-weight: 900;
        display: flex;
        align-items: center;
        justify-content: center;
        clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);
    }}
    .nav-brand span {{
        font-family: 'Orbitron', sans-serif;
        font-size: 1.3rem;
        font-weight: 800;
        color: {text};
    }}
    .nav-pills {{
        display: flex;
        gap: 8px;
        padding: 6px;
        background: {text}08;
        border-radius: 100px;
    }}
    .pill {{
        padding: 12px 24px;
        color: {secondary};
        text-decoration: none;
        font-weight: 600;
        border-radius: 100px;
        transition: all 0.3s ease;
    }}
    .pill:hover {{
        color: {text};
        background: {text}08;
    }}
    .pill.active {{
        background: {primary};
        color: {background};
        box-shadow: 0 4px 20px {primary}40;
    }}
    .nav-actions {{
        display: flex;
        align-items: center;
        gap: 16px;
    }}
    .user-btn {{
        width: 44px;
        height: 44px;
        background: {text}08;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.2rem;
        text-decoration: none;
        transition: all 0.3s ease;
    }}
    .user-btn:hover {{
        background: {primary}20;
    }}
    .btn-glow {{
        padding: 12px 28px;
        background: {primary};
        color: {background};
        text-decoration: none;
        font-weight: 700;
        border-radius: 10px;
        position: relative;
        overflow: hidden;
        transition: all 0.3s ease;
    }}
    .btn-glow::before {{
        content: '';
        position: absolute;
        inset: -2px;
        background: linear-gradient(90deg, {primary}, {secondary}, {primary});
        z-index: -1;
        border-radius: 12px;
        opacity: 0;
        filter: blur(10px);
        transition: opacity 0.3s ease;
    }}
    .btn-glow:hover {{
        transform: scale(1.05);
    }}
    .btn-glow:hover::before {{
        opacity: 1;
    }}
    @media (max-width: 900px) {{
        .nav-pills {{ display: none; }}
    }}
    </style>
    '''
