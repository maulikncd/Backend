from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Floating Glass Navbar"""
    logo = props.get("logoText", "GAMEDEV")
    primary = colors.get("primary", "#8B5CF6")
    
    return f'''
    <header class="gaming-nav-glass"><div class="nav-container"><a href="#" class="logo">{logo}</a><nav><a href="#games">Games</a><a href="#about">About</a><a href="#news">News</a><a href="#community">Community</a></nav><a href="#" class="cta-btn">Play Free</a></div></header>
    <style>
    .gaming-nav-glass {{ position: fixed; top: 20px; left: 50%; transform: translateX(-50%); width: 90%; max-width: 1200px; z-index: 1000; }}
    .nav-container {{ background: rgba(13,13,21,0.8); backdrop-filter: blur(20px); border: 1px solid rgba(255,255,255,0.1); border-radius: 60px; padding: 15px 30px; display: flex; align-items: center; justify-content: space-between; }}
    .logo {{ font-size: 1.5rem; font-weight: 900; color: #fff; text-decoration: none; }}
    nav {{ display: flex; gap: 30px; }}
    nav a {{ color: rgba(255,255,255,0.7); text-decoration: none; font-weight: 500; transition: 0.3s; }}
    nav a:hover {{ color: {primary}; }}
    .cta-btn {{ padding: 12px 30px; background: {primary}; color: #fff; text-decoration: none; font-weight: 700; border-radius: 50px; transition: 0.3s; }}
    .cta-btn:hover {{ transform: scale(1.05); }}
    @media (max-width: 768px) {{ nav {{ display: none; }} }}
    </style>
    '''
