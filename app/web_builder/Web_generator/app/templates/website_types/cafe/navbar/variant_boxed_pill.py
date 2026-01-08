from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Boxed Contained Navbar"""
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
    <header class="navbar-boxed"><div class="nav-box"><a href="#" class="nav-logo">{logo}</a><nav class="nav-links">{links_html}</nav><a href="#contact" class="nav-cta">Book Table</a></div></header>
    <style>
    .navbar-boxed {{ position: fixed; top: 20px; left: 20px; right: 20px; z-index: 1000; }}
    .nav-box {{ max-width: 1300px; margin: 0 auto; padding: 18px 30px; display: flex; align-items: center; justify-content: space-between; background: #fff; border-radius: 60px; box-shadow: 0 10px 40px rgba(0,0,0,0.08); }}
    .nav-logo {{ font-family: 'Playfair Display', serif; font-size: 1.6rem; color: {text}; text-decoration: none; }}
    .nav-links {{ display: flex; gap: 30px; }}
    .nav-links a {{ color: {text}; text-decoration: none; font-weight: 500; font-size: 0.95rem; transition: 0.3s; }}
    .nav-links a:hover {{ color: {primary}; }}
    .nav-cta {{ padding: 12px 28px; background: {primary}; color: #fff; text-decoration: none; border-radius: 50px; font-weight: 600; font-size: 0.9rem; transition: 0.3s; }}
    .nav-cta:hover {{ transform: scale(1.05); }}
    @media (max-width: 768px) {{ .nav-links {{ display: none; }} }}
    </style>
    '''
