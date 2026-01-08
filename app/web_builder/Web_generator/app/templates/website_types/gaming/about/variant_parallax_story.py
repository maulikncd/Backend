from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Parallax Story - Immersive storytelling with scroll effects"""
    title = props.get("title", "Our Journey")
    content = props.get("content", "From a small team of passionate gamers to a global gaming empire")
    
    # Dynamic colors from user's palette
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="gaming-about-parallax" id="about">
        <div class="parallax-bg">
            <div class="parallax-layer layer-1"></div>
            <div class="parallax-layer layer-2"></div>
        </div>
        <div class="parallax-content">
            <div class="timeline-vertical">
                <div class="timeline-line"></div>
                <div class="timeline-item">
                    <div class="timeline-year">2018</div>
                    <div class="timeline-card">
                        <h4>The Beginning</h4>
                        <p>Started with a dream and 5 passionate gamers in a small garage.</p>
                    </div>
                </div>
                <div class="timeline-item">
                    <div class="timeline-year">2020</div>
                    <div class="timeline-card">
                        <h4>First Million</h4>
                        <p>Reached 1 million active players and hosted our first major tournament.</p>
                    </div>
                </div>
                <div class="timeline-item">
                    <div class="timeline-year">2022</div>
                    <div class="timeline-card">
                        <h4>Global Expansion</h4>
                        <p>Expanded to 50+ countries with dedicated regional servers.</p>
                    </div>
                </div>
                <div class="timeline-item">
                    <div class="timeline-year">2024</div>
                    <div class="timeline-card featured">
                        <h4>Industry Leader</h4>
                        <p>Now serving 50M+ players with the most advanced gaming platform.</p>
                    </div>
                </div>
            </div>
            <div class="story-side">
                <div class="floating-badge">🚀 Rapid Growth</div>
                <h2>{title}</h2>
                <p class="story-text">{content}</p>
                <div class="growth-metrics">
                    <div class="metric">
                        <div class="metric-chart">
                            <svg viewBox="0 0 100 60" class="line-chart">
                                <path d="M0,55 Q25,50 35,40 T60,25 T85,15 T100,5" fill="none" stroke="url(#gradient)" stroke-width="3"/>
                                <defs>
                                    <linearGradient id="gradient" x1="0%" y1="0%" x2="100%" y2="0%">
                                        <stop offset="0%" style="stop-color:{secondary}"/>
                                        <stop offset="100%" style="stop-color:{primary}"/>
                                    </linearGradient>
                                </defs>
                            </svg>
                        </div>
                        <span>User Growth</span>
                    </div>
                    <div class="metric">
                        <div class="metric-value">98%</div>
                        <span>Satisfaction</span>
                    </div>
                </div>
                <a href="#team" class="btn-story">Read Full Story →</a>
            </div>
        </div>
    </section>
    
    <style>
    .gaming-about-parallax {{
        padding: 140px 24px;
        background: {background};
        position: relative;
        overflow: hidden;
        min-height: 100vh;
    }}
    .parallax-bg {{
        position: absolute;
        inset: 0;
        pointer-events: none;
    }}
    .parallax-layer {{
        position: absolute;
        inset: 0;
    }}
    .layer-1 {{
        background: radial-gradient(ellipse at 20% 80%, {primary}15 0%, transparent 50%);
    }}
    .layer-2 {{
        background: radial-gradient(ellipse at 80% 20%, {secondary}10 0%, transparent 50%);
    }}
    .parallax-content {{
        max-width: 1300px;
        margin: 0 auto;
        display: grid;
        grid-template-columns: 1fr 1.2fr;
        gap: 100px;
        align-items: center;
        position: relative;
        z-index: 2;
    }}
    .timeline-vertical {{
        position: relative;
        padding-left: 40px;
    }}
    .timeline-line {{
        position: absolute;
        left: 0;
        top: 0;
        bottom: 0;
        width: 3px;
        background: linear-gradient(to bottom, {primary}, {secondary});
        border-radius: 10px;
    }}
    .timeline-item {{
        display: flex;
        align-items: flex-start;
        gap: 24px;
        margin-bottom: 40px;
        position: relative;
    }}
    .timeline-item::before {{
        content: '';
        position: absolute;
        left: -44px;
        top: 8px;
        width: 12px;
        height: 12px;
        background: {primary};
        border-radius: 50%;
        box-shadow: 0 0 20px {primary};
    }}
    .timeline-year {{
        font-family: 'Orbitron', sans-serif;
        font-size: 1.5rem;
        font-weight: 900;
        color: {primary};
        min-width: 80px;
    }}
    .timeline-card {{
        background: {text}05;
        border: 1px solid {text}10;
        border-radius: 16px;
        padding: 24px;
        flex: 1;
        transition: all 0.3s ease;
    }}
    .timeline-card:hover {{
        border-color: {primary}40;
        transform: translateX(8px);
    }}
    .timeline-card.featured {{
        background: linear-gradient(135deg, {primary}15, {primary}05);
        border-color: {primary}40;
    }}
    .timeline-card h4 {{
        color: {text};
        font-size: 1.2rem;
        font-weight: 700;
        margin-bottom: 8px;
    }}
    .timeline-card p {{
        color: {secondary};
        font-size: 0.95rem;
        line-height: 1.6;
    }}
    .story-side {{
        padding: 40px;
    }}
    .floating-badge {{
        display: inline-block;
        padding: 10px 24px;
        background: {primary}15;
        border: 1px solid {primary}30;
        border-radius: 100px;
        color: {primary};
        font-weight: 700;
        font-size: 0.9rem;
        margin-bottom: 32px;
        animation: float 3s ease-in-out infinite;
    }}
    @keyframes float {{
        0%, 100% {{ transform: translateY(0); }}
        50% {{ transform: translateY(-10px); }}
    }}
    .story-side h2 {{
        font-family: 'Rajdhani', sans-serif;
        font-size: clamp(3rem, 5vw, 4.5rem);
        font-weight: 800;
        color: {text};
        line-height: 1;
        margin-bottom: 24px;
    }}
    .story-text {{
        font-size: 1.2rem;
        color: {secondary};
        line-height: 1.8;
        margin-bottom: 48px;
    }}
    .growth-metrics {{
        display: flex;
        gap: 48px;
        margin-bottom: 48px;
    }}
    .metric {{
        text-align: center;
    }}
    .metric-chart {{
        width: 120px;
        height: 60px;
        margin-bottom: 12px;
    }}
    .line-chart {{
        width: 100%;
        height: 100%;
    }}
    .metric-value {{
        font-size: 3rem;
        font-weight: 900;
        color: {primary};
        line-height: 1;
        margin-bottom: 8px;
    }}
    .metric span {{
        font-size: 0.85rem;
        color: {secondary};
        text-transform: uppercase;
        letter-spacing: 2px;
    }}
    .btn-story {{
        display: inline-block;
        padding: 16px 36px;
        background: {primary};
        color: {background};
        font-weight: 700;
        text-decoration: none;
        border-radius: 8px;
        transition: all 0.3s ease;
    }}
    .btn-story:hover {{
        transform: translateY(-4px);
        box-shadow: 0 20px 40px {primary}40;
    }}
    @media (max-width: 1024px) {{
        .parallax-content {{ grid-template-columns: 1fr; gap: 60px; }}
        .timeline-vertical {{ order: 2; }}
    }}
    </style>
    '''
