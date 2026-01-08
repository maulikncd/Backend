from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Featured News - Large hero article with sidebar"""
    title = props.get("title", "Latest News")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="gaming-news-featured" id="news">
        <div class="news-container">
            <div class="news-header">
                <span class="section-tag">📰 News</span>
                <h2>{title}</h2>
            </div>
            <div class="news-layout">
                <article class="featured-article">
                    <img src="https://images.unsplash.com/photo-1542751371-adc38448a05e?w=1200" alt="Featured">
                    <div class="article-overlay">
                        <span class="tag">Featured</span>
                        <h3>Season 5 Update: New Maps, Weapons & Game Modes</h3>
                        <p>The biggest update of the year brings revolutionary changes...</p>
                        <div class="article-meta">
                            <span>🕐 2 hours ago</span>
                            <span>💬 234 comments</span>
                        </div>
                    </div>
                </article>
                <div class="news-sidebar">
                    <article class="sidebar-article">
                        <img src="https://images.unsplash.com/photo-1538481199705-c710c4e965fc?w=300" alt="News">
                        <div class="article-info">
                            <span class="cat">Tournament</span>
                            <h4>World Championship Finals Set for December</h4>
                            <span class="time">5 hours ago</span>
                        </div>
                    </article>
                    <article class="sidebar-article">
                        <img src="https://images.unsplash.com/photo-1511512578047-dfb367046420?w=300" alt="News">
                        <div class="article-info">
                            <span class="cat">Update</span>
                            <h4>Patch 5.2 Brings Balance Changes</h4>
                            <span class="time">1 day ago</span>
                        </div>
                    </article>
                    <article class="sidebar-article">
                        <img src="https://images.unsplash.com/photo-1493711662062-fa541f7f069d?w=300" alt="News">
                        <div class="article-info">
                            <span class="cat">Community</span>
                            <h4>Pro Player Breaks World Record</h4>
                            <span class="time">2 days ago</span>
                        </div>
                    </article>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    .gaming-news-featured {{
        padding: 120px 24px;
        background: {background};
    }}
    .news-container {{
        max-width: 1400px;
        margin: 0 auto;
    }}
    .news-header {{
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
    .news-header h2 {{
        font-family: 'Rajdhani', sans-serif;
        font-size: clamp(2.5rem, 5vw, 4rem);
        font-weight: 800;
        color: {text};
    }}
    .news-layout {{
        display: grid;
        grid-template-columns: 2fr 1fr;
        gap: 32px;
    }}
    .featured-article {{
        position: relative;
        border-radius: 24px;
        overflow: hidden;
        aspect-ratio: 16/10;
    }}
    .featured-article img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
    }}
    .article-overlay {{
        position: absolute;
        inset: 0;
        background: linear-gradient(to top, {background}E6, transparent 50%);
        padding: 40px;
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
    }}
    .tag {{
        display: inline-block;
        padding: 6px 16px;
        background: {primary};
        color: {background};
        font-size: 0.8rem;
        font-weight: 700;
        border-radius: 100px;
        margin-bottom: 16px;
        width: fit-content;
    }}
    .article-overlay h3 {{
        font-size: 2rem;
        font-weight: 800;
        color: {text};
        margin-bottom: 12px;
    }}
    .article-overlay p {{
        color: {secondary};
        margin-bottom: 16px;
    }}
    .article-meta {{
        display: flex;
        gap: 20px;
        color: {secondary};
        font-size: 0.9rem;
    }}
    .news-sidebar {{
        display: flex;
        flex-direction: column;
        gap: 20px;
    }}
    .sidebar-article {{
        display: flex;
        gap: 16px;
        padding: 16px;
        background: {text}05;
        border-radius: 16px;
        transition: all 0.3s ease;
        cursor: pointer;
    }}
    .sidebar-article:hover {{
        background: {primary}10;
    }}
    .sidebar-article img {{
        width: 100px;
        height: 80px;
        object-fit: cover;
        border-radius: 10px;
    }}
    .article-info {{
        flex: 1;
    }}
    .cat {{
        display: inline-block;
        padding: 3px 10px;
        background: {primary}20;
        color: {primary};
        font-size: 0.7rem;
        font-weight: 700;
        border-radius: 100px;
        margin-bottom: 8px;
    }}
    .article-info h4 {{
        font-size: 1rem;
        font-weight: 700;
        color: {text};
        margin-bottom: 8px;
        line-height: 1.4;
    }}
    .time {{
        font-size: 0.8rem;
        color: {secondary};
    }}
    @media (max-width: 900px) {{
        .news-layout {{ grid-template-columns: 1fr; }}
    }}
    </style>
    '''
