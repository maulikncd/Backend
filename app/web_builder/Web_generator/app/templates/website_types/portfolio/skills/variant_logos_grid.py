from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Grid Logos - Skills with logo style"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    skills = [
        {"icon": "⚛️", "name": "React"},
        {"icon": "🔷", "name": "Next.js"},
        {"icon": "📗", "name": "Vue"},
        {"icon": "📘", "name": "TypeScript"},
        {"icon": "🟢", "name": "Node.js"},
        {"icon": "🐍", "name": "Python"},
        {"icon": "🗃️", "name": "PostgreSQL"},
        {"icon": "🍃", "name": "MongoDB"},
        {"icon": "🐳", "name": "Docker"},
        {"icon": "☁️", "name": "AWS"},
    ]
    
    logos_html = ""
    for s in skills:
        logos_html += f'''
        <div class="logo-item">
            <span class="logo-icon">{s['icon']}</span>
            <span class="logo-name">{s['name']}</span>
        </div>
        '''
    
    return f'''
    <section class="portfolio-skills-logos" id="skills">
        <div class="logos-container">
            <div class="logos-header"><span class="tag">Tech Stack</span><h2>Tools & Technologies</h2></div>
            <div class="logos-grid">{logos_html}</div>
        </div>
    </section>
    
    <style>
    .portfolio-skills-logos {{ padding: 120px 24px; background: linear-gradient(135deg, {primary}08, {background}); }}
    .logos-container {{ max-width: 1000px; margin: 0 auto; }}
    .logos-header {{ text-align: center; margin-bottom: 60px; }}
    .tag {{ display: inline-block; padding: 10px 24px; background: {primary}15; color: {primary}; font-weight: 600; border-radius: 100px; margin-bottom: 20px; }}
    .logos-header h2 {{ font-size: clamp(2.5rem, 5vw, 4rem); font-weight: 800; color: {text}; }}
    .logos-grid {{ display: grid; grid-template-columns: repeat(5, 1fr); gap: 24px; }}
    .logo-item {{ background: {background}; border-radius: 20px; padding: 32px 16px; text-align: center; box-shadow: 0 10px 40px {primary}08; transition: all 0.4s ease; }}
    .logo-item:hover {{ transform: translateY(-8px); box-shadow: 0 20px 60px {primary}15; }}
    .logo-icon {{ display: block; font-size: 3rem; margin-bottom: 12px; }}
    .logo-name {{ display: block; font-weight: 600; color: {text}; }}
    @media (max-width: 900px) {{ .logos-grid {{ grid-template-columns: repeat(3, 1fr); }} }}
    </style>
    '''
