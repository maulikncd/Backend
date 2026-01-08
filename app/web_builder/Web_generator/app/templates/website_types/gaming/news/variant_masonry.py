from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Masonry News - Pinterest style layout"""
    title = props.get("title", "News & Updates")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    news = [
        {"img": "https://images.unsplash.com/photo-1542751371-adc38448a05e?w=600", "cat": "Featured", "title": "Season 5 Launch", "tall": True},
        {"img": "https://images.unsplash.com/photo-1538481199705-c710c4e965fc?w=600", "cat": "Esports", "title": "Pro League Update", "tall": False},
        {"img": "https://images.unsplash.com/photo-1511512578047-dfb367046420?w=600", "cat": "Update", "title": "New Map Preview", "tall": False},
        {"img": "https://images.unsplash.com/photo-1493711662062-fa541f7f069d?w=600", "cat": "Guide", "title": "Beginner Tips", "tall": True},
        {"img": "https://images.unsplash.com/photo-1542751110-97427bbecf20?w=600", "cat": "Event", "title": "Community Day", "tall": False},
        {"img": "https://images.unsplash.com/photo-1612287230202-1ff1d85d1bdf?w=600", "cat": "Patch", "title": "Balance Changes", "tall": False},
    ]
    
    cards_html = ""
    for item in news:
        tall_class = "tall" if item["tall"] else ""
        cards_html += f'''
        <article class="masonry-news {tall_class}">
            <img src="{item['img']}" alt="{item['title']}">
            <div class="news-overlay">
                <span class="news-cat">{item['cat']}</span>
                <h3>{item['title']}</h3>
            </div>
        </article>
        '''
    
    return f'''
    <section class="gaming-news-masonry" id="news">
        <div class="masonry-container">
            <div class="masonry-header">
                <span class="tag">📰 News</span>
                <h2>{title}</h2>
            </div>
            <div class="masonry-grid">
                {cards_html}
            </div>
        </div>
    </section>
    
    <style>
    .gaming-news-masonry {{
        padding: 120px 24px;
        background: {background};
    }}
    .masonry-container {{
        max-width: 1200px;
        margin: 0 auto;
    }}
    .masonry-header {{
        text-align: center;
        margin-bottom: 60px;
    }}
    .tag {{
        display: inline-block;
        padding: 10px 24px;
        background: {primary}15;
        color: {primary};
        font-weight: 700;
        border-radius: 100px;
        margin-bottom: 20px;
    }}
    .masonry-header h2 {{
        font-family: 'Rajdhani', sans-serif;
        font-size: clamp(2.5rem, 5vw, 4rem);
        font-weight: 800;
        color: {text};
    }}
    .masonry-grid {{
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        grid-auto-rows: 180px;
        gap: 24px;
    }}
    .masonry-news {{
        position: relative;
        border-radius: 20px;
        overflow: hidden;
        cursor: pointer;
    }}
    .masonry-news.tall {{
        grid-row: span 2;
    }}
    .masonry-news img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.5s ease;
    }}
    .masonry-news:hover img {{
        transform: scale(1.1);
    }}
    .news-overlay {{
        position: absolute;
        inset: 0;
        background: linear-gradient(to top, {background}E6, transparent 50%);
        padding: 24px;
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
    }}
    .news-cat {{
        display: inline-block;
        padding: 5px 12px;
        background: {primary};
        color: {background};
        font-size: 0.75rem;
        font-weight: 700;
        border-radius: 100px;
        margin-bottom: 8px;
        width: fit-content;
    }}
    .news-overlay h3 {{
        font-size: 1.2rem;
        font-weight: 700;
        color: {text};
    }}
    @media (max-width: 900px) {{
        .masonry-grid {{ grid-template-columns: repeat(2, 1fr); }}
    }}
    @media (max-width: 600px) {{
        .masonry-grid {{ grid-template-columns: 1fr; }}
        .masonry-news.tall {{ grid-row: span 1; }}
    }}
    </style>
    '''
