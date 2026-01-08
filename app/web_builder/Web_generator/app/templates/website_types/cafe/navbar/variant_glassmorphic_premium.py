from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Premium Glassmorphic Navbar - Ultra Modern with glass effect and smooth animations"""
    logo = props.get("logo_text", props.get("logo", "Brand"))
    links = props.get("links", [
        {"text": "Home", "url": "#home"},
        {"text": "About", "url": "#about"},
        {"text": "Services", "url": "#services"},
        {"text": "Contact", "url": "#contact"}
    ])
    cta_text = props.get("cta_text", "Get Started")
    cta_url = props.get("cta_url", "#contact")
    
    links_html = ""
    for link in links:
        links_html += f'''
            <a href="{link.get("url", "#")}" class="premium-nav-link group">
                <span class="link-text">{link.get("text", "Link")}</span>
                <span class="link-underline"></span>
            </a>'''
    
    primary = colors.get("primary", "#6366F1")
    secondary = colors.get("secondary", "#EC4899")
    
    return f'''
    <!-- Premium Glassmorphic Navbar -->
    <nav id="premium-navbar" class="premium-navbar">
        <div class="nav-inner">
            <!-- Logo -->
            <a href="#" class="nav-logo-wrapper">
                <span class="logo-icon">✦</span>
                <span class="logo-text">{logo}</span>
            </a>
            
            <!-- Desktop Links -->
            <div class="nav-links-wrapper">
                {links_html}
            </div>
            
            <!-- CTA Button -->
            <a href="{cta_url}" class="nav-cta-btn">
                <span class="cta-text">{cta_text}</span>
                <span class="cta-arrow">→</span>
            </a>
            
            <!-- Mobile Menu Toggle -->
            <button class="mobile-menu-toggle" onclick="toggleMobileMenu()">
                <span class="hamburger-line"></span>
                <span class="hamburger-line"></span>
                <span class="hamburger-line"></span>
            </button>
        </div>
        
        <!-- Mobile Menu -->
        <div class="mobile-menu" id="mobile-menu">
            <div class="mobile-menu-inner">
                {links_html}
                <a href="{cta_url}" class="mobile-cta">{cta_text}</a>
            </div>
        </div>
    </nav>
    
    <style>
    .premium-navbar {{
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 9999;
        padding: 16px 24px;
        transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
    }}
    
    .premium-navbar.scrolled {{
        padding: 12px 24px;
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(20px) saturate(180%);
        -webkit-backdrop-filter: blur(20px) saturate(180%);
        border-bottom: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.08);
    }}
    
    .nav-inner {{
        max-width: 1280px;
        margin: 0 auto;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 8px 24px;
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border-radius: 100px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 4px 24px rgba(0, 0, 0, 0.06);
    }}
    
    .premium-navbar.scrolled .nav-inner {{
        background: transparent;
        backdrop-filter: none;
        border: none;
        box-shadow: none;
    }}
    
    /* Logo */
    .nav-logo-wrapper {{
        display: flex;
        align-items: center;
        gap: 10px;
        text-decoration: none;
        color: #fff;
        transition: transform 0.3s ease;
    }}
    
    .nav-logo-wrapper:hover {{
        transform: scale(1.02);
    }}
    
    .scrolled .nav-logo-wrapper {{
        color: #1a1a1a;
    }}
    
    .logo-icon {{
        font-size: 1.5rem;
        background: linear-gradient(135deg, {primary}, {secondary});
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        animation: iconPulse 2s ease-in-out infinite;
    }}
    
    @keyframes iconPulse {{
        0%, 100% {{ transform: scale(1); }}
        50% {{ transform: scale(1.1); }}
    }}
    
    .logo-text {{
        font-family: 'Inter', sans-serif;
        font-size: 1.25rem;
        font-weight: 700;
        letter-spacing: -0.02em;
    }}
    
    /* Navigation Links */
    .nav-links-wrapper {{
        display: flex;
        align-items: center;
        gap: 8px;
    }}
    
    .premium-nav-link {{
        position: relative;
        padding: 10px 18px;
        color: rgba(255, 255, 255, 0.9);
        text-decoration: none;
        font-size: 0.925rem;
        font-weight: 500;
        border-radius: 50px;
        transition: all 0.3s ease;
    }}
    
    .scrolled .premium-nav-link {{
        color: #4a4a4a;
    }}
    
    .premium-nav-link:hover {{
        background: rgba(255, 255, 255, 0.15);
        color: #fff;
    }}
    
    .scrolled .premium-nav-link:hover {{
        background: rgba(0, 0, 0, 0.05);
        color: {primary};
    }}
    
    .link-underline {{
        position: absolute;
        bottom: 6px;
        left: 50%;
        transform: translateX(-50%) scaleX(0);
        width: 20px;
        height: 2px;
        background: linear-gradient(90deg, {primary}, {secondary});
        border-radius: 2px;
        transition: transform 0.3s ease;
    }}
    
    .premium-nav-link:hover .link-underline {{
        transform: translateX(-50%) scaleX(1);
    }}
    
    /* CTA Button */
    .nav-cta-btn {{
        display: flex;
        align-items: center;
        gap: 8px;
        padding: 12px 24px;
        background: linear-gradient(135deg, {primary}, {secondary});
        color: #fff;
        text-decoration: none;
        font-size: 0.9rem;
        font-weight: 600;
        border-radius: 50px;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 4px 15px rgba(99, 102, 241, 0.4);
        overflow: hidden;
        position: relative;
    }}
    
    .nav-cta-btn::before {{
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
        transition: left 0.5s ease;
    }}
    
    .nav-cta-btn:hover::before {{
        left: 100%;
    }}
    
    .nav-cta-btn:hover {{
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(99, 102, 241, 0.5);
    }}
    
    .cta-arrow {{
        transition: transform 0.3s ease;
    }}
    
    .nav-cta-btn:hover .cta-arrow {{
        transform: translateX(4px);
    }}
    
    /* Mobile Menu Toggle */
    .mobile-menu-toggle {{
        display: none;
        flex-direction: column;
        gap: 5px;
        padding: 10px;
        background: transparent;
        border: none;
        cursor: pointer;
    }}
    
    .hamburger-line {{
        width: 24px;
        height: 2px;
        background: #fff;
        border-radius: 2px;
        transition: all 0.3s ease;
    }}
    
    .scrolled .hamburger-line {{
        background: #1a1a1a;
    }}
    
    /* Mobile Menu */
    .mobile-menu {{
        display: none;
        position: absolute;
        top: 100%;
        left: 16px;
        right: 16px;
        margin-top: 8px;
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(20px);
        border-radius: 24px;
        padding: 24px;
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.15);
        opacity: 0;
        transform: translateY(-10px);
        transition: all 0.3s ease;
    }}
    
    .mobile-menu.active {{
        opacity: 1;
        transform: translateY(0);
    }}
    
    .mobile-menu-inner {{
        display: flex;
        flex-direction: column;
        gap: 8px;
    }}
    
    .mobile-menu .premium-nav-link {{
        color: #1a1a1a;
        padding: 14px 20px;
        border-radius: 12px;
    }}
    
    .mobile-menu .premium-nav-link:hover {{
        background: rgba(99, 102, 241, 0.1);
    }}
    
    .mobile-cta {{
        margin-top: 16px;
        padding: 16px 24px;
        background: linear-gradient(135deg, {primary}, {secondary});
        color: #fff;
        text-decoration: none;
        text-align: center;
        font-weight: 600;
        border-radius: 12px;
    }}
    
    /* Responsive */
    @media (max-width: 768px) {{
        .nav-links-wrapper,
        .nav-cta-btn {{
            display: none;
        }}
        
        .mobile-menu-toggle {{
            display: flex;
        }}
        
        .mobile-menu.active {{
            display: block;
        }}
        
        .nav-inner {{
            padding: 12px 20px;
        }}
    }}
    </style>
    
    <script>
    // Scroll effect
    window.addEventListener('scroll', () => {{
        const nav = document.getElementById('premium-navbar');
        if (window.scrollY > 50) {{
            nav.classList.add('scrolled');
        }} else {{
            nav.classList.remove('scrolled');
        }}
    }});
    
    // Mobile menu toggle
    function toggleMobileMenu() {{
        const menu = document.getElementById('mobile-menu');
        menu.classList.toggle('active');
    }}
    </script>
    '''
