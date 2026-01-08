from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Featured Hero - Large hero card with featured game"""
    title = props.get("title", "Featured Games")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="gaming-games-hero" id="games">
        <div class="games-container">
            <div class="section-header">
                <span class="section-tag">🎮 Our Games</span>
                <h2>{title}</h2>
            </div>
            <div class="games-layout">
                <div class="featured-game">
                    <img src="https://images.unsplash.com/photo-1542751371-adc38448a05e?w=1200" alt="Featured Game">
                    <div class="featured-overlay">
                        <span class="game-badge">Featured</span>
                        <h3>Cyber Warriors</h3>
                        <p>The ultimate battle royale experience</p>
                        <div class="game-meta">
                            <span>👥 10M+ Players</span>
                            <span>⭐ 4.9 Rating</span>
                        </div>
                        <a href="#" class="btn-play">Play Now</a>
                    </div>
                </div>
                <div class="games-sidebar">
                    <div class="sidebar-game">
                        <img src="https://images.unsplash.com/photo-1538481199705-c710c4e965fc?w=400" alt="Game">
                        <div class="sidebar-info">
                            <h4>Speed Legends</h4>
                            <span>Racing • 5M Players</span>
                        </div>
                    </div>
                    <div class="sidebar-game">
                        <img src="https://images.unsplash.com/photo-1511512578047-dfb367046420?w=400" alt="Game">
                        <div class="sidebar-info">
                            <h4>Shadow Quest</h4>
                            <span>RPG • 8M Players</span>
                        </div>
                    </div>
                    <div class="sidebar-game">
                        <img src="https://images.unsplash.com/photo-1493711662062-fa541f7f069d?w=400" alt="Game">
                        <div class="sidebar-info">
                            <h4>Arena Masters</h4>
                            <span>MOBA • 15M Players</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    .gaming-games-hero {{
        padding: 120px 24px;
        background: {background};
    }}
    .games-container {{
        max-width: 1400px;
        margin: 0 auto;
    }}
    .section-header {{
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
        letter-spacing: 2px;
        border-radius: 100px;
        margin-bottom: 20px;
    }}
    .section-header h2 {{
        font-family: 'Rajdhani', sans-serif;
        font-size: clamp(2.5rem, 5vw, 4rem);
        font-weight: 800;
        color: {text};
    }}
    .games-layout {{
        display: grid;
        grid-template-columns: 2fr 1fr;
        gap: 32px;
    }}
    .featured-game {{
        position: relative;
        border-radius: 24px;
        overflow: hidden;
        aspect-ratio: 16/10;
    }}
    .featured-game img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
    }}
    .featured-overlay {{
        position: absolute;
        inset: 0;
        background: linear-gradient(to top, {background}E6, transparent 60%);
        padding: 40px;
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
    }}
    .game-badge {{
        display: inline-block;
        padding: 8px 20px;
        background: {primary};
        color: {background};
        font-weight: 700;
        font-size: 0.8rem;
        border-radius: 100px;
        margin-bottom: 16px;
        width: fit-content;
    }}
    .featured-overlay h3 {{
        font-size: 2.5rem;
        font-weight: 800;
        color: {text};
        margin-bottom: 8px;
    }}
    .featured-overlay p {{
        color: {secondary};
        margin-bottom: 16px;
    }}
    .game-meta {{
        display: flex;
        gap: 20px;
        color: {secondary};
        margin-bottom: 24px;
    }}
    .btn-play {{
        display: inline-block;
        padding: 14px 36px;
        background: {primary};
        color: {background};
        font-weight: 700;
        text-decoration: none;
        border-radius: 10px;
        width: fit-content;
        transition: all 0.3s ease;
    }}
    .btn-play:hover {{
        transform: scale(1.05);
        box-shadow: 0 15px 40px {primary}40;
    }}
    .games-sidebar {{
        display: flex;
        flex-direction: column;
        gap: 24px;
    }}
    .sidebar-game {{
        display: flex;
        gap: 16px;
        padding: 16px;
        background: {text}05;
        border-radius: 16px;
        transition: all 0.3s ease;
        cursor: pointer;
    }}
    .sidebar-game:hover {{
        background: {primary}10;
        transform: translateX(8px);
    }}
    .sidebar-game img {{
        width: 100px;
        height: 80px;
        object-fit: cover;
        border-radius: 10px;
    }}
    .sidebar-info {{
        display: flex;
        flex-direction: column;
        justify-content: center;
    }}
    .sidebar-info h4 {{
        font-size: 1.1rem;
        font-weight: 700;
        color: {text};
        margin-bottom: 4px;
    }}
    .sidebar-info span {{
        font-size: 0.9rem;
        color: {secondary};
    }}
    @media (max-width: 900px) {{
        .games-layout {{ grid-template-columns: 1fr; }}
    }}
    </style>
    '''
