from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Underline Animation Navbar"""
    logo = props.get("logoText", "Cafe")
    links = props.get("links", [])
    primary = colors.get("primary", "#8B7355")
    text = colors.get("text", "#2D2013")
    
    links_html = ""
    if links:
        for link in links[:5]:
            links_html += f'<a href="{link.get("href", "#")}" class="underline-link">{link.get("text", "")}</a>'
    else:
        links_html = '<a href="#home" class="underline-link">Home</a><a href="#menu" class="underline-link">Menu</a><a href="#about" class="underline-link">About</a><a href="#contact" class="underline-link">Contact</a>'
    
    return f'''
    <header class="navbar-underline"><div class="nav-container"><a href="#" class="nav-logo">{logo}</a><nav class="nav-links">{links_html}</nav><a href="#contact" class="nav-cta">Book Now</a></div></header>
    <style>
    .navbar-underline {{ position: fixed; top: 0; left: 0; right: 0; z-index: 1000; background: rgba(255,255,255,0.98); }}
    .nav-container {{ max-width: 1300px; margin: 0 auto; padding: 22px 40px; display: flex; align-items: center; justify-content: space-between; }}
    .nav-logo {{ font-family: 'Playfair Display', serif; font-size: 1.8rem; color: {text}; text-decoration: none; }}
    .nav-links {{ display: flex; gap: 35px; }}
    .underline-link {{ color: {text}; text-decoration: none; font-weight: 500; position: relative; padding-bottom: 5px; }}
    .underline-link::after {{ content: ''; position: absolute; bottom: 0; left: 0; width: 0; height: 2px; background: {primary}; transition: width 0.3s; }}
    .underline-link:hover::after {{ width: 100%; }}
    .nav-cta {{ padding: 12px 30px; background: {text}; color: #fff; text-decoration: none; border-radius: 8px; font-weight: 600; transition: 0.3s; }}
    .nav-cta:hover {{ background: {primary}; }}
    @media (max-width: 768px) {{ .nav-links {{ display: none; }} }}
    </style>
    '''
