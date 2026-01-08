from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Luxury Elegant Navbar - High-end design with serif fonts and gold accents"""
    logo = props.get("logo_text", props.get("logo", "Brand"))
    links = props.get("links", [
        {"text": "Home", "url": "#home"},
        {"text": "About", "url": "#about"},
        {"text": "Menu", "url": "#menu"},
        {"text": "Gallery", "url": "#gallery"},
        {"text": "Contact", "url": "#contact"}
    ])
    cta_text = props.get("cta_text", "Reserve Table")
    cta_url = props.get("cta_url", "#contact")
    
    links_html = ""
    for i, link in enumerate(links):
        links_html += f'''<a href="{link.get("url", "#")}" class="luxury-link"><span class="link-num">0{i+1}</span>{link.get("text", "Link")}</a>'''
    
    primary = colors.get("primary", "#B8860B")
    
    return f'''
    <!-- Luxury Elegant Navbar -->
    <nav id="luxury-navbar" class="luxury-navbar">
        <div class="luxury-nav-inner">
            <!-- Left Side -->
            <div class="luxury-left">
                <a href="#" class="luxury-logo">
                    <span class="logo-decorator">❖</span>
                    <span class="logo-main">{logo}</span>
                    <span class="logo-decorator">❖</span>
                </a>
            </div>
            
            <!-- Center: Navigation -->
            <div class="luxury-center">
                <div class="luxury-links">
                    {links_html}
                </div>
            </div>
            
            <!-- Right Side -->
            <div class="luxury-right">
                <a href="{cta_url}" class="luxury-cta">
                    <span class="cta-line"></span>
                    <span class="cta-label">{cta_text}</span>
                    <span class="cta-line"></span>
                </a>
            </div>
            
            <!-- Mobile Toggle -->
            <button class="luxury-mobile-toggle" onclick="toggleLuxuryMenu()">
                <span></span><span></span>
            </button>
        </div>
        
        <!-- Mobile Menu -->
        <div class="luxury-mobile-menu" id="luxury-mobile-menu">
            <div class="mobile-menu-content">
                {links_html}
                <a href="{cta_url}" class="luxury-mobile-cta">{cta_text}</a>
            </div>
        </div>
    </nav>
    
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&display=swap');
    
    .luxury-navbar {{
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 9999;
        padding: 24px 48px;
        transition: all 0.6s cubic-bezier(0.4, 0, 0.2, 1);
    }}
    
    .luxury-navbar.scrolled {{
        padding: 16px 48px;
        background: rgba(255, 252, 247, 0.98);
        backdrop-filter: blur(16px);
        box-shadow: 0 1px 0 rgba(0, 0, 0, 0.05);
    }}
    
    .luxury-nav-inner {{
        max-width: 1400px;
        margin: 0 auto;
        display: grid;
        grid-template-columns: 1fr auto 1fr;
        align-items: center;
        gap: 40px;
    }}
    
    /* Logo */
    .luxury-logo {{
        display: flex;
        align-items: center;
        gap: 16px;
        text-decoration: none;
        color: #fff;
    }}
    
    .scrolled .luxury-logo {{
        color: #1a1a1a;
    }}
    
    .logo-decorator {{
        color: {primary};
        font-size: 0.75rem;
        opacity: 0.8;
    }}
    
    .logo-main {{
        font-family: 'Cormorant Garamond', serif;
        font-size: 2rem;
        font-weight: 600;
        letter-spacing: 0.15em;
        text-transform: uppercase;
    }}
    
    /* Links */
    .luxury-links {{
        display: flex;
        align-items: center;
        gap: 48px;
    }}
    
    .luxury-link {{
        position: relative;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 4px;
        text-decoration: none;
        color: rgba(255, 255, 255, 0.85);
        font-family: 'Cormorant Garamond', serif;
        font-size: 1rem;
        font-weight: 500;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        transition: all 0.3s ease;
    }}
    
    .scrolled .luxury-link {{
        color: #4a4a4a;
    }}
    
    .luxury-link:hover {{
        color: {primary};
    }}
    
    .link-num {{
        font-size: 0.65rem;
        letter-spacing: 0.05em;
        opacity: 0.5;
    }}
    
    .luxury-link::after {{
        content: '';
        position: absolute;
        bottom: -8px;
        left: 50%;
        transform: translateX(-50%);
        width: 0;
        height: 1px;
        background: {primary};
        transition: width 0.4s ease;
    }}
    
    .luxury-link:hover::after {{
        width: 100%;
    }}
    
    /* CTA */
    .luxury-right {{
        display: flex;
        justify-content: flex-end;
    }}
    
    .luxury-cta {{
        display: flex;
        align-items: center;
        gap: 16px;
        text-decoration: none;
        color: #fff;
        font-family: 'Cormorant Garamond', serif;
        font-size: 0.9rem;
        font-weight: 500;
        letter-spacing: 0.15em;
        text-transform: uppercase;
        transition: all 0.3s ease;
    }}
    
    .scrolled .luxury-cta {{
        color: #1a1a1a;
    }}
    
    .cta-line {{
        width: 40px;
        height: 1px;
        background: {primary};
        transition: width 0.3s ease;
    }}
    
    .luxury-cta:hover .cta-line {{
        width: 24px;
    }}
    
    .luxury-cta:hover {{
        color: {primary};
    }}
    
    /* Mobile Toggle */
    .luxury-mobile-toggle {{
        display: none;
        flex-direction: column;
        gap: 8px;
        padding: 12px;
        background: transparent;
        border: 1px solid rgba(255, 255, 255, 0.2);
        cursor: pointer;
    }}
    
    .scrolled .luxury-mobile-toggle {{
        border-color: rgba(0, 0, 0, 0.1);
    }}
    
    .luxury-mobile-toggle span {{
        width: 28px;
        height: 1px;
        background: #fff;
        transition: all 0.3s ease;
    }}
    
    .scrolled .luxury-mobile-toggle span {{
        background: #1a1a1a;
    }}
    
    /* Mobile Menu */
    .luxury-mobile-menu {{
        display: none;
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(26, 26, 26, 0.98);
        padding: 100px 40px 40px;
        opacity: 0;
        transition: opacity 0.4s ease;
    }}
    
    .luxury-mobile-menu.active {{
        display: block;
        opacity: 1;
    }}
    
    .mobile-menu-content {{
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 32px;
    }}
    
    .luxury-mobile-menu .luxury-link {{
        color: rgba(255, 255, 255, 0.9);
        font-size: 1.5rem;
    }}
    
    .luxury-mobile-cta {{
        margin-top: 40px;
        padding: 20px 48px;
        background: transparent;
        border: 1px solid {primary};
        color: {primary};
        text-decoration: none;
        font-family: 'Cormorant Garamond', serif;
        font-size: 1rem;
        letter-spacing: 0.15em;
        text-transform: uppercase;
        transition: all 0.3s ease;
    }}
    
    .luxury-mobile-cta:hover {{
        background: {primary};
        color: #fff;
    }}
    
    @media (max-width: 1024px) {{
        .luxury-links,
        .luxury-right {{
            display: none;
        }}
        
        .luxury-mobile-toggle {{
            display: flex;
        }}
        
        .luxury-nav-inner {{
            grid-template-columns: 1fr auto;
        }}
        
        .luxury-navbar {{
            padding: 16px 24px;
        }}
    }}
    </style>
    
    <script>
    window.addEventListener('scroll', () => {{
        const nav = document.getElementById('luxury-navbar');
        if (window.scrollY > 80) {{
            nav.classList.add('scrolled');
        }} else {{
            nav.classList.remove('scrolled');
        }}
    }});
    
    function toggleLuxuryMenu() {{
        document.getElementById('luxury-mobile-menu').classList.toggle('active');
    }}
    </script>
    '''
