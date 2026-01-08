from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Scroll Reveal - Animated reveal on scroll"""
    name = props.get("name", "John Doe")
    title = props.get("title", "Creative Developer")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="portfolio-hero-scroll" id="hero">
        <div class="scroll-content">
            <div class="hero-text">
                <span class="overline">Portfolio 2024</span>
                <h1><span class="line">{name.split()[0] if " " in name else name}</span><br/><span class="line accent">{name.split()[1] if " " in name else title.split()[0]}</span></h1>
                <p class="subtitle">{title}</p>
            </div>
            <div class="hero-visual">
                <div class="circle-outer">
                    <div class="circle-inner">
                        <span>{name[0]}</span>
                    </div>
                </div>
            </div>
            <div class="scroll-indicator">
                <span>Scroll to explore</span>
                <div class="scroll-line"></div>
            </div>
        </div>
    </section>
    
    <style>
    .portfolio-hero-scroll {{ min-height: 100vh; background: {background}; display: flex; align-items: center; position: relative; }}
    .scroll-content {{ max-width: 1400px; margin: 0 auto; padding: 80px 40px; display: grid; grid-template-columns: 1fr 1fr; gap: 60px; align-items: center; width: 100%; }}
    .overline {{ display: inline-block; padding: 10px 24px; background: {primary}15; color: {primary}; font-weight: 600; border-radius: 100px; margin-bottom: 24px; font-size: 0.9rem; letter-spacing: 2px; }}
    .hero-text h1 {{ font-size: clamp(4rem, 10vw, 8rem); font-weight: 900; line-height: 0.95; margin-bottom: 24px; }}
    .line {{ display: block; color: {text}; }}
    .line.accent {{ color: {primary}; }}
    .subtitle {{ font-size: 1.5rem; color: {secondary}; font-weight: 500; }}
    .hero-visual {{ display: flex; justify-content: center; }}
    .circle-outer {{ width: 350px; height: 350px; border: 2px solid {primary}30; border-radius: 50%; display: flex; align-items: center; justify-content: center; animation: rotate 20s linear infinite; }}
    .circle-inner {{ width: 280px; height: 280px; background: linear-gradient(135deg, {primary}, {primary}80); border-radius: 50%; display: flex; align-items: center; justify-content: center; }}
    .circle-inner span {{ font-size: 8rem; font-weight: 900; color: {background}; }}
    @keyframes rotate {{ from {{ transform: rotate(0deg); }} to {{ transform: rotate(360deg); }} }}
    .scroll-indicator {{ position: absolute; bottom: 40px; left: 50%; transform: translateX(-50%); text-align: center; }}
    .scroll-indicator span {{ display: block; color: {secondary}; font-size: 0.85rem; margin-bottom: 12px; }}
    .scroll-line {{ width: 2px; height: 40px; background: linear-gradient(to bottom, {primary}, transparent); margin: 0 auto; animation: scrollAnim 2s infinite; }}
    @keyframes scrollAnim {{ 0% {{ opacity: 0; transform: translateY(-10px); }} 50% {{ opacity: 1; }} 100% {{ opacity: 0; transform: translateY(10px); }} }}
    @media (max-width: 900px) {{ .scroll-content {{ grid-template-columns: 1fr; text-align: center; }} .hero-visual {{ margin-top: 40px; }} }}
    </style>
    '''
