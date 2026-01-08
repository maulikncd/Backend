from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Timeline Feed - Social media style news feed"""
    title = props.get("title", "News Feed")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    news = [
        {"type": "update", "icon": "🔄", "title": "Season 5 Now Live", "desc": "New maps and weapons available", "time": "2h ago"},
        {"type": "event", "icon": "🏆", "title": "Tournament Registration Open", "desc": "Sign up for the Winter Championship", "time": "5h ago"},
        {"type": "patch", "icon": "🔧", "title": "Patch Notes 5.2", "desc": "Balance changes and bug fixes", "time": "1d ago"},
        {"type": "community", "icon": "👥", "title": "New Community Challenge", "desc": "Complete 1M matches together", "time": "2d ago"},
    ]
    
    feed_html = ""
    for item in news:
        feed_html += f'''
        <div class="feed-item">
            <div class="feed-icon">{item['icon']}</div>
            <div class="feed-line"></div>
            <div class="feed-content">
                <span class="feed-type">{item['type']}</span>
                <h3>{item['title']}</h3>
                <p>{item['desc']}</p>
                <span class="feed-time">{item['time']}</span>
            </div>
        </div>
        '''
    
    return f'''
    <section class="gaming-news-timeline" id="news">
        <div class="timeline-container">
            <div class="timeline-header">
                <h2>{title}</h2>
                <a href="#" class="view-all">View All →</a>
            </div>
            <div class="timeline-feed">
                {feed_html}
            </div>
        </div>
    </section>
    
    <style>
    .gaming-news-timeline {{
        padding: 120px 24px;
        background: {background};
    }}
    .timeline-container {{
        max-width: 700px;
        margin: 0 auto;
    }}
    .timeline-header {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 48px;
    }}
    .timeline-header h2 {{
        font-family: 'Rajdhani', sans-serif;
        font-size: 2.5rem;
        font-weight: 800;
        color: {text};
    }}
    .view-all {{
        color: {primary};
        text-decoration: none;
        font-weight: 600;
    }}
    .timeline-feed {{
        position: relative;
    }}
    .feed-item {{
        display: flex;
        gap: 24px;
        padding-bottom: 40px;
        position: relative;
    }}
    .feed-icon {{
        width: 50px;
        height: 50px;
        background: {primary}15;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.5rem;
        flex-shrink: 0;
        position: relative;
        z-index: 2;
    }}
    .feed-line {{
        position: absolute;
        left: 24px;
        top: 50px;
        bottom: 0;
        width: 2px;
        background: {text}10;
    }}
    .feed-item:last-child .feed-line {{
        display: none;
    }}
    .feed-content {{
        flex: 1;
        padding: 4px 0;
    }}
    .feed-type {{
        display: inline-block;
        padding: 4px 12px;
        background: {primary}20;
        color: {primary};
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        border-radius: 100px;
        margin-bottom: 12px;
    }}
    .feed-content h3 {{
        font-size: 1.3rem;
        font-weight: 700;
        color: {text};
        margin-bottom: 8px;
    }}
    .feed-content p {{
        color: {secondary};
        margin-bottom: 12px;
    }}
    .feed-time {{
        font-size: 0.85rem;
        color: {secondary};
    }}
    </style>
    '''
