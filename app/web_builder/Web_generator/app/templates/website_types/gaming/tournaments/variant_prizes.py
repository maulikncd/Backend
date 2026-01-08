from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Prize Pool - Prize distribution display"""
    title = props.get("title", "Prize Pool")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    prizes = [
        {"place": "1st", "amount": "$500,000", "icon": "🥇"},
        {"place": "2nd", "amount": "$250,000", "icon": "🥈"},
        {"place": "3rd", "amount": "$125,000", "icon": "🥉"},
        {"place": "4th", "amount": "$62,500", "icon": "4"},
        {"place": "5-8th", "amount": "$15,625", "icon": "🏆"},
    ]
    
    prizes_html = ""
    for i, p in enumerate(prizes):
        main = "main" if i == 0 else ""
        prizes_html += f'''
        <div class="prize-item {main}">
            <span class="prize-icon">{p['icon']}</span>
            <span class="prize-place">{p['place']}</span>
            <span class="prize-amount">{p['amount']}</span>
        </div>
        '''
    
    return f'''
    <section class="gaming-tournament-prizes" id="tournaments">
        <div class="prizes-container">
            <div class="prizes-header">
                <span class="total-prize">$1,000,000</span>
                <h2>{title}</h2>
            </div>
            <div class="prizes-grid">{prizes_html}</div>
        </div>
    </section>
    
    <style>
    .gaming-tournament-prizes {{ padding: 120px 24px; background: {background}; }}
    .prizes-container {{ max-width: 1000px; margin: 0 auto; text-align: center; }}
    .prizes-header {{ margin-bottom: 60px; }}
    .total-prize {{ font-family: 'Orbitron', sans-serif; font-size: 4rem; font-weight: 900; color: {primary}; text-shadow: 0 0 50px {primary}50; }}
    .prizes-header h2 {{ font-family: 'Rajdhani', sans-serif; font-size: 1.5rem; font-weight: 600; color: {secondary}; margin-top: 12px; }}
    .prizes-grid {{ display: flex; justify-content: center; gap: 24px; flex-wrap: wrap; }}
    .prize-item {{ background: {text}05; border: 1px solid {text}10; border-radius: 20px; padding: 32px; min-width: 150px; transition: all 0.4s ease; }}
    .prize-item:hover {{ transform: translateY(-8px); border-color: {primary}40; }}
    .prize-item.main {{ background: linear-gradient(135deg, {primary}15, {primary}05); border-color: {primary}; transform: scale(1.1); }}
    .prize-item.main:hover {{ transform: scale(1.1) translateY(-8px); }}
    .prize-icon {{ display: block; font-size: 3rem; margin-bottom: 12px; }}
    .prize-place {{ display: block; color: {secondary}; margin-bottom: 8px; font-weight: 600; }}
    .prize-amount {{ display: block; font-size: 1.5rem; font-weight: 900; color: {text}; }}
    .prize-item.main .prize-amount {{ color: {primary}; }}
    @media (max-width: 600px) {{ .prize-item.main {{ transform: none; }} }}
    </style>
    '''
