from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Magazine Layout - Editorial style with large images"""
    title = props.get("title", "Gaming Magazine")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="gaming-news-magazine" id="news">
        <div class="magazine-container">
            <div class="magazine-header">
                <h2>{title}</h2>
                <div class="category-tabs">
                    <button class="tab active">All</button>
                    <button class="tab">Updates</button>
                    <button class="tab">Esports</button>
                    <button class="tab">Community</button>
                </div>
            </div>
            <div class="magazine-grid">
                <article class="mag-article main">
                    <img src="https://images.unsplash.com/photo-1542751371-adc38448a05e?w=1200" alt="News">
                    <div class="mag-overlay">
                        <span class="mag-cat">Featured</span>
                        <h3>The Future of Competitive Gaming: 2025 Preview</h3>
                        <div class="mag-meta">
                            <span>By GameZone Editorial</span>
                            <span>•</span>
                            <span>5 min read</span>
                        </div>
                    </div>
                </article>
                <article class="mag-article">
                    <img src="https://images.unsplash.com/photo-1538481199705-c710c4e965fc?w=600" alt="News">
                    <div class="mag-overlay small">
                        <span class="mag-cat">Esports</span>
                        <h4>Pro League Season 8 Kicks Off</h4>
                    </div>
                </article>
                <article class="mag-article">
                    <img src="https://images.unsplash.com/photo-1511512578047-dfb367046420?w=600" alt="News">
                    <div class="mag-overlay small">
                        <span class="mag-cat">Update</span>
                        <h4>New Night Map Revealed</h4>
                    </div>
                </article>
                <article class="mag-article wide">
                    <img src="https://images.unsplash.com/photo-1493711662062-fa541f7f069d?w=900" alt="News">
                    <div class="mag-overlay small">
                        <span class="mag-cat">Interview</span>
                        <h4>Exclusive: World Champion Shares Secrets</h4>
                    </div>
                </article>
            </div>
        </div>
    </section>
    
    <style>
    .gaming-news-magazine {{
        padding: 120px 24px;
        background: {background};
    }}
    .magazine-container {{
        max-width: 1200px;
        margin: 0 auto;
    }}
    .magazine-header {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 48px;
        flex-wrap: wrap;
        gap: 24px;
    }}
    .magazine-header h2 {{
        font-family: 'Rajdhani', sans-serif;
        font-size: 2.5rem;
        font-weight: 800;
        color: {text};
    }}
    .category-tabs {{
        display: flex;
        gap: 8px;
    }}
    .tab {{
        padding: 10px 24px;
        background: {text}08;
        border: none;
        color: {secondary};
        font-weight: 600;
        border-radius: 100px;
        cursor: pointer;
        transition: all 0.3s ease;
    }}
    .tab.active, .tab:hover {{
        background: {primary};
        color: {background};
    }}
    .magazine-grid {{
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        grid-template-rows: repeat(2, 250px);
        gap: 24px;
    }}
    .mag-article {{
        position: relative;
        border-radius: 20px;
        overflow: hidden;
        cursor: pointer;
    }}
    .mag-article.main {{
        grid-column: span 2;
        grid-row: span 2;
    }}
    .mag-article.wide {{
        grid-column: span 2;
    }}
    .mag-article img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.5s ease;
    }}
    .mag-article:hover img {{
        transform: scale(1.1);
    }}
    .mag-overlay {{
        position: absolute;
        inset: 0;
        background: linear-gradient(to top, {background}E6, transparent 50%);
        padding: 32px;
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
    }}
    .mag-overlay.small {{
        padding: 20px;
    }}
    .mag-cat {{
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
    .mag-overlay h3 {{
        font-size: 2rem;
        font-weight: 800;
        color: {text};
        margin-bottom: 12px;
    }}
    .mag-overlay h4 {{
        font-size: 1.1rem;
        font-weight: 700;
        color: {text};
    }}
    .mag-meta {{
        display: flex;
        gap: 12px;
        color: {secondary};
        font-size: 0.9rem;
    }}
    @media (max-width: 900px) {{
        .magazine-grid {{ grid-template-columns: 1fr 1fr; }}
        .mag-article.main {{ grid-column: span 2; grid-row: span 1; }}
        .mag-article.wide {{ grid-column: span 2; }}
    }}
    </style>
    '''
