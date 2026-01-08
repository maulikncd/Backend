from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Timeline - Tournament schedule timeline"""
    title = props.get("title", "Upcoming Events")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    events = [
        {"date": "Dec 15", "name": "World Championship Opens", "type": "Major"},
        {"date": "Dec 18", "name": "Group Stage Begins", "type": "Stage"},
        {"date": "Dec 19", "name": "Quarterfinals", "type": "Playoffs"},
        {"date": "Dec 20", "name": "Grand Finals", "type": "Finals"},
    ]
    
    timeline_html = ""
    for e in events:
        timeline_html += f'''
        <div class="timeline-item">
            <div class="timeline-date">{e['date']}</div>
            <div class="timeline-dot"></div>
            <div class="timeline-content">
                <span class="event-type">{e['type']}</span>
                <h3>{e['name']}</h3>
            </div>
        </div>
        '''
    
    return f'''
    <section class="gaming-tournament-timeline" id="tournaments">
        <div class="timeline-container">
            <div class="timeline-header"><h2>{title}</h2></div>
            <div class="timeline">{timeline_html}</div>
        </div>
    </section>
    
    <style>
    .gaming-tournament-timeline {{ padding: 120px 24px; background: {background}; }}
    .timeline-container {{ max-width: 800px; margin: 0 auto; }}
    .timeline-header {{ text-align: center; margin-bottom: 60px; }}
    .timeline-header h2 {{ font-family: 'Rajdhani', sans-serif; font-size: 3rem; font-weight: 800; color: {text}; }}
    .timeline {{ position: relative; }}
    .timeline::before {{ content: ''; position: absolute; left: 120px; top: 0; bottom: 0; width: 2px; background: {primary}30; }}
    .timeline-item {{ display: flex; align-items: center; gap: 24px; padding: 24px 0; position: relative; }}
    .timeline-date {{ width: 100px; text-align: right; font-weight: 700; color: {primary}; font-size: 1.1rem; }}
    .timeline-dot {{ width: 16px; height: 16px; background: {primary}; border-radius: 50%; position: relative; z-index: 2; box-shadow: 0 0 20px {primary}50; }}
    .timeline-content {{ flex: 1; background: {text}05; border-radius: 16px; padding: 24px; }}
    .event-type {{ display: inline-block; padding: 4px 12px; background: {primary}20; color: {primary}; font-size: 0.75rem; font-weight: 700; border-radius: 100px; margin-bottom: 8px; }}
    .timeline-content h3 {{ font-size: 1.3rem; font-weight: 700; color: {text}; }}
    @media (max-width: 600px) {{ .timeline::before {{ left: 20px; }} .timeline-date {{ width: auto; font-size: 0.9rem; }} }}
    </style>
    '''
