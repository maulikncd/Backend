from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Masonry Grid - Pinterest style layout"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    projects = [
        {"title": "E-Commerce", "cat": "Web", "tall": True},
        {"title": "Dashboard", "cat": "App", "tall": False},
        {"title": "Portfolio", "cat": "Web", "tall": False},
        {"title": "Mobile App", "cat": "Mobile", "tall": True},
        {"title": "Analytics", "cat": "Dashboard", "tall": False},
        {"title": "SaaS Tool", "cat": "SaaS", "tall": False},
    ]
    
    cards_html = ""
    for p in projects:
        tall = "tall" if p["tall"] else ""
        cards_html += f'''
        <div class="masonry-card {tall}">
            <div class="card-visual"><span>{p['title'][0]}</span></div>
            <div class="card-overlay">
                <span class="cat">{p['cat']}</span>
                <h3>{p['title']}</h3>
            </div>
        </div>
        '''
    
    return f'''
    <section class="portfolio-projects-masonry" id="projects">
        <div class="masonry-container">
            <div class="masonry-header">
                <h2>My Work</h2>
            </div>
            <div class="masonry-grid">{cards_html}</div>
        </div>
    </section>
    
    <style>
    .portfolio-projects-masonry {{ padding: 120px 24px; background: {background}; }}
    .masonry-container {{ max-width: 1200px; margin: 0 auto; }}
    .masonry-header {{ text-align: center; margin-bottom: 60px; }}
    .masonry-header h2 {{ font-size: clamp(2.5rem, 5vw, 4rem); font-weight: 800; color: {text}; }}
    .masonry-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); grid-auto-rows: 180px; gap: 24px; }}
    .masonry-card {{ position: relative; border-radius: 20px; overflow: hidden; cursor: pointer; }}
    .masonry-card.tall {{ grid-row: span 2; }}
    .card-visual {{ width: 100%; height: 100%; background: linear-gradient(135deg, {primary}25, {primary}05); display: flex; align-items: center; justify-content: center; transition: transform 0.5s ease; }}
    .card-visual span {{ font-size: 4rem; font-weight: 900; color: {primary}40; }}
    .masonry-card:hover .card-visual {{ transform: scale(1.1); }}
    .card-overlay {{ position: absolute; inset: 0; background: linear-gradient(to top, {background}E6, transparent 50%); padding: 24px; display: flex; flex-direction: column; justify-content: flex-end; opacity: 0; transition: opacity 0.3s ease; }}
    .masonry-card:hover .card-overlay {{ opacity: 1; }}
    .cat {{ display: inline-block; padding: 5px 12px; background: {primary}; color: {background}; font-size: 0.75rem; font-weight: 700; border-radius: 100px; margin-bottom: 8px; width: fit-content; }}
    .card-overlay h3 {{ font-size: 1.2rem; font-weight: 700; color: {text}; }}
    @media (max-width: 900px) {{ .masonry-grid {{ grid-template-columns: 1fr 1fr; }} }}
    </style>
    '''
