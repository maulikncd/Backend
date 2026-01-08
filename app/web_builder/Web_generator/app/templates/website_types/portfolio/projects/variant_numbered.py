from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Numbered List - Projects with numbers"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    projects = [
        {"title": "E-Commerce Platform", "desc": "Full-stack online store", "year": "2024"},
        {"title": "Analytics Dashboard", "desc": "Real-time data visualization", "year": "2024"},
        {"title": "Mobile Banking App", "desc": "Secure mobile banking", "year": "2023"},
        {"title": "Portfolio Builder", "desc": "No-code portfolio tool", "year": "2023"},
    ]
    
    list_html = ""
    for i, p in enumerate(projects, 1):
        list_html += f'''
        <div class="num-project">
            <span class="num">0{i}</span>
            <div class="project-info">
                <h3>{p['title']}</h3>
                <p>{p['desc']}</p>
            </div>
            <span class="year">{p['year']}</span>
            <a href="#" class="arrow">→</a>
        </div>
        '''
    
    return f'''
    <section class="portfolio-projects-numbered" id="projects">
        <div class="numbered-container">
            <div class="numbered-header"><h2>Selected Work</h2></div>
            <div class="numbered-list">{list_html}</div>
        </div>
    </section>
    
    <style>
    .portfolio-projects-numbered {{ padding: 120px 24px; background: {background}; }}
    .numbered-container {{ max-width: 1000px; margin: 0 auto; }}
    .numbered-header {{ margin-bottom: 60px; }}
    .numbered-header h2 {{ font-size: clamp(2.5rem, 5vw, 4rem); font-weight: 800; color: {text}; }}
    .numbered-list {{ display: flex; flex-direction: column; }}
    .num-project {{ display: flex; align-items: center; gap: 40px; padding: 40px 0; border-bottom: 1px solid {text}10; transition: all 0.3s ease; }}
    .num-project:hover {{ padding-left: 24px; background: {primary}05; }}
    .num {{ font-size: 3rem; font-weight: 900; color: {primary}30; min-width: 80px; }}
    .project-info {{ flex: 1; }}
    .project-info h3 {{ font-size: 1.5rem; font-weight: 700; color: {text}; margin-bottom: 6px; }}
    .project-info p {{ color: {secondary}; }}
    .year {{ color: {secondary}; font-size: 0.95rem; }}
    .arrow {{ width: 50px; height: 50px; background: {primary}; color: {background}; text-decoration: none; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.3rem; transition: all 0.3s ease; }}
    .arrow:hover {{ transform: scale(1.1); }}
    @media (max-width: 768px) {{ .num-project {{ flex-wrap: wrap; gap: 20px; }} .num {{ min-width: auto; }} }}
    </style>
    '''
