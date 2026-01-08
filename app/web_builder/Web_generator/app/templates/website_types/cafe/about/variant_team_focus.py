from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Team Focus About - Showcase the people behind the cafe"""
    title = props.get("title", "Meet Our Team")
    story = props.get("story", "")[:200]
    
    primary = colors.get("primary", "#8B7355")
    text = colors.get("text", "#2D2013")
    bg = colors.get("background", "#FAF7F4")
    
    team = [
        {"name": "Alex Chen", "role": "Head Barista", "image": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=300"},
        {"name": "Maria Santos", "role": "Pastry Chef", "image": "https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=300"},
        {"name": "James Wilson", "role": "Founder", "image": "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=300"}
    ]
    
    team_html = ""
    for member in team:
        team_html += f'''
        <div class="team-card">
            <div class="member-img" style="background-image: url('{member["image"]}')"></div>
            <div class="member-info">
                <h4>{member["name"]}</h4>
                <span>{member["role"]}</span>
            </div>
        </div>
        '''
    
    return f'''
    <section class="about-team" id="about">
        <div class="team-container">
            <div class="team-intro">
                <span class="pre-title">Our Team</span>
                <h2>{title}</h2>
                <p>{story if story else "The passionate people who make your coffee experience special every single day."}</p>
            </div>
            <div class="team-grid">
                {team_html}
            </div>
        </div>
    </section>
    
    <style>
    .about-team {{ padding: 120px 40px; background: {bg}; }}
    .team-container {{ max-width: 1200px; margin: 0 auto; }}
    .team-intro {{ text-align: center; margin-bottom: 80px; }}
    .pre-title {{ color: {primary}; text-transform: uppercase; letter-spacing: 4px; font-size: 0.85rem; font-weight: 600; }}
    .about-team h2 {{ font-family: 'Playfair Display', serif; font-size: 3.5rem; color: {text}; margin: 16px 0 20px; }}
    .about-team .team-intro p {{ font-size: 1.1rem; color: #666; max-width: 500px; margin: 0 auto; }}
    .team-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 40px; }}
    .team-card {{ text-align: center; transition: 0.3s; }}
    .team-card:hover {{ transform: translateY(-10px); }}
    .member-img {{ width: 200px; height: 200px; border-radius: 50%; background-size: cover; background-position: center; margin: 0 auto 24px; border: 5px solid {primary}20; transition: 0.3s; }}
    .team-card:hover .member-img {{ border-color: {primary}; }}
    .member-info h4 {{ font-family: 'Playfair Display', serif; font-size: 1.5rem; color: {text}; margin-bottom: 8px; }}
    .member-info span {{ color: {primary}; font-weight: 500; }}
    @media (max-width: 768px) {{ .team-grid {{ grid-template-columns: 1fr; }} }}
    </style>
    '''
