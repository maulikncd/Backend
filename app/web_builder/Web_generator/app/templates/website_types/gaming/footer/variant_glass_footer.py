from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Glass Footer - Glassmorphism style with blur effects"""
    brand = props.get("brand", "GameZone")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <footer class="gaming-footer-glass">
        <div class="footer-glow"></div>
        <div class="footer-container">
            <div class="footer-main">
                <div class="footer-brand">
                    <h3>{brand}</h3>
                    <p>The Ultimate Gaming Platform</p>
                    <div class="social-row">
                        <a href="#" class="social-icon">🎮</a>
                        <a href="#" class="social-icon">📺</a>
                        <a href="#" class="social-icon">🐦</a>
                        <a href="#" class="social-icon">💬</a>
                    </div>
                </div>
                <div class="footer-links">
                    <div class="link-col">
                        <h4>Platform</h4>
                        <a href="#">Games</a>
                        <a href="#">Tournaments</a>
                        <a href="#">Leaderboards</a>
                        <a href="#">Store</a>
                    </div>
                    <div class="link-col">
                        <h4>Community</h4>
                        <a href="#">Forums</a>
                        <a href="#">Discord</a>
                        <a href="#">Events</a>
                        <a href="#">Blog</a>
                    </div>
                    <div class="link-col">
                        <h4>Support</h4>
                        <a href="#">Help Center</a>
                        <a href="#">Contact</a>
                        <a href="#">FAQ</a>
                        <a href="#">Status</a>
                    </div>
                </div>
            </div>
            <div class="footer-bottom">
                <span>© 2024 {brand}. All rights reserved.</span>
                <div class="legal-links">
                    <a href="#">Privacy</a>
                    <a href="#">Terms</a>
                    <a href="#">Cookies</a>
                </div>
            </div>
        </div>
    </footer>
    
    <style>
    .gaming-footer-glass {{
        background: {background};
        padding: 80px 24px 40px;
        position: relative;
        overflow: hidden;
    }}
    .footer-glow {{
        position: absolute;
        top: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 600px;
        height: 300px;
        background: {primary};
        filter: blur(150px);
        opacity: 0.15;
    }}
    .footer-container {{
        max-width: 1200px;
        margin: 0 auto;
        position: relative;
        z-index: 2;
    }}
    .footer-main {{
        display: grid;
        grid-template-columns: 1.5fr 2fr;
        gap: 80px;
        padding-bottom: 60px;
        border-bottom: 1px solid {text}10;
    }}
    .footer-brand h3 {{
        font-family: 'Orbitron', sans-serif;
        font-size: 2rem;
        font-weight: 900;
        color: {primary};
        margin-bottom: 12px;
    }}
    .footer-brand p {{
        color: {secondary};
        margin-bottom: 24px;
    }}
    .social-row {{
        display: flex;
        gap: 12px;
    }}
    .social-icon {{
        width: 48px;
        height: 48px;
        background: {text}08;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.3rem;
        text-decoration: none;
        transition: all 0.3s ease;
    }}
    .social-icon:hover {{
        background: {primary}20;
        transform: translateY(-4px);
    }}
    .footer-links {{
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 40px;
    }}
    .link-col h4 {{
        color: {text};
        font-weight: 700;
        margin-bottom: 20px;
        font-size: 1rem;
    }}
    .link-col a {{
        display: block;
        color: {secondary};
        text-decoration: none;
        padding: 8px 0;
        transition: color 0.3s ease;
    }}
    .link-col a:hover {{
        color: {primary};
    }}
    .footer-bottom {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding-top: 30px;
        flex-wrap: wrap;
        gap: 20px;
    }}
    .footer-bottom span {{
        color: {secondary};
        font-size: 0.9rem;
    }}
    .legal-links {{
        display: flex;
        gap: 24px;
    }}
    .legal-links a {{
        color: {secondary};
        text-decoration: none;
        font-size: 0.9rem;
        transition: color 0.3s ease;
    }}
    .legal-links a:hover {{
        color: {primary};
    }}
    @media (max-width: 900px) {{
        .footer-main {{ grid-template-columns: 1fr; gap: 48px; }}
        .footer-links {{ grid-template-columns: repeat(2, 1fr); }}
    }}
    </style>
    '''
