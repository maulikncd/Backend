from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """3D Cards - Hover tilt effect game cards"""
    title = props.get("title", "Featured Games")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    games = [
        {"name": "Cyber Warriors", "cat": "Battle Royale", "img": "https://images.unsplash.com/photo-1542751371-adc38448a05e?w=500"},
        {"name": "Speed Legends", "cat": "Racing", "img": "https://images.unsplash.com/photo-1538481199705-c710c4e965fc?w=500"},
        {"name": "Shadow Quest", "cat": "RPG", "img": "https://images.unsplash.com/photo-1511512578047-dfb367046420?w=500"},
        {"name": "Arena Masters", "cat": "MOBA", "img": "https://images.unsplash.com/photo-1493711662062-fa541f7f069d?w=500"},
    ]
    
    cards_html = ""
    for game in games:
        cards_html += f'''
        <div class="game-3d-card">
            <div class="card-inner">
                <img src="{game['img']}" alt="{game['name']}">
                <div class="card-shine"></div>
                <div class="card-content">
                    <span class="cat">{game['cat']}</span>
                    <h3>{game['name']}</h3>
                    <a href="#">Play Now →</a>
                </div>
            </div>
        </div>
        '''
    
    return f'''
    <section class="gaming-games-3d" id="games">
        <div class="cards-container">
            <div class="cards-header">
                <h2>{title}</h2>
                <p>Hover for 3D effect</p>
            </div>
            <div class="cards-3d-grid">
                {cards_html}
            </div>
        </div>
    </section>
    
    <style>
    .gaming-games-3d {{
        padding: 120px 24px;
        background: {background};
        perspective: 1000px;
    }}
    .cards-container {{
        max-width: 1200px;
        margin: 0 auto;
    }}
    .cards-header {{
        text-align: center;
        margin-bottom: 60px;
    }}
    .cards-header h2 {{
        font-family: 'Rajdhani', sans-serif;
        font-size: clamp(2.5rem, 5vw, 4rem);
        font-weight: 800;
        color: {text};
        margin-bottom: 8px;
    }}
    .cards-header p {{
        color: {secondary};
    }}
    .cards-3d-grid {{
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 32px;
    }}
    .game-3d-card {{
        perspective: 1000px;
    }}
    .card-inner {{
        position: relative;
        border-radius: 20px;
        overflow: hidden;
        aspect-ratio: 3/4;
        transform-style: preserve-3d;
        transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
    }}
    .game-3d-card:hover .card-inner {{
        transform: rotateY(-10deg) rotateX(5deg);
    }}
    .card-inner img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
    }}
    .card-shine {{
        position: absolute;
        inset: 0;
        background: linear-gradient(135deg, transparent 40%, {primary}15 50%, transparent 60%);
        opacity: 0;
        transition: opacity 0.4s ease;
    }}
    .game-3d-card:hover .card-shine {{
        opacity: 1;
    }}
    .card-content {{
        position: absolute;
        inset: 0;
        background: linear-gradient(to top, {background}E6, transparent 60%);
        padding: 24px;
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
    }}
    .cat {{
        display: inline-block;
        padding: 5px 12px;
        background: {primary}30;
        color: {primary};
        font-size: 0.75rem;
        font-weight: 700;
        border-radius: 100px;
        margin-bottom: 8px;
        width: fit-content;
    }}
    .card-content h3 {{
        font-size: 1.3rem;
        font-weight: 700;
        color: {text};
        margin-bottom: 12px;
    }}
    .card-content a {{
        color: {primary};
        text-decoration: none;
        font-weight: 600;
        font-size: 0.9rem;
    }}
    @media (max-width: 900px) {{
        .cards-3d-grid {{ grid-template-columns: repeat(2, 1fr); }}
    }}
    @media (max-width: 500px) {{
        .cards-3d-grid {{ grid-template-columns: 1fr; }}
    }}
    </style>
    '''
