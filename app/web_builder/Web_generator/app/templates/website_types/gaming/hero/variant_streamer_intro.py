from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    name = props.get("name", "NINJA")
    subtitle = props.get("subtitle", "Top Tier Gameplay & Entertainment")
    socials = props.get("socials", ["Twitch", "YouTube", "Twitter"])
    
    # Use colors from user's selected palette - no hardcoded fallbacks
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    accent = colors.get("accent")
    text = colors.get("text")
    
    # Build social links separately
    social_links = ""
    for s in socials:
        social_links += f'<a href="#" class="social-pill">{s}</a>'
    
    return f'''
    <section class="gaming-hero gaming-hero-streamer" id="hero">
        <div class="streamer-grid"></div>
        <div class="hero-content">
            <div class="streamer-avatar">
                <div class="live-dot">LIVE</div>
            </div>
            <h1 class="hero-title">{name}</h1>
            <p class="hero-subtitle">{subtitle}</p>
            <div class="social-links">
                {social_links}
            </div>
            <a href="#subscribe" class="btn-streamer">Subscribe Now</a>
        </div>
        <div class="floating-icons">
            <div class="icon-box">🎮</div>
            <div class="icon-box">🎧</div>
            <div class="icon-box">🎙️</div>
        </div>
    </section>
    
    <style>
    .gaming-hero-streamer {{
        min-height: 100vh;
        background: {background};
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
        overflow: hidden;
    }}
    .streamer-grid {{
        position: absolute;
        inset: 0;
        background: radial-gradient(circle at center, transparent 0%, {background}CC 100%),
                    repeating-linear-gradient({primary}10 0 1px, transparent 1px 40px),
                    repeating-linear-gradient(90deg, {primary}10 0 1px, transparent 1px 40px);
    }}
    .hero-content {{ position: relative; z-index: 2; text-align: center; }}
    .streamer-avatar {{
        width: 150px;
        height: 150px;
        background: {secondary}30;
        border-radius: 50%;
        margin: 0 auto 30px;
        border: 4px solid {primary};
        position: relative;
        box-shadow: 0 0 50px {primary}40;
    }}
    .live-dot {{
        position: absolute;
        bottom: 5px;
        right: 5px;
        background: {accent};
        color: {background};
        padding: 4px 12px;
        border-radius: 4px;
        font-size: 0.7rem;
        font-weight: 800;
        animation: pulseLive 1.5s infinite;
    }}
    @keyframes pulseLive {{
        0%, 100% {{ opacity: 1; }}
        50% {{ opacity: 0.5; }}
    }}
    .gaming-hero-streamer .hero-title {{
        font-family: 'Rajdhani', sans-serif;
        font-size: 5rem;
        font-weight: 900;
        color: {text};
        margin-bottom: 10px;
        letter-spacing: 5px;
    }}
    .gaming-hero-streamer .hero-subtitle {{
        color: {secondary};
        font-size: 1.2rem;
        margin-bottom: 40px;
    }}
    .social-links {{ display: flex; gap: 15px; justify-content: center; margin-bottom: 50px; }}
    .social-pill {{
        background: {primary}10;
        color: {text};
        padding: 8px 20px;
        border-radius: 50px;
        text-decoration: none;
        border: 1px solid {primary}30;
        transition: 0.3s;
    }}
    .social-pill:hover {{ background: {primary}20; border-color: {primary}; }}
    .btn-streamer {{
        padding: 15px 50px;
        background: {primary};
        color: {background};
        font-weight: 800;
        text-transform: uppercase;
        text-decoration: none;
        border-radius: 5px;
    }}
    .floating-icons {{ position: absolute; inset: 0; pointer-events: none; }}
    .icon-box {{
        position: absolute;
        font-size: 2rem;
        opacity: 0.2;
        animation: floatIcon 6s infinite ease-in-out;
    }}
    .icon-box:nth-child(1) {{ top: 20%; left: 15%; animation-delay: 0s; }}
    .icon-box:nth-child(2) {{ top: 30%; right: 15%; animation-delay: 2s; }}
    .icon-box:nth-child(3) {{ bottom: 20%; left: 20%; animation-delay: 4s; }}
    @keyframes floatIcon {{
        0%, 100% {{ transform: translateY(0); }}
        50% {{ transform: translateY(-30px); }}
    }}
    </style>
    '''
