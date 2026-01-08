from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Parallax Layers Hero - Multi-layer depth effect"""
    title = props.get("title", "INFINITE WORLDS")
    cta = props.get("cta", "Explore")
    
    # Use colors from user's selected palette - no hardcoded fallbacks
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="gaming-hero-parallax" id="hero">
        <div class="parallax-layer layer-3"></div>
        <div class="parallax-layer layer-2"></div>
        <div class="parallax-layer layer-1"></div>
        <div class="parallax-content"><h1>{title}</h1><a href="#" class="explore-btn">{cta}</a></div>
    </section>
    <style>
    .gaming-hero-parallax {{ min-height: 100vh; position: relative; overflow: hidden; display: flex; align-items: flex-end; justify-content: center; padding-bottom: 100px; }}
    .parallax-layer {{ position: absolute; inset: 0; background-size: cover; background-position: center bottom; }}
    .layer-3 {{ background-color: {background}; background-image: linear-gradient(to bottom, {background}, {secondary}30); }}
    .layer-2 {{ background: url('https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1920') center/cover; opacity: 0.5; }}
    .layer-1 {{ background: linear-gradient(to top, {background}, transparent 50%); }}
    .parallax-content {{ position: relative; z-index: 10; text-align: center; color: {text}; }}
    .gaming-hero-parallax h1 {{ font-size: clamp(4rem, 12vw, 10rem); font-weight: 900; text-transform: uppercase; letter-spacing: 10px; text-shadow: 0 0 60px {primary}50; margin-bottom: 40px; color: {text}; }}
    .explore-btn {{ display: inline-block; padding: 20px 80px; background: transparent; border: 2px solid {primary}; color: {primary}; font-weight: 700; text-decoration: none; text-transform: uppercase; letter-spacing: 5px; transition: 0.3s; }}
    .explore-btn:hover {{ background: {primary}; color: {background}; box-shadow: 0 0 50px {primary}50; }}
    </style>
    '''
