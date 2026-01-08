from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Video News - Video-focused news layout"""
    title = props.get("title", "Video Updates")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    videos = [
        {"thumb": "https://images.unsplash.com/photo-1542751371-adc38448a05e?w=800", "title": "Season 5 Trailer", "views": "2.5M", "duration": "3:24"},
        {"thumb": "https://images.unsplash.com/photo-1538481199705-c710c4e965fc?w=600", "title": "Developer Update #47", "views": "890K", "duration": "12:45"},
        {"thumb": "https://images.unsplash.com/photo-1511512578047-dfb367046420?w=600", "title": "New Map Walkthrough", "views": "1.2M", "duration": "8:30"},
        {"thumb": "https://images.unsplash.com/photo-1493711662062-fa541f7f069d?w=600", "title": "Pro Tips: Advanced Movement", "views": "567K", "duration": "15:20"},
    ]
    
    cards_html = ""
    for i, vid in enumerate(videos):
        featured = "featured" if i == 0 else ""
        cards_html += f'''
        <article class="video-card {featured}">
            <div class="video-thumb">
                <img src="{vid['thumb']}" alt="{vid['title']}">
                <div class="play-btn">▶</div>
                <span class="duration">{vid['duration']}</span>
            </div>
            <div class="video-info">
                <h3>{vid['title']}</h3>
                <span class="views">{vid['views']} views</span>
            </div>
        </article>
        '''
    
    return f'''
    <section class="gaming-news-video" id="news">
        <div class="video-container">
            <div class="video-header">
                <span class="section-tag">🎬 Videos</span>
                <h2>{title}</h2>
            </div>
            <div class="video-grid">
                {cards_html}
            </div>
        </div>
    </section>
    
    <style>
    .gaming-news-video {{
        padding: 120px 24px;
        background: {background};
    }}
    .video-container {{
        max-width: 1200px;
        margin: 0 auto;
    }}
    .video-header {{
        text-align: center;
        margin-bottom: 60px;
    }}
    .section-tag {{
        display: inline-block;
        padding: 10px 24px;
        background: {primary}15;
        color: {primary};
        font-weight: 700;
        border-radius: 100px;
        margin-bottom: 20px;
    }}
    .video-header h2 {{
        font-family: 'Rajdhani', sans-serif;
        font-size: clamp(2.5rem, 5vw, 4rem);
        font-weight: 800;
        color: {text};
    }}
    .video-grid {{
        display: grid;
        grid-template-columns: 2fr 1fr;
        grid-template-rows: repeat(3, auto);
        gap: 24px;
    }}
    .video-card {{
        cursor: pointer;
    }}
    .video-card.featured {{
        grid-row: span 3;
    }}
    .video-thumb {{
        position: relative;
        border-radius: 16px;
        overflow: hidden;
        margin-bottom: 16px;
    }}
    .video-card.featured .video-thumb {{
        aspect-ratio: 16/10;
    }}
    .video-card:not(.featured) .video-thumb {{
        aspect-ratio: 16/9;
    }}
    .video-thumb img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.5s ease;
    }}
    .video-card:hover .video-thumb img {{
        transform: scale(1.1);
    }}
    .play-btn {{
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 70px;
        height: 70px;
        background: {primary};
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: {background};
        font-size: 1.5rem;
        opacity: 0;
        transition: all 0.3s ease;
        box-shadow: 0 10px 40px {primary}60;
    }}
    .video-card:hover .play-btn {{
        opacity: 1;
    }}
    .duration {{
        position: absolute;
        bottom: 12px;
        right: 12px;
        padding: 6px 12px;
        background: {background}CC;
        color: {text};
        font-size: 0.85rem;
        font-weight: 600;
        border-radius: 6px;
    }}
    .video-info h3 {{
        font-size: 1.2rem;
        font-weight: 700;
        color: {text};
        margin-bottom: 6px;
    }}
    .video-card.featured .video-info h3 {{
        font-size: 1.8rem;
    }}
    .views {{
        color: {secondary};
        font-size: 0.9rem;
    }}
    @media (max-width: 900px) {{
        .video-grid {{ grid-template-columns: 1fr; }}
        .video-card.featured {{ grid-row: span 1; }}
    }}
    </style>
    '''
