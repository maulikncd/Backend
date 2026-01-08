from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Bento Games - Modern bento grid for games"""
    title = props.get("title", "Popular Games")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="gaming-games-bento" id="games">
        <div class="bento-container">
            <div class="bento-header">
                <span class="section-tag">🔥 Popular</span>
                <h2>{title}</h2>
            </div>
            <div class="games-bento-grid">
                <div class="bento-game main">
                    <img src="https://images.unsplash.com/photo-1542751371-adc38448a05e?w=1200" alt="Main Game">
                    <div class="game-overlay">
                        <span class="live-badge">🔴 LIVE</span>
                        <h3>Cyber Warriors</h3>
                        <p>10M+ Players Online</p>
                        <a href="#" class="btn-bento">Play Now</a>
                    </div>
                </div>
                <div class="bento-game">
                    <img src="https://images.unsplash.com/photo-1538481199705-c710c4e965fc?w=600" alt="Game">
                    <div class="game-overlay small">
                        <h4>Speed Legends</h4>
                        <span>Racing</span>
                    </div>
                </div>
                <div class="bento-game">
                    <img src="https://images.unsplash.com/photo-1511512578047-dfb367046420?w=600" alt="Game">
                    <div class="game-overlay small">
                        <h4>Shadow Quest</h4>
                        <span>RPG</span>
                    </div>
                </div>
                <div class="bento-game wide">
                    <img src="https://images.unsplash.com/photo-1493711662062-fa541f7f069d?w=900" alt="Game">
                    <div class="game-overlay small">
                        <h4>Arena Masters</h4>
                        <span>MOBA • 15M Players</span>
                    </div>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    .gaming-games-bento {{
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
    .section-tag {{
        display: inline-block;
        padding: 10px 24px;
        background: {primary}15;
        color: {primary};
        font-weight: 700;
        font-size: 0.85rem;
        border-radius: 100px;
        margin-bottom: 20px;
    }}
    .bento-header h2 {{
        font-family: 'Rajdhani', sans-serif;
        font-size: clamp(2.5rem, 5vw, 4rem);
        font-weight: 800;
        color: {text};
    }}
    .games-bento-grid {{
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        grid-template-rows: repeat(2, 250px);
        gap: 24px;
    }}
    .bento-game {{
        position: relative;
        border-radius: 24px;
        overflow: hidden;
    }}
    .bento-game.main {{
        grid-column: span 2;
        grid-row: span 2;
    }}
    .bento-game.wide {{
        grid-column: span 2;
    }}
    .bento-game img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.5s ease;
    }}
    .bento-game:hover img {{
        transform: scale(1.1);
    }}
    .game-overlay {{
        position: absolute;
        inset: 0;
        background: linear-gradient(to top, {background}E6, transparent 50%);
        padding: 32px;
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
    }}
    .game-overlay.small {{
        padding: 20px;
    }}
    .live-badge {{
        display: inline-block;
        padding: 6px 14px;
        background: #ff3b3b;
        color: #fff;
        font-size: 0.8rem;
        font-weight: 700;
        border-radius: 100px;
        margin-bottom: 16px;
        width: fit-content;
        animation: pulse 2s infinite;
    }}
    @keyframes pulse {{
        0%, 100% {{ opacity: 1; }}
        50% {{ opacity: 0.7; }}
    }}
    .game-overlay h3 {{
        font-size: 2.5rem;
        font-weight: 800;
        color: {text};
        margin-bottom: 8px;
    }}
    .game-overlay h4 {{
        font-size: 1.2rem;
        font-weight: 700;
        color: {text};
        margin-bottom: 4px;
    }}
    .game-overlay p, .game-overlay span {{
        color: {secondary};
    }}
    .btn-bento {{
        display: inline-block;
        padding: 14px 32px;
        background: {primary};
        color: {background};
        text-decoration: none;
        font-weight: 700;
        border-radius: 10px;
        margin-top: 20px;
        width: fit-content;
        transition: all 0.3s ease;
    }}
    .btn-bento:hover {{
        transform: scale(1.05);
        box-shadow: 0 15px 40px {primary}40;
    }}
    @media (max-width: 900px) {{
        .games-bento-grid {{ grid-template-columns: 1fr 1fr; }}
        .bento-game.main {{ grid-column: span 2; grid-row: span 1; }}
        .bento-game.wide {{ grid-column: span 2; }}
    }}
    </style>
    '''
