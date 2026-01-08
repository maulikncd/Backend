from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Progress Bars - Skills with progress indicators"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    skills = [
        {"name": "React / Next.js", "level": 95},
        {"name": "Node.js / Express", "level": 90},
        {"name": "Python / Django", "level": 85},
        {"name": "TypeScript", "level": 88},
        {"name": "PostgreSQL / MongoDB", "level": 82},
        {"name": "UI/UX Design", "level": 78},
    ]
    
    bars_html = ""
    for s in skills:
        bars_html += f'''
        <div class="skill-bar">
            <div class="skill-info"><span class="skill-name">{s['name']}</span><span class="skill-level">{s['level']}%</span></div>
            <div class="bar-track"><div class="bar-fill" style="width: {s['level']}%"></div></div>
        </div>
        '''
    
    return f'''
    <section class="portfolio-skills-bars" id="skills">
        <div class="bars-container">
            <div class="bars-header"><span class="tag">Skills</span><h2>Technical Expertise</h2></div>
            <div class="bars-list">{bars_html}</div>
        </div>
    </section>
    
    <style>
    .portfolio-skills-bars {{ padding: 120px 24px; background: {background}; }}
    .bars-container {{ max-width: 800px; margin: 0 auto; }}
    .bars-header {{ text-align: center; margin-bottom: 60px; }}
    .tag {{ display: inline-block; padding: 10px 24px; background: {primary}15; color: {primary}; font-weight: 600; border-radius: 100px; margin-bottom: 20px; }}
    .bars-header h2 {{ font-size: clamp(2.5rem, 5vw, 4rem); font-weight: 800; color: {text}; }}
    .bars-list {{ display: flex; flex-direction: column; gap: 28px; }}
    .skill-bar {{ }}
    .skill-info {{ display: flex; justify-content: space-between; margin-bottom: 10px; }}
    .skill-name {{ font-weight: 600; color: {text}; }}
    .skill-level {{ color: {primary}; font-weight: 700; }}
    .bar-track {{ height: 12px; background: {text}10; border-radius: 100px; overflow: hidden; }}
    .bar-fill {{ height: 100%; background: linear-gradient(90deg, {primary}, {primary}80); border-radius: 100px; transition: width 1s ease; }}
    </style>
    '''
