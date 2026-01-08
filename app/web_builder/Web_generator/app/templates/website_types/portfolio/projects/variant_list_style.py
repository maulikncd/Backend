from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """List Style - Clean list layout"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    projects = [
        {"title": "E-Commerce Platform", "cat": "Web App", "year": "2024", "tech": ["React", "Node.js"]},
        {"title": "Analytics Dashboard", "cat": "Dashboard", "year": "2024", "tech": ["Vue", "Python"]},
        {"title": "Mobile Banking", "cat": "Mobile", "year": "2023", "tech": ["React Native"]},
        {"title": "Portfolio Builder", "cat": "SaaS", "year": "2023", "tech": ["Next.js"]},
    ]
    
    list_html = ""
    for p in projects:
        techs = " • ".join(p['tech'])
        list_html += f'''
        <div class="project-row">
            <div class="row-left">
                <h3>{p['title']}</h3>
                <span class="techs">{techs}</span>
            </div>
            <div class="row-right">
                <span class="cat">{p['cat']}</span>
                <span class="year">{p['year']}</span>
                <a href="#" class="link">View →</a>
            </div>
        </div>
        '''
    
    return f'''
    <section class="portfolio-projects-list" id="projects">
        <div class="list-container">
            <div class="list-header">
                <span class="tag">Work</span>
                <h2>Projects</h2>
            </div>
            <div class="projects-list">{list_html}</div>
        </div>
    </section>
    
    <style>
    .portfolio-projects-list {{ padding: 120px 24px; background: {background}; }}
    .list-container {{ max-width: 1000px; margin: 0 auto; }}
    .list-header {{ text-align: center; margin-bottom: 60px; }}
    .tag {{ display: inline-block; padding: 10px 24px; background: {primary}15; color: {primary}; font-weight: 600; border-radius: 100px; margin-bottom: 20px; }}
    .list-header h2 {{ font-size: clamp(2.5rem, 5vw, 4rem); font-weight: 800; color: {text}; }}
    .projects-list {{ display: flex; flex-direction: column; }}
    .project-row {{ display: flex; justify-content: space-between; align-items: center; padding: 32px 0; border-bottom: 1px solid {text}10; transition: all 0.3s ease; }}
    .project-row:hover {{ padding-left: 16px; background: {primary}05; }}
    .row-left h3 {{ font-size: 1.5rem; font-weight: 700; color: {text}; margin-bottom: 6px; }}
    .techs {{ color: {secondary}; font-size: 0.9rem; }}
    .row-right {{ display: flex; align-items: center; gap: 32px; }}
    .cat {{ padding: 6px 16px; background: {primary}15; color: {primary}; font-size: 0.85rem; font-weight: 600; border-radius: 100px; }}
    .year {{ color: {secondary}; }}
    .link {{ color: {primary}; text-decoration: none; font-weight: 600; }}
    @media (max-width: 768px) {{ .project-row {{ flex-direction: column; align-items: flex-start; gap: 16px; }} .row-right {{ flex-wrap: wrap; }} }}
    </style>
    '''
