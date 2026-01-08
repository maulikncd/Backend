from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """
    Aura Premium About - Split layout with timeline and 
    premium photography
    """
    title = props.get("title", "Our Story")
    story = props.get("story", props.get("content", "From humble beginnings to becoming a beloved community gathering place."))
    stats = props.get("stats", [])
    milestones = props.get("milestones", [])
    
    primary = colors.get("primary", "#8B7355")
    bg = colors.get("background", "#FAF7F4")
    text = colors.get("text", "#2D2013")
    
    # Build stats
    stats_html = ""
    if stats:
        for stat in stats[:4]:
            stats_html += f'''
            <div class="stat-box">
                <span class="stat-number">{stat.get("value", "0")}</span>
                <span class="stat-label">{stat.get("label", "")}</span>
            </div>
            '''
    else:
        stats_html = '''
            <div class="stat-box"><span class="stat-number">15+</span><span class="stat-label">Years Experience</span></div>
            <div class="stat-box"><span class="stat-number">50K+</span><span class="stat-label">Cups Served</span></div>
            <div class="stat-box"><span class="stat-number">30+</span><span class="stat-label">Coffee Origins</span></div>
            <div class="stat-box"><span class="stat-number">100%</span><span class="stat-label">Organic Beans</span></div>
        '''
    
    # Build timeline
    timeline_html = ""
    if milestones:
        for ms in milestones[:4]:
            timeline_html += f'''
            <div class="timeline-item">
                <span class="timeline-year">{ms.get("year", "2024")}</span>
                <div class="timeline-content">
                    <h4>{ms.get("title", "Milestone")}</h4>
                    <p>{ms.get("description", "")[:100]}</p>
                </div>
            </div>
            '''
    else:
        timeline_html = '''
            <div class="timeline-item"><span class="timeline-year">2020</span><div class="timeline-content"><h4>The Dream Begins</h4><p>Founded with a vision to craft exceptional coffee</p></div></div>
            <div class="timeline-item"><span class="timeline-year">2022</span><div class="timeline-content"><h4>Grand Opening</h4><p>Welcomed our first customers through our doors</p></div></div>
            <div class="timeline-item"><span class="timeline-year">2024</span><div class="timeline-content"><h4>Award Winner</h4><p>Recognized as the best local cafe</p></div></div>
        '''
    
    display_story = story[:400] + "..." if len(story) > 400 else story
    
    return f'''
    <section class="aura-about" id="about">
        <div class="about-grid">
            <div class="about-images">
                <div class="img-main">
                    <img src="https://images.unsplash.com/photo-1445116572660-236099ec97a0?w=600" alt="Our Cafe">
                </div>
                <div class="img-secondary">
                    <img src="https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=400" alt="Coffee Making">
                </div>
                <div class="experience-badge">
                    <span class="exp-number">15+</span>
                    <span class="exp-text">Years of Excellence</span>
                </div>
            </div>
            <div class="about-content">
                <span class="section-badge">About Us</span>
                <h2 class="about-title">{title}</h2>
                <p class="about-story">{display_story}</p>
                
                <div class="stats-grid">
                    {stats_html}
                </div>
                
                <div class="timeline">
                    {timeline_html}
                </div>
                
                <a href="#contact" class="btn-learn-more">Learn More About Us</a>
            </div>
        </div>
    </section>
    
    <style>
    .aura-about {{
        padding: 120px 60px;
        background: #fff;
    }}
    .about-grid {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 80px;
        max-width: 1300px;
        margin: 0 auto;
        align-items: center;
    }}
    .about-images {{ position: relative; }}
    .img-main {{
        width: 80%;
        aspect-ratio: 3/4;
        border-radius: 20px;
        overflow: hidden;
        box-shadow: 0 30px 60px rgba(0,0,0,0.15);
    }}
    .img-main img {{ width: 100%; height: 100%; object-fit: cover; }}
    .img-secondary {{
        position: absolute;
        bottom: -30px;
        right: 0;
        width: 50%;
        aspect-ratio: 1;
        border-radius: 20px;
        overflow: hidden;
        border: 6px solid #fff;
        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
    }}
    .img-secondary img {{ width: 100%; height: 100%; object-fit: cover; }}
    .experience-badge {{
        position: absolute;
        top: 30px;
        right: 30px;
        background: {primary};
        color: #fff;
        padding: 20px;
        border-radius: 16px;
        text-align: center;
    }}
    .exp-number {{ display: block; font-size: 2.5rem; font-weight: 800; }}
    .exp-text {{ font-size: 0.8rem; text-transform: uppercase; letter-spacing: 1px; }}
    .about-content .section-badge {{
        display: inline-block;
        padding: 8px 20px;
        background: {primary}15;
        color: {primary};
        border-radius: 50px;
        font-size: 0.85rem;
        font-weight: 600;
        margin-bottom: 20px;
    }}
    .about-title {{
        font-family: 'Playfair Display', serif;
        font-size: clamp(2.5rem, 4vw, 3.5rem);
        color: {text};
        margin-bottom: 24px;
    }}
    .about-story {{
        color: #666;
        font-size: 1.1rem;
        line-height: 1.8;
        margin-bottom: 40px;
    }}
    .stats-grid {{
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 20px;
        margin-bottom: 40px;
    }}
    .stat-box {{ text-align: center; padding: 20px; background: {bg}; border-radius: 12px; }}
    .stat-number {{ display: block; font-size: 1.8rem; font-weight: 800; color: {primary}; }}
    .stat-label {{ font-size: 0.8rem; color: #888; }}
    .timeline {{ margin-bottom: 40px; }}
    .timeline-item {{
        display: flex;
        gap: 20px;
        padding: 20px 0;
        border-bottom: 1px solid #eee;
    }}
    .timeline-year {{
        font-weight: 800;
        color: {primary};
        min-width: 60px;
    }}
    .timeline-content h4 {{
        font-family: 'Playfair Display', serif;
        font-size: 1.2rem;
        margin-bottom: 6px;
        color: {text};
    }}
    .timeline-content p {{ color: #888; font-size: 0.95rem; }}
    .btn-learn-more {{
        display: inline-block;
        padding: 16px 40px;
        background: {primary};
        color: #fff;
        text-decoration: none;
        border-radius: 50px;
        font-weight: 600;
        transition: all 0.3s;
    }}
    .btn-learn-more:hover {{
        transform: translateY(-2px);
        box-shadow: 0 10px 30px {primary}40;
    }}
    @media (max-width: 1024px) {{
        .about-grid {{ grid-template-columns: 1fr; gap: 60px; }}
        .aura-about {{ padding: 80px 24px; }}
        .stats-grid {{ grid-template-columns: repeat(2, 1fr); }}
    }}
    </style>
    '''
