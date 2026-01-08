from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Filter Tabs - Projects with category filters"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    projects = [
        {"title": "E-Commerce", "cat": "Web"},
        {"title": "Dashboard", "cat": "App"},
        {"title": "Mobile App", "cat": "Mobile"},
        {"title": "Portfolio", "cat": "Web"},
        {"title": "Analytics", "cat": "App"},
        {"title": "SaaS Tool", "cat": "Web"},
    ]
    
    cards_html = ""
    for p in projects:
        cards_html += f'''
        <div class="filter-card" data-cat="{p['cat'].lower()}">
            <div class="card-thumb"><span>{p['title'][0]}</span></div>
            <div class="card-info">
                <span class="cat">{p['cat']}</span>
                <h3>{p['title']}</h3>
            </div>
        </div>
        '''
    
    return f'''
    <section class="portfolio-projects-filter" id="projects">
        <div class="filter-container">
            <div class="filter-header">
                <h2>My Projects</h2>
                <div class="filter-tabs">
                    <button class="tab active">All</button>
                    <button class="tab">Web</button>
                    <button class="tab">App</button>
                    <button class="tab">Mobile</button>
                </div>
            </div>
            <div class="filter-grid">{cards_html}</div>
        </div>
    </section>
    
    <style>
    .portfolio-projects-filter {{ padding: 120px 24px; background: {background}; }}
    .filter-container {{ max-width: 1200px; margin: 0 auto; }}
    .filter-header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 48px; flex-wrap: wrap; gap: 24px; }}
    .filter-header h2 {{ font-size: clamp(2rem, 4vw, 3rem); font-weight: 800; color: {text}; }}
    .filter-tabs {{ display: flex; gap: 10px; }}
    .tab {{ padding: 10px 24px; background: {text}08; border: none; color: {secondary}; font-weight: 600; border-radius: 100px; cursor: pointer; transition: all 0.3s ease; }}
    .tab.active, .tab:hover {{ background: {primary}; color: {background}; }}
    .filter-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 32px; }}
    .filter-card {{ background: {text}05; border-radius: 20px; overflow: hidden; transition: all 0.4s ease; cursor: pointer; }}
    .filter-card:hover {{ transform: translateY(-8px); box-shadow: 0 30px 60px {primary}10; }}
    .card-thumb {{ aspect-ratio: 4/3; background: linear-gradient(135deg, {primary}20, {primary}05); display: flex; align-items: center; justify-content: center; }}
    .card-thumb span {{ font-size: 4rem; font-weight: 900; color: {primary}30; }}
    .card-info {{ padding: 24px; }}
    .cat {{ display: inline-block; padding: 4px 12px; background: {primary}15; color: {primary}; font-size: 0.8rem; font-weight: 600; border-radius: 100px; margin-bottom: 8px; }}
    .card-info h3 {{ font-size: 1.3rem; font-weight: 700; color: {text}; }}
    @media (max-width: 900px) {{ .filter-grid {{ grid-template-columns: repeat(2, 1fr); }} }}
    </style>
    '''
