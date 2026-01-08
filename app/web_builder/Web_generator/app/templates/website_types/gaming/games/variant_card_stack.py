from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Card Stack - Stacked cards with category filters"""
    title = props.get("title", "Game Library")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    games = [
        {"name": "Cyber Warriors", "cat": "Battle Royale", "img": "https://images.unsplash.com/photo-1542751371-adc38448a05e?w=500", "players": "10M+"},
        {"name": "Speed Legends", "cat": "Racing", "img": "https://images.unsplash.com/photo-1538481199705-c710c4e965fc?w=500", "players": "5M+"},
        {"name": "Shadow Quest", "cat": "RPG", "img": "https://images.unsplash.com/photo-1511512578047-dfb367046420?w=500", "players": "8M+"},
        {"name": "Arena Masters", "cat": "MOBA", "img": "https://images.unsplash.com/photo-1493711662062-fa541f7f069d?w=500", "players": "15M+"},
        {"name": "Tactical Ops", "cat": "FPS", "img": "https://images.unsplash.com/photo-1542751110-97427bbecf20?w=500", "players": "12M+"},
        {"name": "Empire Builder", "cat": "Strategy", "img": "https://images.unsplash.com/photo-1612287230202-1ff1d85d1bdf?w=500", "players": "3M+"},
    ]
    
    cards_html = ""
    for game in games:
        cards_html += f'''
        <div class="game-card-stack">
            <div class="card-image">
                <img src="{game['img']}" alt="{game['name']}">
                <div class="card-overlay"></div>
            </div>
            <div class="card-body">
                <span class="game-category">{game['cat']}</span>
                <h3>{game['name']}</h3>
                <div class="card-footer">
                    <span class="players">👥 {game['players']} Players</span>
                    <a href="#" class="play-link">Play →</a>
                </div>
            </div>
        </div>
        '''
    
    return f'''
    <section class="gaming-games-stack" id="games">
        <div class="stack-container">
            <div class="stack-header">
                <h2>{title}</h2>
                <div class="category-filters">
                    <button class="filter-btn active">All</button>
                    <button class="filter-btn">Battle Royale</button>
                    <button class="filter-btn">RPG</button>
                    <button class="filter-btn">FPS</button>
                    <button class="filter-btn">Racing</button>
                </div>
            </div>
            <div class="cards-grid">
                {cards_html}
            </div>
        </div>
    </section>
    
    <style>
    .gaming-games-stack {{
        padding: 120px 24px;
        background: {background};
    }}
    .stack-container {{
        max-width: 1200px;
        margin: 0 auto;
    }}
    .stack-header {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 60px;
        flex-wrap: wrap;
        gap: 24px;
    }}
    .stack-header h2 {{
        font-family: 'Rajdhani', sans-serif;
        font-size: clamp(2rem, 4vw, 3rem);
        font-weight: 800;
        color: {text};
    }}
    .category-filters {{
        display: flex;
        gap: 12px;
        flex-wrap: wrap;
    }}
    .filter-btn {{
        padding: 10px 24px;
        background: {text}08;
        border: 1px solid transparent;
        color: {secondary};
        font-weight: 600;
        border-radius: 100px;
        cursor: pointer;
        transition: all 0.3s ease;
    }}
    .filter-btn:hover, .filter-btn.active {{
        background: {primary}15;
        border-color: {primary}40;
        color: {primary};
    }}
    .cards-grid {{
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 32px;
    }}
    .game-card-stack {{
        background: {text}05;
        border-radius: 20px;
        overflow: hidden;
        transition: all 0.4s ease;
    }}
    .game-card-stack:hover {{
        transform: translateY(-12px);
        box-shadow: 0 30px 60px {primary}15;
    }}
    .card-image {{
        position: relative;
        aspect-ratio: 16/10;
    }}
    .card-image img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
    }}
    .card-overlay {{
        position: absolute;
        inset: 0;
        background: linear-gradient(to top, {background}, transparent 50%);
    }}
    .card-body {{
        padding: 24px;
        margin-top: -40px;
        position: relative;
    }}
    .game-category {{
        display: inline-block;
        padding: 6px 14px;
        background: {primary}20;
        color: {primary};
        font-size: 0.8rem;
        font-weight: 700;
        border-radius: 100px;
        margin-bottom: 12px;
    }}
    .card-body h3 {{
        font-size: 1.4rem;
        font-weight: 800;
        color: {text};
        margin-bottom: 16px;
    }}
    .card-footer {{
        display: flex;
        justify-content: space-between;
        align-items: center;
    }}
    .players {{
        font-size: 0.9rem;
        color: {secondary};
    }}
    .play-link {{
        color: {primary};
        text-decoration: none;
        font-weight: 600;
        transition: transform 0.3s ease;
    }}
    .play-link:hover {{
        transform: translateX(4px);
    }}
    @media (max-width: 900px) {{
        .cards-grid {{ grid-template-columns: repeat(2, 1fr); }}
    }}
    @media (max-width: 600px) {{
        .cards-grid {{ grid-template-columns: 1fr; }}
        .stack-header {{ flex-direction: column; text-align: center; }}
    }}
    </style>
    '''
