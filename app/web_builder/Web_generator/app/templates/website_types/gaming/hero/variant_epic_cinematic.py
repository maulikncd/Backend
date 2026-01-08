from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Epic Cinematic Hero - Movie-style with video bg"""
    title = props.get("title", "The Legend Awaits")
    subtitle = props.get("subtitle", "Your destiny begins here")
    cta = props.get("cta", "Begin Journey")
    
    # Use colors from user's selected palette - no hardcoded fallbacks
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="gaming-hero-cinematic" id="hero">
        <video autoplay muted loop playsinline class="hero-video"><source src="https://assets.mixkit.co/videos/preview/mixkit-futuristic-city-traffic-at-night-11755-large.mp4" type="video/mp4"></video>
        <div class="cinematic-overlay"></div>
        <div class="cinematic-content">
            <span class="release-badge">Available Now</span>
            <h1>{title}</h1>
            <p>{subtitle}</p>
            <div class="cta-row"><a href="#" class="primary-btn">{cta}</a><a href="#" class="play-trailer"><span class="play-icon">▶</span> Watch Trailer</a></div>
        </div>
        <div class="scroll-hint"><span>Scroll</span><div class="scroll-arrow"></div></div>
    </section>
    <style>
    .gaming-hero-cinematic {{ min-height: 100vh; position: relative; display: flex; align-items: center; overflow: hidden; }}
    .hero-video {{ position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; }}
    .cinematic-overlay {{ position: absolute; inset: 0; background: linear-gradient(90deg, {background}E6 0%, {background}50 100%); }}
    .cinematic-content {{ position: relative; z-index: 2; color: {text}; padding: 0 80px; max-width: 800px; }}
    .release-badge {{ display: inline-block; padding: 10px 25px; background: {primary}; font-weight: 700; text-transform: uppercase; letter-spacing: 3px; font-size: 0.8rem; margin-bottom: 30px; color: {background}; }}
    .gaming-hero-cinematic h1 {{ font-size: clamp(3rem, 8vw, 6rem); font-weight: 900; line-height: 1; margin-bottom: 20px; text-transform: uppercase; color: {text}; }}
    .gaming-hero-cinematic p {{ font-size: 1.3rem; color: {secondary}; margin-bottom: 40px; max-width: 500px; }}
    .cta-row {{ display: flex; align-items: center; gap: 30px; }}
    .primary-btn {{ padding: 18px 50px; background: {primary}; color: {background}; font-weight: 700; text-decoration: none; text-transform: uppercase; letter-spacing: 2px; transition: 0.3s; }}
    .primary-btn:hover {{ transform: scale(1.05); box-shadow: 0 10px 40px {primary}50; }}
    .play-trailer {{ display: flex; align-items: center; gap: 15px; color: {text}; text-decoration: none; font-weight: 600; }}
    .play-icon {{ width: 50px; height: 50px; border: 2px solid {text}; border-radius: 50%; display: flex; align-items: center; justify-content: center; transition: 0.3s; }}
    .play-trailer:hover .play-icon {{ background: {primary}; border-color: {primary}; }}
    .scroll-hint {{ position: absolute; bottom: 40px; left: 50%; transform: translateX(-50%); color: {text}; text-align: center; font-size: 0.8rem; letter-spacing: 3px; }}
    .scroll-arrow {{ width: 1px; height: 40px; background: linear-gradient(to bottom, {text}, transparent); margin: 10px auto; animation: scrollBounce 2s infinite; }}
    @keyframes scrollBounce {{ 0%, 100% {{ opacity: 1; transform: translateY(0); }} 50% {{ opacity: 0.5; transform: translateY(10px); }} }}
    </style>
    '''
