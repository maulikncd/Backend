from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Neon Grid Footer - Cyberpunk style with grid background"""
    brand = props.get("brand", "GameZone")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <footer class="gaming-footer-neon">
        <div class="neon-grid-bg"></div>
        <div class="footer-container">
            <div class="footer-content">
                <div class="brand-box">
                    <div class="neon-logo">{brand[0]}</div>
                    <h3>{brand}</h3>
                    <p>// NEXT_GEN_GAMING</p>
                </div>
                <div class="links-row">
                    <a href="#" class="neon-link">GAMES</a>
                    <a href="#" class="neon-link">TOURNAMENTS</a>
                    <a href="#" class="neon-link">COMMUNITY</a>
                    <a href="#" class="neon-link">STORE</a>
                    <a href="#" class="neon-link">SUPPORT</a>
                </div>
                <div class="social-neon">
                    <a href="#" class="neon-social">🎮</a>
                    <a href="#" class="neon-social">📺</a>
                    <a href="#" class="neon-social">💬</a>
                    <a href="#" class="neon-social">🐦</a>
                </div>
            </div>
            <div class="neon-divider"></div>
            <div class="footer-legal">
                <span>© 2024 {brand} // ALL_RIGHTS_RESERVED</span>
            </div>
        </div>
    </footer>
    
    <style>
    .gaming-footer-neon {{
        background: {background};
        padding: 80px 24px 40px;
        position: relative;
        overflow: hidden;
    }}
    .neon-grid-bg {{
        position: absolute;
        inset: 0;
        background-image: 
            linear-gradient({primary}08 1px, transparent 1px),
            linear-gradient(90deg, {primary}08 1px, transparent 1px);
        background-size: 40px 40px;
        opacity: 0.5;
    }}
    .footer-container {{
        max-width: 1000px;
        margin: 0 auto;
        position: relative;
        z-index: 2;
        text-align: center;
    }}
    .brand-box {{
        margin-bottom: 48px;
    }}
    .neon-logo {{
        width: 80px;
        height: 80px;
        background: {primary}20;
        border: 2px solid {primary};
        color: {primary};
        font-family: 'Orbitron', sans-serif;
        font-size: 2.5rem;
        font-weight: 900;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 20px;
        clip-path: polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%);
        box-shadow: 0 0 30px {primary}50;
    }}
    .brand-box h3 {{
        font-family: 'Orbitron', sans-serif;
        font-size: 1.8rem;
        color: {text};
        margin-bottom: 8px;
    }}
    .brand-box p {{
        font-family: 'JetBrains Mono', monospace;
        color: {primary};
        font-size: 0.9rem;
        letter-spacing: 2px;
    }}
    .links-row {{
        display: flex;
        justify-content: center;
        gap: 40px;
        flex-wrap: wrap;
        margin-bottom: 48px;
    }}
    .neon-link {{
        color: {secondary};
        text-decoration: none;
        font-weight: 700;
        font-size: 0.9rem;
        letter-spacing: 2px;
        padding: 8px 0;
        position: relative;
        transition: color 0.3s ease;
    }}
    .neon-link::after {{
        content: '';
        position: absolute;
        bottom: 0;
        left: 0;
        width: 0;
        height: 2px;
        background: {primary};
        transition: width 0.3s ease;
        box-shadow: 0 0 10px {primary};
    }}
    .neon-link:hover {{
        color: {primary};
    }}
    .neon-link:hover::after {{
        width: 100%;
    }}
    .social-neon {{
        display: flex;
        justify-content: center;
        gap: 20px;
    }}
    .neon-social {{
        width: 50px;
        height: 50px;
        background: {text}05;
        border: 1px solid {primary}30;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.5rem;
        text-decoration: none;
        transition: all 0.3s ease;
    }}
    .neon-social:hover {{
        background: {primary}20;
        border-color: {primary};
        box-shadow: 0 0 20px {primary}50;
        transform: translateY(-4px);
    }}
    .neon-divider {{
        height: 1px;
        background: linear-gradient(90deg, transparent, {primary}50, transparent);
        margin: 48px 0 24px;
    }}
    .footer-legal span {{
        font-family: 'JetBrains Mono', monospace;
        color: {secondary};
        font-size: 0.85rem;
        letter-spacing: 1px;
    }}
    @media (max-width: 600px) {{
        .links-row {{ gap: 20px; }}
    }}
    </style>
    '''
