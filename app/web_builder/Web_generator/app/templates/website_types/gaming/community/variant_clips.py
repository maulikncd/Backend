from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Clips Hub - Community game clips"""
    title = props.get("title", "Top Clips")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    clips = [
        {"user": "ShadowKing", "title": "Insane 1v5 Clutch", "views": "245K", "img": "https://images.unsplash.com/photo-1542751371-adc38448a05e?w=600"},
        {"user": "NeonSlayer", "title": "World Record Speed Run", "views": "189K", "img": "https://images.unsplash.com/photo-1538481199705-c710c4e965fc?w=600"},
        {"user": "CyberWolf", "title": "Epic Snipe Shot", "views": "156K", "img": "https://images.unsplash.com/photo-1511512578047-dfb367046420?w=600"},
    ]
    
    clips_html = ""
    for c in clips:
        clips_html += f'''
        <div class="clip-card">
            <div class="clip-thumb">
                <img src="{c['img']}" alt="{c['title']}">
                <div class="play-btn">▶</div>
            </div>
            <div class="clip-info">
                <h4>{c['title']}</h4>
                <div class="clip-meta">
                    <span class="user">by {c['user']}</span>
                    <span class="views">👁️ {c['views']}</span>
                </div>
            </div>
        </div>
        '''
    
    return f'''
    <section class="gaming-community-clips" id="community">
        <div class="clips-container">
            <div class="clips-header"><h2>{title}</h2></div>
            <div class="clips-grid">{clips_html}</div>
        </div>
    </section>
    
    <style>
    .gaming-community-clips {{ padding: 120px 24px; background: {background}; }}
    .clips-container {{ max-width: 1000px; margin: 0 auto; }}
    .clips-header {{ text-align: center; margin-bottom: 48px; }}
    .clips-header h2 {{ font-family: 'Rajdhani', sans-serif; font-size: 2.5rem; font-weight: 800; color: {text}; }}
    .clips-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; }}
    .clip-card {{ background: {text}05; border-radius: 20px; overflow: hidden; transition: all 0.4s ease; }}
    .clip-card:hover {{ transform: translateY(-8px); }}
    .clip-thumb {{ position: relative; aspect-ratio: 16/9; }}
    .clip-thumb img {{ width: 100%; height: 100%; object-fit: cover; }}
    .play-btn {{ position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 60px; height: 60px; background: {primary}; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: {background}; font-size: 1.2rem; opacity: 0; transition: all 0.3s ease; cursor: pointer; }}
    .clip-card:hover .play-btn {{ opacity: 1; }}
    .clip-info {{ padding: 20px; }}
    .clip-info h4 {{ font-size: 1.1rem; font-weight: 700; color: {text}; margin-bottom: 8px; }}
    .clip-meta {{ display: flex; justify-content: space-between; color: {secondary}; font-size: 0.85rem; }}
    @media (max-width: 900px) {{ .clips-grid {{ grid-template-columns: 1fr; }} }}
    </style>
    '''
