from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """List View - Detailed list with game info"""
    title = props.get("title", "All Games")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    games = [
        {"name": "Cyber Warriors", "cat": "Battle Royale", "img": "https://images.unsplash.com/photo-1542751371-adc38448a05e?w=300", "players": "10M+", "rating": "4.9"},
        {"name": "Speed Legends", "cat": "Racing", "img": "https://images.unsplash.com/photo-1538481199705-c710c4e965fc?w=300", "players": "5M+", "rating": "4.7"},
        {"name": "Shadow Quest", "cat": "RPG", "img": "https://images.unsplash.com/photo-1511512578047-dfb367046420?w=300", "players": "8M+", "rating": "4.8"},
        {"name": "Arena Masters", "cat": "MOBA", "img": "https://images.unsplash.com/photo-1493711662062-fa541f7f069d?w=300", "players": "15M+", "rating": "4.6"},
    ]
    
    rows_html = ""
    for i, game in enumerate(games):
        rows_html += f'''
        <div class="game-list-item">
            <span class="rank">#{i+1}</span>
            <img src="{game['img']}" alt="{game['name']}">
            <div class="item-info">
                <h3>{game['name']}</h3>
                <span class="item-cat">{game['cat']}</span>
            </div>
            <div class="item-stats">
                <div class="stat">
                    <span class="val">{game['players']}</span>
                    <span class="lbl">Players</span>
                </div>
                <div class="stat">
                    <span class="val">⭐ {game['rating']}</span>
                    <span class="lbl">Rating</span>
                </div>
            </div>
            <a href="#" class="item-btn">Play</a>
        </div>
        '''
    
    return f'''
    <section class="gaming-games-list" id="games">
        <div class="list-container">
            <div class="list-header">
                <h2>{title}</h2>
                <div class="sort-options">
                    <span>Sort by:</span>
                    <select>
                        <option>Most Popular</option>
                        <option>Top Rated</option>
                        <option>Newest</option>
                    </select>
                </div>
            </div>
            <div class="games-list">
                {rows_html}
            </div>
        </div>
    </section>
    
    <style>
    .gaming-games-list {{
        padding: 120px 24px;
        background: {background};
    }}
    .list-container {{
        max-width: 1000px;
        margin: 0 auto;
    }}
    .list-header {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 40px;
        flex-wrap: wrap;
        gap: 20px;
    }}
    .list-header h2 {{
        font-family: 'Rajdhani', sans-serif;
        font-size: clamp(2rem, 4vw, 3rem);
        font-weight: 800;
        color: {text};
    }}
    .sort-options {{
        display: flex;
        align-items: center;
        gap: 12px;
        color: {secondary};
    }}
    .sort-options select {{
        padding: 10px 20px;
        background: {text}08;
        border: 1px solid {text}15;
        color: {text};
        border-radius: 8px;
        font-size: 0.95rem;
    }}
    .games-list {{
        display: flex;
        flex-direction: column;
        gap: 16px;
    }}
    .game-list-item {{
        display: flex;
        align-items: center;
        gap: 24px;
        padding: 20px 24px;
        background: {text}05;
        border-radius: 16px;
        transition: all 0.3s ease;
    }}
    .game-list-item:hover {{
        background: {primary}10;
        transform: translateX(8px);
    }}
    .rank {{
        font-family: 'Orbitron', sans-serif;
        font-size: 1.2rem;
        font-weight: 700;
        color: {primary};
        min-width: 50px;
    }}
    .game-list-item img {{
        width: 80px;
        height: 60px;
        object-fit: cover;
        border-radius: 10px;
    }}
    .item-info {{
        flex: 1;
    }}
    .item-info h3 {{
        font-size: 1.2rem;
        font-weight: 700;
        color: {text};
        margin-bottom: 4px;
    }}
    .item-cat {{
        font-size: 0.9rem;
        color: {secondary};
    }}
    .item-stats {{
        display: flex;
        gap: 32px;
    }}
    .stat {{
        text-align: center;
    }}
    .stat .val {{
        display: block;
        font-weight: 700;
        color: {text};
    }}
    .stat .lbl {{
        font-size: 0.8rem;
        color: {secondary};
    }}
    .item-btn {{
        padding: 12px 28px;
        background: {primary};
        color: {background};
        text-decoration: none;
        font-weight: 700;
        border-radius: 10px;
        transition: all 0.3s ease;
    }}
    .item-btn:hover {{
        transform: scale(1.05);
        box-shadow: 0 10px 30px {primary}40;
    }}
    @media (max-width: 768px) {{
        .game-list-item {{ flex-wrap: wrap; }}
        .item-stats {{ width: 100%; justify-content: space-around; margin: 12px 0; }}
        .item-btn {{ width: 100%; text-align: center; }}
    }}
    </style>
    '''
