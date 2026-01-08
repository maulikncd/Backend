from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Floating Cards - Hero with floating project cards"""
    name = props.get("name", "John Doe")
    title = props.get("title", "Full Stack Developer")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    accent = colors.get("accent")
    
    return f'''
    <section class="portfolio-hero-floating" id="hero">
        <div class="floating-cards">
            <div class="float-card c1"></div>
            <div class="float-card c2"></div>
            <div class="float-card c3"></div>
        </div>
        <div class="hero-container">
            <div class="hero-content">
                <span class="greeting">👋 Hello, I'm</span>
                <h1>{name}</h1>
                <p class="role">{title}</p>
                <p class="intro">Crafting digital experiences with clean code and creative design.</p>
                <div class="hero-actions">
                    <a href="#projects" class="btn-primary">View Projects</a>
                    <a href="#contact" class="btn-secondary">Let's Talk</a>
                </div>
                <div class="social-links">
                    <a href="#">GitHub</a>
                    <a href="#">LinkedIn</a>
                    <a href="#">Twitter</a>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    .portfolio-hero-floating {{ min-height: 100vh; background: {background}; display: flex; align-items: center; position: relative; overflow: hidden; }}
    .floating-cards {{ position: absolute; inset: 0; pointer-events: none; }}
    .float-card {{ position: absolute; background: linear-gradient(135deg, {primary}20, {primary}05); border: 1px solid {primary}20; border-radius: 24px; }}
    .float-card.c1 {{ width: 300px; height: 200px; top: 15%; right: 10%; animation: float1 8s ease-in-out infinite; }}
    .float-card.c2 {{ width: 250px; height: 180px; top: 50%; right: 25%; animation: float2 10s ease-in-out infinite; }}
    .float-card.c3 {{ width: 200px; height: 150px; bottom: 20%; right: 15%; animation: float3 7s ease-in-out infinite; }}
    @keyframes float1 {{ 0%, 100% {{ transform: translateY(0) rotate(5deg); }} 50% {{ transform: translateY(-30px) rotate(-5deg); }} }}
    @keyframes float2 {{ 0%, 100% {{ transform: translateY(0) rotate(-3deg); }} 50% {{ transform: translateY(25px) rotate(3deg); }} }}
    @keyframes float3 {{ 0%, 100% {{ transform: translateY(0) rotate(2deg); }} 50% {{ transform: translateY(-20px) rotate(-2deg); }} }}
    .hero-container {{ max-width: 1200px; margin: 0 auto; padding: 120px 24px; position: relative; z-index: 2; }}
    .hero-content {{ max-width: 600px; }}
    .greeting {{ display: inline-block; padding: 10px 24px; background: {primary}15; color: {primary}; font-weight: 600; border-radius: 100px; margin-bottom: 24px; }}
    .hero-content h1 {{ font-size: clamp(3rem, 8vw, 6rem); font-weight: 900; color: {text}; line-height: 1.1; margin-bottom: 16px; }}
    .role {{ font-size: 1.5rem; color: {primary}; font-weight: 600; margin-bottom: 20px; }}
    .intro {{ font-size: 1.2rem; color: {secondary}; line-height: 1.7; margin-bottom: 40px; }}
    .hero-actions {{ display: flex; gap: 16px; margin-bottom: 48px; }}
    .btn-primary {{ padding: 16px 36px; background: {primary}; color: {background}; text-decoration: none; font-weight: 700; border-radius: 12px; transition: all 0.3s ease; }}
    .btn-primary:hover {{ transform: translateY(-4px); box-shadow: 0 20px 40px {primary}40; }}
    .btn-secondary {{ padding: 16px 36px; background: transparent; border: 2px solid {text}20; color: {text}; text-decoration: none; font-weight: 700; border-radius: 12px; transition: all 0.3s ease; }}
    .btn-secondary:hover {{ border-color: {primary}; color: {primary}; }}
    .social-links {{ display: flex; gap: 24px; }}
    .social-links a {{ color: {secondary}; text-decoration: none; font-weight: 500; transition: color 0.3s ease; }}
    .social-links a:hover {{ color: {primary}; }}
    </style>
    '''
