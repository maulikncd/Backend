from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Minimal Line Navbar"""
    logo = props.get("logoText", "Cafe")
    links = props.get("links", [])
    primary = colors.get("primary", "#8B7355")
    text = colors.get("text", "#2D2013")
    
    links_html = ""
    if links:
        for link in links[:4]:
            links_html += f'<a href="{link.get("href", "#")}">{link.get("text", "")}</a>'
    else:
        links_html = '<a href="#home">Home</a><a href="#menu">Menu</a><a href="#about">About</a><a href="#contact">Contact</a>'
    
    return f'''
    <header class="navbar-minimal-line"><div class="nav-container"><a href="#" class="nav-logo">{logo}</a><nav class="nav-links">{links_html}</nav></div><div class="nav-line"></div></header>
    <style>
    .navbar-minimal-line {{ position: fixed; top: 0; left: 0; right: 0; z-index: 1000; background: #fff; }}
    .nav-container {{ max-width: 1200px; margin: 0 auto; padding: 25px 40px; display: flex; align-items: center; justify-content: space-between; }}
    .nav-logo {{ font-family: 'Playfair Display', serif; font-size: 1.8rem; color: {text}; text-decoration: none; }}
    .nav-links {{ display: flex; gap: 40px; }}
    .nav-links a {{ color: #666; text-decoration: none; font-weight: 400; transition: 0.3s; }}
    .nav-links a:hover {{ color: {primary}; }}
    .nav-line {{ height: 1px; background: linear-gradient(90deg, transparent, {primary}, transparent); }}
    @media (max-width: 768px) {{ .nav-links {{ display: none; }} }}
    </style>
    '''
