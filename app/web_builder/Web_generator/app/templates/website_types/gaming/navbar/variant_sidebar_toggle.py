from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Sidebar Toggle - Collapsible sidebar navigation"""
    brand = props.get("brand", "GameZone")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <nav class="gaming-nav-sidebar" id="navbar">
        <div class="nav-bar">
            <a href="#" class="nav-brand">{brand}</a>
            <button class="menu-toggle" onclick="document.querySelector('.side-menu').classList.toggle('open')">
                <span></span>
                <span></span>
                <span></span>
            </button>
        </div>
        <div class="side-menu">
            <div class="side-header">
                <span class="side-brand">{brand}</span>
                <button class="close-btn" onclick="document.querySelector('.side-menu').classList.remove('open')">✕</button>
            </div>
            <div class="side-links">
                <a href="#home">Home</a>
                <a href="#games">Games</a>
                <a href="#tournaments">Tournaments</a>
                <a href="#community">Community</a>
                <a href="#store">Store</a>
                <a href="#support">Support</a>
            </div>
            <div class="side-footer">
                <a href="#login" class="btn-side">Sign In</a>
                <a href="#signup" class="btn-side primary">Create Account</a>
            </div>
        </div>
        <div class="side-overlay" onclick="document.querySelector('.side-menu').classList.remove('open')"></div>
    </nav>
    
    <style>
    .gaming-nav-sidebar {{
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 1000;
    }}
    .nav-bar {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 20px 24px;
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
    .menu-toggle {{
        display: flex;
        flex-direction: column;
        gap: 6px;
        background: none;
        border: none;
        cursor: pointer;
        padding: 8px;
    }}
    .menu-toggle span {{
        width: 28px;
        height: 3px;
        background: {text};
        border-radius: 2px;
        transition: all 0.3s ease;
    }}
    .side-menu {{
        position: fixed;
        top: 0;
        right: -320px;
        width: 320px;
        height: 100vh;
        background: {background};
        padding: 24px;
        display: flex;
        flex-direction: column;
        transition: right 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        z-index: 1001;
        box-shadow: -20px 0 60px {background};
    }}
    .side-menu.open {{
        right: 0;
    }}
    .side-overlay {{
        position: fixed;
        inset: 0;
        background: {background}80;
        opacity: 0;
        visibility: hidden;
        transition: all 0.3s ease;
        z-index: 1000;
    }}
    .side-menu.open ~ .side-overlay {{
        opacity: 1;
        visibility: visible;
    }}
    .side-header {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 40px;
    }}
    .side-brand {{
        font-family: 'Orbitron', sans-serif;
        font-size: 1.3rem;
        font-weight: 900;
        color: {primary};
    }}
    .close-btn {{
        background: {text}10;
        border: none;
        width: 40px;
        height: 40px;
        border-radius: 10px;
        color: {text};
        font-size: 1.2rem;
        cursor: pointer;
        transition: all 0.3s ease;
    }}
    .close-btn:hover {{
        background: {primary}20;
        color: {primary};
    }}
    .side-links {{
        flex: 1;
        display: flex;
        flex-direction: column;
    }}
    .side-links a {{
        color: {text};
        text-decoration: none;
        font-size: 1.2rem;
        font-weight: 600;
        padding: 16px 0;
        border-bottom: 1px solid {text}08;
        transition: all 0.3s ease;
    }}
    .side-links a:hover {{
        color: {primary};
        padding-left: 12px;
    }}
    .side-footer {{
        display: flex;
        flex-direction: column;
        gap: 12px;
        margin-top: 24px;
    }}
    .btn-side {{
        padding: 16px;
        text-align: center;
        text-decoration: none;
        font-weight: 700;
        border-radius: 12px;
        transition: all 0.3s ease;
        color: {text};
        background: {text}08;
    }}
    .btn-side.primary {{
        background: {primary};
        color: {background};
    }}
    .btn-side:hover {{
        transform: scale(1.02);
    }}
    </style>
    '''
