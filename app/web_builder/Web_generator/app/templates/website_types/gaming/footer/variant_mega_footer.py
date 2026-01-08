from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Mega Footer - Large comprehensive footer with all info"""
    brand = props.get("brand", "GameZone")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <footer class="gaming-footer-mega">
        <div class="footer-top-section">
            <div class="cta-banner">
                <div class="cta-content">
                    <h3>Ready to Level Up?</h3>
                    <p>Join millions of players worldwide</p>
                </div>
                <a href="#" class="cta-btn">Get Started Free</a>
            </div>
        </div>
        <div class="footer-main-section">
            <div class="footer-grid">
                <div class="footer-about">
                    <h2>{brand}</h2>
                    <p>The world's leading competitive gaming platform. Play, compete, and win.</p>
                    <div class="app-badges">
                        <a href="#" class="app-badge">📱 iOS</a>
                        <a href="#" class="app-badge">🤖 Android</a>
                        <a href="#" class="app-badge">🖥️ PC</a>
                    </div>
                </div>
                <div class="footer-col">
                    <h4>Games</h4>
                    <a href="#">All Games</a>
                    <a href="#">New Releases</a>
                    <a href="#">Popular</a>
                    <a href="#">Free to Play</a>
                    <a href="#">Esports</a>
                </div>
                <div class="footer-col">
                    <h4>Community</h4>
                    <a href="#">Forums</a>
                    <a href="#">Discord</a>
                    <a href="#">Tournaments</a>
                    <a href="#">Leaderboards</a>
                    <a href="#">Teams</a>
                </div>
                <div class="footer-col">
                    <h4>Company</h4>
                    <a href="#">About Us</a>
                    <a href="#">Careers</a>
                    <a href="#">Press</a>
                    <a href="#">Partners</a>
                    <a href="#">Blog</a>
                </div>
                <div class="footer-col">
                    <h4>Support</h4>
                    <a href="#">Help Center</a>
                    <a href="#">Contact Us</a>
                    <a href="#">Bug Report</a>
                    <a href="#">Status</a>
                    <a href="#">API</a>
                </div>
            </div>
        </div>
        <div class="footer-bottom-section">
            <div class="bottom-grid">
                <p>© 2024 {brand}. All rights reserved.</p>
                <div class="legal">
                    <a href="#">Privacy Policy</a>
                    <a href="#">Terms of Service</a>
                    <a href="#">Cookie Settings</a>
                </div>
                <div class="social-icons">
                    <a href="#">🐦</a>
                    <a href="#">💬</a>
                    <a href="#">📺</a>
                    <a href="#">📸</a>
                </div>
            </div>
        </div>
    </footer>
    
    <style>
    .gaming-footer-mega {{
        background: {background};
    }}
    .footer-top-section {{
        padding: 60px 24px;
        border-bottom: 1px solid {text}10;
    }}
    .cta-banner {{
        max-width: 1200px;
        margin: 0 auto;
        background: linear-gradient(135deg, {primary}20, {primary}05);
        border: 1px solid {primary}30;
        border-radius: 20px;
        padding: 48px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 24px;
    }}
    .cta-content h3 {{
        font-size: 2rem;
        font-weight: 800;
        color: {text};
        margin-bottom: 8px;
    }}
    .cta-content p {{
        color: {secondary};
    }}
    .cta-btn {{
        padding: 16px 40px;
        background: {primary};
        color: {background};
        font-weight: 700;
        text-decoration: none;
        border-radius: 10px;
        transition: all 0.3s ease;
    }}
    .cta-btn:hover {{
        transform: translateY(-3px);
        box-shadow: 0 15px 40px {primary}40;
    }}
    .footer-main-section {{
        padding: 80px 24px;
    }}
    .footer-grid {{
        max-width: 1200px;
        margin: 0 auto;
        display: grid;
        grid-template-columns: 2fr repeat(4, 1fr);
        gap: 48px;
    }}
    .footer-about h2 {{
        font-family: 'Orbitron', sans-serif;
        font-size: 2rem;
        color: {primary};
        margin-bottom: 16px;
    }}
    .footer-about p {{
        color: {secondary};
        line-height: 1.7;
        margin-bottom: 24px;
    }}
    .app-badges {{
        display: flex;
        gap: 12px;
        flex-wrap: wrap;
    }}
    .app-badge {{
        padding: 10px 20px;
        background: {text}08;
        color: {text};
        text-decoration: none;
        border-radius: 8px;
        font-size: 0.9rem;
        transition: all 0.3s ease;
    }}
    .app-badge:hover {{
        background: {primary}20;
    }}
    .footer-col h4 {{
        color: {text};
        font-weight: 700;
        margin-bottom: 20px;
    }}
    .footer-col a {{
        display: block;
        color: {secondary};
        text-decoration: none;
        padding: 8px 0;
        transition: color 0.3s ease;
    }}
    .footer-col a:hover {{
        color: {primary};
    }}
    .footer-bottom-section {{
        padding: 30px 24px;
        border-top: 1px solid {text}10;
    }}
    .bottom-grid {{
        max-width: 1200px;
        margin: 0 auto;
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 20px;
    }}
    .bottom-grid p {{
        color: {secondary};
        font-size: 0.9rem;
    }}
    .legal {{
        display: flex;
        gap: 24px;
    }}
    .legal a {{
        color: {secondary};
        text-decoration: none;
        font-size: 0.9rem;
    }}
    .legal a:hover {{
        color: {primary};
    }}
    .social-icons {{
        display: flex;
        gap: 16px;
    }}
    .social-icons a {{
        font-size: 1.3rem;
        text-decoration: none;
        transition: transform 0.3s ease;
    }}
    .social-icons a:hover {{
        transform: scale(1.2);
    }}
    @media (max-width: 900px) {{
        .footer-grid {{ grid-template-columns: 1fr 1fr; }}
        .footer-about {{ grid-column: span 2; }}
        .cta-banner {{ text-align: center; justify-content: center; }}
        .bottom-grid {{ flex-direction: column; text-align: center; }}
    }}
    </style>
    '''
