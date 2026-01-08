from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Card Grid - Tournament cards layout"""
    title = props.get("title", "Active Tournaments")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    tournaments = [
        {"name": "Pro League Season 8", "prize": "$500K", "teams": "32", "status": "Live", "img": "https://images.unsplash.com/photo-1542751371-adc38448a05e?w=600"},
        {"name": "Weekly Cup #47", "prize": "$10K", "teams": "64", "status": "Registering", "img": "https://images.unsplash.com/photo-1538481199705-c710c4e965fc?w=600"},
        {"name": "Rookie Championship", "prize": "$25K", "teams": "128", "status": "Starting Soon", "img": "https://images.unsplash.com/photo-1511512578047-dfb367046420?w=600"},
        {"name": "Masters Invitational", "prize": "$100K", "teams": "16", "status": "Live", "img": "https://images.unsplash.com/photo-1493711662062-fa541f7f069d?w=600"},
    ]
    
    cards_html = ""
    for t in tournaments:
        status_class = "live" if t["status"] == "Live" else ""
        cards_html += f'''
        <div class="tournament-card">
            <div class="card-image"><img src="{t['img']}" alt="{t['name']}"></div>
            <div class="card-content">
                <span class="status {status_class}">{t['status']}</span>
                <h3>{t['name']}</h3>
                <div class="card-stats">
                    <div><span>{t['prize']}</span><label>Prize</label></div>
                    <div><span>{t['teams']}</span><label>Teams</label></div>
                </div>
                <a href="#" class="card-btn">View Details</a>
            </div>
        </div>
        '''
    
    return f'''
    <section class="gaming-tournament-cards" id="tournaments">
        <div class="cards-container">
            <div class="cards-header"><h2>{title}</h2></div>
            <div class="tournament-grid">{cards_html}</div>
        </div>
    </section>
    
    <style>
    .gaming-tournament-cards {{ padding: 120px 24px; background: {background}; }}
    .cards-container {{ max-width: 1200px; margin: 0 auto; }}
    .cards-header {{ text-align: center; margin-bottom: 60px; }}
    .cards-header h2 {{ font-family: 'Rajdhani', sans-serif; font-size: 3rem; font-weight: 800; color: {text}; }}
    .tournament-grid {{ display: grid; grid-template-columns: repeat(2, 1fr); gap: 32px; }}
    .tournament-card {{ background: {text}05; border-radius: 24px; overflow: hidden; display: flex; transition: all 0.4s ease; }}
    .tournament-card:hover {{ transform: translateY(-8px); box-shadow: 0 30px 60px {primary}15; }}
    .card-image {{ width: 200px; flex-shrink: 0; }}
    .card-image img {{ width: 100%; height: 100%; object-fit: cover; }}
    .card-content {{ padding: 24px; flex: 1; }}
    .status {{ display: inline-block; padding: 5px 14px; background: {primary}20; color: {primary}; font-size: 0.75rem; font-weight: 700; border-radius: 100px; margin-bottom: 12px; }}
    .status.live {{ background: #ff3b3b; color: white; animation: pulse 2s infinite; }}
    .card-content h3 {{ font-size: 1.3rem; font-weight: 700; color: {text}; margin-bottom: 16px; }}
    .card-stats {{ display: flex; gap: 32px; margin-bottom: 16px; }}
    .card-stats div span {{ display: block; font-weight: 900; color: {primary}; font-size: 1.3rem; }}
    .card-stats div label {{ font-size: 0.8rem; color: {secondary}; }}
    .card-btn {{ display: inline-block; padding: 10px 24px; background: {primary}; color: {background}; text-decoration: none; font-weight: 700; border-radius: 8px; transition: all 0.3s ease; }}
    .card-btn:hover {{ transform: scale(1.05); }}
    @media (max-width: 900px) {{ .tournament-grid {{ grid-template-columns: 1fr; }} .tournament-card {{ flex-direction: column; }} .card-image {{ width: 100%; height: 200px; }} }}
    </style>
    '''
