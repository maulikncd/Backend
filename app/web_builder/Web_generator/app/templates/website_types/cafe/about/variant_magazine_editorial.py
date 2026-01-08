from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Magazine Layout About - Editorial two-column design"""
    title = props.get("title", "The Art of Coffee")
    story = props.get("story", props.get("content", ""))
    stats = props.get("stats", [])
    
    primary = colors.get("primary", "#8B7355")
    text = colors.get("text", "#2D2013")
    
    story_p1 = story[:300] if story else "Our journey began with a simple passion: to craft the perfect cup of coffee."
    story_p2 = story[300:600] if len(story) > 300 else "Today, we continue that tradition with the same dedication and love."
    
    stats_html = ""
    if stats:
        for stat in stats[:3]:
            stats_html += f'<div class="stat"><span class="stat-num">{stat.get("value", "0")}</span><span class="stat-text">{stat.get("label", "")}</span></div>'
    else:
        stats_html = '''
            <div class="stat"><span class="stat-num">15+</span><span class="stat-text">Years</span></div>
            <div class="stat"><span class="stat-num">50K</span><span class="stat-text">Customers</span></div>
            <div class="stat"><span class="stat-num">30</span><span class="stat-text">Blends</span></div>
        '''
    
    return f'''
    <section class="about-magazine" id="about">
        <div class="magazine-container">
            <div class="mag-left">
                <span class="chapter">Chapter One</span>
                <h2>{title}</h2>
                <div class="mag-line"></div>
                <p class="lead-text">{story_p1}...</p>
            </div>
            <div class="mag-right">
                <div class="text-column">
                    <p>{story_p2}...</p>
                    <div class="stats-row">{stats_html}</div>
                </div>
                <div class="image-column">
                    <img src="https://images.unsplash.com/photo-1442512595331-e89e73853f31?w=600" alt="Coffee">
                </div>
            </div>
        </div>
    </section>
    
    <style>
    .about-magazine {{ padding: 120px 40px; background: #fff; }}
    .magazine-container {{ max-width: 1300px; margin: 0 auto; }}
    .mag-left {{ margin-bottom: 80px; max-width: 600px; }}
    .chapter {{ color: {primary}; text-transform: uppercase; letter-spacing: 4px; font-size: 0.85rem; font-weight: 600; }}
    .about-magazine h2 {{ font-family: 'Playfair Display', serif; font-size: 4rem; color: {text}; margin: 20px 0 30px; line-height: 1.1; }}
    .mag-line {{ width: 80px; height: 2px; background: {primary}; margin-bottom: 30px; }}
    .lead-text {{ font-size: 1.3rem; line-height: 1.8; color: #666; }}
    .mag-right {{ display: grid; grid-template-columns: 1fr 1fr; gap: 60px; align-items: center; }}
    .text-column p {{ font-size: 1.1rem; line-height: 1.9; color: #666; margin-bottom: 40px; }}
    .stats-row {{ display: flex; gap: 50px; }}
    .stat {{ text-align: center; }}
    .stat-num {{ display: block; font-size: 2.5rem; font-weight: 700; color: {primary}; }}
    .stat-text {{ font-size: 0.9rem; color: #888; text-transform: uppercase; letter-spacing: 1px; }}
    .image-column img {{ width: 100%; border-radius: 20px; box-shadow: 0 30px 60px rgba(0,0,0,0.1); }}
    @media (max-width: 968px) {{ .mag-right {{ grid-template-columns: 1fr; }} }}
    </style>
    '''
