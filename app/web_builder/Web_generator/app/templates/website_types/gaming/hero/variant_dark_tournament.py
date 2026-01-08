from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    title = props.get("title", "PRO LEAGUE 2024")
    subtitle = props.get("subtitle", "Registration Ends in 02:45:10")
    prize = props.get("prize", "$50,000")
    
    # Use colors from user's selected palette - no hardcoded fallbacks
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    accent = colors.get("accent")
    text = colors.get("text")
    
    return f'''
    <section class="gaming-hero gaming-hero-tournament" id="hero">
        <div class="tournament-bg"></div>
        <div class="hero-content">
            <div class="tournament-badge">WORLD CHAMPIONSHIP</div>
            <h1 class="hero-title">{title}</h1>
            <div class="prize-pool">
                <span class="prize-label">PRIZE POOL</span>
                <span class="prize-amount">{prize}</span>
            </div>
            <p class="hero-subtitle">{subtitle}</p>
            <div class="tournament-actions">
                <a href="#register" class="btn-tournament primary">Register Team</a>
                <a href="#rules" class="btn-tournament secondary">Rules &amp; Info</a>
            </div>
        </div>
        <div class="bracket-bg"></div>
    </section>
    
    <style>
    .gaming-hero-tournament {{
        min-height: 100vh;
        background: {background};
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
        overflow: hidden;
    }}
    .tournament-bg {{
        position: absolute;
        inset: 0;
        background: radial-gradient(circle at 50% 50%, {primary}20 0%, transparent 70%);
        animation: glowPulse 4s infinite alternate;
    }}
    @keyframes glowPulse {{
        from {{ opacity: 0.3; }}
        to {{ opacity: 0.8; }}
    }}
    .hero-content {{ position: relative; z-index: 2; text-align: center; }}
    .tournament-badge {{
        color: {primary};
        font-weight: 900;
        letter-spacing: 10px;
        margin-bottom: 20px;
        font-size: 0.9rem;
    }}
    .gaming-hero-tournament .hero-title {{
        font-family: 'Rajdhani', sans-serif;
        font-size: clamp(3rem, 10vw, 8rem);
        font-weight: 900;
        color: {text};
        line-height: 0.9;
        margin-bottom: 40px;
        font-style: italic;
    }}
    .prize-pool {{
        display: inline-flex;
        flex-direction: column;
        border: 2px solid {primary}30;
        padding: 20px 60px;
        margin-bottom: 40px;
        background: {primary}05;
    }}
    .prize-label {{ color: {secondary}; font-size: 0.8rem; margin-bottom: 10px; }}
    .prize-amount {{ font-size: 3rem; font-weight: 800; color: {text}; }}
    .gaming-hero-tournament .hero-subtitle {{
        color: {primary};
        font-family: 'Orbitron', sans-serif;
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 50px;
    }}
    .tournament-actions {{ display: flex; gap: 20px; justify-content: center; }}
    .btn-tournament {{
        padding: 18px 45px;
        font-weight: 800;
        text-transform: uppercase;
        text-decoration: none;
        transition: 0.3s;
        clip-path: polygon(15% 0, 100% 0, 85% 100%, 0 100%);
    }}
    .btn-tournament.primary {{ background: {primary}; color: {background}; }}
    .btn-tournament.secondary {{ background: {secondary}20; color: {text}; }}
    .bracket-bg {{
        position: absolute;
        inset: 0;
        opacity: 0.05;
        background-image: url('https://www.transparenttextures.com/patterns/carbon-fibre.png');
    }}
    </style>
    '''
