from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    title = props.get("title", "GAME ON")
    subtitle = props.get("subtitle", "Enter the next level")
    cta = props.get("cta", "PLAY NOW")
    
    # Use colors from user's selected palette - no hardcoded fallbacks
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="gaming-hero gaming-hero-glitch" id="hero">
        <div class="scan-lines"></div>
        <div class="hero-content">
            <h1 class="glitch-title" data-text="{title}">{title}</h1>
            <p class="hero-subtitle">{subtitle}</p>
            <a href="#play" class="btn-glitch">{cta}</a>
        </div>
    </section>
    
    <style>
    .gaming-hero-glitch {{
        min-height: 100vh;
        background: {background};
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
        overflow: hidden;
    }}
    .scan-lines {{
        position: absolute;
        inset: 0;
        background: repeating-linear-gradient(
            0deg,
            rgba(0,0,0,0.1) 0px,
            rgba(0,0,0,0.1) 1px,
            transparent 1px,
            transparent 2px
        );
        pointer-events: none;
        z-index: 10;
    }}
    .gaming-hero-glitch .hero-content {{
        position: relative;
        z-index: 2;
        text-align: center;
        padding: 40px;
    }}
    .glitch-title {{
        font-family: 'Orbitron', sans-serif;
        font-size: clamp(4rem, 15vw, 12rem);
        font-weight: 900;
        color: #fff;
        position: relative;
        text-transform: uppercase;
        animation: glitch 1s infinite;
    }}
    .glitch-title::before,
    .glitch-title::after {{
        content: attr(data-text);
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
    }}
    .glitch-title::before {{
        color: {primary};
        animation: glitch-1 2s infinite linear alternate-reverse;
        clip-path: polygon(0 0, 100% 0, 100% 35%, 0 35%);
    }}
    .glitch-title::after {{
        color: {secondary};
        animation: glitch-2 3s infinite linear alternate-reverse;
        clip-path: polygon(0 65%, 100% 65%, 100% 100%, 0 100%);
    }}
    @keyframes glitch {{
        2%, 64% {{ transform: translate(2px, 0) skew(0deg); }}
        4%, 60% {{ transform: translate(-2px, 0) skew(0deg); }}
        62% {{ transform: translate(0, 0) skew(5deg); }}
    }}
    @keyframes glitch-1 {{
        0% {{ transform: translateX(0); }}
        20% {{ transform: translateX(-3px); }}
        40% {{ transform: translateX(3px); }}
        60% {{ transform: translateX(-1px); }}
        80% {{ transform: translateX(2px); }}
        100% {{ transform: translateX(0); }}
    }}
    @keyframes glitch-2 {{
        0% {{ transform: translateX(0); }}
        20% {{ transform: translateX(3px); }}
        40% {{ transform: translateX(-3px); }}
        60% {{ transform: translateX(1px); }}
        80% {{ transform: translateX(-2px); }}
        100% {{ transform: translateX(0); }}
    }}
    .gaming-hero-glitch .hero-subtitle {{
        font-size: 1.2rem;
        color: #666;
        letter-spacing: 6px;
        text-transform: uppercase;
        margin: 30px 0 50px;
    }}
    .btn-glitch {{
        display: inline-block;
        padding: 20px 60px;
        background: {primary};
        color: #000;
        font-weight: 800;
        font-size: 1rem;
        letter-spacing: 3px;
        text-decoration: none;
        text-transform: uppercase;
        position: relative;
        overflow: hidden;
        transition: all 0.3s;
    }}
    .btn-glitch:hover {{
        box-shadow: 0 0 50px {primary}80;
        transform: scale(1.05);
    }}
    .btn-glitch::before {{
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
        animation: shine 2s infinite;
    }}
    @keyframes shine {{
        to {{ left: 100%; }}
    }}
    </style>
    '''
