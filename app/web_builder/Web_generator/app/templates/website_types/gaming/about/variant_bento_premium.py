from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Bento Premium - Modern bento grid with interactive elements"""
    title = props.get("title", "What Makes Us Different")
    content = props.get("content", "A platform built by gamers, for gamers")
    
    # Dynamic colors from user's palette
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    accent = colors.get("accent")
    
    return f'''
    <section class="gaming-about-bento" id="about">
        <div class="bento-container">
            <div class="bento-header">
                <span class="label-chip">About Us</span>
                <h2>{title}</h2>
                <p>{content}</p>
            </div>
            
            <div class="bento-grid">
                <!-- Large Feature Card -->
                <div class="bento-card large">
                    <div class="card-visual">
                        <img src="https://images.unsplash.com/photo-1538481199705-c710c4e965fc?w=600" alt="Gaming">
                        <div class="visual-overlay"></div>
                    </div>
                    <div class="card-body">
                        <div class="chip chip-primary">Core Feature</div>
                        <h3>Built for Competitive Excellence</h3>
                        <p>Every millisecond counts. Our platform is optimized for professional-level gaming with industry-leading performance.</p>
                    </div>
                </div>
                
                <!-- Stats Card -->
                <div class="bento-card stats">
                    <div class="stats-content">
                        <div class="big-stat">
                            <span class="stat-num">50M+</span>
                            <span class="stat-label">Active Players</span>
                        </div>
                        <div class="stats-row">
                            <div class="small-stat">
                                <span>150+</span>
                                <span>Countries</span>
                            </div>
                            <div class="small-stat">
                                <span>24/7</span>
                                <span>Support</span>
                            </div>
                        </div>
                    </div>
                    <div class="stats-bg-pattern"></div>
                </div>
                
                <!-- Feature Cards -->
                <div class="bento-card feature">
                    <div class="feature-icon">🚀</div>
                    <h4>Ultra Low Latency</h4>
                    <p>Sub-10ms response times for competitive edge</p>
                </div>
                
                <div class="bento-card feature">
                    <div class="feature-icon">🛡️</div>
                    <h4>Secure Platform</h4>
                    <p>Advanced anti-cheat and fraud protection</p>
                </div>
                
                <!-- Quote Card -->
                <div class="bento-card quote">
                    <blockquote>
                        "The most seamless gaming experience I've ever had. It's not just a platform, it's home."
                    </blockquote>
                    <div class="quote-author">
                        <div class="author-avatar">🎮</div>
                        <div class="author-info">
                            <span class="author-name">ProGamer_X</span>
                            <span class="author-title">Esports Champion</span>
                        </div>
                    </div>
                </div>
                
                <!-- CTA Card -->
                <div class="bento-card cta">
                    <div class="cta-content">
                        <h4>Ready to Level Up?</h4>
                        <p>Join millions of players worldwide</p>
                        <a href="#start" class="btn-bento">Get Started Free</a>
                    </div>
                    <div class="cta-glow"></div>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    .gaming-about-bento {{
        padding: 140px 24px;
        background: {background};
    }}
    .bento-container {{
        max-width: 1200px;
        margin: 0 auto;
    }}
    .bento-header {{
        text-align: center;
        margin-bottom: 80px;
    }}
    .label-chip {{
        display: inline-block;
        padding: 8px 20px;
        background: {primary}15;
        color: {primary};
        font-weight: 700;
        font-size: 0.85rem;
        letter-spacing: 2px;
        text-transform: uppercase;
        border-radius: 100px;
        margin-bottom: 24px;
    }}
    .bento-header h2 {{
        font-family: 'Rajdhani', sans-serif;
        font-size: clamp(2.5rem, 5vw, 4rem);
        font-weight: 800;
        color: {text};
        margin-bottom: 16px;
    }}
    .bento-header p {{
        font-size: 1.2rem;
        color: {secondary};
    }}
    .bento-grid {{
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        grid-template-rows: auto auto auto;
        gap: 24px;
    }}
    .bento-card {{
        background: {text}05;
        border: 1px solid {text}08;
        border-radius: 24px;
        overflow: hidden;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    }}
    .bento-card:hover {{
        border-color: {primary}30;
        transform: translateY(-8px);
    }}
    .bento-card.large {{
        grid-column: span 2;
        grid-row: span 2;
    }}
    .bento-card.stats {{
        grid-column: span 2;
        position: relative;
        overflow: hidden;
        background: linear-gradient(135deg, {primary}15, {primary}05);
    }}
    .bento-card.feature {{
        padding: 32px;
        display: flex;
        flex-direction: column;
    }}
    .bento-card.quote {{
        grid-column: span 2;
        padding: 40px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }}
    .bento-card.cta {{
        grid-column: span 2;
        position: relative;
        overflow: hidden;
        background: linear-gradient(135deg, {primary}20, {secondary}10);
    }}
    .card-visual {{
        height: 250px;
        position: relative;
        overflow: hidden;
    }}
    .card-visual img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
    }}
    .visual-overlay {{
        position: absolute;
        inset: 0;
        background: linear-gradient(to top, {background}, transparent 50%);
    }}
    .card-body {{
        padding: 32px;
    }}
    .chip {{
        display: inline-block;
        padding: 6px 14px;
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 1px;
        text-transform: uppercase;
        border-radius: 100px;
        margin-bottom: 16px;
    }}
    .chip-primary {{
        background: {primary}20;
        color: {primary};
    }}
    .card-body h3 {{
        font-size: 1.5rem;
        font-weight: 800;
        color: {text};
        margin-bottom: 12px;
    }}
    .card-body p {{
        color: {secondary};
        line-height: 1.7;
    }}
    .stats-content {{
        position: relative;
        z-index: 2;
        padding: 48px 40px;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }}
    .big-stat {{
        margin-bottom: 32px;
    }}
    .stat-num {{
        display: block;
        font-family: 'Rajdhani', sans-serif;
        font-size: 4rem;
        font-weight: 900;
        color: {text};
        line-height: 1;
    }}
    .stat-label {{
        font-size: 1rem;
        color: {secondary};
    }}
    .stats-row {{
        display: flex;
        gap: 40px;
    }}
    .small-stat span:first-child {{
        display: block;
        font-size: 1.8rem;
        font-weight: 800;
        color: {primary};
    }}
    .small-stat span:last-child {{
        font-size: 0.85rem;
        color: {secondary};
    }}
    .stats-bg-pattern {{
        position: absolute;
        right: -20px;
        bottom: -20px;
        width: 200px;
        height: 200px;
        background: {primary};
        opacity: 0.1;
        border-radius: 50%;
        filter: blur(60px);
    }}
    .feature-icon {{
        font-size: 2.5rem;
        margin-bottom: 20px;
    }}
    .bento-card.feature h4 {{
        font-size: 1.2rem;
        font-weight: 700;
        color: {text};
        margin-bottom: 8px;
    }}
    .bento-card.feature p {{
        color: {secondary};
        font-size: 0.95rem;
    }}
    blockquote {{
        font-size: 1.3rem;
        font-style: italic;
        color: {text};
        line-height: 1.6;
        margin-bottom: 24px;
    }}
    .quote-author {{
        display: flex;
        align-items: center;
        gap: 16px;
    }}
    .author-avatar {{
        width: 50px;
        height: 50px;
        background: {primary}20;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.5rem;
    }}
    .author-name {{
        display: block;
        font-weight: 700;
        color: {text};
    }}
    .author-title {{
        font-size: 0.85rem;
        color: {secondary};
    }}
    .cta-content {{
        position: relative;
        z-index: 2;
        padding: 48px 40px;
        text-align: center;
    }}
    .bento-card.cta h4 {{
        font-size: 1.5rem;
        font-weight: 800;
        color: {text};
        margin-bottom: 8px;
    }}
    .bento-card.cta p {{
        color: {secondary};
        margin-bottom: 24px;
    }}
    .btn-bento {{
        display: inline-block;
        padding: 16px 36px;
        background: {primary};
        color: {background};
        font-weight: 700;
        text-decoration: none;
        border-radius: 12px;
        transition: all 0.3s ease;
    }}
    .btn-bento:hover {{
        transform: scale(1.05);
        box-shadow: 0 20px 40px {primary}40;
    }}
    .cta-glow {{
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 200px;
        height: 200px;
        background: {primary};
        filter: blur(100px);
        opacity: 0.3;
    }}
    @media (max-width: 900px) {{
        .bento-grid {{ grid-template-columns: 1fr 1fr; }}
        .bento-card.large, .bento-card.stats, .bento-card.quote, .bento-card.cta {{ grid-column: span 2; }}
    }}
    @media (max-width: 600px) {{
        .bento-grid {{ grid-template-columns: 1fr; }}
        .bento-card.large, .bento-card.stats, .bento-card.quote, .bento-card.cta, .bento-card.feature {{ grid-column: span 1; }}
    }}
    </style>
    '''
