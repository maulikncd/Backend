from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Split Layout - Photo on one side, text on other"""
    name = props.get("name", "John Doe")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="portfolio-about-split" id="about">
        <div class="split-container">
            <div class="about-image">
                <div class="image-frame">
                    <div class="avatar">{name[0]}</div>
                </div>
                <div class="decorative-box"></div>
            </div>
            <div class="about-content">
                <span class="tag">About Me</span>
                <h2>Passionate about creating impactful digital experiences</h2>
                <p>I'm a creative developer with 5+ years of experience building modern web applications. I specialize in creating intuitive user interfaces and seamless user experiences.</p>
                <p>When I'm not coding, you'll find me exploring new technologies, contributing to open source, or sharing knowledge with the developer community.</p>
                <div class="stats-row">
                    <div class="stat"><span>5+</span><label>Years Exp.</label></div>
                    <div class="stat"><span>50+</span><label>Projects</label></div>
                    <div class="stat"><span>30+</span><label>Clients</label></div>
                </div>
                <a href="#contact" class="btn-about">Let's Work Together</a>
            </div>
        </div>
    </section>
    
    <style>
    .portfolio-about-split {{ padding: 120px 24px; background: {background}; }}
    .split-container {{ max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: 1fr 1.2fr; gap: 80px; align-items: center; }}
    .about-image {{ position: relative; }}
    .image-frame {{ background: linear-gradient(135deg, {primary}20, {primary}05); border-radius: 24px; padding: 40px; display: flex; align-items: center; justify-content: center; }}
    .avatar {{ width: 250px; height: 300px; background: {primary}; color: {background}; border-radius: 16px; display: flex; align-items: center; justify-content: center; font-size: 8rem; font-weight: 900; }}
    .decorative-box {{ position: absolute; width: 100%; height: 100%; border: 3px solid {primary}30; border-radius: 24px; top: 20px; left: 20px; z-index: -1; }}
    .tag {{ display: inline-block; padding: 10px 24px; background: {primary}15; color: {primary}; font-weight: 600; border-radius: 100px; margin-bottom: 20px; }}
    .about-content h2 {{ font-size: clamp(2rem, 4vw, 3rem); font-weight: 800; color: {text}; line-height: 1.3; margin-bottom: 24px; }}
    .about-content p {{ color: {secondary}; font-size: 1.1rem; line-height: 1.8; margin-bottom: 20px; }}
    .stats-row {{ display: flex; gap: 40px; margin: 40px 0; }}
    .stat span {{ display: block; font-size: 2.5rem; font-weight: 900; color: {primary}; }}
    .stat label {{ color: {secondary}; }}
    .btn-about {{ display: inline-block; padding: 16px 36px; background: {primary}; color: {background}; text-decoration: none; font-weight: 700; border-radius: 12px; transition: all 0.3s ease; }}
    .btn-about:hover {{ transform: translateY(-4px); box-shadow: 0 20px 40px {primary}40; }}
    @media (max-width: 900px) {{ .split-container {{ grid-template-columns: 1fr; }} }}
    </style>
    '''
