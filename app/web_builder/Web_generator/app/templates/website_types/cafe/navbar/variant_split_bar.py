from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Split Bar Navbar - Top accent bar with main nav below"""
    logo = props.get("logoText", "Cafe")
    links = props.get("links", [])
    primary = colors.get("primary", "#8B7355")
    text = colors.get("text", "#2D2013")
    
    links_html = ""
    if links:
        for link in links[:5]:
            links_html += f'<a href="{link.get("href", "#")}">{link.get("text", "")}</a>'
    else:
        links_html = '<a href="#home">Home</a><a href="#menu">Menu</a><a href="#about">About</a><a href="#gallery">Gallery</a><a href="#contact">Contact</a>'
    
    return f'''
    <header class="navbar-split-bar"><div class="top-bar"><span>📍 123 Coffee Lane, NYC</span><span>☎ +1 (555) 123-4567</span></div><div class="main-nav"><div class="nav-container"><a href="#" class="nav-logo">{logo}</a><nav class="nav-links">{links_html}</nav><a href="#contact" class="nav-cta">Reserve</a></div></div></header>
    <style>
    .navbar-split-bar {{ position: fixed; top: 0; left: 0; right: 0; z-index: 1000; }}
    .top-bar {{ background: {primary}; padding: 10px 40px; display: flex; justify-content: space-between; color: #fff; font-size: 0.85rem; }}
    .main-nav {{ background: #fff; box-shadow: 0 2px 20px rgba(0,0,0,0.05); }}
    .nav-container {{ max-width: 1300px; margin: 0 auto; padding: 18px 40px; display: flex; align-items: center; justify-content: space-between; }}
    .nav-logo {{ font-family: 'Playfair Display', serif; font-size: 1.8rem; color: {text}; text-decoration: none; }}
    .nav-links {{ display: flex; gap: 35px; }}
    .nav-links a {{ color: {text}; text-decoration: none; font-weight: 500; transition: 0.3s; }}
    .nav-links a:hover {{ color: {primary}; }}
    .nav-cta {{ padding: 12px 28px; background: {primary}; color: #fff; text-decoration: none; border-radius: 50px; font-weight: 600; }}
    @media (max-width: 768px) {{ .top-bar {{ display: none; }} .nav-links {{ display: none; }} }}
    </style>
    '''
