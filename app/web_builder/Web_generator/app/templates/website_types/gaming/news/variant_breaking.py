from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Breaking News - Live ticker style"""
    title = props.get("title", "Breaking News")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="gaming-news-breaking" id="news">
        <div class="breaking-ticker">
            <span class="ticker-label">🔴 LIVE</span>
            <div class="ticker-text">
                <span>Season 5 is NOW LIVE! • Championship Finals Start December 20 • New Character "Phantom" Revealed • Patch 5.2 Deployed •</span>
            </div>
        </div>
        <div class="breaking-container">
            <div class="breaking-header">
                <h2>{title}</h2>
            </div>
            <div class="breaking-main">
                <article class="breaking-story">
                    <div class="story-badge">
                        <span class="badge-live">🔴 BREAKING</span>
                        <span class="badge-time">JUST NOW</span>
                    </div>
                    <img src="https://images.unsplash.com/photo-1542751371-adc38448a05e?w=1200" alt="Breaking News">
                    <div class="story-content">
                        <h3>Season 5 "Awakening" Launched Worldwide</h3>
                        <p>The biggest update in gaming history is now live, featuring 3 new maps, 10 new weapons, and completely revamped ranked system.</p>
                        <a href="#" class="read-now">Read Full Story →</a>
                    </div>
                </article>
                <div class="breaking-sidebar">
                    <h4>Also Happening</h4>
                    <article class="mini-story">
                        <span class="mini-time">2h ago</span>
                        <p>Championship bracket finalized with 32 teams</p>
                    </article>
                    <article class="mini-story">
                        <span class="mini-time">4h ago</span>
                        <p>Pro player breaks kill record in tournament</p>
                    </article>
                    <article class="mini-story">
                        <span class="mini-time">6h ago</span>
                        <p>Server maintenance completed ahead of schedule</p>
                    </article>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    .gaming-news-breaking {{
        background: {background};
    }}
    .breaking-ticker {{
        display: flex;
        align-items: center;
        background: {primary};
        padding: 12px 24px;
        overflow: hidden;
    }}
    .ticker-label {{
        background: {background};
        color: {primary};
        padding: 8px 16px;
        font-weight: 800;
        font-size: 0.85rem;
        border-radius: 6px;
        flex-shrink: 0;
        margin-right: 24px;
        animation: pulse 2s infinite;
    }}
    @keyframes pulse {{
        0%, 100% {{ opacity: 1; }}
        50% {{ opacity: 0.7; }}
    }}
    .ticker-text {{
        flex: 1;
        overflow: hidden;
        white-space: nowrap;
    }}
    .ticker-text span {{
        display: inline-block;
        color: {background};
        font-weight: 600;
        animation: scroll 20s linear infinite;
    }}
    @keyframes scroll {{
        from {{ transform: translateX(100%); }}
        to {{ transform: translateX(-100%); }}
    }}
    .breaking-container {{
        padding: 80px 24px;
        max-width: 1200px;
        margin: 0 auto;
    }}
    .breaking-header {{
        margin-bottom: 48px;
    }}
    .breaking-header h2 {{
        font-family: 'Rajdhani', sans-serif;
        font-size: 2.5rem;
        font-weight: 800;
        color: {text};
    }}
    .breaking-main {{
        display: grid;
        grid-template-columns: 2fr 1fr;
        gap: 40px;
    }}
    .breaking-story {{
        position: relative;
    }}
    .story-badge {{
        display: flex;
        gap: 12px;
        margin-bottom: 16px;
    }}
    .badge-live {{
        padding: 8px 16px;
        background: #ff3b3b;
        color: white;
        font-weight: 800;
        font-size: 0.8rem;
        border-radius: 6px;
    }}
    .badge-time {{
        padding: 8px 16px;
        background: {text}10;
        color: {secondary};
        font-weight: 600;
        font-size: 0.8rem;
        border-radius: 6px;
    }}
    .breaking-story img {{
        width: 100%;
        aspect-ratio: 16/9;
        object-fit: cover;
        border-radius: 20px;
        margin-bottom: 24px;
    }}
    .story-content h3 {{
        font-size: 2rem;
        font-weight: 800;
        color: {text};
        margin-bottom: 16px;
    }}
    .story-content p {{
        color: {secondary};
        font-size: 1.1rem;
        line-height: 1.7;
        margin-bottom: 24px;
    }}
    .read-now {{
        color: {primary};
        text-decoration: none;
        font-weight: 700;
        font-size: 1.1rem;
    }}
    .breaking-sidebar h4 {{
        color: {text};
        font-weight: 700;
        margin-bottom: 24px;
        padding-bottom: 16px;
        border-bottom: 2px solid {primary};
    }}
    .mini-story {{
        padding: 20px 0;
        border-bottom: 1px solid {text}10;
    }}
    .mini-time {{
        display: inline-block;
        padding: 4px 10px;
        background: {primary}15;
        color: {primary};
        font-size: 0.75rem;
        font-weight: 700;
        border-radius: 100px;
        margin-bottom: 8px;
    }}
    .mini-story p {{
        color: {text};
        font-weight: 600;
        line-height: 1.5;
    }}
    @media (max-width: 900px) {{
        .breaking-main {{ grid-template-columns: 1fr; }}
    }}
    </style>
    '''
