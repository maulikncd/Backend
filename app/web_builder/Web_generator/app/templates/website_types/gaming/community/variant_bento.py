from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Bento Community - Modern bento grid"""
    title = props.get("title", "Community")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="gaming-community-bento" id="community">
        <div class="bento-container">
            <div class="bento-header"><h2>{title}</h2></div>
            <div class="bento-grid">
                <div class="bento-item main">
                    <div class="bento-content">
                        <span class="icon">💬</span>
                        <h3>Join Discord</h3>
                        <p>2.5M members online</p>
                        <a href="#" class="btn">Join Now</a>
                    </div>
                </div>
                <div class="bento-item">
                    <div class="stat-content"><span class="num">50M+</span><span class="label">Players</span></div>
                </div>
                <div class="bento-item">
                    <div class="stat-content"><span class="num">150+</span><span class="label">Countries</span></div>
                </div>
                <div class="bento-item wide">
                    <div class="bento-links">
                        <a href="#">📺 Twitch</a>
                        <a href="#">🎬 YouTube</a>
                        <a href="#">🐦 Twitter</a>
                        <a href="#">📸 Instagram</a>
                    </div>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    .gaming-community-bento {{ padding: 120px 24px; background: {background}; }}
    .bento-container {{ max-width: 1000px; margin: 0 auto; }}
    .bento-header {{ text-align: center; margin-bottom: 48px; }}
    .bento-header h2 {{ font-family: 'Rajdhani', sans-serif; font-size: 2.5rem; font-weight: 800; color: {text}; }}
    .bento-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); grid-template-rows: repeat(2, 200px); gap: 24px; }}
    .bento-item {{ background: {text}05; border-radius: 24px; display: flex; align-items: center; justify-content: center; }}
    .bento-item.main {{ grid-column: span 2; grid-row: span 2; background: linear-gradient(135deg, {primary}15, {primary}05); }}
    .bento-item.wide {{ grid-column: span 2; }}
    .bento-content {{ text-align: center; padding: 40px; }}
    .icon {{ font-size: 4rem; display: block; margin-bottom: 20px; }}
    .bento-content h3 {{ font-size: 2rem; font-weight: 800; color: {text}; margin-bottom: 8px; }}
    .bento-content p {{ color: {secondary}; margin-bottom: 24px; }}
    .btn {{ display: inline-block; padding: 14px 36px; background: {primary}; color: {background}; text-decoration: none; font-weight: 700; border-radius: 10px; transition: all 0.3s ease; }}
    .btn:hover {{ transform: scale(1.05); }}
    .stat-content {{ text-align: center; }}
    .stat-content .num {{ display: block; font-family: 'Orbitron', sans-serif; font-size: 2.5rem; font-weight: 900; color: {primary}; }}
    .stat-content .label {{ color: {secondary}; }}
    .bento-links {{ display: flex; justify-content: center; gap: 20px; }}
    .bento-links a {{ padding: 16px 28px; background: {text}10; color: {text}; text-decoration: none; font-weight: 600; border-radius: 12px; transition: all 0.3s ease; }}
    .bento-links a:hover {{ background: {primary}20; }}
    @media (max-width: 768px) {{ .bento-grid {{ grid-template-columns: 1fr 1fr; }} .bento-item.main {{ grid-column: span 2; grid-row: span 1; }} }}
    </style>
    '''
