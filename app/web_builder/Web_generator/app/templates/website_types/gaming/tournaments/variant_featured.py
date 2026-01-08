from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Featured Tournament - Hero style tournament display"""
    title = props.get("title", "Tournaments")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="gaming-tournament-featured" id="tournaments">
        <div class="tournament-hero">
            <img src="https://images.unsplash.com/photo-1542751371-adc38448a05e?w=1920" alt="Tournament">
            <div class="hero-overlay">
                <span class="live-badge">🔴 REGISTRATION OPEN</span>
                <h1>World Championship 2024</h1>
                <p>$1,000,000 Prize Pool • 64 Teams • December 15-20</p>
                <div class="tournament-stats">
                    <div class="stat"><span>64</span><label>Teams</label></div>
                    <div class="stat"><span>$1M</span><label>Prize</label></div>
                    <div class="stat"><span>5</span><label>Days</label></div>
                </div>
                <a href="#" class="btn-register">Register Now</a>
            </div>
        </div>
    </section>
    
    <style>
    .gaming-tournament-featured {{ background: {background}; }}
    .tournament-hero {{ position: relative; min-height: 80vh; display: flex; align-items: center; justify-content: center; }}
    .tournament-hero img {{ position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; }}
    .hero-overlay {{ position: relative; z-index: 2; text-align: center; padding: 60px 24px; background: {background}80; border-radius: 24px; backdrop-filter: blur(10px); max-width: 700px; margin: 0 auto; }}
    .live-badge {{ display: inline-block; padding: 10px 24px; background: #ff3b3b; color: white; font-weight: 700; font-size: 0.85rem; border-radius: 100px; margin-bottom: 24px; animation: pulse 2s infinite; }}
    @keyframes pulse {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: 0.7; }} }}
    .hero-overlay h1 {{ font-family: 'Rajdhani', sans-serif; font-size: clamp(2.5rem, 6vw, 4rem); font-weight: 900; color: {text}; margin-bottom: 16px; }}
    .hero-overlay p {{ color: {secondary}; font-size: 1.2rem; margin-bottom: 40px; }}
    .tournament-stats {{ display: flex; justify-content: center; gap: 48px; margin-bottom: 40px; }}
    .stat {{ text-align: center; }}
    .stat span {{ display: block; font-family: 'Orbitron', sans-serif; font-size: 2.5rem; font-weight: 900; color: {primary}; text-shadow: 0 0 30px {primary}50; }}
    .stat label {{ color: {secondary}; font-size: 0.9rem; }}
    .btn-register {{ display: inline-block; padding: 18px 48px; background: {primary}; color: {background}; text-decoration: none; font-weight: 700; border-radius: 12px; transition: all 0.3s ease; }}
    .btn-register:hover {{ transform: scale(1.05); box-shadow: 0 20px 50px {primary}40; }}
    </style>
    '''
