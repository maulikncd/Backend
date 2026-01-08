from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Dark Overlay Navbar"""
    logo = props.get("logoText", "Cafe")
    links = props.get("links", [])
    primary = colors.get("primary", "#8B7355")
    
    links_html = ""
    if links:
        for link in links[:5]:
            links_html += f'<a href="{link.get("href", "#")}">{link.get("text", "")}</a>'
    else:
        links_html = '<a href="#home">Home</a><a href="#menu">Menu</a><a href="#about">About</a><a href="#gallery">Gallery</a><a href="#contact">Contact</a>'
    
    return f'''
    <header class="navbar-dark-overlay"><div class="nav-container"><a href="#" class="nav-logo">{logo}</a><nav class="nav-links">{links_html}</nav><a href="#contact" class="nav-cta">Reserve</a></div></header>
    <style>
    .navbar-dark-overlay {{ position: fixed; top: 0; left: 0; right: 0; z-index: 1000; background: rgba(13,13,13,0.95); backdrop-filter: blur(10px); }}
    .nav-container {{ max-width: 1400px; margin: 0 auto; padding: 20px 40px; display: flex; align-items: center; justify-content: space-between; }}
    .nav-logo {{ font-family: 'Playfair Display', serif; font-size: 1.8rem; color: #fff; text-decoration: none; }}
    .nav-links {{ display: flex; gap: 35px; }}
    .nav-links a {{ color: rgba(255,255,255,0.7); text-decoration: none; font-size: 0.95rem; transition: 0.3s; }}
    .nav-links a:hover {{ color: {primary}; }}
    .nav-cta {{ padding: 12px 28px; background: {primary}; color: #fff; text-decoration: none; border-radius: 50px; font-weight: 600; transition: 0.3s; }}
    .nav-cta:hover {{ transform: translateY(-2px); }}
    @media (max-width: 768px) {{ .nav-links {{ display: none; }} }}
    </style>
    '''
