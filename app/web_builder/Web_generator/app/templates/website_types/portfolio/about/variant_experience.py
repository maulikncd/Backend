from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Experience Focus - Highlighting work experience"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    experiences = [
        {"company": "Tech Corp", "role": "Senior Developer", "period": "2022 - Present"},
        {"company": "Startup Inc", "role": "Full Stack Developer", "period": "2020 - 2022"},
        {"company": "Agency XYZ", "role": "Frontend Developer", "period": "2018 - 2020"},
    ]
    
    exp_html = ""
    for e in experiences:
        exp_html += f'''
        <div class="exp-item">
            <div class="exp-period">{e['period']}</div>
            <div class="exp-info">
                <h4>{e['role']}</h4>
                <span class="company">{e['company']}</span>
            </div>
        </div>
        '''
    
    return f'''
    <section class="portfolio-about-experience" id="about">
        <div class="exp-container">
            <div class="exp-header">
                <span class="tag">About</span>
                <h2>My Journey</h2>
                <p>A timeline of my professional experience</p>
            </div>
            <div class="exp-list">{exp_html}</div>
        </div>
    </section>
    
    <style>
    .portfolio-about-experience {{ padding: 120px 24px; background: {background}; }}
    .exp-container {{ max-width: 800px; margin: 0 auto; }}
    .exp-header {{ text-align: center; margin-bottom: 60px; }}
    .tag {{ display: inline-block; padding: 10px 24px; background: {primary}15; color: {primary}; font-weight: 600; border-radius: 100px; margin-bottom: 20px; }}
    .exp-header h2 {{ font-size: clamp(2.5rem, 5vw, 4rem); font-weight: 800; color: {text}; margin-bottom: 12px; }}
    .exp-header p {{ color: {secondary}; font-size: 1.2rem; }}
    .exp-list {{ display: flex; flex-direction: column; gap: 24px; }}
    .exp-item {{ display: flex; gap: 40px; padding: 32px; background: {text}05; border-radius: 20px; transition: all 0.3s ease; }}
    .exp-item:hover {{ background: {primary}08; transform: translateX(8px); }}
    .exp-period {{ color: {primary}; font-weight: 600; min-width: 150px; font-size: 0.95rem; }}
    .exp-info h4 {{ font-size: 1.3rem; font-weight: 700; color: {text}; margin-bottom: 6px; }}
    .company {{ color: {secondary}; }}
    @media (max-width: 600px) {{ .exp-item {{ flex-direction: column; gap: 12px; }} }}
    </style>
    '''
