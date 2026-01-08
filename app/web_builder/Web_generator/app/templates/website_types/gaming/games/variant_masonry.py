from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Masonry Layout - Pinterest-style game cards"""
    title = props.get("title", "Explore Games")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    games = [
        {"name": "Cyber Warriors", "cat": "Battle Royale", "img": "https://images.unsplash.com/photo-1542751371-adc38448a05e?w=500", "tall": True},
        {"name": "Speed Legends", "cat": "Racing", "img": "https://images.unsplash.com/photo-1538481199705-c710c4e965fc?w=500", "tall": False},
        {"name": "Shadow Quest", "cat": "RPG", "img": "https://images.unsplash.com/photo-1511512578047-dfb367046420?w=500", "tall": False},
        {"name": "Arena Masters", "cat": "MOBA", "img": "https://images.unsplash.com/photo-1493711662062-fa541f7f069d?w=500", "tall": True},
        {"name": "Tactical Ops", "cat": "FPS", "img": "https://images.unsplash.com/photo-1542751110-97427bbecf20?w=500", "tall": False},
        {"name": "Empire Builder", "cat": "Strategy", "img": "https://images.unsplash.com/photo-1612287230202-1ff1d85d1bdf?w=500", "tall": False},
    ]
    
    cards_html = ""
    for game in games:
        tall_class = "tall" if game["tall"] else ""
        cards_html += f'''
        <div class="masonry-game {tall_class}">
            <img src="{game['img']}" alt="{game['name']}">
            <div class="game-info">
                <span class="cat">{game['cat']}</span>
                <h3>{game['name']}</h3>
            </div>
        </div>
        '''
    
    return f'''
    <section class="gaming-games-masonry" id="games">
        <div class="masonry-container">
            <div class="masonry-header">
                <span class="tag">🎮 Games</span>
                <h2>{title}</h2>
            </div>
            <div class="masonry-grid">
                {cards_html}
            </div>
        </div>
    </section>
    
    <style>
    .gaming-games-masonry {{
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
        font-size: 0.85rem;
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
    .masonry-game {{
        position: relative;
        border-radius: 20px;
        overflow: hidden;
        cursor: pointer;
    }}
    .masonry-game.tall {{
        grid-row: span 2;
    }}
    .masonry-game img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.5s ease;
    }}
    .masonry-game:hover img {{
        transform: scale(1.1);
    }}
    .game-info {{
        position: absolute;
        inset: 0;
        background: linear-gradient(to top, {background}E6, transparent 60%);
        padding: 24px;
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
        opacity: 0;
        transition: opacity 0.3s ease;
    }}
    .masonry-game:hover .game-info {{
        opacity: 1;
    }}
    .cat {{
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
    .game-info h3 {{
        font-size: 1.3rem;
        font-weight: 700;
        color: {text};
    }}
    @media (max-width: 900px) {{
        .masonry-grid {{ grid-template-columns: repeat(2, 1fr); }}
    }}
    @media (max-width: 600px) {{
        .masonry-grid {{ grid-template-columns: 1fr; }}
        .masonry-game.tall {{ grid-row: span 1; }}
    }}
    </style>
    '''
