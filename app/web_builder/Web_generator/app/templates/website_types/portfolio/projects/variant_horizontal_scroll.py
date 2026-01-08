from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Horizontal Scroll - Side scrolling projects"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    projects = [
        {"title": "E-Commerce Platform", "cat": "Web App", "year": "2024"},
        {"title": "Mobile Banking App", "cat": "Mobile", "year": "2024"},
        {"title": "Analytics Dashboard", "cat": "Dashboard", "year": "2023"},
        {"title": "Portfolio Builder", "cat": "SaaS", "year": "2023"},
        {"title": "Task Manager", "cat": "Web App", "year": "2023"},
    ]
    
    cards_html = ""
    for p in projects:
        cards_html += f'''
        <div class="scroll-project">
            <div class="project-visual"><span>{p['title'][0]}</span></div>
            <div class="project-details">
                <span class="cat">{p['cat']}</span>
                <h3>{p['title']}</h3>
                <span class="year">{p['year']}</span>
            </div>
        </div>
        '''
    
    return f'''
    <section class="portfolio-projects-scroll" id="projects">
        <div class="scroll-header">
            <h2>Selected Work</h2>
            <div class="nav-arrows">
                <button class="arrow">←</button>
                <button class="arrow">→</button>
            </div>
        </div>
        <div class="scroll-track">{cards_html}</div>
    </section>
    
    <style>
    .portfolio-projects-scroll {{ padding: 120px 0; background: {background}; }}
    .scroll-header {{ max-width: 1400px; margin: 0 auto 48px; padding: 0 24px; display: flex; justify-content: space-between; align-items: center; }}
    .scroll-header h2 {{ font-size: clamp(2.5rem, 5vw, 4rem); font-weight: 800; color: {text}; }}
    .nav-arrows {{ display: flex; gap: 12px; }}
    .arrow {{ width: 50px; height: 50px; background: {text}08; border: none; border-radius: 50%; color: {text}; font-size: 1.3rem; cursor: pointer; transition: all 0.3s ease; }}
    .arrow:hover {{ background: {primary}; color: {background}; }}
    .scroll-track {{ display: flex; gap: 32px; overflow-x: auto; padding: 0 24px 20px; scroll-snap-type: x mandatory; scrollbar-width: none; }}
    .scroll-track::-webkit-scrollbar {{ display: none; }}
    .scroll-project {{ flex-shrink: 0; width: 400px; background: {text}05; border-radius: 24px; overflow: hidden; scroll-snap-align: start; transition: all 0.4s ease; cursor: pointer; }}
    .scroll-project:hover {{ transform: translateY(-8px); }}
    .project-visual {{ aspect-ratio: 4/3; background: linear-gradient(135deg, {primary}20, {primary}05); display: flex; align-items: center; justify-content: center; }}
    .project-visual span {{ font-size: 5rem; font-weight: 900; color: {primary}30; }}
    .project-details {{ padding: 28px; }}
    .cat {{ display: inline-block; padding: 5px 14px; background: {primary}20; color: {primary}; font-size: 0.8rem; font-weight: 600; border-radius: 100px; margin-bottom: 12px; }}
    .project-details h3 {{ font-size: 1.4rem; font-weight: 700; color: {text}; margin-bottom: 8px; }}
    .year {{ color: {secondary}; }}
    </style>
    '''
