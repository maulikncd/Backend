from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Horizontal Scroll - Scrollable news cards"""
    title = props.get("title", "Trending Now")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    news = [
        {"img": "https://images.unsplash.com/photo-1542751371-adc38448a05e?w=600", "cat": "Featured", "title": "Season 5 Launch Event", "time": "2h ago"},
        {"img": "https://images.unsplash.com/photo-1538481199705-c710c4e965fc?w=600", "cat": "Esports", "title": "Championship Bracket Revealed", "time": "5h ago"},
        {"img": "https://images.unsplash.com/photo-1511512578047-dfb367046420?w=600", "cat": "Update", "title": "New Character Teased", "time": "1d ago"},
        {"img": "https://images.unsplash.com/photo-1493711662062-fa541f7f069d?w=600", "cat": "Guide", "title": "Pro Tips for Beginners", "time": "2d ago"},
        {"img": "https://images.unsplash.com/photo-1542751110-97427bbecf20?w=600", "cat": "Community", "title": "Fan Art Contest Winners", "time": "3d ago"},
    ]
    
    cards_html = ""
    for item in news:
        cards_html += f'''
        <article class="scroll-card">
            <img src="{item['img']}" alt="{item['title']}">
            <div class="card-overlay">
                <span class="card-cat">{item['cat']}</span>
                <h3>{item['title']}</h3>
                <span class="card-time">{item['time']}</span>
            </div>
        </article>
        '''
    
    return f'''
    <section class="gaming-news-scroll" id="news">
        <div class="scroll-header">
            <h2>{title}</h2>
            <div class="scroll-arrows">
                <button class="arrow-btn">←</button>
                <button class="arrow-btn">→</button>
            </div>
        </div>
        <div class="scroll-track">
            {cards_html}
        </div>
    </section>
    
    <style>
    .gaming-news-scroll {{
        padding: 120px 0;
        background: {background};
    }}
    .scroll-header {{
        max-width: 1400px;
        margin: 0 auto 40px;
        padding: 0 24px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }}
    .scroll-header h2 {{
        font-family: 'Rajdhani', sans-serif;
        font-size: 2.5rem;
        font-weight: 800;
        color: {text};
    }}
    .scroll-arrows {{
        display: flex;
        gap: 12px;
    }}
    .arrow-btn {{
        width: 48px;
        height: 48px;
        background: {text}08;
        border: none;
        border-radius: 50%;
        color: {text};
        font-size: 1.2rem;
        cursor: pointer;
        transition: all 0.3s ease;
    }}
    .arrow-btn:hover {{
        background: {primary};
        color: {background};
    }}
    .scroll-track {{
        display: flex;
        gap: 24px;
        overflow-x: auto;
        padding: 0 24px 20px;
        scroll-snap-type: x mandatory;
        scrollbar-width: none;
    }}
    .scroll-track::-webkit-scrollbar {{
        display: none;
    }}
    .scroll-card {{
        flex-shrink: 0;
        width: 350px;
        aspect-ratio: 4/5;
        position: relative;
        border-radius: 24px;
        overflow: hidden;
        scroll-snap-align: start;
        cursor: pointer;
    }}
    .scroll-card img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.5s ease;
    }}
    .scroll-card:hover img {{
        transform: scale(1.1);
    }}
    .card-overlay {{
        position: absolute;
        inset: 0;
        background: linear-gradient(to top, {background}E6, transparent 50%);
        padding: 32px;
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
    }}
    .card-cat {{
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
    .card-overlay h3 {{
        font-size: 1.5rem;
        font-weight: 800;
        color: {text};
        margin-bottom: 8px;
    }}
    .card-time {{
        color: {secondary};
        font-size: 0.9rem;
    }}
    </style>
    '''
