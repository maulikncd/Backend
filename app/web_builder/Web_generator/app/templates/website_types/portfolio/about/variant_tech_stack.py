from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Tech Stack - Showcasing technologies"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    stacks = [
        {"category": "Frontend", "techs": ["React", "Vue", "TypeScript", "Tailwind"]},
        {"category": "Backend", "techs": ["Node.js", "Python", "PostgreSQL", "Redis"]},
        {"category": "Tools", "techs": ["Git", "Docker", "AWS", "Figma"]},
    ]
    
    stacks_html = ""
    for s in stacks:
        techs_html = "".join([f'<span class="tech">{t}</span>' for t in s['techs']])
        stacks_html += f'''
        <div class="stack-card">
            <h3>{s['category']}</h3>
            <div class="techs">{techs_html}</div>
        </div>
        '''
    
    return f'''
    <section class="portfolio-about-stack" id="about">
        <div class="stack-container">
            <div class="stack-intro">
                <span class="tag">About</span>
                <h2>Tech Stack</h2>
                <p>Technologies I work with to bring ideas to life</p>
            </div>
            <div class="stacks-grid">{stacks_html}</div>
        </div>
    </section>
    
    <style>
    .portfolio-about-stack {{ padding: 120px 24px; background: {background}; }}
    .stack-container {{ max-width: 1000px; margin: 0 auto; }}
    .stack-intro {{ text-align: center; margin-bottom: 60px; }}
    .tag {{ display: inline-block; padding: 10px 24px; background: {primary}15; color: {primary}; font-weight: 600; border-radius: 100px; margin-bottom: 20px; }}
    .stack-intro h2 {{ font-size: clamp(2.5rem, 5vw, 4rem); font-weight: 800; color: {text}; margin-bottom: 12px; }}
    .stack-intro p {{ color: {secondary}; font-size: 1.2rem; }}
    .stacks-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 32px; }}
    .stack-card {{ background: {text}05; border: 1px solid {text}10; border-radius: 24px; padding: 32px; }}
    .stack-card h3 {{ font-size: 1.3rem; font-weight: 700; color: {text}; margin-bottom: 20px; padding-bottom: 16px; border-bottom: 2px solid {primary}30; }}
    .techs {{ display: flex; flex-wrap: wrap; gap: 12px; }}
    .tech {{ padding: 10px 20px; background: {primary}15; color: {primary}; font-weight: 600; border-radius: 100px; font-size: 0.9rem; }}
    @media (max-width: 900px) {{ .stacks-grid {{ grid-template-columns: 1fr; }} }}
    </style>
    '''
