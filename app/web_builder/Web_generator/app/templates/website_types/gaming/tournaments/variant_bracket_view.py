from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Esports Bracket - Tournament bracket view"""
    title = props.get("title", "Current Tournament")
    primary = colors.get("primary", "#FFD700")
    
    return f'''
    <section class="gaming-tournaments" id="tournaments"><div class="container"><div class="section-header"><span class="live-badge">🔴 LIVE</span><h2>{title}</h2></div><div class="tournament-grid"><div class="bracket-preview"><div class="match"><div class="team">Team Alpha <span class="score">2</span></div><div class="team winner">Team Beta <span class="score">3</span></div></div><div class="match"><div class="team winner">Team Gamma <span class="score">3</span></div><div class="team">Team Delta <span class="score">1</span></div></div></div><div class="tournament-info"><div class="prize-section"><span class="prize-label">Prize Pool</span><span class="prize-amount">$500,000</span></div><div class="info-stats"><div class="stat"><span class="num">32</span><span class="label">Teams</span></div><div class="stat"><span class="num">128</span><span class="label">Players</span></div></div><a href="#" class="watch-btn">Watch Live</a></div></div></div></section>
    <style>
    .gaming-tournaments {{ padding: 100px 40px; background: #0D0D15; }}
    .container {{ max-width: 1200px; margin: 0 auto; }}
    .section-header {{ display: flex; align-items: center; gap: 20px; margin-bottom: 50px; }}
    .live-badge {{ padding: 8px 20px; background: #FF0000; color: #fff; font-weight: 700; font-size: 0.8rem; animation: pulse 2s infinite; }}
    @keyframes pulse {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: 0.5; }} }}
    .section-header h2 {{ font-size: 2.5rem; color: #fff; font-weight: 800; }}
    .tournament-grid {{ display: grid; grid-template-columns: 2fr 1fr; gap: 40px; }}
    .bracket-preview {{ background: #1a1a2e; border-radius: 16px; padding: 30px; }}
    .match {{ margin-bottom: 20px; }}
    .team {{ display: flex; justify-content: space-between; padding: 15px 20px; background: #252540; border-radius: 8px; color: #fff; margin-bottom: 5px; }}
    .team.winner {{ background: {primary}20; border-left: 4px solid {primary}; }}
    .score {{ font-weight: 800; color: {primary}; }}
    .tournament-info {{ background: linear-gradient(135deg, {primary}, #FFA500); border-radius: 16px; padding: 40px; text-align: center; }}
    .prize-label {{ display: block; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 3px; margin-bottom: 10px; }}
    .prize-amount {{ font-size: 3rem; font-weight: 900; display: block; margin-bottom: 30px; }}
    .info-stats {{ display: flex; justify-content: center; gap: 40px; margin-bottom: 30px; }}
    .info-stats .num {{ display: block; font-size: 2rem; font-weight: 800; }}
    .info-stats .label {{ font-size: 0.85rem; }}
    .watch-btn {{ display: inline-block; padding: 15px 40px; background: #000; color: #fff; text-decoration: none; font-weight: 700; }}
    @media (max-width: 900px) {{ .tournament-grid {{ grid-template-columns: 1fr; }} }}
    </style>
    '''
