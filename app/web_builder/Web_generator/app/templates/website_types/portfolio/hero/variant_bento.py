from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Bento Hero - Modern bento grid layout"""
    name = props.get("name", "John Doe")
    title = props.get("title", "Creative Developer")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="portfolio-hero-bento" id="hero">
        <div class="bento-container">
            <div class="bento-grid">
                <div class="bento-item intro">
                    <span class="label">Hello, I'm</span>
                    <h1>{name}</h1>
                    <p>{title} crafting beautiful digital experiences</p>
                    <a href="#contact" class="cta">Get in Touch →</a>
                </div>
                <div class="bento-item photo">
                    <div class="avatar">{name[0]}</div>
                </div>
                <div class="bento-item stat">
                    <span class="num">5+</span>
                    <span class="lbl">Years Experience</span>
                </div>
                <div class="bento-item stat">
                    <span class="num">50+</span>
                    <span class="lbl">Projects Completed</span>
                </div>
                <div class="bento-item skills">
                    <span class="skill">React</span>
                    <span class="skill">Node.js</span>
                    <span class="skill">Python</span>
                    <span class="skill">UI/UX</span>
                </div>
                <div class="bento-item social">
                    <a href="#">GitHub</a>
                    <a href="#">LinkedIn</a>
                    <a href="#">Twitter</a>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    .portfolio-hero-bento {{ min-height: 100vh; background: {background}; display: flex; align-items: center; padding: 80px 24px; }}
    .bento-container {{ max-width: 1100px; margin: 0 auto; width: 100%; }}
    .bento-grid {{ display: grid; grid-template-columns: repeat(4, 1fr); grid-template-rows: repeat(3, auto); gap: 20px; }}
    .bento-item {{ background: {text}05; border: 1px solid {text}10; border-radius: 24px; padding: 32px; }}
    .bento-item.intro {{ grid-column: span 2; grid-row: span 2; display: flex; flex-direction: column; justify-content: center; }}
    .bento-item.photo {{ grid-row: span 2; display: flex; align-items: center; justify-content: center; background: linear-gradient(135deg, {primary}20, {primary}05); }}
    .bento-item.skills {{ grid-column: span 2; display: flex; gap: 12px; flex-wrap: wrap; align-items: center; }}
    .bento-item.social {{ grid-column: span 2; display: flex; gap: 24px; align-items: center; justify-content: center; }}
    .label {{ color: {primary}; font-weight: 600; margin-bottom: 8px; }}
    .intro h1 {{ font-size: clamp(2.5rem, 5vw, 4rem); font-weight: 900; color: {text}; line-height: 1.1; margin-bottom: 16px; }}
    .intro p {{ color: {secondary}; font-size: 1.1rem; line-height: 1.6; margin-bottom: 32px; }}
    .cta {{ color: {primary}; text-decoration: none; font-weight: 700; font-size: 1.1rem; }}
    .avatar {{ width: 150px; height: 150px; background: {primary}; color: {background}; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 4rem; font-weight: 900; }}
    .stat {{ text-align: center; }}
    .num {{ display: block; font-size: 2.5rem; font-weight: 900; color: {primary}; }}
    .lbl {{ color: {secondary}; font-size: 0.9rem; }}
    .skill {{ padding: 10px 20px; background: {primary}15; color: {primary}; font-weight: 600; border-radius: 100px; font-size: 0.9rem; }}
    .social a {{ color: {text}; text-decoration: none; font-weight: 600; transition: color 0.3s ease; }}
    .social a:hover {{ color: {primary}; }}
    @media (max-width: 900px) {{ .bento-grid {{ grid-template-columns: 1fr 1fr; }} .bento-item.intro {{ grid-column: span 2; }} }}
    </style>
    '''
