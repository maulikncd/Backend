from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Neon Cyber Hero - Cyberpunk style with neon glows"""
    title = props.get("title", "Enter the Game")
    subtitle = props.get("subtitle", "Experience the next level")
    cta = props.get("cta", "Play Now")
    
    # Use colors from user's selected palette - no hardcoded fallbacks
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="gaming-hero-cyber" id="hero">
        <div class="cyber-bg"><div class="grid-lines"></div></div>
        <div class="cyber-content">
            <div class="glitch-text">{title}</div>
            <p class="cyber-subtitle">{subtitle}</p>
            <div class="cyber-cta"><a href="#games" class="neon-btn">{cta}</a><a href="#trailer" class="ghost-btn">Watch Trailer</a></div>
            <div class="cyber-stats"><div class="stat"><span class="num">2M+</span><span class="label">Players</span></div><div class="stat"><span class="num">4.9</span><span class="label">Rating</span></div><div class="stat"><span class="num">50+</span><span class="label">Awards</span></div></div>
        </div>
    </section>
    <style>
    .gaming-hero-cyber {{ min-height: 100vh; background: {background}; position: relative; display: flex; align-items: center; justify-content: center; text-align: center; overflow: hidden; }}
    .cyber-bg {{ position: absolute; inset: 0; }}
    .grid-lines {{ position: absolute; inset: 0; background-image: linear-gradient({primary}10 1px, transparent 1px), linear-gradient(90deg, {primary}10 1px, transparent 1px); background-size: 50px 50px; animation: gridMove 20s linear infinite; }}
    @keyframes gridMove {{ 0% {{ transform: perspective(500px) rotateX(60deg) translateY(0); }} 100% {{ transform: perspective(500px) rotateX(60deg) translateY(50px); }} }}
    .cyber-content {{ position: relative; z-index: 2; color: #fff; }}
    .glitch-text {{ font-size: clamp(4rem, 12vw, 10rem); font-weight: 900; text-transform: uppercase; letter-spacing: -5px; text-shadow: 0 0 30px {primary}, 0 0 60px {primary}50; animation: glitch 3s infinite; }}
    @keyframes glitch {{ 0%, 90%, 100% {{ transform: translate(0); }} 92% {{ transform: translate(-5px, 2px); }} 94% {{ transform: translate(5px, -2px); }} }}
    .cyber-subtitle {{ font-size: 1.5rem; color: {primary}; margin: 20px 0 40px; letter-spacing: 5px; text-transform: uppercase; }}
    .cyber-cta {{ display: flex; gap: 20px; justify-content: center; margin-bottom: 60px; }}
    .neon-btn {{ padding: 18px 50px; background: {primary}; color: #000; font-weight: 700; text-decoration: none; text-transform: uppercase; letter-spacing: 2px; clip-path: polygon(10% 0, 100% 0, 90% 100%, 0 100%); transition: 0.3s; }}
    .neon-btn:hover {{ box-shadow: 0 0 30px {primary}; }}
    .ghost-btn {{ padding: 18px 50px; border: 2px solid {primary}; color: {primary}; font-weight: 700; text-decoration: none; text-transform: uppercase; letter-spacing: 2px; transition: 0.3s; }}
    .ghost-btn:hover {{ background: {primary}20; }}
    .cyber-stats {{ display: flex; gap: 60px; justify-content: center; }}
    .stat .num {{ display: block; font-size: 3rem; font-weight: 800; color: {primary}; }}
    .stat .label {{ font-size: 0.9rem; color: #888; text-transform: uppercase; letter-spacing: 2px; }}
    </style>
    '''
