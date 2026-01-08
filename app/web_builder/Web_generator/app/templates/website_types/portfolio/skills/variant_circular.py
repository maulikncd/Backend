from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Circular Progress - Skills with circular progress"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    skills = [
        {"name": "React", "level": 95},
        {"name": "Node.js", "level": 90},
        {"name": "Python", "level": 85},
        {"name": "TypeScript", "level": 88},
        {"name": "UI/UX", "level": 80},
        {"name": "DevOps", "level": 75},
    ]
    
    circles_html = ""
    for s in skills:
        dash = 283 * s['level'] / 100
        circles_html += f'''
        <div class="circle-skill">
            <svg viewBox="0 0 100 100">
                <circle class="track" cx="50" cy="50" r="45"/>
                <circle class="fill" cx="50" cy="50" r="45" stroke-dasharray="{dash} 283"/>
            </svg>
            <div class="circle-content"><span class="level">{s['level']}%</span><span class="name">{s['name']}</span></div>
        </div>
        '''
    
    return f'''
    <section class="portfolio-skills-circular" id="skills">
        <div class="circular-container">
            <div class="circular-header"><h2>Skills</h2></div>
            <div class="circles-grid">{circles_html}</div>
        </div>
    </section>
    
    <style>
    .portfolio-skills-circular {{ padding: 120px 24px; background: {background}; }}
    .circular-container {{ max-width: 1000px; margin: 0 auto; }}
    .circular-header {{ text-align: center; margin-bottom: 60px; }}
    .circular-header h2 {{ font-size: clamp(2.5rem, 5vw, 4rem); font-weight: 800; color: {text}; }}
    .circles-grid {{ display: grid; grid-template-columns: repeat(6, 1fr); gap: 24px; }}
    .circle-skill {{ position: relative; text-align: center; }}
    .circle-skill svg {{ width: 120px; height: 120px; transform: rotate(-90deg); }}
    .track {{ fill: none; stroke: {text}10; stroke-width: 8; }}
    .fill {{ fill: none; stroke: {primary}; stroke-width: 8; stroke-linecap: round; transition: stroke-dasharray 1s ease; }}
    .circle-content {{ position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); }}
    .level {{ display: block; font-size: 1.3rem; font-weight: 900; color: {primary}; }}
    .name {{ display: block; font-size: 0.85rem; color: {secondary}; margin-top: 4px; }}
    @media (max-width: 900px) {{ .circles-grid {{ grid-template-columns: repeat(3, 1fr); }} }}
    </style>
    '''
