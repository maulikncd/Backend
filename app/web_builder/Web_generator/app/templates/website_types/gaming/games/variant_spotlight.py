from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Spotlight - Single featured game with details"""
    title = props.get("title", "Game Spotlight")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="gaming-games-spotlight" id="games">
        <div class="spotlight-bg">
            <img src="https://images.unsplash.com/photo-1542751371-adc38448a05e?w=1920" alt="Background">
            <div class="bg-overlay"></div>
        </div>
        <div class="spotlight-container">
            <div class="spotlight-content">
                <span class="spotlight-tag">🎮 {title}</span>
                <h1>Cyber Warriors</h1>
                <p class="spotlight-desc">Enter the arena and prove your worth. Battle against millions of players worldwide in this ultimate competitive experience.</p>
                <div class="spotlight-stats">
                    <div class="stat">
                        <span class="val">10M+</span>
                        <span class="lbl">Active Players</span>
                    </div>
                    <div class="stat">
                        <span class="val">4.9</span>
                        <span class="lbl">User Rating</span>
                    </div>
                    <div class="stat">
                        <span class="val">100K</span>
                        <span class="lbl">Daily Matches</span>
                    </div>
                </div>
                <div class="spotlight-actions">
                    <a href="#" class="btn-primary">Play Free</a>
                    <a href="#" class="btn-secondary">Watch Trailer</a>
                </div>
                <div class="platforms">
                    <span>Available on:</span>
                    <div class="platform-icons">
                        <span>🖥️</span>
                        <span>🎮</span>
                        <span>📱</span>
                    </div>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    .gaming-games-spotlight {{
        min-height: 100vh;
        position: relative;
        display: flex;
        align-items: center;
    }}
    .spotlight-bg {{
        position: absolute;
        inset: 0;
    }}
    .spotlight-bg img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
    }}
    .bg-overlay {{
        position: absolute;
        inset: 0;
        background: linear-gradient(90deg, {background}F2 0%, {background}B3 50%, transparent 100%);
    }}
    .spotlight-container {{
        position: relative;
        z-index: 2;
        max-width: 1400px;
        margin: 0 auto;
        padding: 120px 60px;
        width: 100%;
    }}
    .spotlight-content {{
        max-width: 650px;
    }}
    .spotlight-tag {{
        display: inline-block;
        padding: 10px 24px;
        background: {primary}20;
        color: {primary};
        font-weight: 700;
        font-size: 0.9rem;
        letter-spacing: 2px;
        border-radius: 100px;
        margin-bottom: 24px;
    }}
    .spotlight-content h1 {{
        font-family: 'Rajdhani', sans-serif;
        font-size: clamp(3rem, 7vw, 6rem);
        font-weight: 900;
        color: {text};
        line-height: 1;
        margin-bottom: 24px;
    }}
    .spotlight-desc {{
        font-size: 1.2rem;
        color: {secondary};
        line-height: 1.8;
        margin-bottom: 40px;
    }}
    .spotlight-stats {{
        display: flex;
        gap: 48px;
        margin-bottom: 40px;
    }}
    .stat {{
        text-align: center;
    }}
    .stat .val {{
        display: block;
        font-family: 'Orbitron', sans-serif;
        font-size: 2.5rem;
        font-weight: 900;
        color: {primary};
        text-shadow: 0 0 30px {primary}50;
    }}
    .stat .lbl {{
        font-size: 0.85rem;
        color: {secondary};
    }}
    .spotlight-actions {{
        display: flex;
        gap: 16px;
        margin-bottom: 32px;
    }}
    .btn-primary {{
        padding: 18px 48px;
        background: {primary};
        color: {background};
        font-weight: 700;
        text-decoration: none;
        border-radius: 10px;
        transition: all 0.3s ease;
    }}
    .btn-primary:hover {{
        transform: scale(1.05);
        box-shadow: 0 20px 50px {primary}40;
    }}
    .btn-secondary {{
        padding: 18px 48px;
        background: transparent;
        border: 2px solid {text}30;
        color: {text};
        font-weight: 700;
        text-decoration: none;
        border-radius: 10px;
        transition: all 0.3s ease;
    }}
    .btn-secondary:hover {{
        border-color: {primary};
        color: {primary};
    }}
    .platforms {{
        display: flex;
        align-items: center;
        gap: 16px;
        color: {secondary};
    }}
    .platform-icons {{
        display: flex;
        gap: 12px;
        font-size: 1.5rem;
    }}
    @media (max-width: 768px) {{
        .spotlight-container {{ padding: 100px 24px; }}
        .spotlight-stats {{ gap: 24px; }}
        .spotlight-actions {{ flex-direction: column; }}
    }}
    </style>
    '''
