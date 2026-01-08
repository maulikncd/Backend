from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Icon Cards - Skills with icons in cards"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    skills = [
        {"icon": "⚛️", "name": "React", "desc": "Frontend framework"},
        {"icon": "🟢", "name": "Node.js", "desc": "Backend runtime"},
        {"icon": "🐍", "name": "Python", "desc": "Backend & AI"},
        {"icon": "📘", "name": "TypeScript", "desc": "Type-safe JS"},
        {"icon": "🎨", "name": "Figma", "desc": "UI/UX Design"},
        {"icon": "☁️", "name": "AWS", "desc": "Cloud services"},
        {"icon": "🐳", "name": "Docker", "desc": "Containerization"},
        {"icon": "📊", "name": "Data", "desc": "Analytics & viz"},
    ]
    
    cards_html = ""
    for s in skills:
        cards_html += f'''
        <div class="skill-card">
            <span class="skill-icon">{s['icon']}</span>
            <h3>{s['name']}</h3>
            <p>{s['desc']}</p>
        </div>
        '''
    
    return f'''
    <section class="portfolio-skills-icons" id="skills">
        <div class="icons-container">
            <div class="icons-header"><h2>Skills & Tools</h2></div>
            <div class="icons-grid">{cards_html}</div>
        </div>
    </section>
    
    <style>
    .portfolio-skills-icons {{ padding: 120px 24px; background: {background}; }}
    .icons-container {{ max-width: 1100px; margin: 0 auto; }}
    .icons-header {{ text-align: center; margin-bottom: 60px; }}
    .icons-header h2 {{ font-size: clamp(2.5rem, 5vw, 4rem); font-weight: 800; color: {text}; }}
    .icons-grid {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px; }}
    .skill-card {{ background: {text}05; border: 1px solid {text}10; border-radius: 20px; padding: 32px; text-align: center; transition: all 0.4s ease; }}
    .skill-card:hover {{ transform: translateY(-8px); border-color: {primary}40; box-shadow: 0 30px 60px {primary}10; }}
    .skill-icon {{ display: block; font-size: 3rem; margin-bottom: 16px; }}
    .skill-card h3 {{ font-size: 1.2rem; font-weight: 700; color: {text}; margin-bottom: 6px; }}
    .skill-card p {{ color: {secondary}; font-size: 0.9rem; }}
    @media (max-width: 900px) {{ .icons-grid {{ grid-template-columns: repeat(2, 1fr); }} }}
    </style>
    '''
