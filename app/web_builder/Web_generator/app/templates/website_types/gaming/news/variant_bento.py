from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Bento News - Modern bento grid layout"""
    title = props.get("title", "Latest Updates")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="gaming-news-bento" id="news">
        <div class="bento-container">
            <div class="bento-header">
                <span class="tag">📰 News</span>
                <h2>{title}</h2>
            </div>
            <div class="news-bento-grid">
                <article class="bento-news main">
                    <img src="https://images.unsplash.com/photo-1542751371-adc38448a05e?w=1200" alt="Featured">
                    <div class="bento-overlay">
                        <span class="cat">Featured</span>
                        <h3>Season 5: Everything You Need to Know</h3>
                        <p>Complete guide to all new features</p>
                    </div>
                </article>
                <article class="bento-news">
                    <img src="https://images.unsplash.com/photo-1538481199705-c710c4e965fc?w=600" alt="News">
                    <div class="bento-overlay small">
                        <span class="cat">Esports</span>
                        <h4>Finals Schedule</h4>
                    </div>
                </article>
                <article class="bento-news">
                    <img src="https://images.unsplash.com/photo-1511512578047-dfb367046420?w=600" alt="News">
                    <div class="bento-overlay small">
                        <span class="cat">Update</span>
                        <h4>Patch Notes 5.2</h4>
                    </div>
                </article>
                <article class="bento-news wide">
                    <img src="https://images.unsplash.com/photo-1493711662062-fa541f7f069d?w=900" alt="News">
                    <div class="bento-overlay small">
                        <span class="cat">Interview</span>
                        <h4>Champion's Journey: From Amateur to Pro</h4>
                    </div>
                </article>
            </div>
        </div>
    </section>
    
    <style>
    .gaming-news-bento {{
        padding: 120px 24px;
        background: {background};
    }}
    .bento-container {{
        max-width: 1200px;
        margin: 0 auto;
    }}
    .bento-header {{
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
    .bento-header h2 {{
        font-family: 'Rajdhani', sans-serif;
        font-size: clamp(2.5rem, 5vw, 4rem);
        font-weight: 800;
        color: {text};
    }}
    .news-bento-grid {{
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        grid-template-rows: repeat(2, 250px);
        gap: 24px;
    }}
    .bento-news {{
        position: relative;
        border-radius: 24px;
        overflow: hidden;
        cursor: pointer;
    }}
    .bento-news.main {{
        grid-column: span 2;
        grid-row: span 2;
    }}
    .bento-news.wide {{
        grid-column: span 2;
    }}
    .bento-news img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.5s ease;
    }}
    .bento-news:hover img {{
        transform: scale(1.1);
    }}
    .bento-overlay {{
        position: absolute;
        inset: 0;
        background: linear-gradient(to top, {background}E6, transparent 50%);
        padding: 32px;
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
    }}
    .bento-overlay.small {{
        padding: 20px;
    }}
    .cat {{
        display: inline-block;
        padding: 5px 14px;
        background: {primary};
        color: {background};
        font-size: 0.75rem;
        font-weight: 700;
        border-radius: 100px;
        margin-bottom: 12px;
        width: fit-content;
    }}
    .bento-overlay h3 {{
        font-size: 2rem;
        font-weight: 800;
        color: {text};
        margin-bottom: 8px;
    }}
    .bento-overlay h4 {{
        font-size: 1.2rem;
        font-weight: 700;
        color: {text};
    }}
    .bento-overlay p {{
        color: {secondary};
    }}
    @media (max-width: 900px) {{
        .news-bento-grid {{ grid-template-columns: 1fr 1fr; }}
        .bento-news.main {{ grid-column: span 2; grid-row: span 1; }}
        .bento-news.wide {{ grid-column: span 2; }}
    }}
    </style>
    '''
