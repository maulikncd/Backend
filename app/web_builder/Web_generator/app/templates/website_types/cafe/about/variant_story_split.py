from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    title = props.get("title", "Our Story")
    story = props.get("story", props.get("content", "What started as a small dream has grown into a beloved community gathering place."))
    image = props.get("image", "https://images.unsplash.com/photo-1453614512568-c4024d13c247?w=800")
    
    # Get stats from blueprint
    stats = props.get("stats", [])
    
    # Build stats HTML
    stats_html = ""
    if stats:
        for stat in stats[:3]:
            stats_html += f'''
                <div class="stat">
                    <span class="stat-number">{stat.get("value", "0")}</span>
                    <span class="stat-label">{stat.get("label", "")}</span>
                </div>
            '''
    else:
        # Default stats
        stats_html = '''
            <div class="stat">
                <span class="stat-number">10+</span>
                <span class="stat-label">Years of brewing</span>
            </div>
            <div class="stat">
                <span class="stat-number">50K+</span>
                <span class="stat-label">Happy customers</span>
            </div>
            <div class="stat">
                <span class="stat-number">100%</span>
                <span class="stat-label">Organic beans</span>
            </div>
        '''
    
    # Truncate story for display
    display_story = story[:600] + "..." if len(story) > 600 else story
    
    return f'''
    <section class="cafe-about cafe-about-split" id="about">
        <div class="about-container">
            <div class="about-image">
                <img src="{image}" alt="Our Story">
                <div class="image-accent"></div>
            </div>
            <div class="about-content">
                <span class="about-badge">📖 Our Journey</span>
                <h2 class="about-title">{title}</h2>
                <p class="about-text">{display_story}</p>
                <div class="about-stats">
                    {stats_html}
                </div>
            </div>
        </div>
    </section>
    
    <style>
    .cafe-about-split {{
        padding: 100px 24px;
        background: {colors.get("background", "#FFF8F0")};
    }}
    .about-container {{
        max-width: 1200px;
        margin: 0 auto;
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 80px;
        align-items: center;
    }}
    .about-image {{ position: relative; }}
    .about-image img {{
        width: 100%;
        border-radius: 20px;
        box-shadow: 0 30px 60px rgba(0,0,0,0.15);
    }}
    .image-accent {{
        position: absolute;
        inset: 20px -20px -20px 20px;
        border: 3px solid {colors.get("primary", "#6F4E37")};
        border-radius: 20px;
        z-index: -1;
    }}
    .about-badge {{
        display: inline-block;
        padding: 8px 16px;
        background: {colors.get("primary", "#6F4E37")}15;
        color: {colors.get("primary", "#6F4E37")};
        border-radius: 50px;
        font-size: 0.9rem;
        font-weight: 600;
        margin-bottom: 20px;
    }}
    .about-title {{
        font-family: 'Playfair Display', serif;
        font-size: clamp(2rem, 4vw, 3rem);
        color: {colors.get("text", "#2D2013")};
        margin-bottom: 20px;
    }}
    .about-text {{
        font-size: 1.1rem;
        color: {colors.get("text_muted", "#8B7355")};
        line-height: 1.8;
        margin-bottom: 40px;
    }}
    .about-stats {{ display: flex; gap: 40px; flex-wrap: wrap; }}
    .stat {{ text-align: center; }}
    .stat-number {{
        display: block;
        font-size: 2rem;
        font-weight: 700;
        color: {colors.get("primary", "#6F4E37")};
    }}
    .stat-label {{ font-size: 0.9rem; color: {colors.get("text_muted", "#8B7355")}; }}
    @media (max-width: 968px) {{
        .about-container {{ grid-template-columns: 1fr; gap: 40px; }}
    }}
    </style>
    '''
