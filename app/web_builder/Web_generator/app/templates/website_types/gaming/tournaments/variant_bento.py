from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Bento Tournaments - Modern bento layout"""
    title = props.get("title", "Tournaments")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="gaming-tournament-bento" id="tournaments">
        <div class="bento-container">
            <div class="bento-header"><h2>{title}</h2></div>
            <div class="bento-grid">
                <div class="bento-item main">
                    <img src="https://images.unsplash.com/photo-1542751371-adc38448a05e?w=1200" alt="Tournament">
                    <div class="bento-overlay">
                        <span class="live">🔴 Live</span>
                        <h3>World Championship</h3>
                        <span class="prize">$1M Prize Pool</span>
                    </div>
                </div>
                <div class="bento-item">
                    <div class="stat-card"><span class="num">64</span><span class="label">Teams</span></div>
                </div>
                <div class="bento-item">
                    <div class="stat-card"><span class="num">5</span><span class="label">Days</span></div>
                </div>
                <div class="bento-item wide">
                    <img src="https://images.unsplash.com/photo-1538481199705-c710c4e965fc?w=900" alt="Tournament">
                    <div class="bento-overlay small">
                        <h4>Weekly Cup</h4><span class="prize">$10K</span>
                    </div>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    .gaming-tournament-bento {{ padding: 120px 24px; background: {background}; }}
    .bento-container {{ max-width: 1200px; margin: 0 auto; }}
    .bento-header {{ text-align: center; margin-bottom: 60px; }}
    .bento-header h2 {{ font-family: 'Rajdhani', sans-serif; font-size: 3rem; font-weight: 800; color: {text}; }}
    .bento-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); grid-template-rows: repeat(2, 250px); gap: 24px; }}
    .bento-item {{ position: relative; border-radius: 24px; overflow: hidden; }}
    .bento-item.main {{ grid-column: span 2; grid-row: span 2; }}
    .bento-item.wide {{ grid-column: span 2; }}
    .bento-item img {{ width: 100%; height: 100%; object-fit: cover; }}
    .bento-overlay {{ position: absolute; inset: 0; background: linear-gradient(to top, {background}E6, transparent 50%); padding: 32px; display: flex; flex-direction: column; justify-content: flex-end; }}
    .bento-overlay.small {{ padding: 20px; }}
    .live {{ display: inline-block; padding: 6px 14px; background: #ff3b3b; color: white; font-size: 0.75rem; font-weight: 700; border-radius: 100px; margin-bottom: 12px; width: fit-content; }}
    .bento-overlay h3 {{ font-size: 2rem; font-weight: 800; color: {text}; margin-bottom: 8px; }}
    .bento-overlay h4 {{ font-size: 1.2rem; font-weight: 700; color: {text}; margin-bottom: 4px; }}
    .prize {{ color: {primary}; font-weight: 700; }}
    .stat-card {{ height: 100%; background: {text}05; display: flex; flex-direction: column; align-items: center; justify-content: center; }}
    .stat-card .num {{ font-family: 'Orbitron', sans-serif; font-size: 3rem; font-weight: 900; color: {primary}; }}
    .stat-card .label {{ color: {secondary}; }}
    @media (max-width: 900px) {{ .bento-grid {{ grid-template-columns: 1fr 1fr; }} .bento-item.main {{ grid-column: span 2; grid-row: span 1; }} }}
    </style>
    '''
