from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    title = props.get("title", "DOMINATE")
    subtitle = props.get("subtitle", "The battlefield awaits")
    cta = props.get("cta", "GET STARTED")
    
    # Use colors from user's selected palette - no hardcoded fallbacks
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="gaming-hero gaming-hero-particles" id="hero">
        <div class="particles">
            <div class="particle"></div>
            <div class="particle"></div>
            <div class="particle"></div>
            <div class="particle"></div>
            <div class="particle"></div>
            <div class="particle"></div>
            <div class="particle"></div>
            <div class="particle"></div>
        </div>
        <div class="hero-content">
            <h1 class="hero-title">{title}</h1>
            <div class="title-underline"></div>
            <p class="hero-subtitle">{subtitle}</p>
            <a href="#start" class="btn-particles">{cta}</a>
        </div>
    </section>
    
    <style>
    .gaming-hero-particles {{
        min-height: 100vh;
        background: radial-gradient(ellipse at center, {secondary}30 0%, {background} 100%);
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
        overflow: hidden;
    }}
    .particles {{
        position: absolute;
        inset: 0;
        overflow: hidden;
    }}
    .particle {{
        position: absolute;
        width: 4px;
        height: 4px;
        background: {primary};
        border-radius: 50%;
        animation: rise 10s infinite;
    }}
    .particle:nth-child(1) {{ left: 10%; animation-delay: 0s; }}
    .particle:nth-child(2) {{ left: 20%; animation-delay: 1s; }}
    .particle:nth-child(3) {{ left: 35%; animation-delay: 2s; }}
    .particle:nth-child(4) {{ left: 50%; animation-delay: 3s; }}
    .particle:nth-child(5) {{ left: 65%; animation-delay: 1.5s; }}
    .particle:nth-child(6) {{ left: 75%; animation-delay: 2.5s; }}
    .particle:nth-child(7) {{ left: 85%; animation-delay: 0.5s; }}
    .particle:nth-child(8) {{ left: 95%; animation-delay: 3.5s; }}
    @keyframes rise {{
        0% {{ bottom: -10%; opacity: 0; transform: scale(0); }}
        10% {{ opacity: 1; transform: scale(1); }}
        90% {{ opacity: 1; }}
        100% {{ bottom: 110%; opacity: 0; transform: scale(0.5); }}
    }}
    .gaming-hero-particles .hero-content {{
        position: relative;
        z-index: 2;
        text-align: center;
        padding: 40px;
    }}
    .gaming-hero-particles .hero-title {{
        font-family: 'Orbitron', sans-serif;
        font-size: clamp(4rem, 12vw, 10rem);
        font-weight: 900;
        color: {text};
        text-transform: uppercase;
        margin-bottom: 16px;
        text-shadow: 0 0 60px {primary}40;
    }}
    .title-underline {{
        width: 200px;
        height: 4px;
        background: linear-gradient(90deg, transparent, {primary}, transparent);
        margin: 0 auto 30px;
    }}
    .gaming-hero-particles .hero-subtitle {{
        font-size: 1.1rem;
        color: {secondary};
        letter-spacing: 4px;
        text-transform: uppercase;
        margin-bottom: 50px;
    }}
    .btn-particles {{
        display: inline-block;
        padding: 20px 50px;
        border: 2px solid {primary};
        color: {primary};
        font-weight: 700;
        font-size: 0.9rem;
        letter-spacing: 3px;
        text-decoration: none;
        text-transform: uppercase;
        transition: all 0.3s;
    }}
    .btn-particles:hover {{
        background: {primary};
        color: {background};
        box-shadow: 0 0 40px {primary}60;
    }}
    </style>
    '''
