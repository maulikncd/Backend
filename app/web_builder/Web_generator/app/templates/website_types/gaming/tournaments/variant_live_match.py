from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Live Match - Current match display"""
    title = props.get("title", "Live Now")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="gaming-tournament-live" id="tournaments">
        <div class="live-container">
            <div class="live-header">
                <span class="live-badge">🔴 LIVE</span>
                <h2>{title}</h2>
            </div>
            <div class="match-display">
                <div class="team team-a">
                    <div class="team-logo">A</div>
                    <h3>Team Alpha</h3>
                    <span class="team-score">2</span>
                </div>
                <div class="match-center">
                    <span class="vs">VS</span>
                    <span class="match-time">Game 3 • Round 5</span>
                    <a href="#" class="watch-btn">Watch Live</a>
                </div>
                <div class="team team-b">
                    <div class="team-logo">B</div>
                    <h3>Pro Squad</h3>
                    <span class="team-score">1</span>
                </div>
            </div>
            <div class="match-stats">
                <div class="stat"><span>245K</span><label>Viewers</label></div>
                <div class="stat"><span>$500K</span><label>Prize</label></div>
                <div class="stat"><span>Finals</span><label>Stage</label></div>
            </div>
        </div>
    </section>
    
    <style>
    .gaming-tournament-live {{ padding: 120px 24px; background: linear-gradient(135deg, {primary}10, {background}); }}
    .live-container {{ max-width: 1000px; margin: 0 auto; text-align: center; }}
    .live-header {{ margin-bottom: 60px; }}
    .live-badge {{ display: inline-block; padding: 10px 24px; background: #ff3b3b; color: white; font-weight: 700; font-size: 0.85rem; border-radius: 100px; margin-bottom: 20px; animation: pulse 2s infinite; }}
    @keyframes pulse {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: 0.7; }} }}
    .live-header h2 {{ font-family: 'Rajdhani', sans-serif; font-size: 3rem; font-weight: 800; color: {text}; }}
    .match-display {{ display: flex; justify-content: center; align-items: center; gap: 60px; margin-bottom: 60px; }}
    .team {{ text-align: center; }}
    .team-logo {{ width: 100px; height: 100px; background: {text}10; border-radius: 20px; display: flex; align-items: center; justify-content: center; font-size: 2.5rem; font-weight: 900; color: {primary}; margin: 0 auto 16px; }}
    .team h3 {{ font-size: 1.5rem; font-weight: 700; color: {text}; margin-bottom: 8px; }}
    .team-score {{ font-family: 'Orbitron', sans-serif; font-size: 4rem; font-weight: 900; color: {primary}; text-shadow: 0 0 30px {primary}50; }}
    .match-center {{ text-align: center; }}
    .vs {{ display: block; font-size: 2rem; font-weight: 900; color: {secondary}; margin-bottom: 8px; }}
    .match-time {{ display: block; color: {secondary}; margin-bottom: 24px; }}
    .watch-btn {{ display: inline-block; padding: 14px 36px; background: {primary}; color: {background}; text-decoration: none; font-weight: 700; border-radius: 10px; transition: all 0.3s ease; }}
    .watch-btn:hover {{ transform: scale(1.05); box-shadow: 0 15px 40px {primary}40; }}
    .match-stats {{ display: flex; justify-content: center; gap: 60px; }}
    .match-stats .stat span {{ display: block; font-size: 2rem; font-weight: 900; color: {text}; }}
    .match-stats .stat label {{ color: {secondary}; }}
    @media (max-width: 768px) {{ .match-display {{ flex-direction: column; gap: 40px; }} }}
    </style>
    '''
