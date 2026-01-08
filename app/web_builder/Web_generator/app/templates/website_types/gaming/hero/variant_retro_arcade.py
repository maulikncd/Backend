from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Retro Arcade Hero - 80s arcade style"""
    title = props.get("title", "PLAYER ONE")
    subtitle = props.get("subtitle", "Insert coin to continue")
    cta = props.get("cta", "Start Game")
    
    # Use colors from user's selected palette - no hardcoded fallbacks
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    accent = colors.get("accent")
    
    return f'''
    <section class="gaming-hero-retro" id="hero">
        <div class="retro-scanlines"></div>
        <div class="retro-content">
            <div class="pixel-border"><h1>{title}</h1></div>
            <p class="blink-text">{subtitle}</p>
            <a href="#games" class="arcade-btn">{cta}</a>
            <div class="high-scores"><span class="hs-title">HIGH SCORES</span><div class="score">1. PRO_GAMER - 999,999</div><div class="score">2. NOOB_SLAYER - 888,888</div><div class="score">3. SPEED_RUN - 777,777</div></div>
        </div>
    </section>
    <style>
    .gaming-hero-retro {{ min-height: 100vh; background: {background}; display: flex; align-items: center; justify-content: center; text-align: center; position: relative; overflow: hidden; }}
    .retro-scanlines {{ position: absolute; inset: 0; background: repeating-linear-gradient(0deg, transparent, transparent 2px, rgba(0,0,0,0.3) 2px, rgba(0,0,0,0.3) 4px); pointer-events: none; z-index: 10; }}
    .retro-content {{ position: relative; z-index: 2; color: #fff; }}
    .pixel-border {{ border: 4px solid {primary}; padding: 20px 60px; margin-bottom: 30px; box-shadow: 0 0 30px {primary}50, inset 0 0 30px {primary}20; }}
    .gaming-hero-retro h1 {{ font-family: 'Press Start 2P', monospace, sans-serif; font-size: clamp(2rem, 6vw, 5rem); color: {primary}; text-shadow: 4px 4px 0 {secondary}, 0 0 20px {primary}; letter-spacing: 5px; }}
    .blink-text {{ font-family: monospace; font-size: 1.2rem; color: {secondary}; animation: blink 1s infinite; margin-bottom: 40px; }}
    @keyframes blink {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: 0; }} }}
    .arcade-btn {{ display: inline-block; padding: 20px 60px; background: {primary}; color: #000; font-family: 'Press Start 2P', monospace; font-size: 1rem; text-decoration: none; border: none; cursor: pointer; box-shadow: 0 6px 0 {secondary}; transition: 0.1s; }}
    .arcade-btn:hover {{ transform: translateY(3px); box-shadow: 0 3px 0 {secondary}; }}
    .high-scores {{ margin-top: 60px; text-align: left; display: inline-block; }}
    .hs-title {{ display: block; color: {secondary}; font-family: monospace; margin-bottom: 15px; letter-spacing: 3px; }}
    .score {{ font-family: monospace; color: {accent}; padding: 5px 0; }}
    </style>
    '''
