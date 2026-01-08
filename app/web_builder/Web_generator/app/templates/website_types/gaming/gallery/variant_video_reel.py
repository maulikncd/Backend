from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Video Reel - Instagram-style video thumbnails"""
    title = props.get("title", "Video Highlights")
    subtitle = props.get("subtitle", "Watch our best moments")
    
    # Dynamic colors from user's palette
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    videos = [
        {"thumb": "https://images.unsplash.com/photo-1542751371-adc38448a05e?w=400", "title": "Championship Finals", "duration": "12:34", "views": "1.2M"},
        {"thumb": "https://images.unsplash.com/photo-1538481199705-c710c4e965fc?w=400", "title": "Setup Tour 2024", "duration": "8:45", "views": "890K"},
        {"thumb": "https://images.unsplash.com/photo-1511512578047-dfb367046420?w=400", "title": "Night Stream Highlights", "duration": "15:20", "views": "654K"},
        {"thumb": "https://images.unsplash.com/photo-1493711662062-fa541f7f069d?w=400", "title": "Gear Review", "duration": "10:15", "views": "432K"},
        {"thumb": "https://images.unsplash.com/photo-1542751110-97427bbecf20?w=400", "title": "Tournament Recap", "duration": "20:00", "views": "2.1M"},
        {"thumb": "https://images.unsplash.com/photo-1612287230202-1ff1d85d1bdf?w=400", "title": "Pro Tips & Tricks", "duration": "6:30", "views": "567K"},
    ]
    
    videos_html = ""
    for vid in videos:
        videos_html += f'''
        <div class="video-card">
            <div class="video-thumb">
                <img src="{vid['thumb']}" alt="{vid['title']}">
                <div class="play-overlay">
                    <div class="play-btn">
                        <svg viewBox="0 0 24 24" fill="currentColor">
                            <path d="M8 5v14l11-7z"/>
                        </svg>
                    </div>
                </div>
                <span class="duration">{vid['duration']}</span>
            </div>
            <div class="video-info">
                <h4>{vid['title']}</h4>
                <span class="views">{vid['views']} views</span>
            </div>
        </div>
        '''
    
    return f'''
    <section class="gaming-gallery-videos" id="gallery">
        <div class="videos-container">
            <div class="videos-header">
                <div class="header-left">
                    <span class="video-tag">🎬 Videos</span>
                    <h2>{title}</h2>
                    <p>{subtitle}</p>
                </div>
                <a href="#all-videos" class="view-all-btn">View All →</a>
            </div>
            <div class="videos-grid">
                {videos_html}
            </div>
        </div>
    </section>
    
    <style>
    .gaming-gallery-videos {{
        padding: 140px 24px;
        background: {background};
    }}
    .videos-container {{
        max-width: 1200px;
        margin: 0 auto;
    }}
    .videos-header {{
        display: flex;
        justify-content: space-between;
        align-items: flex-end;
        margin-bottom: 60px;
        flex-wrap: wrap;
        gap: 24px;
    }}
    .video-tag {{
        display: inline-block;
        padding: 8px 20px;
        background: {primary}15;
        color: {primary};
        font-weight: 700;
        font-size: 0.85rem;
        letter-spacing: 2px;
        border-radius: 100px;
        margin-bottom: 16px;
    }}
    .header-left h2 {{
        font-family: 'Rajdhani', sans-serif;
        font-size: clamp(2rem, 4vw, 3rem);
        font-weight: 800;
        color: {text};
        margin-bottom: 8px;
    }}
    .header-left p {{
        color: {secondary};
    }}
    .view-all-btn {{
        padding: 14px 32px;
        background: transparent;
        border: 2px solid {primary};
        color: {primary};
        font-weight: 700;
        text-decoration: none;
        border-radius: 10px;
        transition: all 0.3s ease;
    }}
    .view-all-btn:hover {{
        background: {primary};
        color: {background};
    }}
    .videos-grid {{
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 32px;
    }}
    .video-card {{
        cursor: pointer;
        transition: transform 0.4s ease;
    }}
    .video-card:hover {{
        transform: translateY(-8px);
    }}
    .video-thumb {{
        position: relative;
        border-radius: 16px;
        overflow: hidden;
        aspect-ratio: 16/9;
        margin-bottom: 16px;
    }}
    .video-thumb img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.6s ease;
    }}
    .video-card:hover .video-thumb img {{
        transform: scale(1.1);
    }}
    .play-overlay {{
        position: absolute;
        inset: 0;
        background: {background}60;
        display: flex;
        align-items: center;
        justify-content: center;
        opacity: 0;
        transition: opacity 0.3s ease;
    }}
    .video-card:hover .play-overlay {{
        opacity: 1;
    }}
    .play-btn {{
        width: 70px;
        height: 70px;
        background: {primary};
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        transition: transform 0.3s ease;
        box-shadow: 0 0 40px {primary}60;
    }}
    .play-btn svg {{
        width: 28px;
        height: 28px;
        color: {background};
        margin-left: 4px;
    }}
    .video-card:hover .play-btn {{
        transform: scale(1.1);
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
    .video-info h4 {{
        font-size: 1.1rem;
        font-weight: 700;
        color: {text};
        margin-bottom: 4px;
    }}
    .views {{
        font-size: 0.9rem;
        color: {secondary};
    }}
    @media (max-width: 900px) {{
        .videos-grid {{ grid-template-columns: repeat(2, 1fr); }}
    }}
    @media (max-width: 600px) {{
        .videos-grid {{ grid-template-columns: 1fr; }}
        .videos-header {{ flex-direction: column; align-items: flex-start; }}
    }}
    </style>
    '''
