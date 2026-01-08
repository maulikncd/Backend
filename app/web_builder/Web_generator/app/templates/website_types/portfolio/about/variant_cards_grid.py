from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Cards Grid - Multiple info cards"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    cards = [
        {"icon": "💻", "title": "Development", "desc": "Building scalable web applications with modern technologies"},
        {"icon": "🎨", "title": "Design", "desc": "Creating beautiful and intuitive user interfaces"},
        {"icon": "🚀", "title": "Performance", "desc": "Optimizing for speed and user experience"},
        {"icon": "🤝", "title": "Collaboration", "desc": "Working closely with teams to deliver quality"},
    ]
    
    cards_html = ""
    for c in cards:
        cards_html += f'''
        <div class="about-card">
            <span class="card-icon">{c['icon']}</span>
            <h3>{c['title']}</h3>
            <p>{c['desc']}</p>
        </div>
        '''
    
    return f'''
    <section class="portfolio-about-cards" id="about">
        <div class="cards-container">
            <div class="about-header">
                <span class="tag">About</span>
                <h2>What I Do</h2>
                <p>I specialize in creating digital experiences that make a difference</p>
            </div>
            <div class="cards-grid">{cards_html}</div>
        </div>
    </section>
    
    <style>
    .portfolio-about-cards {{ padding: 120px 24px; background: {background}; }}
    .cards-container {{ max-width: 1100px; margin: 0 auto; }}
    .about-header {{ text-align: center; margin-bottom: 60px; }}
    .tag {{ display: inline-block; padding: 10px 24px; background: {primary}15; color: {primary}; font-weight: 600; border-radius: 100px; margin-bottom: 20px; }}
    .about-header h2 {{ font-size: clamp(2.5rem, 5vw, 4rem); font-weight: 800; color: {text}; margin-bottom: 16px; }}
    .about-header p {{ color: {secondary}; font-size: 1.2rem; }}
    .cards-grid {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px; }}
    .about-card {{ background: {text}05; border: 1px solid {text}10; border-radius: 24px; padding: 32px; text-align: center; transition: all 0.4s ease; }}
    .about-card:hover {{ transform: translateY(-8px); border-color: {primary}40; box-shadow: 0 30px 60px {primary}10; }}
    .card-icon {{ display: block; font-size: 3rem; margin-bottom: 20px; }}
    .about-card h3 {{ font-size: 1.3rem; font-weight: 700; color: {text}; margin-bottom: 12px; }}
    .about-card p {{ color: {secondary}; font-size: 0.95rem; line-height: 1.6; }}
    @media (max-width: 900px) {{ .cards-grid {{ grid-template-columns: repeat(2, 1fr); }} }}
    @media (max-width: 600px) {{ .cards-grid {{ grid-template-columns: 1fr; }} }}
    </style>
    '''
