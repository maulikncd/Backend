from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Alternating - Left-right alternating layout"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    projects = [
        {"title": "E-Commerce Platform", "desc": "A full-featured online store with payment integration", "tech": ["React", "Node.js", "MongoDB"]},
        {"title": "Analytics Dashboard", "desc": "Real-time data visualization for business metrics", "tech": ["Vue", "D3.js", "Python"]},
        {"title": "Mobile Banking App", "desc": "Secure mobile banking with biometric authentication", "tech": ["React Native", "Firebase"]},
    ]
    
    projects_html = ""
    for i, p in enumerate(projects):
        reverse = "reverse" if i % 2 == 1 else ""
        techs_html = "".join([f'<span>{t}</span>' for t in p['tech']])
        projects_html += f'''
        <div class="alt-project {reverse}">
            <div class="project-visual"><span>{p['title'][0]}</span></div>
            <div class="project-content">
                <h3>{p['title']}</h3>
                <p>{p['desc']}</p>
                <div class="tech-stack">{techs_html}</div>
                <a href="#" class="project-link">View Project →</a>
            </div>
        </div>
        '''
    
    return f'''
    <section class="portfolio-projects-alt" id="projects">
        <div class="alt-container">
            <div class="alt-header"><h2>Featured Projects</h2></div>
            <div class="alt-projects">{projects_html}</div>
        </div>
    </section>
    
    <style>
    .portfolio-projects-alt {{ padding: 120px 24px; background: {background}; }}
    .alt-container {{ max-width: 1100px; margin: 0 auto; }}
    .alt-header {{ text-align: center; margin-bottom: 80px; }}
    .alt-header h2 {{ font-size: clamp(2.5rem, 5vw, 4rem); font-weight: 800; color: {text}; }}
    .alt-projects {{ display: flex; flex-direction: column; gap: 100px; }}
    .alt-project {{ display: grid; grid-template-columns: 1fr 1fr; gap: 60px; align-items: center; }}
    .alt-project.reverse {{ direction: rtl; }}
    .alt-project.reverse > * {{ direction: ltr; }}
    .project-visual {{ aspect-ratio: 4/3; background: linear-gradient(135deg, {primary}20, {primary}05); border-radius: 24px; display: flex; align-items: center; justify-content: center; }}
    .project-visual span {{ font-size: 6rem; font-weight: 900; color: {primary}30; }}
    .project-content h3 {{ font-size: 2rem; font-weight: 800; color: {text}; margin-bottom: 16px; }}
    .project-content p {{ color: {secondary}; font-size: 1.1rem; line-height: 1.7; margin-bottom: 24px; }}
    .tech-stack {{ display: flex; gap: 10px; margin-bottom: 24px; }}
    .tech-stack span {{ padding: 8px 16px; background: {primary}15; color: {primary}; font-size: 0.9rem; font-weight: 600; border-radius: 100px; }}
    .project-link {{ color: {primary}; text-decoration: none; font-weight: 700; font-size: 1.1rem; }}
    @media (max-width: 900px) {{ .alt-project, .alt-project.reverse {{ grid-template-columns: 1fr; direction: ltr; }} }}
    </style>
    '''
