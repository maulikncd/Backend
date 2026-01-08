from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Horizontal Scroll - Netflix-style horizontal game rows"""
    title = props.get("title", "Discover Games")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    categories = [
        {"name": "Trending Now", "games": [
            {"name": "Cyber Warriors", "img": "https://images.unsplash.com/photo-1542751371-adc38448a05e?w=400"},
            {"name": "Speed Legends", "img": "https://images.unsplash.com/photo-1538481199705-c710c4e965fc?w=400"},
            {"name": "Shadow Quest", "img": "https://images.unsplash.com/photo-1511512578047-dfb367046420?w=400"},
            {"name": "Arena Masters", "img": "https://images.unsplash.com/photo-1493711662062-fa541f7f069d?w=400"},
            {"name": "Tactical Ops", "img": "https://images.unsplash.com/photo-1542751110-97427bbecf20?w=400"},
        ]},
        {"name": "New Releases", "games": [
            {"name": "Empire Builder", "img": "https://images.unsplash.com/photo-1612287230202-1ff1d85d1bdf?w=400"},
            {"name": "Neon Drift", "img": "https://images.unsplash.com/photo-1493711662062-fa541f7f069d?w=400"},
            {"name": "Dark Legends", "img": "https://images.unsplash.com/photo-1542751371-adc38448a05e?w=400"},
            {"name": "Storm Raiders", "img": "https://images.unsplash.com/photo-1538481199705-c710c4e965fc?w=400"},
            {"name": "Galaxy Wars", "img": "https://images.unsplash.com/photo-1511512578047-dfb367046420?w=400"},
        ]}
    ]
    
    rows_html = ""
    for cat in categories:
        games_html = ""
        for game in cat["games"]:
            games_html += f'''
            <div class="scroll-game-card">
                <img src="{game['img']}" alt="{game['name']}">
                <div class="game-hover">
                    <h4>{game['name']}</h4>
                    <a href="#">Play</a>
                </div>
            </div>
            '''
        rows_html += f'''
        <div class="game-row">
            <div class="row-header">
                <h3>{cat['name']}</h3>
                <a href="#" class="see-all">See All →</a>
            </div>
            <div class="row-scroll">
                {games_html}
            </div>
        </div>
        '''
    
    return f'''
    <section class="gaming-games-scroll" id="games">
        <div class="scroll-container">
            <div class="scroll-header">
                <h2>{title}</h2>
            </div>
            {rows_html}
        </div>
    </section>
    
    <style>
    .gaming-games-scroll {{
        padding: 120px 0;
        background: {background};
    }}
    .scroll-container {{
        max-width: 100%;
    }}
    .scroll-header {{
        max-width: 1400px;
        margin: 0 auto 60px;
        padding: 0 24px;
    }}
    .scroll-header h2 {{
        font-family: 'Rajdhani', sans-serif;
        font-size: clamp(2.5rem, 5vw, 4rem);
        font-weight: 800;
        color: {text};
    }}
    .game-row {{
        margin-bottom: 48px;
    }}
    .row-header {{
        max-width: 1400px;
        margin: 0 auto 24px;
        padding: 0 24px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }}
    .row-header h3 {{
        font-size: 1.5rem;
        font-weight: 700;
        color: {text};
    }}
    .see-all {{
        color: {primary};
        text-decoration: none;
        font-weight: 600;
    }}
    .row-scroll {{
        display: flex;
        gap: 24px;
        overflow-x: auto;
        padding: 0 24px 20px;
        scroll-snap-type: x mandatory;
        -webkit-overflow-scrolling: touch;
        scrollbar-width: none;
    }}
    .row-scroll::-webkit-scrollbar {{
        display: none;
    }}
    .scroll-game-card {{
        flex-shrink: 0;
        width: 280px;
        aspect-ratio: 16/10;
        border-radius: 16px;
        overflow: hidden;
        position: relative;
        scroll-snap-align: start;
        cursor: pointer;
    }}
    .scroll-game-card img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.5s ease;
    }}
    .scroll-game-card:hover img {{
        transform: scale(1.1);
    }}
    .game-hover {{
        position: absolute;
        inset: 0;
        background: linear-gradient(to top, {background}E6, transparent 60%);
        padding: 20px;
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
        opacity: 0;
        transition: opacity 0.3s ease;
    }}
    .scroll-game-card:hover .game-hover {{
        opacity: 1;
    }}
    .game-hover h4 {{
        font-size: 1.1rem;
        font-weight: 700;
        color: {text};
        margin-bottom: 8px;
    }}
    .game-hover a {{
        display: inline-block;
        padding: 8px 20px;
        background: {primary};
        color: {background};
        text-decoration: none;
        border-radius: 8px;
        font-weight: 600;
        font-size: 0.9rem;
        width: fit-content;
    }}
    </style>
    '''
