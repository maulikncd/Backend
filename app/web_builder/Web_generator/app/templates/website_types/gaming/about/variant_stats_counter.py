from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Stats Counter About"""
    title = props.get("title", "By The Numbers")
    primary = colors.get("primary", "#FF4444")
    
    return f'''
    <section class="gaming-about-stats" id="about"><div class="container"><h2>{title}</h2><div class="stats-grid"><div class="stat-box"><span class="num">50M+</span><span class="label">Downloads</span></div><div class="stat-box"><span class="num">4.8</span><span class="label">Rating</span></div><div class="stat-box"><span class="num">100+</span><span class="label">Awards</span></div><div class="stat-box"><span class="num">200</span><span class="label">Team Size</span></div></div></div></section>
    <style>
    .gaming-about-stats {{ padding: 100px 40px; background: #0D0D15; text-align: center; color: #fff; }}
    .container {{ max-width: 1100px; margin: 0 auto; }}
    .gaming-about-stats h2 {{ font-size: 3rem; margin-bottom: 60px; }}
    .stats-grid {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 30px; }}
    .stat-box {{ padding: 50px 30px; background: linear-gradient(135deg, #1a1a2e, #252540); border-radius: 16px; border: 1px solid {primary}30; }}
    .stat-box:hover {{ border-color: {primary}; }}
    .num {{ display: block; font-size: 4rem; font-weight: 900; color: {primary}; margin-bottom: 10px; }}
    .label {{ text-transform: uppercase; letter-spacing: 3px; color: #888; font-size: 0.9rem; }}
    @media (max-width: 768px) {{ .stats-grid {{ grid-template-columns: repeat(2, 1fr); }} }}
    </style>
    '''
