from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Mega Footer Gaming"""
    logo = props.get("logoText", "GAMEDEV")
    primary = colors.get("primary", "#8B5CF6")
    
    return f'''
    <footer class="gaming-footer-mega"><div class="container"><div class="footer-top"><div class="brand"><h3>{logo}</h3><p>Creating unforgettable gaming experiences since 2020.</p><div class="socials"><a href="#">🎮</a><a href="#">💬</a><a href="#">📺</a><a href="#">🐦</a></div></div><div class="links-grid"><div class="link-col"><h4>Games</h4><a href="#">All Games</a><a href="#">New Releases</a><a href="#">Free to Play</a></div><div class="link-col"><h4>Community</h4><a href="#">Discord</a><a href="#">Forums</a><a href="#">Events</a></div><div class="link-col"><h4>Support</h4><a href="#">Help Center</a><a href="#">Contact</a><a href="#">Report Bug</a></div></div></div><div class="footer-bottom"><span>© 2025 {logo}. All rights reserved.</span><div class="legal"><a href="#">Privacy</a><a href="#">Terms</a><a href="#">Cookies</a></div></div></div></footer>
    <style>
    .gaming-footer-mega {{ background: #0a0a0f; padding: 80px 40px 30px; color: #fff; }}
    .container {{ max-width: 1200px; margin: 0 auto; }}
    .footer-top {{ display: grid; grid-template-columns: 1fr 2fr; gap: 80px; margin-bottom: 60px; }}
    .brand h3 {{ font-size: 2rem; margin-bottom: 15px; }}
    .brand p {{ color: #888; margin-bottom: 25px; }}
    .socials {{ display: flex; gap: 10px; }}
    .socials a {{ width: 45px; height: 45px; background: #1a1a2e; border-radius: 10px; display: flex; align-items: center; justify-content: center; text-decoration: none; font-size: 1.2rem; transition: 0.3s; }}
    .socials a:hover {{ background: {primary}; }}
    .links-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 40px; }}
    .link-col h4 {{ font-size: 1rem; margin-bottom: 20px; color: {primary}; }}
    .link-col a {{ display: block; color: #888; text-decoration: none; padding: 8px 0; transition: 0.3s; }}
    .link-col a:hover {{ color: #fff; }}
    .footer-bottom {{ display: flex; justify-content: space-between; padding-top: 30px; border-top: 1px solid #222; color: #666; font-size: 0.9rem; }}
    .legal a {{ color: #666; text-decoration: none; margin-left: 20px; }}
    .legal a:hover {{ color: #fff; }}
    @media (max-width: 900px) {{ .footer-top {{ grid-template-columns: 1fr; }} .links-grid {{ grid-template-columns: 1fr; }} }}
    </style>
    '''
