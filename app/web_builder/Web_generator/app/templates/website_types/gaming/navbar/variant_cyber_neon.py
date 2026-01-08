from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    logo = props.get("logo", "GAMER_ZONE")
    links = props.get("links", ["Home", "Games", "Tournaments", "Shop"])
    
    primary = colors.get("primary", "#00FF88")
    
    # Build nav links separately
    nav_links = ""
    for l in links:
        nav_links += f'<a href="#{l.lower()}" class="nav-link">{l}</a>'
    
    logo_rest = logo[1:] if len(logo) > 1 else ""
    
    return f'''
    <nav class="gaming-nav gaming-nav-cyber" id="navbar">
        <div class="nav-container">
            <a href="#" class="nav-logo">
                <span class="logo-prefix">G</span>{logo_rest}
            </a>
            <div class="nav-links">
                {nav_links}
            </div>
            <div class="nav-right">
                <a href="#login" class="btn-cyber-minimal">Login</a>
                <a href="#join" class="btn-cyber-fill">Join Pro</a>
            </div>
            <div class="mobile-toggle">
                <span></span><span></span><span></span>
            </div>
        </div>
        <div class="nav-glow-line"></div>
    </nav>
    
    <style>
    .gaming-nav-cyber {{
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 1000;
        background: rgba(10, 10, 15, 0.9);
        backdrop-filter: blur(10px);
        padding: 20px 0;
        transition: 0.3s;
    }}
    .nav-container {{
        max-width: 1400px;
        margin: 0 auto;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0 40px;
    }}
    .nav-logo {{
        font-family: 'Rajdhani', sans-serif;
        font-size: 1.8rem;
        font-weight: 800;
        color: #fff;
        text-decoration: none;
        letter-spacing: 2px;
    }}
    .logo-prefix {{ color: {primary}; text-shadow: 0 0 10px {primary}; }}
    .nav-links {{ display: flex; gap: 40px; }}
    .nav-link {{
        color: #888;
        text-decoration: none;
        font-weight: 600;
        text-transform: uppercase;
        font-size: 0.9rem;
        letter-spacing: 1px;
        transition: 0.3s;
    }}
    .nav-link:hover {{ color: #fff; text-shadow: 0 0 10px rgba(255,255,255,0.5); }}
    .nav-right {{ display: flex; gap: 20px; align-items: center; }}
    .btn-cyber-minimal {{
        color: #fff;
        text-decoration: none;
        font-weight: 700;
        font-size: 0.9rem;
    }}
    .btn-cyber-fill {{
        background: {primary};
        color: #000;
        padding: 10px 25px;
        font-weight: 800;
        text-decoration: none;
        clip-path: polygon(10% 0, 100% 0, 90% 100%, 0 100%);
        transition: 0.3s;
    }}
    .btn-cyber-fill:hover {{ box-shadow: 0 0 20px {primary}80; transform: translateY(-2px); }}
    .nav-glow-line {{
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 1px;
        background: linear-gradient(90deg, transparent, {primary}, transparent);
    }}
    @media (max-width: 1024px) {{ .nav-links, .nav-right {{ display: none; }} }}
    </style>
    '''
