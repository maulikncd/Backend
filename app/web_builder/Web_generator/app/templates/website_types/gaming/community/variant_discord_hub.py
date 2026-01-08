from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Community Hub - Discord/social integration"""
    title = props.get("title", "Join Our Community")
    primary = colors.get("primary", "#5865F2")
    
    return f'''
    <section class="gaming-community" id="community"><div class="container"><div class="community-grid"><div class="community-main"><h2>{title}</h2><p>Connect with millions of players worldwide. Join discussions, find teammates, and stay updated.</p><div class="community-stats"><div class="stat"><span class="num">2M+</span><span class="label">Members</span></div><div class="stat"><span class="num">50K</span><span class="label">Online Now</span></div><div class="stat"><span class="num">100K+</span><span class="label">Daily Messages</span></div></div><div class="platform-links"><a href="#" class="discord-btn"><svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M20.317 4.37a19.791 19.791 0 0 0-4.885-1.515.074.074 0 0 0-.079.037c-.21.375-.444.864-.608 1.25a18.27 18.27 0 0 0-5.487 0 12.64 12.64 0 0 0-.617-1.25.077.077 0 0 0-.079-.037A19.736 19.736 0 0 0 3.677 4.37a.07.07 0 0 0-.032.027C.533 9.046-.32 13.58.099 18.057a.082.082 0 0 0 .031.057 19.9 19.9 0 0 0 5.993 3.03.078.078 0 0 0 .084-.028c.462-.63.874-1.295 1.226-1.994.021-.041.001-.09-.041-.106a13.107 13.107 0 0 1-1.872-.892.077.077 0 0 1-.008-.128 10.2 10.2 0 0 0 .372-.292.074.074 0 0 1 .077-.01c3.928 1.793 8.18 1.793 12.062 0a.074.074 0 0 1 .078.01c.12.098.246.198.373.292a.077.077 0 0 1-.006.127 12.299 12.299 0 0 1-1.873.892.077.077 0 0 0-.041.107c.36.698.772 1.362 1.225 1.993a.076.076 0 0 0 .084.028 19.839 19.839 0 0 0 6.002-3.03.077.077 0 0 0 .032-.054c.5-5.177-.838-9.674-3.549-13.66a.061.061 0 0 0-.031-.03z"/></svg> Join Discord</a><a href="#" class="twitter-btn">🐦 Twitter</a><a href="#" class="reddit-btn">📢 Reddit</a></div></div><div class="community-preview"><div class="discord-widget"><div class="widget-header"><span class="online-dot"></span> 52,847 Online</div><div class="channels"><div class="channel"># general-chat</div><div class="channel"># looking-for-group</div><div class="channel"># bug-reports</div><div class="channel">🔊 Voice Channel 1</div></div></div></div></div></div></section>
    <style>
    .gaming-community {{ padding: 120px 40px; background: linear-gradient(135deg, #0D0D15, #1a1a2e); }}
    .container {{ max-width: 1200px; margin: 0 auto; }}
    .community-grid {{ display: grid; grid-template-columns: 1.5fr 1fr; gap: 60px; align-items: center; }}
    .community-main {{ color: #fff; }}
    .community-main h2 {{ font-size: 3rem; font-weight: 800; margin-bottom: 20px; }}
    .community-main p {{ color: rgba(255,255,255,0.7); font-size: 1.2rem; margin-bottom: 40px; max-width: 500px; }}
    .community-stats {{ display: flex; gap: 50px; margin-bottom: 40px; }}
    .stat .num {{ display: block; font-size: 2.5rem; font-weight: 800; color: {primary}; }}
    .stat .label {{ color: #888; font-size: 0.9rem; }}
    .platform-links {{ display: flex; gap: 15px; flex-wrap: wrap; }}
    .discord-btn {{ display: flex; align-items: center; gap: 10px; padding: 15px 30px; background: #5865F2; color: #fff; text-decoration: none; font-weight: 600; transition: 0.3s; }}
    .discord-btn:hover {{ transform: translateY(-3px); }}
    .twitter-btn, .reddit-btn {{ padding: 15px 25px; border: 1px solid #555; color: #fff; text-decoration: none; font-weight: 600; transition: 0.3s; }}
    .twitter-btn:hover, .reddit-btn:hover {{ border-color: {primary}; }}
    .discord-widget {{ background: #2C2F33; border-radius: 12px; overflow: hidden; }}
    .widget-header {{ background: #23272A; padding: 15px 20px; display: flex; align-items: center; gap: 10px; color: #fff; }}
    .online-dot {{ width: 10px; height: 10px; background: #43B581; border-radius: 50%; }}
    .channels {{ padding: 20px; }}
    .channel {{ padding: 10px 15px; color: #B9BBBE; font-size: 0.95rem; border-radius: 6px; margin-bottom: 5px; }}
    .channel:hover {{ background: #36393F; cursor: pointer; }}
    @media (max-width: 900px) {{ .community-grid {{ grid-template-columns: 1fr; }} }}
    </style>
    '''
