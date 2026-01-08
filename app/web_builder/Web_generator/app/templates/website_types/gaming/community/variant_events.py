from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Events Calendar - Upcoming events"""
    title = props.get("title", "Community Events")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    events = [
        {"date": "Dec 15", "name": "Community Game Night", "type": "Event", "time": "8:00 PM EST"},
        {"date": "Dec 18", "name": "Dev Stream Q&A", "type": "Stream", "time": "3:00 PM EST"},
        {"date": "Dec 20", "name": "Weekly Tournament", "type": "Tournament", "time": "6:00 PM EST"},
        {"date": "Dec 22", "name": "Holiday Special Event", "type": "Event", "time": "5:00 PM EST"},
    ]
    
    events_html = ""
    for e in events:
        events_html += f'''
        <div class="event-card">
            <div class="event-date">{e['date']}</div>
            <div class="event-info">
                <span class="event-type">{e['type']}</span>
                <h3>{e['name']}</h3>
                <span class="event-time">{e['time']}</span>
            </div>
            <button class="remind-btn">🔔</button>
        </div>
        '''
    
    return f'''
    <section class="gaming-community-events" id="community">
        <div class="events-container">
            <div class="events-header"><h2>{title}</h2></div>
            <div class="events-list">{events_html}</div>
        </div>
    </section>
    
    <style>
    .gaming-community-events {{ padding: 120px 24px; background: {background}; }}
    .events-container {{ max-width: 800px; margin: 0 auto; }}
    .events-header {{ text-align: center; margin-bottom: 48px; }}
    .events-header h2 {{ font-family: 'Rajdhani', sans-serif; font-size: 2.5rem; font-weight: 800; color: {text}; }}
    .events-list {{ display: flex; flex-direction: column; gap: 16px; }}
    .event-card {{ display: flex; align-items: center; gap: 24px; padding: 24px; background: {text}05; border-radius: 16px; transition: all 0.3s ease; }}
    .event-card:hover {{ background: {primary}10; }}
    .event-date {{ background: {primary}; color: {background}; padding: 16px; border-radius: 12px; text-align: center; font-weight: 700; font-size: 0.9rem; min-width: 80px; }}
    .event-info {{ flex: 1; }}
    .event-type {{ display: inline-block; padding: 3px 10px; background: {primary}20; color: {primary}; font-size: 0.7rem; font-weight: 700; border-radius: 100px; margin-bottom: 6px; }}
    .event-info h3 {{ font-size: 1.2rem; font-weight: 700; color: {text}; margin-bottom: 4px; }}
    .event-time {{ color: {secondary}; font-size: 0.9rem; }}
    .remind-btn {{ width: 48px; height: 48px; background: {text}10; border: none; border-radius: 12px; font-size: 1.2rem; cursor: pointer; transition: all 0.3s ease; }}
    .remind-btn:hover {{ background: {primary}20; }}
    </style>
    '''
