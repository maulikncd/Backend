from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Cinematic Split - Movie-style storytelling with dramatic imagery"""
    title = props.get("title", "Our Legacy")
    content = props.get("content", "From humble beginnings to global esports domination. We've rewritten the rules of competitive gaming.")
    
    # Dynamic colors from user's palette
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="gaming-about-cinematic" id="about">
        <div class="cinematic-container">
            <div class="cinematic-left">
                <div class="video-showcase">
                    <img src="https://images.unsplash.com/photo-1542751371-adc38448a05e?w=800" alt="Gaming Setup">
                    <div class="play-overlay">
                        <div class="play-btn">
                            <svg viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>
                        </div>
                        <span>Watch Our Story</span>
                    </div>
                    <div class="video-glow"></div>
                </div>
            </div>
            <div class="cinematic-right">
                <div class="badge-premium">
                    <span class="badge-icon">🏆</span>
                    <span>Award Winning Studio</span>
                </div>
                <h2 class="section-title">{title}</h2>
                <div class="title-accent"></div>
                <p class="section-desc">{content}</p>
                <div class="achievements-row">
                    <div class="achievement">
                        <div class="ach-value">50M+</div>
                        <div class="ach-label">Players</div>
                    </div>
                    <div class="achievement">
                        <div class="ach-value">120+</div>
                        <div class="ach-label">Countries</div>
                    </div>
                    <div class="achievement">
                        <div class="ach-value">$10M</div>
                        <div class="ach-label">Prize Pool</div>
                    </div>
                </div>
                <a href="#team" class="btn-cinematic">Meet the Team</a>
            </div>
        </div>
    </section>
    
    <style>
    .gaming-about-cinematic {{
        padding: 140px 60px;
        background: {background};
        position: relative;
        overflow: hidden;
    }}
    .gaming-about-cinematic::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 1px;
        background: linear-gradient(90deg, transparent, {primary}50, transparent);
    }}
    .cinematic-container {{
        max-width: 1400px;
        margin: 0 auto;
        display: grid;
        grid-template-columns: 1.2fr 1fr;
        gap: 100px;
        align-items: center;
    }}
    .video-showcase {{
        position: relative;
        border-radius: 24px;
        overflow: hidden;
        box-shadow: 0 60px 120px {background}80, 0 0 0 1px {primary}20;
    }}
    .video-showcase img {{
        width: 100%;
        aspect-ratio: 16/10;
        object-fit: cover;
        filter: brightness(0.7);
    }}
    .play-overlay {{
        position: absolute;
        inset: 0;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        gap: 16px;
        background: linear-gradient(to top, {background}90, transparent);
        cursor: pointer;
    }}
    .play-btn {{
        width: 80px;
        height: 80px;
        border-radius: 50%;
        background: {primary};
        display: flex;
        align-items: center;
        justify-content: center;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 0 60px {primary}60;
    }}
    .play-btn svg {{
        width: 32px;
        height: 32px;
        color: {background};
        margin-left: 4px;
    }}
    .play-overlay:hover .play-btn {{
        transform: scale(1.15);
        box-shadow: 0 0 80px {primary}80;
    }}
    .play-overlay span {{
        color: {text};
        font-weight: 600;
        letter-spacing: 2px;
        text-transform: uppercase;
        font-size: 0.85rem;
    }}
    .video-glow {{
        position: absolute;
        bottom: -50%;
        left: 50%;
        transform: translateX(-50%);
        width: 80%;
        height: 100%;
        background: {primary};
        filter: blur(100px);
        opacity: 0.2;
        pointer-events: none;
    }}
    .badge-premium {{
        display: inline-flex;
        align-items: center;
        gap: 10px;
        padding: 12px 24px;
        background: {primary}15;
        border: 1px solid {primary}30;
        border-radius: 100px;
        margin-bottom: 32px;
    }}
    .badge-icon {{ font-size: 1.2rem; }}
    .badge-premium span:last-child {{
        color: {primary};
        font-weight: 700;
        font-size: 0.85rem;
        letter-spacing: 2px;
        text-transform: uppercase;
    }}
    .section-title {{
        font-family: 'Rajdhani', sans-serif;
        font-size: clamp(3rem, 5vw, 4.5rem);
        font-weight: 800;
        color: {text};
        line-height: 1;
        margin-bottom: 20px;
    }}
    .title-accent {{
        width: 80px;
        height: 4px;
        background: linear-gradient(90deg, {primary}, {secondary});
        margin-bottom: 32px;
        border-radius: 2px;
    }}
    .section-desc {{
        color: {secondary};
        font-size: 1.15rem;
        line-height: 1.8;
        margin-bottom: 48px;
    }}
    .achievements-row {{
        display: flex;
        gap: 48px;
        margin-bottom: 48px;
    }}
    .achievement {{
        text-align: center;
    }}
    .ach-value {{
        font-size: 2.5rem;
        font-weight: 900;
        color: {primary};
        line-height: 1;
        margin-bottom: 8px;
    }}
    .ach-label {{
        font-size: 0.85rem;
        color: {secondary};
        text-transform: uppercase;
        letter-spacing: 2px;
    }}
    .btn-cinematic {{
        display: inline-flex;
        align-items: center;
        gap: 12px;
        padding: 18px 40px;
        background: transparent;
        border: 2px solid {primary};
        color: {primary};
        font-weight: 700;
        font-size: 0.9rem;
        letter-spacing: 2px;
        text-transform: uppercase;
        text-decoration: none;
        transition: all 0.3s ease;
    }}
    .btn-cinematic:hover {{
        background: {primary};
        color: {background};
        box-shadow: 0 20px 40px {primary}40;
        transform: translateY(-3px);
    }}
    @media (max-width: 1024px) {{
        .cinematic-container {{ grid-template-columns: 1fr; gap: 60px; }}
        .gaming-about-cinematic {{ padding: 80px 24px; }}
    }}
    </style>
    '''
