from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    logo = props.get("logo", "GAMER")
    
    return f'''
    <nav class="gaming-nav-minimal">
        <div class="nav-content">
            <a href="#" class="logo">{logo}</a>
            <div class="links">
                <a href="#games">Games</a>
                <a href="#media">Media</a>
                <a href="#about">About</a>
                <a href="#contact">Contact</a>
            </div>
            <div class="actions">
                <button class="btn-search">🔍</button>
            </div>
        </div>
    </nav>
    
    <style>
    .gaming-nav-minimal {{
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 1000;
        background: #000;
        padding: 15px 0;
        border-bottom: 2px solid #111;
    }}
    .nav-content {{
        max-width: 1200px;
        margin: 0 auto;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0 20px;
    }}
    .logo {{
        font-family: 'Orbitron', sans-serif;
        font-weight: 700;
        font-size: 1.5rem;
        color: #fff;
        text-decoration: none;
    }}
    .links {{ display: flex; gap: 30px; }}
    .links a {{
        color: #666;
        text-decoration: none;
        font-size: 0.85rem;
        text-transform: uppercase;
        font-weight: 600;
        transition: 0.3s;
    }}
    .links a:hover {{ color: {colors.get("primary", "#00FF88")}; }}
    .btn-search {{
        background: none;
        border: none;
        color: #fff;
        font-size: 1.2rem;
        cursor: pointer;
    }}
    </style>
    '''
