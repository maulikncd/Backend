from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Centered Logo Navbar"""
    logo = props.get("logoText", "Cafe")
    links = props.get("links", [])
    primary = colors.get("primary", "#8B7355")
    text = colors.get("text", "#2D2013")
    
    left_links = links[:2] if links else [{"href": "#home", "text": "Home"}, {"href": "#menu", "text": "Menu"}]
    right_links = links[2:4] if len(links) > 2 else [{"href": "#about", "text": "About"}, {"href": "#contact", "text": "Contact"}]
    
    left_html = "".join([f'<a href="{l.get("href", "#")}">{l.get("text", "")}</a>' for l in left_links])
    right_html = "".join([f'<a href="{l.get("href", "#")}">{l.get("text", "")}</a>' for l in right_links])
    
    return f'''
    <header class="navbar-centered-logo"><div class="nav-container"><nav class="nav-left">{left_html}</nav><a href="#" class="nav-logo-center">{logo}</a><nav class="nav-right">{right_html}</nav></div></header>
    <style>
    .navbar-centered-logo {{ position: fixed; top: 0; left: 0; right: 0; z-index: 1000; background: #fff; box-shadow: 0 2px 20px rgba(0,0,0,0.05); }}
    .nav-container {{ max-width: 1200px; margin: 0 auto; padding: 25px 40px; display: grid; grid-template-columns: 1fr auto 1fr; align-items: center; }}
    .nav-left, .nav-right {{ display: flex; gap: 40px; }}
    .nav-right {{ justify-content: flex-end; }}
    .nav-left a, .nav-right a {{ color: {text}; text-decoration: none; font-weight: 500; transition: 0.3s; }}
    .nav-left a:hover, .nav-right a:hover {{ color: {primary}; }}
    .nav-logo-center {{ font-family: 'Playfair Display', serif; font-size: 2.2rem; color: {text}; text-decoration: none; }}
    @media (max-width: 768px) {{ .nav-left, .nav-right {{ display: none; }} .nav-container {{ grid-template-columns: 1fr; justify-items: center; }} }}
    </style>
    '''
