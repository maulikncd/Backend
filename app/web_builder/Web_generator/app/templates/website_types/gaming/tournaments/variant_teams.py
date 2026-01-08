from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Teams Grid - Participating teams display"""
    title = props.get("title", "Participating Teams")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    teams = [
        {"name": "Team Alpha", "region": "NA", "seed": "#1"},
        {"name": "Pro Squad", "region": "EU", "seed": "#2"},
        {"name": "Elite Gaming", "region": "ASIA", "seed": "#3"},
        {"name": "Thunder FC", "region": "NA", "seed": "#4"},
        {"name": "Phoenix Rising", "region": "EU", "seed": "#5"},
        {"name": "Storm Raiders", "region": "ASIA", "seed": "#6"},
        {"name": "Dark Legion", "region": "NA", "seed": "#7"},
        {"name": "Cyber Wolves", "region": "EU", "seed": "#8"},
    ]
    
    teams_html = ""
    for t in teams:
        teams_html += f'''
        <div class="team-card">
            <div class="team-logo">{t['name'][0]}</div>
            <h3>{t['name']}</h3>
            <div class="team-meta">
                <span class="region">{t['region']}</span>
                <span class="seed">{t['seed']}</span>
            </div>
        </div>
        '''
    
    return f'''
    <section class="gaming-tournament-teams" id="tournaments">
        <div class="teams-container">
            <div class="teams-header"><h2>{title}</h2></div>
            <div class="teams-grid">{teams_html}</div>
        </div>
    </section>
    
    <style>
    .gaming-tournament-teams {{ padding: 120px 24px; background: {background}; }}
    .teams-container {{ max-width: 1200px; margin: 0 auto; }}
    .teams-header {{ text-align: center; margin-bottom: 60px; }}
    .teams-header h2 {{ font-family: 'Rajdhani', sans-serif; font-size: 3rem; font-weight: 800; color: {text}; }}
    .teams-grid {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px; }}
    .team-card {{ background: {text}05; border-radius: 20px; padding: 32px; text-align: center; transition: all 0.4s ease; }}
    .team-card:hover {{ transform: translateY(-8px); background: {primary}10; }}
    .team-logo {{ width: 80px; height: 80px; background: {primary}20; border-radius: 16px; display: flex; align-items: center; justify-content: center; font-size: 2rem; font-weight: 900; color: {primary}; margin: 0 auto 16px; }}
    .team-card h3 {{ font-size: 1.2rem; font-weight: 700; color: {text}; margin-bottom: 12px; }}
    .team-meta {{ display: flex; justify-content: center; gap: 12px; }}
    .region {{ padding: 4px 12px; background: {primary}; color: {background}; font-size: 0.75rem; font-weight: 700; border-radius: 100px; }}
    .seed {{ padding: 4px 12px; background: {text}10; color: {secondary}; font-size: 0.75rem; font-weight: 700; border-radius: 100px; }}
    @media (max-width: 900px) {{ .teams-grid {{ grid-template-columns: repeat(2, 1fr); }} }}
    </style>
    '''
