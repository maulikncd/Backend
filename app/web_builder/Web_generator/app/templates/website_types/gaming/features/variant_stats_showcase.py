from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    stats = props.get("stats", [
        {"label": "Active Players", "value": "2.5M", "icon": "👥"},
        {"label": "Match Wins", "value": "500K+", "icon": "🔫"},
        {"label": "Hours Streamed", "value": "1.2M", "icon": "🎥"},
        {"label": "Server Uptime", "value": "99.9%", "icon": "🔌"}
    ])
    
    primary = colors.get("primary", "#00FF88")
    
    # Build stat boxes separately
    stat_boxes = ""
    for s in stats:
        stat_boxes += f'''
            <div class="stat-box">
                <div class="stat-icon">{s["icon"]}</div>
                <div class="stat-number">{s["value"]}</div>
                <div class="stat-label">{s["label"]}</div>
                <div class="stat-progress"><div class="stat-fill" style="width: 70%"></div></div>
            </div>
        '''
    
    return f'''
    <section class="gaming-stats-showcase">
        <div class="stats-container">
            {stat_boxes}
        </div>
    </section>
    
    <style>
    .gaming-stats-showcase {{
        padding: 100px 20px;
        background: #000;
    }}
    .stats-container {{
        max-width: 1200px;
        margin: 0 auto;
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 40px;
    }}
    .stat-box {{
        text-align: center;
        background: rgba(255,255,255,0.02);
        padding: 40px;
        border-radius: 10px;
        transition: 0.3s;
    }}
    .stat-box:hover {{ background: rgba(255,255,255,0.05); transform: translateY(-5px); }}
    .stat-icon {{ font-size: 2.5rem; margin-bottom: 20px; }}
    .stat-number {{
        font-family: 'Rajdhani', sans-serif;
        font-size: 3rem;
        font-weight: 800;
        color: {primary};
        margin-bottom: 10px;
    }}
    .stat-label {{ color: #888; text-transform: uppercase; font-size: 0.9rem; margin-bottom: 20px; }}
    .stat-progress {{ height: 4px; background: rgba(255,255,255,0.1); border-radius: 2px; overflow: hidden; }}
    .stat-fill {{ height: 100%; background: {primary}; }}
    </style>
    '''
