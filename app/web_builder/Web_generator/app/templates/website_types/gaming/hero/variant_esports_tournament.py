from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Esports Tournament Hero - Competitive gaming style"""
    title = props.get("title", "WORLD CHAMPIONSHIP")
    subtitle = props.get("subtitle", "The ultimate battle awaits")
    cta = props.get("cta", "Register Now")
    
    # Use colors from user's selected palette - no hardcoded fallbacks
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    accent = colors.get("accent")
    text = colors.get("text")
    
    return f'''
    <section class="gaming-hero-esports" id="hero">
        <div class="esports-bg" style="background: url('https://images.unsplash.com/photo-1542751371-adc38448a05e?w=1920') center/cover"></div>
        <div class="esports-overlay"></div>
        <div class="esports-content">
            <div class="prize-pool"><span class="prize-label">PRIZE POOL</span><span class="prize-amount">$1,000,000</span></div>
            <h1>{title}</h1>
            <p>{subtitle}</p>
            <div class="tournament-info"><div class="info-item"><span class="info-num">256</span><span class="info-label">Teams</span></div><div class="info-item"><span class="info-num">48</span><span class="info-label">Countries</span></div><div class="info-item"><span class="info-num">3</span><span class="info-label">Days</span></div></div>
            <a href="#register" class="register-btn">{cta}</a>
        </div>
    </section>
    <style>
    .gaming-hero-esports {{ min-height: 100vh; position: relative; display: flex; align-items: center; justify-content: center; text-align: center; }}
    .esports-bg {{ position: absolute; inset: 0; }}
    .esports-overlay {{ position: absolute; inset: 0; background: linear-gradient(135deg, {background}E6, {background}CC); }}
    .esports-content {{ position: relative; z-index: 2; color: {text}; }}
    .prize-pool {{ margin-bottom: 30px; }}
    .prize-label {{ display: block; font-size: 0.9rem; letter-spacing: 5px; color: {primary}; margin-bottom: 5px; }}
    .prize-amount {{ font-size: 4rem; font-weight: 900; color: {primary}; text-shadow: 0 0 30px {primary}50; }}
    .gaming-hero-esports h1 {{ font-size: clamp(3rem, 8vw, 6rem); font-weight: 900; text-transform: uppercase; margin-bottom: 15px; letter-spacing: 5px; color: {text}; }}
    .gaming-hero-esports p {{ font-size: 1.3rem; color: {secondary}; margin-bottom: 40px; }}
    .tournament-info {{ display: flex; gap: 60px; justify-content: center; margin-bottom: 50px; }}
    .info-item {{ text-align: center; }}
    .info-num {{ display: block; font-size: 3rem; font-weight: 800; color: {primary}; }}
    .info-label {{ font-size: 0.9rem; text-transform: uppercase; letter-spacing: 2px; color: {secondary}; }}
    .register-btn {{ display: inline-block; padding: 20px 70px; background: linear-gradient(135deg, {primary}, {accent}); color: {background}; font-weight: 800; font-size: 1.1rem; text-decoration: none; text-transform: uppercase; letter-spacing: 3px; transition: 0.3s; }}
    .register-btn:hover {{ transform: scale(1.05); box-shadow: 0 10px 40px {primary}50; }}
    </style>
    '''
