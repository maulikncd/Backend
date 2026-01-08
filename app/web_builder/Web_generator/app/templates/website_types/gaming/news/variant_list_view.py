from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """List View - Clean list with thumbnails"""
    title = props.get("title", "Latest Updates")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    news = [
        {"img": "https://images.unsplash.com/photo-1542751371-adc38448a05e?w=300", "cat": "Update", "title": "Season 5 Brings Massive Changes", "excerpt": "New maps, weapons, and game modes are here", "date": "Dec 15, 2024", "read": "5 min"},
        {"img": "https://images.unsplash.com/photo-1538481199705-c710c4e965fc?w=300", "cat": "Esports", "title": "Championship Finals Schedule Released", "excerpt": "Mark your calendars for the biggest event", "date": "Dec 14, 2024", "read": "3 min"},
        {"img": "https://images.unsplash.com/photo-1511512578047-dfb367046420?w=300", "cat": "Patch", "title": "Patch 5.2 Notes", "excerpt": "Balance changes and bug fixes", "date": "Dec 12, 2024", "read": "8 min"},
        {"img": "https://images.unsplash.com/photo-1493711662062-fa541f7f069d?w=300", "cat": "Community", "title": "Creator Program Expansion", "excerpt": "New benefits for content creators", "date": "Dec 10, 2024", "read": "4 min"},
    ]
    
    list_html = ""
    for item in news:
        list_html += f'''
        <article class="news-list-item">
            <img src="{item['img']}" alt="{item['title']}">
            <div class="item-content">
                <span class="item-cat">{item['cat']}</span>
                <h3>{item['title']}</h3>
                <p>{item['excerpt']}</p>
                <div class="item-meta">
                    <span>{item['date']}</span>
                    <span>•</span>
                    <span>{item['read']} read</span>
                </div>
            </div>
            <a href="#" class="read-link">Read →</a>
        </article>
        '''
    
    return f'''
    <section class="gaming-news-list" id="news">
        <div class="list-container">
            <div class="list-header">
                <h2>{title}</h2>
            </div>
            <div class="news-list">
                {list_html}
            </div>
            <div class="list-footer">
                <a href="#" class="load-more">Load More Articles</a>
            </div>
        </div>
    </section>
    
    <style>
    .gaming-news-list {{
        padding: 120px 24px;
        background: {background};
    }}
    .list-container {{
        max-width: 900px;
        margin: 0 auto;
    }}
    .list-header {{
        margin-bottom: 48px;
    }}
    .list-header h2 {{
        font-family: 'Rajdhani', sans-serif;
        font-size: 2.5rem;
        font-weight: 800;
        color: {text};
    }}
    .news-list {{
        display: flex;
        flex-direction: column;
        gap: 24px;
    }}
    .news-list-item {{
        display: flex;
        align-items: center;
        gap: 24px;
        padding: 24px;
        background: {text}05;
        border-radius: 20px;
        transition: all 0.3s ease;
    }}
    .news-list-item:hover {{
        background: {primary}08;
        transform: translateX(8px);
    }}
    .news-list-item img {{
        width: 180px;
        height: 120px;
        object-fit: cover;
        border-radius: 12px;
        flex-shrink: 0;
    }}
    .item-content {{
        flex: 1;
    }}
    .item-cat {{
        display: inline-block;
        padding: 4px 12px;
        background: {primary}20;
        color: {primary};
        font-size: 0.75rem;
        font-weight: 700;
        border-radius: 100px;
        margin-bottom: 10px;
    }}
    .item-content h3 {{
        font-size: 1.3rem;
        font-weight: 700;
        color: {text};
        margin-bottom: 8px;
    }}
    .item-content p {{
        color: {secondary};
        font-size: 0.95rem;
        margin-bottom: 12px;
    }}
    .item-meta {{
        display: flex;
        gap: 10px;
        color: {secondary};
        font-size: 0.85rem;
    }}
    .read-link {{
        padding: 12px 24px;
        background: {primary};
        color: {background};
        text-decoration: none;
        font-weight: 700;
        border-radius: 10px;
        flex-shrink: 0;
        transition: all 0.3s ease;
    }}
    .read-link:hover {{
        transform: scale(1.05);
    }}
    .list-footer {{
        text-align: center;
        margin-top: 48px;
    }}
    .load-more {{
        padding: 16px 48px;
        background: transparent;
        border: 2px solid {primary};
        color: {primary};
        text-decoration: none;
        font-weight: 700;
        border-radius: 10px;
        transition: all 0.3s ease;
    }}
    .load-more:hover {{
        background: {primary};
        color: {background};
    }}
    @media (max-width: 768px) {{
        .news-list-item {{ flex-direction: column; text-align: center; }}
        .news-list-item img {{ width: 100%; height: 180px; }}
        .read-link {{ width: 100%; text-align: center; }}
        .item-meta {{ justify-content: center; }}
    }}
    </style>
    '''
