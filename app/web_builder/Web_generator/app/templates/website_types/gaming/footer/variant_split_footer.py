from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Split Footer - Two-tone split design"""
    brand = props.get("brand", "GameZone")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <footer class="gaming-footer-split">
        <div class="split-left">
            <div class="left-content">
                <h2>{brand}</h2>
                <p>Join the ultimate gaming community. Play, compete, and connect with millions of players worldwide.</p>
                <div class="newsletter-box">
                    <input type="email" placeholder="Enter your email">
                    <button>Subscribe</button>
                </div>
            </div>
        </div>
        <div class="split-right">
            <div class="right-content">
                <div class="links-grid">
                    <div class="link-group">
                        <h4>Platform</h4>
                        <a href="#">Games</a>
                        <a href="#">Tournaments</a>
                        <a href="#">Store</a>
                    </div>
                    <div class="link-group">
                        <h4>Community</h4>
                        <a href="#">Discord</a>
                        <a href="#">Forums</a>
                        <a href="#">Teams</a>
                    </div>
                    <div class="link-group">
                        <h4>Legal</h4>
                        <a href="#">Privacy</a>
                        <a href="#">Terms</a>
                        <a href="#">Support</a>
                    </div>
                </div>
                <div class="copyright">
                    © 2024 {brand}. All rights reserved.
                </div>
            </div>
        </div>
    </footer>
    
    <style>
    .gaming-footer-split {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        min-height: 400px;
    }}
    .split-left {{
        background: linear-gradient(135deg, {primary}, {primary}CC);
        padding: 80px 60px;
        display: flex;
        align-items: center;
    }}
    .split-right {{
        background: {background};
        padding: 80px 60px;
        display: flex;
        align-items: center;
    }}
    .left-content {{
        max-width: 400px;
    }}
    .left-content h2 {{
        font-family: 'Orbitron', sans-serif;
        font-size: 2.5rem;
        color: {background};
        margin-bottom: 20px;
    }}
    .left-content p {{
        color: {background}CC;
        line-height: 1.7;
        margin-bottom: 32px;
    }}
    .newsletter-box {{
        display: flex;
        gap: 12px;
    }}
    .newsletter-box input {{
        flex: 1;
        padding: 14px 20px;
        background: {background}20;
        border: 1px solid {background}40;
        border-radius: 8px;
        color: {background};
        font-size: 1rem;
    }}
    .newsletter-box input::placeholder {{
        color: {background}80;
    }}
    .newsletter-box button {{
        padding: 14px 28px;
        background: {background};
        color: {primary};
        border: none;
        border-radius: 8px;
        font-weight: 700;
        cursor: pointer;
        transition: transform 0.3s ease;
    }}
    .newsletter-box button:hover {{
        transform: scale(1.05);
    }}
    .right-content {{
        width: 100%;
    }}
    .links-grid {{
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 40px;
        margin-bottom: 48px;
    }}
    .link-group h4 {{
        color: {text};
        font-weight: 700;
        margin-bottom: 16px;
    }}
    .link-group a {{
        display: block;
        color: {secondary};
        text-decoration: none;
        padding: 6px 0;
        transition: color 0.3s ease;
    }}
    .link-group a:hover {{
        color: {primary};
    }}
    .copyright {{
        color: {secondary};
        font-size: 0.9rem;
        padding-top: 24px;
        border-top: 1px solid {text}10;
    }}
    @media (max-width: 900px) {{
        .gaming-footer-split {{ grid-template-columns: 1fr; }}
        .split-left, .split-right {{ padding: 60px 24px; }}
        .links-grid {{ grid-template-columns: 1fr 1fr; }}
    }}
    </style>
    '''
