from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Team Roster About - Game studio team showcase"""
    title = props.get("title", "Meet the Team")
    primary = colors.get("primary", "#8B5CF6")
    
    team = [
        {"name": "Alex Storm", "role": "Lead Developer", "img": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=300"},
        {"name": "Maya Chen", "role": "Art Director", "img": "https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=300"},
        {"name": "Jake Wilson", "role": "Game Designer", "img": "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=300"},
        {"name": "Sarah Lee", "role": "Sound Engineer", "img": "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=300"}
    ]
    
    team_html = ""
    for t in team:
        team_html += f'''<div class="team-member"><img src="{t["img"]}" alt="{t["name"]}"><div class="member-info"><h4>{t["name"]}</h4><span>{t["role"]}</span></div><div class="member-socials"><a href="#">🐦</a><a href="#">💼</a></div></div>'''
    
    return f'''
    <section class="gaming-about-team" id="about"><div class="container"><div class="section-header"><span class="tag">Our Studio</span><h2>{title}</h2></div><div class="team-grid">{team_html}</div></div></section>
    <style>
    .gaming-about-team {{ padding: 120px 40px; background: #0D0D15; }}
    .container {{ max-width: 1200px; margin: 0 auto; }}
    .section-header {{ text-align: center; margin-bottom: 60px; color: #fff; }}
    .tag {{ color: {primary}; text-transform: uppercase; letter-spacing: 4px; font-size: 0.9rem; }}
    .section-header h2 {{ font-size: 3rem; font-weight: 800; margin-top: 15px; }}
    .team-grid {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 30px; }}
    .team-member {{ background: #1a1a2e; border-radius: 16px; overflow: hidden; text-align: center; transition: 0.3s; }}
    .team-member:hover {{ transform: translateY(-10px); box-shadow: 0 20px 50px rgba(139,92,246,0.2); }}
    .team-member img {{ width: 100%; height: 250px; object-fit: cover; }}
    .member-info {{ padding: 25px; color: #fff; }}
    .member-info h4 {{ font-size: 1.3rem; margin-bottom: 5px; }}
    .member-info span {{ color: {primary}; font-size: 0.9rem; }}
    .member-socials {{ padding: 0 25px 25px; display: flex; justify-content: center; gap: 10px; }}
    .member-socials a {{ width: 40px; height: 40px; border: 1px solid #333; border-radius: 50%; display: flex; align-items: center; justify-content: center; text-decoration: none; transition: 0.3s; }}
    .member-socials a:hover {{ border-color: {primary}; background: {primary}20; }}
    @media (max-width: 900px) {{ .team-grid {{ grid-template-columns: repeat(2, 1fr); }} }}
    </style>
    '''
