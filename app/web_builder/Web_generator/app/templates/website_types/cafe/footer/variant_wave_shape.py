from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Animated Wave Footer"""
    logo = props.get("logo", "Cafe")
    primary = colors.get("primary", "#8B7355")
    
    return f'''
    <footer class="footer-wave"><div class="wave-shape"><svg viewBox="0 0 1440 120" fill="none"><path d="M0,64L80,69.3C160,75,320,85,480,80C640,75,800,53,960,48C1120,43,1280,53,1360,58.7L1440,64L1440,120L1360,120C1280,120,1120,120,960,120C800,120,640,120,480,120C320,120,160,120,80,120L0,120Z" fill="{primary}"/></svg></div><div class="wave-content"><div class="wave-grid"><div class="wave-col brand"><h3>{logo}</h3><p>Crafted with passion</p></div><div class="wave-col"><a href="#">Menu</a><a href="#">About</a><a href="#">Contact</a></div><div class="wave-col"><a href="#">Instagram</a><a href="#">Facebook</a><a href="#">Twitter</a></div></div><span class="wave-copyright">© 2025 {logo}</span></div></footer>
    <style>
    .footer-wave {{ background: #fff; }}
    .wave-shape {{ margin-top: -1px; }}
    .wave-shape svg {{ display: block; width: 100%; }}
    .wave-content {{ background: {primary}; padding: 60px 40px 30px; color: #fff; }}
    .wave-grid {{ max-width: 1000px; margin: 0 auto 40px; display: grid; grid-template-columns: 2fr 1fr 1fr; gap: 50px; }}
    .brand h3 {{ font-family: 'Playfair Display', serif; font-size: 2rem; margin-bottom: 10px; }}
    .brand p {{ opacity: 0.8; }}
    .wave-col a {{ display: block; color: rgba(255,255,255,0.8); text-decoration: none; padding: 8px 0; transition: 0.3s; }}
    .wave-col a:hover {{ color: #fff; padding-left: 10px; }}
    .wave-copyright {{ display: block; text-align: center; opacity: 0.7; font-size: 0.9rem; }}
    @media (max-width: 768px) {{ .wave-grid {{ grid-template-columns: 1fr; text-align: center; }} }}
    </style>
    '''
