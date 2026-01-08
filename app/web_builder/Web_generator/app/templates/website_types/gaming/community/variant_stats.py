from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Stats Overview - Community statistics"""
    title = props.get("title", "Our Community")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    stats = [
        {"label": "Active Players", "value": "50M+", "icon": "🎮"},
        {"label": "Daily Matches", "value": "10K+", "icon": "⚔️"},
        {"label": "Discord Members", "value": "2.5M", "icon": "💬"},
        {"label": "Countries", "value": "150+", "icon": "🌍"},
    ]
    
    stats_html = ""
    for s in stats:
        stats_html += f'''
        <div class="stat-card">
            <span class="stat-icon">{s['icon']}</span>
            <span class="stat-value">{s['value']}</span>
            <span class="stat-label">{s['label']}</span>
        </div>
        '''
    
    return f'''
    <section class="gaming-community-stats" id="community">
        <div class="stats-container">
            <div class="stats-header">
                <span class="tag">🌟 Community</span>
                <h2>{title}</h2>
                <p>Join millions of players worldwide</p>
            </div>
            <div class="stats-grid">{stats_html}</div>
            <div class="cta-section">
                <a href="#" class="join-btn">Join the Community</a>
            </div>
        </div>
    </section>
    
    <style>
    .gaming-community-stats {{ padding: 120px 24px; background: linear-gradient(135deg, {primary}10, {background}); }}
    .stats-container {{ max-width: 1000px; margin: 0 auto; text-align: center; }}
    .stats-header {{ margin-bottom: 60px; }}
    .tag {{ display: inline-block; padding: 10px 24px; background: {primary}15; color: {primary}; font-weight: 700; border-radius: 100px; margin-bottom: 20px; }}
    .stats-header h2 {{ font-family: 'Rajdhani', sans-serif; font-size: 3rem; font-weight: 800; color: {text}; margin-bottom: 12px; }}
    .stats-header p {{ color: {secondary}; font-size: 1.2rem; }}
    .stats-grid {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px; margin-bottom: 60px; }}
    .stat-card {{ background: {background}; border-radius: 24px; padding: 40px 24px; transition: all 0.4s ease; }}
    .stat-card:hover {{ transform: translateY(-8px); box-shadow: 0 30px 60px {primary}15; }}
    .stat-icon {{ display: block; font-size: 3rem; margin-bottom: 16px; }}
    .stat-value {{ display: block; font-family: 'Orbitron', sans-serif; font-size: 2.5rem; font-weight: 900; color: {primary}; text-shadow: 0 0 30px {primary}40; margin-bottom: 8px; }}
    .stat-label {{ display: block; color: {secondary}; }}
    .join-btn {{ display: inline-block; padding: 18px 48px; background: {primary}; color: {background}; text-decoration: none; font-weight: 700; font-size: 1.1rem; border-radius: 12px; transition: all 0.3s ease; }}
    .join-btn:hover {{ transform: scale(1.05); box-shadow: 0 20px 50px {primary}40; }}
    @media (max-width: 900px) {{ .stats-grid {{ grid-template-columns: repeat(2, 1fr); }} }}
    </style>
    '''
