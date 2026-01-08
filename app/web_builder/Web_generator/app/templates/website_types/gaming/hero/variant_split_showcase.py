from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Split Showcase Hero - Game art on side"""
    title = props.get("title", "SHADOW LEGENDS")
    subtitle = props.get("subtitle", "Conquer the darkness")
    cta = props.get("cta", "Download Free")
    
    # Use colors from user's selected palette - no hardcoded fallbacks
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="gaming-hero-split" id="hero">
        <div class="split-left">
            <span class="game-badge">NEW RELEASE</span>
            <h1>{title}</h1>
            <p>{subtitle}</p>
            <div class="platform-icons"><span title="PC">🖥️</span><span title="PlayStation">🎮</span><span title="Xbox">🎯</span><span title="Switch">📱</span></div>
            <div class="action-row"><a href="#" class="download-btn">{cta}</a><div class="rating"><span class="stars">★★★★★</span><span class="count">50K+ Reviews</span></div></div>
        </div>
        <div class="split-right"><img src="https://images.unsplash.com/photo-1538481199705-c710c4e965fc?w=800" alt="Game Art"><div class="art-glow"></div></div>
    </section>
    <style>
    .gaming-hero-split {{ min-height: 100vh; background: {background}; display: grid; grid-template-columns: 1fr 1fr; align-items: center; overflow: hidden; }}
    .split-left {{ padding: 80px; color: {text}; }}
    .game-badge {{ display: inline-block; padding: 8px 20px; background: {primary}; color: {background}; font-size: 0.75rem; font-weight: 700; letter-spacing: 2px; margin-bottom: 30px; }}
    .gaming-hero-split h1 {{ font-size: clamp(3rem, 5vw, 5rem); font-weight: 900; text-transform: uppercase; margin-bottom: 20px; background: linear-gradient(135deg, {text}, {primary}); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
    .gaming-hero-split p {{ font-size: 1.2rem; color: {secondary}; margin-bottom: 30px; max-width: 450px; }}
    .platform-icons {{ display: flex; gap: 20px; margin-bottom: 40px; font-size: 2rem; }}
    .action-row {{ display: flex; gap: 30px; align-items: center; }}
    .download-btn {{ padding: 18px 50px; background: {primary}; color: {background}; font-weight: 700; text-decoration: none; text-transform: uppercase; letter-spacing: 2px; transition: 0.3s; }}
    .download-btn:hover {{ transform: translateY(-3px); box-shadow: 0 15px 40px {primary}50; }}
    .rating .stars {{ color: {primary}; font-size: 1.2rem; display: block; }}
    .rating .count {{ font-size: 0.85rem; color: {secondary}; }}
    .split-right {{ position: relative; height: 100%; display: flex; align-items: center; justify-content: center; }}
    .split-right img {{ max-height: 90vh; width: auto; object-fit: contain; }}
    .art-glow {{ position: absolute; width: 300px; height: 300px; background: {primary}; filter: blur(150px); opacity: 0.4; }}
    @media (max-width: 968px) {{ .gaming-hero-split {{ grid-template-columns: 1fr; }} .split-right {{ display: none; }} }}
    </style>
    '''
