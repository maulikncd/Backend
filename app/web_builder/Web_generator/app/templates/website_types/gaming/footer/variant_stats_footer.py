from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Stats Footer - Footer with live stats display"""
    brand = props.get("brand", "GameZone")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <footer class="gaming-footer-stats">
        <div class="stats-banner">
            <div class="stats-container">
                <div class="stat-item">
                    <span class="stat-number">50M+</span>
                    <span class="stat-label">Players</span>
                </div>
                <div class="stat-divider"></div>
                <div class="stat-item">
                    <span class="stat-number">10K+</span>
                    <span class="stat-label">Daily Matches</span>
                </div>
                <div class="stat-divider"></div>
                <div class="stat-item">
                    <span class="stat-number">$50M</span>
                    <span class="stat-label">Prize Pool</span>
                </div>
                <div class="stat-divider"></div>
                <div class="stat-item">
                    <span class="stat-number">150+</span>
                    <span class="stat-label">Countries</span>
                </div>
            </div>
        </div>
        <div class="footer-main-stats">
            <div class="main-container">
                <div class="footer-left">
                    <h3>{brand}</h3>
                    <p>The world's leading competitive gaming platform.</p>
                    <div class="social-bar">
                        <a href="#">🎮</a>
                        <a href="#">📺</a>
                        <a href="#">💬</a>
                    </div>
                </div>
                <div class="footer-links-stats">
                    <a href="#">Games</a>
                    <a href="#">Tournaments</a>
                    <a href="#">Community</a>
                    <a href="#">Store</a>
                    <a href="#">Support</a>
                </div>
            </div>
        </div>
        <div class="footer-bottom-stats">
            <span>© 2024 {brand}. All rights reserved.</span>
            <div class="legal-stats">
                <a href="#">Privacy</a>
                <a href="#">Terms</a>
            </div>
        </div>
    </footer>
    
    <style>
    .gaming-footer-stats {{
        background: {background};
    }}
    .stats-banner {{
        background: linear-gradient(90deg, {primary}15, {secondary}10);
        border-bottom: 1px solid {text}10;
        padding: 40px 24px;
    }}
    .stats-container {{
        max-width: 1000px;
        margin: 0 auto;
        display: flex;
        justify-content: space-around;
        align-items: center;
        flex-wrap: wrap;
        gap: 24px;
    }}
    .stat-item {{
        text-align: center;
    }}
    .stat-number {{
        display: block;
        font-family: 'Orbitron', sans-serif;
        font-size: 2.5rem;
        font-weight: 900;
        color: {primary};
        text-shadow: 0 0 30px {primary}40;
    }}
    .stat-label {{
        color: {secondary};
        font-size: 0.9rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }}
    .stat-divider {{
        width: 1px;
        height: 50px;
        background: {text}15;
    }}
    .footer-main-stats {{
        padding: 60px 24px;
    }}
    .main-container {{
        max-width: 1200px;
        margin: 0 auto;
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 40px;
    }}
    .footer-left h3 {{
        font-family: 'Orbitron', sans-serif;
        font-size: 1.8rem;
        color: {text};
        margin-bottom: 12px;
    }}
    .footer-left p {{
        color: {secondary};
        margin-bottom: 20px;
    }}
    .social-bar {{
        display: flex;
        gap: 12px;
    }}
    .social-bar a {{
        width: 44px;
        height: 44px;
        background: {text}08;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.2rem;
        text-decoration: none;
        transition: all 0.3s ease;
    }}
    .social-bar a:hover {{
        background: {primary}20;
        transform: translateY(-3px);
    }}
    .footer-links-stats {{
        display: flex;
        gap: 32px;
        flex-wrap: wrap;
    }}
    .footer-links-stats a {{
        color: {secondary};
        text-decoration: none;
        font-weight: 500;
        transition: color 0.3s ease;
    }}
    .footer-links-stats a:hover {{
        color: {primary};
    }}
    .footer-bottom-stats {{
        border-top: 1px solid {text}10;
        padding: 24px;
        display: flex;
        justify-content: center;
        gap: 40px;
        flex-wrap: wrap;
    }}
    .footer-bottom-stats span {{
        color: {secondary};
        font-size: 0.9rem;
    }}
    .legal-stats {{
        display: flex;
        gap: 20px;
    }}
    .legal-stats a {{
        color: {secondary};
        text-decoration: none;
        font-size: 0.9rem;
    }}
    .legal-stats a:hover {{
        color: {primary};
    }}
    @media (max-width: 768px) {{
        .stat-divider {{ display: none; }}
        .main-container {{ text-align: center; flex-direction: column; }}
        .footer-links-stats {{ justify-content: center; }}
        .social-bar {{ justify-content: center; }}
    }}
    </style>
    '''
