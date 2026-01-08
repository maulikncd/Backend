from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Bottom Bar - Mobile-style bottom navigation"""
    brand = props.get("brand", "GameZone")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <nav class="gaming-nav-bottom" id="navbar">
        <div class="top-bar">
            <a href="#" class="nav-brand">{brand}</a>
            <div class="top-links">
                <a href="#games">Games</a>
                <a href="#tournaments">Tournaments</a>
                <a href="#community">Community</a>
                <a href="#store">Store</a>
            </div>
            <div class="top-actions">
                <a href="#login">Login</a>
                <a href="#signup" class="btn-cta">Sign Up</a>
            </div>
        </div>
        <div class="bottom-nav">
            <a href="#" class="bottom-item active">
                <span class="icon">🏠</span>
                <span class="label">Home</span>
            </a>
            <a href="#games" class="bottom-item">
                <span class="icon">🎮</span>
                <span class="label">Games</span>
            </a>
            <a href="#play" class="bottom-item center">
                <span class="icon">▶️</span>
            </a>
            <a href="#community" class="bottom-item">
                <span class="icon">👥</span>
                <span class="label">Community</span>
            </a>
            <a href="#profile" class="bottom-item">
                <span class="icon">👤</span>
                <span class="label">Profile</span>
            </a>
        </div>
    </nav>
    
    <style>
    .gaming-nav-bottom {{
        position: fixed;
        z-index: 1000;
    }}
    .top-bar {{
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 16px 40px;
        background: {background};
        border-bottom: 1px solid {text}10;
    }}
    .nav-brand {{
        font-family: 'Orbitron', sans-serif;
        font-size: 1.5rem;
        font-weight: 900;
        color: {primary};
        text-decoration: none;
    }}
    .top-links {{
        display: flex;
        gap: 32px;
    }}
    .top-links a {{
        color: {secondary};
        text-decoration: none;
        font-weight: 600;
        transition: color 0.3s ease;
    }}
    .top-links a:hover {{
        color: {primary};
    }}
    .top-actions {{
        display: flex;
        align-items: center;
        gap: 20px;
    }}
    .top-actions a {{
        color: {text};
        text-decoration: none;
        font-weight: 600;
    }}
    .btn-cta {{
        padding: 10px 24px;
        background: {primary};
        color: {background} !important;
        border-radius: 8px;
        transition: all 0.3s ease;
    }}
    .btn-cta:hover {{
        transform: scale(1.05);
    }}
    .bottom-nav {{
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        display: none;
        justify-content: space-around;
        align-items: center;
        padding: 12px 8px 24px;
        background: {background};
        border-top: 1px solid {text}10;
    }}
    .bottom-item {{
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 4px;
        text-decoration: none;
        color: {secondary};
        transition: all 0.3s ease;
    }}
    .bottom-item.active {{
        color: {primary};
    }}
    .bottom-item .icon {{
        font-size: 1.5rem;
    }}
    .bottom-item .label {{
        font-size: 0.7rem;
        font-weight: 600;
    }}
    .bottom-item.center {{
        width: 56px;
        height: 56px;
        background: {primary};
        border-radius: 50%;
        margin-top: -30px;
        box-shadow: 0 4px 20px {primary}40;
    }}
    .bottom-item.center .icon {{
        font-size: 1.8rem;
    }}
    @media (max-width: 768px) {{
        .top-links, .top-actions {{ display: none; }}
        .bottom-nav {{ display: flex; }}
    }}
    </style>
    '''
