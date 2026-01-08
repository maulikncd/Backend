from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Leaderboard - Top players ranking"""
    title = props.get("title", "Leaderboard")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    players = [
        {"rank": 1, "name": "ShadowKing", "team": "Team Alpha", "points": "15,420", "wins": "98"},
        {"rank": 2, "name": "NeonSlayer", "team": "Pro Squad", "points": "14,890", "wins": "92"},
        {"rank": 3, "name": "CyberWolf", "team": "Elite Gaming", "points": "14,250", "wins": "89"},
        {"rank": 4, "name": "StormRider", "team": "Thunder FC", "points": "13,800", "wins": "85"},
        {"rank": 5, "name": "DarkPhoenix", "team": "Phoenix Rising", "points": "13,420", "wins": "82"},
    ]
    
    rows_html = ""
    for p in players:
        medal = "🥇" if p["rank"] == 1 else "🥈" if p["rank"] == 2 else "🥉" if p["rank"] == 3 else f"#{p['rank']}"
        rows_html += f'''
        <div class="leader-row">
            <div class="rank">{medal}</div>
            <div class="player-info"><h4>{p['name']}</h4><span>{p['team']}</span></div>
            <div class="stat"><span>{p['points']}</span><label>Points</label></div>
            <div class="stat"><span>{p['wins']}</span><label>Wins</label></div>
        </div>
        '''
    
    return f'''
    <section class="gaming-tournament-leaderboard" id="tournaments">
        <div class="leader-container">
            <div class="leader-header"><h2>{title}</h2></div>
            <div class="leaderboard">{rows_html}</div>
        </div>
    </section>
    
    <style>
    .gaming-tournament-leaderboard {{ padding: 120px 24px; background: {background}; }}
    .leader-container {{ max-width: 900px; margin: 0 auto; }}
    .leader-header {{ text-align: center; margin-bottom: 60px; }}
    .leader-header h2 {{ font-family: 'Rajdhani', sans-serif; font-size: 3rem; font-weight: 800; color: {text}; }}
    .leaderboard {{ display: flex; flex-direction: column; gap: 16px; }}
    .leader-row {{ display: flex; align-items: center; gap: 24px; padding: 20px 24px; background: {text}05; border-radius: 16px; transition: all 0.3s ease; }}
    .leader-row:hover {{ background: {primary}10; transform: translateX(8px); }}
    .rank {{ font-size: 1.5rem; font-weight: 900; color: {primary}; min-width: 50px; text-align: center; }}
    .player-info {{ flex: 1; }}
    .player-info h4 {{ font-size: 1.2rem; font-weight: 700; color: {text}; margin-bottom: 4px; }}
    .player-info span {{ font-size: 0.9rem; color: {secondary}; }}
    .stat {{ text-align: center; min-width: 80px; }}
    .stat span {{ display: block; font-weight: 900; color: {primary}; font-size: 1.2rem; }}
    .stat label {{ font-size: 0.75rem; color: {secondary}; }}
    </style>
    '''
