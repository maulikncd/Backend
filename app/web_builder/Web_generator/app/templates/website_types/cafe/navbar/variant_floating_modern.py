from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Modern Floating Navbar - Centered design with luxury feel"""
    logo = props.get("logo_text", props.get("logo", "Brand"))
    links = props.get("links", [
        {"text": "Home", "url": "#home"},
        {"text": "About", "url": "#about"},
        {"text": "Services", "url": "#services"},
        {"text": "Contact", "url": "#contact"}
    ])
    cta_text = props.get("cta_text", "Book Now")
    cta_url = props.get("cta_url", "#contact")
    
    links_html = ""
    for link in links:
        links_html += f'<a href="{link.get("url", "#")}" class="floating-nav-link">{link.get("text", "Link")}</a>'
    
    primary = colors.get("primary", "#6366F1")
    accent = colors.get("accent", "#F59E0B")
    
    return f'''
    <!-- Modern Floating Navbar -->
    <nav id="floating-navbar" class="floating-navbar">
        <div class="floating-nav-container">
            <!-- Left: Logo -->
            <a href="#" class="floating-logo">
                <div class="logo-circle">
                    <span class="logo-initial">{logo[0] if logo else "B"}</span>
                </div>
                <span class="logo-name">{logo}</span>
            </a>
            
            <!-- Center: Links -->
            <div class="floating-nav-links">
                {links_html}
            </div>
            
            <!-- Right: CTA -->
            <a href="{cta_url}" class="floating-cta">
                {cta_text}
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M5 12h14M12 5l7 7-7 7"/>
                </svg>
            </a>
            
            <!-- Mobile Toggle -->
            <button class="floating-mobile-btn" onclick="toggleFloatingMenu()">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <line x1="3" y1="6" x2="21" y2="6"/>
                    <line x1="3" y1="12" x2="21" y2="12"/>
                    <line x1="3" y1="18" x2="21" y2="18"/>
                </svg>
            </button>
        </div>
        
        <!-- Mobile Menu -->
        <div class="floating-mobile-menu" id="floating-mobile-menu">
            {links_html}
            <a href="{cta_url}" class="floating-mobile-cta">{cta_text}</a>
        </div>
    </nav>
    
    <style>
    .floating-navbar {{
        position: fixed;
        top: 20px;
        left: 50%;
        transform: translateX(-50%);
        z-index: 9999;
        width: calc(100% - 48px);
        max-width: 1200px;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    }}
    
    .floating-navbar.nav-scrolled {{
        top: 12px;
    }}
    
    .floating-nav-container {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 12px 12px 12px 20px;
        background: rgba(10, 10, 10, 0.85);
        backdrop-filter: blur(24px) saturate(180%);
        -webkit-backdrop-filter: blur(24px) saturate(180%);
        border-radius: 100px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 
            0 20px 50px rgba(0, 0, 0, 0.3),
            0 0 0 1px rgba(255, 255, 255, 0.05) inset;
    }}
    
    /* Logo */
    .floating-logo {{
        display: flex;
        align-items: center;
        gap: 12px;
        text-decoration: none;
        color: #fff;
    }}
    
    .logo-circle {{
        width: 40px;
        height: 40px;
        background: linear-gradient(135deg, {primary}, {accent});
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 4px 15px rgba(99, 102, 241, 0.4);
    }}
    
    .logo-initial {{
        color: #fff;
        font-weight: 700;
        font-size: 1.1rem;
    }}
    
    .logo-name {{
        font-weight: 600;
        font-size: 1.1rem;
        letter-spacing: -0.01em;
    }}
    
    /* Links */
    .floating-nav-links {{
        display: flex;
        align-items: center;
        gap: 4px;
        padding: 4px;
        background: rgba(255, 255, 255, 0.05);
        border-radius: 50px;
    }}
    
    .floating-nav-link {{
        padding: 10px 20px;
        color: rgba(255, 255, 255, 0.7);
        text-decoration: none;
        font-size: 0.9rem;
        font-weight: 500;
        border-radius: 50px;
        transition: all 0.3s ease;
    }}
    
    .floating-nav-link:hover {{
        color: #fff;
        background: rgba(255, 255, 255, 0.1);
    }}
    
    .floating-nav-link.active {{
        color: #fff;
        background: {primary};
    }}
    
    /* CTA */
    .floating-cta {{
        display: flex;
        align-items: center;
        gap: 8px;
        padding: 12px 24px;
        background: #fff;
        color: #0a0a0a;
        text-decoration: none;
        font-size: 0.9rem;
        font-weight: 600;
        border-radius: 50px;
        transition: all 0.3s ease;
    }}
    
    .floating-cta:hover {{
        background: {primary};
        color: #fff;
        transform: scale(1.03);
    }}
    
    .floating-cta svg {{
        transition: transform 0.3s ease;
    }}
    
    .floating-cta:hover svg {{
        transform: translateX(3px);
    }}
    
    /* Mobile */
    .floating-mobile-btn {{
        display: none;
        padding: 10px;
        background: rgba(255, 255, 255, 0.1);
        border: none;
        border-radius: 50%;
        cursor: pointer;
        color: #fff;
    }}
    
    .floating-mobile-menu {{
        display: none;
        flex-direction: column;
        gap: 8px;
        margin-top: 12px;
        padding: 20px;
        background: rgba(10, 10, 10, 0.95);
        backdrop-filter: blur(24px);
        border-radius: 24px;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }}
    
    .floating-mobile-menu.active {{
        display: flex;
    }}
    
    .floating-mobile-menu .floating-nav-link {{
        padding: 16px 20px;
        border-radius: 12px;
    }}
    
    .floating-mobile-cta {{
        margin-top: 12px;
        padding: 16px;
        background: linear-gradient(135deg, {primary}, {accent});
        color: #fff;
        text-decoration: none;
        text-align: center;
        font-weight: 600;
        border-radius: 12px;
    }}
    
    @media (max-width: 768px) {{
        .floating-nav-links,
        .floating-cta {{
            display: none;
        }}
        
        .floating-mobile-btn {{
            display: flex;
        }}
        
        .floating-navbar {{
            width: calc(100% - 32px);
            top: 12px;
        }}
        
        .floating-nav-container {{
            padding: 8px 12px 8px 16px;
        }}
    }}
    </style>
    
    <script>
    window.addEventListener('scroll', () => {{
        const nav = document.getElementById('floating-navbar');
        if (window.scrollY > 80) {{
            nav.classList.add('nav-scrolled');
        }} else {{
            nav.classList.remove('nav-scrolled');
        }}
    }});
    
    function toggleFloatingMenu() {{
        document.getElementById('floating-mobile-menu').classList.toggle('active');
    }}
    </script>
    '''
