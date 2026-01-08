from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Creators Hub - Content creators showcase"""
    title = props.get("title", "Top Creators")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    creators = [
        {"name": "ShadowKing", "platform": "Twitch", "followers": "2.5M", "icon": "📺"},
        {"name": "NeonSlayer", "platform": "YouTube", "followers": "1.8M", "icon": "🎬"},
        {"name": "CyberWolf", "platform": "TikTok", "followers": "5.2M", "icon": "📱"},
        {"name": "StormRider", "platform": "Twitter", "followers": "890K", "icon": "🐦"},
    ]
    
    creators_html = ""
    for c in creators:
        creators_html += f'''
        <div class="creator-card">
            <div class="creator-avatar">{c['name'][0]}</div>
            <h3>{c['name']}</h3>
            <div class="creator-platform">
                <span class="platform-icon">{c['icon']}</span>
                <span>{c['platform']}</span>
            </div>
            <span class="followers">{c['followers']} Followers</span>
            <button class="follow-btn">Follow</button>
        </div>
        '''
    
    return f'''
    <section class="gaming-community-creators" id="community">
        <div class="creators-container">
            <div class="creators-header">
                <span class="tag">⭐ Creators</span>
                <h2>{title}</h2>
            </div>
            <div class="creators-grid">{creators_html}</div>
        </div>
    </section>
    
    <style>
    .gaming-community-creators {{ padding: 120px 24px; background: {background}; }}
    .creators-container {{ max-width: 1000px; margin: 0 auto; }}
    .creators-header {{ text-align: center; margin-bottom: 60px; }}
    .tag {{ display: inline-block; padding: 10px 24px; background: {primary}15; color: {primary}; font-weight: 700; border-radius: 100px; margin-bottom: 20px; }}
    .creators-header h2 {{ font-family: 'Rajdhani', sans-serif; font-size: 2.5rem; font-weight: 800; color: {text}; }}
    .creators-grid {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px; }}
    .creator-card {{ background: {text}05; border-radius: 24px; padding: 32px; text-align: center; transition: all 0.4s ease; }}
    .creator-card:hover {{ transform: translateY(-8px); box-shadow: 0 30px 60px {primary}15; }}
    .creator-avatar {{ width: 80px; height: 80px; background: linear-gradient(135deg, {primary}, {secondary}); color: {background}; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 2rem; font-weight: 900; margin: 0 auto 16px; }}
    .creator-card h3 {{ font-size: 1.2rem; font-weight: 700; color: {text}; margin-bottom: 8px; }}
    .creator-platform {{ display: flex; justify-content: center; align-items: center; gap: 6px; color: {secondary}; margin-bottom: 8px; }}
    .platform-icon {{ font-size: 1.2rem; }}
    .followers {{ display: block; color: {primary}; font-weight: 700; margin-bottom: 20px; }}
    .follow-btn {{ width: 100%; padding: 12px; background: {primary}; color: {background}; border: none; font-weight: 700; border-radius: 10px; cursor: pointer; transition: all 0.3s ease; }}
    .follow-btn:hover {{ transform: scale(1.02); }}
    @media (max-width: 900px) {{ .creators-grid {{ grid-template-columns: repeat(2, 1fr); }} }}
    </style>
    '''
