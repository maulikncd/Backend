from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Sidebar Toggle Navbar"""
    logo = props.get("logoText", "Cafe")
    primary = colors.get("primary", "#8B7355")
    text = colors.get("text", "#2D2013")
    
    return f'''
    <header class="navbar-sidebar-toggle"><div class="nav-container"><a href="#" class="nav-logo">{logo}</a><button class="menu-toggle"><span></span><span></span><span></span></button></div></header>
    <style>
    .navbar-sidebar-toggle {{ position: fixed; top: 0; left: 0; right: 0; z-index: 1000; background: transparent; }}
    .nav-container {{ max-width: 1400px; margin: 0 auto; padding: 30px 40px; display: flex; align-items: center; justify-content: space-between; }}
    .nav-logo {{ font-family: 'Playfair Display', serif; font-size: 2rem; color: {text}; text-decoration: none; }}
    .menu-toggle {{ background: {primary}; border: none; padding: 15px; border-radius: 12px; cursor: pointer; display: flex; flex-direction: column; gap: 5px; }}
    .menu-toggle span {{ display: block; width: 25px; height: 2px; background: #fff; transition: 0.3s; }}
    .menu-toggle:hover span:nth-child(2) {{ width: 18px; }}
    </style>
    '''
