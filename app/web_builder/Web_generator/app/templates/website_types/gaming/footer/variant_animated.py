from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Animated Footer - Footer with animated elements"""
    brand = props.get("brand", "GameZone")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <footer class="gaming-footer-animated">
        <div class="particles-bg">
            <div class="particle"></div>
            <div class="particle"></div>
            <div class="particle"></div>
            <div class="particle"></div>
            <div class="particle"></div>
        </div>
        <div class="footer-container">
            <div class="footer-brand-anim">
                <div class="logo-animated">{brand}</div>
                <p>Level up your gaming experience</p>
            </div>
            <div class="quick-links">
                <a href="#" class="quick-link">Home</a>
                <span class="link-dot"></span>
                <a href="#" class="quick-link">Games</a>
                <span class="link-dot"></span>
                <a href="#" class="quick-link">Tournaments</a>
                <span class="link-dot"></span>
                <a href="#" class="quick-link">Store</a>
                <span class="link-dot"></span>
                <a href="#" class="quick-link">Contact</a>
            </div>
            <div class="social-animated">
                <a href="#" class="social-anim">🎮</a>
                <a href="#" class="social-anim">📺</a>
                <a href="#" class="social-anim">💬</a>
                <a href="#" class="social-anim">🐦</a>
            </div>
            <div class="footer-bottom-anim">
                <span>© 2024 {brand}. All rights reserved.</span>
            </div>
        </div>
    </footer>
    
    <style>
    .gaming-footer-animated {{
        background: {background};
        padding: 80px 24px 40px;
        position: relative;
        overflow: hidden;
        text-align: center;
    }}
    .particles-bg {{
        position: absolute;
        inset: 0;
        pointer-events: none;
    }}
    .particle {{
        position: absolute;
        width: 4px;
        height: 4px;
        background: {primary};
        border-radius: 50%;
        animation: floatParticle 15s infinite;
    }}
    .particle:nth-child(1) {{ left: 10%; animation-delay: 0s; }}
    .particle:nth-child(2) {{ left: 30%; animation-delay: 3s; }}
    .particle:nth-child(3) {{ left: 50%; animation-delay: 6s; }}
    .particle:nth-child(4) {{ left: 70%; animation-delay: 9s; }}
    .particle:nth-child(5) {{ left: 90%; animation-delay: 12s; }}
    @keyframes floatParticle {{
        0% {{ bottom: -10px; opacity: 0; }}
        10% {{ opacity: 1; }}
        90% {{ opacity: 1; }}
        100% {{ bottom: 100%; opacity: 0; }}
    }}
    .footer-container {{
        max-width: 800px;
        margin: 0 auto;
        position: relative;
        z-index: 2;
    }}
    .footer-brand-anim {{
        margin-bottom: 40px;
    }}
    .logo-animated {{
        font-family: 'Orbitron', sans-serif;
        font-size: 3rem;
        font-weight: 900;
        color: {text};
        margin-bottom: 12px;
        animation: glowPulse 3s ease-in-out infinite;
    }}
    @keyframes glowPulse {{
        0%, 100% {{ text-shadow: 0 0 20px {primary}40; }}
        50% {{ text-shadow: 0 0 40px {primary}80; }}
    }}
    .footer-brand-anim p {{
        color: {secondary};
        font-size: 1.1rem;
    }}
    .quick-links {{
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 24px;
        flex-wrap: wrap;
        margin-bottom: 40px;
    }}
    .quick-link {{
        color: {secondary};
        text-decoration: none;
        font-weight: 500;
        transition: color 0.3s ease;
    }}
    .quick-link:hover {{
        color: {primary};
    }}
    .link-dot {{
        width: 4px;
        height: 4px;
        background: {primary};
        border-radius: 50%;
    }}
    .social-animated {{
        display: flex;
        justify-content: center;
        gap: 16px;
        margin-bottom: 40px;
    }}
    .social-anim {{
        width: 56px;
        height: 56px;
        background: {text}08;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.5rem;
        text-decoration: none;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    }}
    .social-anim:hover {{
        background: {primary};
        transform: translateY(-8px) rotate(10deg);
        box-shadow: 0 20px 40px {primary}40;
    }}
    .footer-bottom-anim span {{
        color: {secondary};
        font-size: 0.9rem;
    }}
    </style>
    '''
