from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Social Feed - Social media style posts"""
    title = props.get("title", "Community Feed")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    posts = [
        {"user": "ShadowKing", "content": "Just hit Diamond rank! Let's go! 🎮", "likes": "1.2K", "time": "2h ago", "img": "https://images.unsplash.com/photo-1542751371-adc38448a05e?w=400"},
        {"user": "NeonSlayer", "content": "New setup is finally complete! Ready to grind.", "likes": "856", "time": "5h ago", "img": "https://images.unsplash.com/photo-1593305841991-05c297ba4575?w=400"},
        {"user": "CyberWolf", "content": "Tournament prep starts now. Who's joining?", "likes": "432", "time": "1d ago", "img": ""},
    ]
    
    posts_html = ""
    for p in posts:
        img_html = f'<img src="{p["img"]}" alt="Post">' if p["img"] else ""
        posts_html += f'''
        <div class="feed-post">
            <div class="post-header">
                <div class="user-avatar">{p['user'][0]}</div>
                <div class="user-info"><h4>{p['user']}</h4><span>{p['time']}</span></div>
            </div>
            <p class="post-content">{p['content']}</p>
            {img_html}
            <div class="post-actions">
                <button>❤️ {p['likes']}</button>
                <button>💬 Comment</button>
                <button>🔄 Share</button>
            </div>
        </div>
        '''
    
    return f'''
    <section class="gaming-community-feed" id="community">
        <div class="feed-container">
            <div class="feed-header"><h2>{title}</h2></div>
            <div class="posts-list">{posts_html}</div>
        </div>
    </section>
    
    <style>
    .gaming-community-feed {{ padding: 120px 24px; background: {background}; }}
    .feed-container {{ max-width: 600px; margin: 0 auto; }}
    .feed-header {{ text-align: center; margin-bottom: 48px; }}
    .feed-header h2 {{ font-family: 'Rajdhani', sans-serif; font-size: 2.5rem; font-weight: 800; color: {text}; }}
    .posts-list {{ display: flex; flex-direction: column; gap: 24px; }}
    .feed-post {{ background: {text}05; border-radius: 20px; padding: 24px; }}
    .post-header {{ display: flex; gap: 12px; margin-bottom: 16px; }}
    .user-avatar {{ width: 48px; height: 48px; background: {primary}; color: {background}; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 1.2rem; }}
    .user-info h4 {{ font-weight: 700; color: {text}; }}
    .user-info span {{ font-size: 0.85rem; color: {secondary}; }}
    .post-content {{ color: {text}; line-height: 1.6; margin-bottom: 16px; }}
    .feed-post img {{ width: 100%; border-radius: 12px; margin-bottom: 16px; }}
    .post-actions {{ display: flex; gap: 16px; }}
    .post-actions button {{ background: {text}08; border: none; padding: 10px 20px; border-radius: 100px; color: {text}; cursor: pointer; transition: all 0.3s ease; }}
    .post-actions button:hover {{ background: {primary}20; }}
    </style>
    '''
