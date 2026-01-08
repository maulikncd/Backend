from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Forums Hub - Discussion forum style"""
    title = props.get("title", "Community Forums")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    topics = [
        {"title": "Season 5 Discussion", "replies": "1.2K", "views": "45K", "hot": True},
        {"title": "Best Loadout Guide", "replies": "856", "views": "23K", "hot": True},
        {"title": "Bug Reports & Fixes", "replies": "432", "views": "12K", "hot": False},
        {"title": "Looking for Team", "replies": "621", "views": "18K", "hot": False},
    ]
    
    topics_html = ""
    for t in topics:
        hot = '<span class="hot-badge">🔥 Hot</span>' if t["hot"] else ""
        topics_html += f'''
        <div class="topic-row">
            <div class="topic-info">
                {hot}
                <h4>{t['title']}</h4>
            </div>
            <div class="topic-stats">
                <div class="stat"><span>{t['replies']}</span><label>Replies</label></div>
                <div class="stat"><span>{t['views']}</span><label>Views</label></div>
            </div>
        </div>
        '''
    
    return f'''
    <section class="gaming-community-forums" id="community">
        <div class="forums-container">
            <div class="forums-header">
                <h2>{title}</h2>
                <a href="#" class="new-topic">+ New Topic</a>
            </div>
            <div class="topics-list">{topics_html}</div>
        </div>
    </section>
    
    <style>
    .gaming-community-forums {{ padding: 120px 24px; background: {background}; }}
    .forums-container {{ max-width: 900px; margin: 0 auto; }}
    .forums-header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 40px; }}
    .forums-header h2 {{ font-family: 'Rajdhani', sans-serif; font-size: 2.5rem; font-weight: 800; color: {text}; }}
    .new-topic {{ padding: 12px 28px; background: {primary}; color: {background}; text-decoration: none; font-weight: 700; border-radius: 10px; transition: all 0.3s ease; }}
    .new-topic:hover {{ transform: scale(1.05); }}
    .topics-list {{ display: flex; flex-direction: column; gap: 16px; }}
    .topic-row {{ display: flex; justify-content: space-between; align-items: center; padding: 24px; background: {text}05; border-radius: 16px; transition: all 0.3s ease; }}
    .topic-row:hover {{ background: {primary}10; transform: translateX(8px); }}
    .topic-info {{ display: flex; align-items: center; gap: 16px; }}
    .hot-badge {{ padding: 4px 12px; background: #ff3b3b; color: white; font-size: 0.7rem; font-weight: 700; border-radius: 100px; }}
    .topic-info h4 {{ font-size: 1.1rem; font-weight: 700; color: {text}; }}
    .topic-stats {{ display: flex; gap: 32px; }}
    .stat {{ text-align: center; }}
    .stat span {{ display: block; font-weight: 700; color: {primary}; }}
    .stat label {{ font-size: 0.75rem; color: {secondary}; }}
    </style>
    '''
