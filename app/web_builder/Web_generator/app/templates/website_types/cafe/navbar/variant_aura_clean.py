from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """
    Aura Premium Navbar - Clean, modern with scroll effects
    """
    logo = props.get("logo", {})
    logo_text = logo.get("text", props.get("logoText", "Cafe"))
    links = props.get("links", [])
    cta = props.get("cta", {})
    
    primary = colors.get("primary", "#8B7355")
    text = colors.get("text", "#2D2013")
    
    # Build nav links
    links_html = ""
    if links:
        for link in links[:6]:
            links_html += f'<a href="{link.get("href", "#")}" class="nav-link">{link.get("text", "Link")}</a>'
    else:
        links_html = '''
            <a href="#home" class="nav-link">Home</a>
            <a href="#about" class="nav-link">About</a>
            <a href="#menu" class="nav-link">Menu</a>
            <a href="#gallery" class="nav-link">Gallery</a>
            <a href="#contact" class="nav-link">Contact</a>
        '''
    
    cta_text = cta.get("text", "Book a Table")
    cta_href = cta.get("href", "#contact")
    
    return f'''
    <header class="aura-navbar" id="navbar">
        <div class="navbar-container">
            <a href="#home" class="navbar-logo">{logo_text}</a>
            <nav class="navbar-links">
                {links_html}
            </nav>
            <div class="navbar-right">
                <a href="{cta_href}" class="navbar-cta">{cta_text}</a>
                <button class="mobile-toggle" aria-label="Menu">
                    <span></span>
                    <span></span>
                    <span></span>
                </button>
            </div>
        </div>
    </header>
    
    <style>
    .aura-navbar {{
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 1000;
        background: rgba(255,255,255,0.95);
        backdrop-filter: blur(10px);
        border-bottom: 1px solid rgba(0,0,0,0.05);
        transition: all 0.3s;
    }}
    .aura-navbar.scrolled {{
        box-shadow: 0 5px 30px rgba(0,0,0,0.08);
    }}
    .navbar-container {{
        max-width: 1400px;
        margin: 0 auto;
        padding: 20px 40px;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }}
    .navbar-logo {{
        font-family: 'Playfair Display', serif;
        font-size: 1.8rem;
        font-weight: 700;
        color: {text};
        text-decoration: none;
        letter-spacing: -0.5px;
    }}
    .navbar-links {{
        display: flex;
        gap: 40px;
    }}
    .navbar-links .nav-link {{
        color: #666;
        text-decoration: none;
        font-weight: 500;
        font-size: 0.95rem;
        position: relative;
        transition: color 0.3s;
    }}
    .navbar-links .nav-link:hover {{
        color: {primary};
    }}
    .navbar-links .nav-link::after {{
        content: '';
        position: absolute;
        bottom: -5px;
        left: 0;
        width: 0;
        height: 2px;
        background: {primary};
        transition: width 0.3s;
    }}
    .navbar-links .nav-link:hover::after {{
        width: 100%;
    }}
    .navbar-right {{
        display: flex;
        align-items: center;
        gap: 20px;
    }}
    .navbar-cta {{
        padding: 12px 28px;
        background: {primary};
        color: #fff;
        text-decoration: none;
        border-radius: 50px;
        font-weight: 600;
        font-size: 0.9rem;
        transition: all 0.3s;
    }}
    .navbar-cta:hover {{
        transform: translateY(-2px);
        box-shadow: 0 10px 25px {primary}40;
    }}
    .mobile-toggle {{
        display: none;
        background: none;
        border: none;
        cursor: pointer;
        padding: 8px;
    }}
    .mobile-toggle span {{
        display: block;
        width: 25px;
        height: 2px;
        background: {text};
        margin: 5px 0;
        transition: 0.3s;
    }}
    @media (max-width: 968px) {{
        .navbar-links {{ display: none; }}
        .mobile-toggle {{ display: block; }}
        .navbar-container {{ padding: 16px 24px; }}
    }}
    </style>
    
    <script>
    (function() {{
        const navbar = document.querySelector('.aura-navbar');
        if (navbar) {{
            window.addEventListener('scroll', function() {{
                if (window.scrollY > 50) {{
                    navbar.classList.add('scrolled');
                }} else {{
                    navbar.classList.remove('scrolled');
                }}
            }});
        }}
    }})();
    </script>
    '''
