from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Split Top Bar Navbar"""
    logo = props.get("logoText", "STUDIO")
    primary = colors.get("primary", "#FF4444")
    
    return f'''
    <header class="gaming-nav-topbar"><div class="top-bar"><span>🔴 New Update Available!</span><span>Download Now →</span></div><div class="main-nav"><a href="#" class="logo">{logo}</a><nav><a href="#games">Games</a><a href="#store">Store</a><a href="#community">Community</a><a href="#support">Support</a></nav><div class="nav-right"><a href="#" class="login">Login</a><a href="#" class="signup">Sign Up Free</a></div></div></header>
    <style>
    .gaming-nav-topbar {{ position: fixed; top: 0; left: 0; right: 0; z-index: 1000; }}
    .top-bar {{ background: {primary}; padding: 10px 40px; display: flex; justify-content: center; gap: 20px; color: #fff; font-size: 0.85rem; font-weight: 600; }}
    .main-nav {{ background: #0D0D15; padding: 18px 40px; display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid #222; }}
    .logo {{ font-size: 1.6rem; font-weight: 900; color: #fff; text-decoration: none; }}
    nav {{ display: flex; gap: 30px; }}
    nav a {{ color: rgba(255,255,255,0.7); text-decoration: none; font-weight: 500; transition: 0.3s; }}
    nav a:hover {{ color: #fff; }}
    .nav-right {{ display: flex; gap: 15px; }}
    .login {{ color: #fff; text-decoration: none; padding: 10px 20px; }}
    .signup {{ background: {primary}; color: #fff; text-decoration: none; padding: 10px 25px; font-weight: 600; }}
    @media (max-width: 768px) {{ nav, .nav-right {{ display: none; }} }}
    </style>
    '''
