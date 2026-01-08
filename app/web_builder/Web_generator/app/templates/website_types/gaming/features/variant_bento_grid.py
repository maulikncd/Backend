from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Bento Grid Features"""
    title = props.get("title", "Game Features")
    primary = colors.get("primary", "#8B5CF6")
    
    return f'''
    <section class="gaming-features-bento" id="features"><div class="container"><h2>{title}</h2><div class="bento-grid">
        <div class="bento-item large" style="background: linear-gradient(135deg, {primary}, #FF6B6B)"><h3>4K Graphics</h3><p>Ultra-realistic visuals</p></div>
        <div class="bento-item"><h3>🎮</h3><p>Controller Support</p></div>
        <div class="bento-item"><h3>🌐</h3><p>Cross-Platform</p></div>
        <div class="bento-item wide" style="background: url('https://images.unsplash.com/photo-1538481199705-c710c4e965fc?w=800') center/cover"><div class="overlay"></div><h3>Epic Battles</h3></div>
        <div class="bento-item"><h3>🏆</h3><p>Ranked Mode</p></div>
    </div></div></section>
    <style>
    .gaming-features-bento {{ padding: 100px 40px; background: #0D0D15; }}
    .container {{ max-width: 1100px; margin: 0 auto; }}
    .gaming-features-bento h2 {{ font-size: 3rem; color: #fff; text-align: center; margin-bottom: 50px; }}
    .bento-grid {{ display: grid; grid-template-columns: repeat(4, 1fr); grid-template-rows: repeat(2, 200px); gap: 20px; }}
    .bento-item {{ background: #1a1a2e; border-radius: 20px; padding: 30px; display: flex; flex-direction: column; justify-content: flex-end; color: #fff; position: relative; overflow: hidden; transition: 0.3s; }}
    .bento-item:hover {{ transform: scale(1.02); }}
    .bento-item.large {{ grid-column: span 2; }}
    .bento-item.wide {{ grid-column: span 2; }}
    .bento-item h3 {{ font-size: 1.8rem; margin-bottom: 5px; position: relative; z-index: 1; }}
    .bento-item p {{ color: rgba(255,255,255,0.7); position: relative; z-index: 1; }}
    .overlay {{ position: absolute; inset: 0; background: rgba(0,0,0,0.5); }}
    @media (max-width: 768px) {{ .bento-grid {{ grid-template-columns: 1fr; }} .bento-item.large, .bento-item.wide {{ grid-column: span 1; }} }}
    </style>
    '''
