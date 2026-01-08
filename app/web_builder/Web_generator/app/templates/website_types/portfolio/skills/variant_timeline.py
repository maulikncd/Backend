from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Timeline Skills - Skills by year learned"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    timeline = [
        {"year": "2020", "skills": ["HTML/CSS", "JavaScript", "React"]},
        {"year": "2021", "skills": ["Node.js", "MongoDB", "TypeScript"]},
        {"year": "2022", "skills": ["Python", "Django", "PostgreSQL"]},
        {"year": "2023", "skills": ["Docker", "AWS", "Kubernetes"]},
        {"year": "2024", "skills": ["AI/ML", "GraphQL", "Next.js 14"]},
    ]
    
    items_html = ""
    for t in timeline:
        skills_html = "".join([f'<span>{s}</span>' for s in t['skills']])
        items_html += f'''
        <div class="timeline-item">
            <span class="year">{t['year']}</span>
            <div class="skills-row">{skills_html}</div>
        </div>
        '''
    
    return f'''
    <section class="portfolio-skills-timeline" id="skills">
        <div class="timeline-container">
            <div class="timeline-header"><h2>Learning Journey</h2></div>
            <div class="skills-timeline">{items_html}</div>
        </div>
    </section>
    
    <style>
    .portfolio-skills-timeline {{ padding: 120px 24px; background: {background}; }}
    .timeline-container {{ max-width: 900px; margin: 0 auto; }}
    .timeline-header {{ text-align: center; margin-bottom: 60px; }}
    .timeline-header h2 {{ font-size: clamp(2.5rem, 5vw, 4rem); font-weight: 800; color: {text}; }}
    .skills-timeline {{ display: flex; flex-direction: column; gap: 24px; }}
    .timeline-item {{ display: flex; align-items: center; gap: 40px; padding: 24px; background: {text}05; border-radius: 16px; }}
    .year {{ font-size: 1.5rem; font-weight: 900; color: {primary}; min-width: 80px; }}
    .skills-row {{ display: flex; flex-wrap: wrap; gap: 10px; }}
    .skills-row span {{ padding: 10px 20px; background: {primary}15; color: {primary}; font-weight: 600; border-radius: 100px; font-size: 0.9rem; }}
    @media (max-width: 600px) {{ .timeline-item {{ flex-direction: column; text-align: center; gap: 16px; }} .skills-row {{ justify-content: center; }} }}
    </style>
    '''
