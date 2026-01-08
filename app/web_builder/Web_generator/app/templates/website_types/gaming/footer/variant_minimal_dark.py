from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Minimal Dark Footer - Clean and modern dark design"""
    brand = props.get("brand", "GameZone")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <footer class="gaming-footer-minimal">
        <div class="footer-container">
            <div class="footer-top">
                <div class="brand-section">
                    <div class="brand-logo">{brand[0]}</div>
                    <span class="brand-name">{brand}</span>
                </div>
                <nav class="footer-nav">
                    <a href="#">Home</a>
                    <a href="#">Games</a>
                    <a href="#">Tournaments</a>
                    <a href="#">Store</a>
                    <a href="#">Support</a>
                </nav>
            </div>
            <div class="footer-divider"></div>
            <div class="footer-bottom">
                <p>© 2024 {brand}. Built for gamers.</p>
                <div class="social-minimal">
                    <a href="#">Twitter</a>
                    <a href="#">Discord</a>
                    <a href="#">YouTube</a>
                </div>
            </div>
        </div>
    </footer>
    
    <style>
    .gaming-footer-minimal {{
        background: {background};
        padding: 60px 24px;
        border-top: 1px solid {text}10;
    }}
    .footer-container {{
        max-width: 1200px;
        margin: 0 auto;
    }}
    .footer-top {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 32px;
    }}
    .brand-section {{
        display: flex;
        align-items: center;
        gap: 12px;
    }}
    .brand-logo {{
        width: 48px;
        height: 48px;
        background: {primary};
        color: {background};
        font-family: 'Orbitron', sans-serif;
        font-size: 1.5rem;
        font-weight: 900;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 12px;
    }}
    .brand-name {{
        font-family: 'Rajdhani', sans-serif;
        font-size: 1.5rem;
        font-weight: 800;
        color: {text};
    }}
    .footer-nav {{
        display: flex;
        gap: 32px;
    }}
    .footer-nav a {{
        color: {secondary};
        text-decoration: none;
        font-weight: 500;
        transition: color 0.3s ease;
    }}
    .footer-nav a:hover {{
        color: {primary};
    }}
    .footer-divider {{
        height: 1px;
        background: linear-gradient(90deg, transparent, {text}15, transparent);
        margin: 40px 0;
    }}
    .footer-bottom {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 20px;
    }}
    .footer-bottom p {{
        color: {secondary};
        font-size: 0.9rem;
    }}
    .social-minimal {{
        display: flex;
        gap: 24px;
    }}
    .social-minimal a {{
        color: {secondary};
        text-decoration: none;
        font-size: 0.9rem;
        transition: color 0.3s ease;
    }}
    .social-minimal a:hover {{
        color: {primary};
    }}
    @media (max-width: 768px) {{
        .footer-top {{ flex-direction: column; text-align: center; }}
        .footer-nav {{ flex-wrap: wrap; justify-content: center; }}
        .footer-bottom {{ flex-direction: column; text-align: center; }}
    }}
    </style>
    '''
