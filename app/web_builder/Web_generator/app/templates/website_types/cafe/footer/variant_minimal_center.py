from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Minimal Centered Footer"""
    logo = props.get("logo", "Cafe")
    tagline = props.get("tagline", "Crafted with love")
    primary = colors.get("primary", "#8B7355")
    
    return f'''
    <footer class="footer-minimal-center"><div class="footer-content"><h3>{logo}</h3><p>{tagline}</p><div class="social-row"><a href="#">FB</a><a href="#">IG</a><a href="#">TW</a></div><span class="copyright">© 2025 {logo}</span></div></footer>
    <style>
    .footer-minimal-center {{ padding: 80px 24px; background: #FAF7F4; text-align: center; }}
    .footer-content h3 {{ font-family: 'Playfair Display', serif; font-size: 2rem; margin-bottom: 10px; }}
    .footer-content p {{ color: #888; margin-bottom: 30px; }}
    .social-row {{ display: flex; justify-content: center; gap: 20px; margin-bottom: 30px; }}
    .social-row a {{ width: 45px; height: 45px; border: 1px solid {primary}; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: {primary}; text-decoration: none; transition: 0.3s; }}
    .social-row a:hover {{ background: {primary}; color: #fff; }}
    .copyright {{ color: #aaa; font-size: 0.9rem; }}
    </style>
    '''
