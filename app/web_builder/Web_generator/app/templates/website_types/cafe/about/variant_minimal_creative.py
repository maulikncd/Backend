from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    # Support blueprint keys
    title = props.get("title", "A Passion for Brewing")
    story = props.get("story", props.get("content", "We don't just make coffee. We create experiences."))
    
    # Get stats from blueprint
    stats = props.get("stats", [])
    
    # Get milestones from blueprint
    milestones = props.get("milestones", [])
    
    # Build feature items from stats or milestones
    features_html = ""
    if stats:
        for i, stat in enumerate(stats[:3], 1):
            features_html += f'''
                <div class="feature-item">
                    <span class="number">0{i}</span>
                    <div class="feat-content">
                        <h4>{stat.get("value", "")}</h4>
                        <p>{stat.get("label", "")}</p>
                    </div>
                </div>
            '''
    elif milestones:
        for i, ms in enumerate(milestones[:3], 1):
            features_html += f'''
                <div class="feature-item">
                    <span class="number">{ms.get("year", f"0{i}")}</span>
                    <div class="feat-content">
                        <h4>{ms.get("title", "")}</h4>
                        <p>{ms.get("description", "")[:80]}...</p>
                    </div>
                </div>
            '''
    else:
        # Default features
        features_html = '''
            <div class="feature-item">
                <span class="number">01</span>
                <div class="feat-content">
                    <h4>Ethical Sourcing</h4>
                    <p>Direct trade with farmers worldwide</p>
                </div>
            </div>
            <div class="feature-item">
                <span class="number">02</span>
                <div class="feat-content">
                    <h4>Artisanal Roasting</h4>
                    <p>Small batches for maximum flavor</p>
                </div>
            </div>
        '''
    
    # Truncate story for display
    display_story = story[:500] + "..." if len(story) > 500 else story
    
    return f'''
    <section class="cafe-about-minimal" id="about">
        <div class="minimal-grid">
            <div class="text-side">
                <h2 class="large-title animate-on-scroll">{title}</h2>
                <div class="line-decorator animate-on-scroll"></div>
                <p class="elegant-text animate-on-scroll">{display_story}</p>
            </div>
            <div class="feature-side animate-on-scroll">
                {features_html}
            </div>
        </div>
    </section>
    
    <style>
    .cafe-about-minimal {{
        padding: 120px 24px;
        background: #fff;
        overflow: hidden;
    }}
    .minimal-grid {{
        max-width: 1200px;
        margin: 0 auto;
        display: grid;
        grid-template-columns: 1.5fr 1fr;
        gap: 100px;
        align-items: center;
    }}
    .large-title {{
        font-family: 'Playfair Display', serif;
        font-size: clamp(2.5rem, 5vw, 4rem);
        line-height: 1.1;
        margin-bottom: 40px;
        color: {colors.get("text", "#2D2013")};
    }}
    .line-decorator {{
        width: 120px;
        height: 2px;
        background: {colors.get("primary", "#6F4E37")};
        margin-bottom: 40px;
    }}
    .elegant-text {{
        font-size: 1.15rem;
        line-height: 1.8;
        color: {colors.get("text_muted", "#666")};
    }}
    .feature-side {{ display: flex; flex-direction: column; gap: 50px; }}
    .feature-item {{ display: flex; gap: 24px; align-items: flex-start; }}
    .feature-item .number {{
        font-weight: 800;
        font-size: 1.5rem;
        color: {colors.get("primary", "#6F4E37")};
        min-width: 60px;
    }}
    .feat-content h4 {{ 
        font-family: 'Playfair Display', serif; 
        font-size: 1.3rem; 
        margin-bottom: 8px; 
        color: {colors.get("text", "#2D2013")};
    }}
    .feat-content p {{ 
        color: {colors.get("text_muted", "#888")}; 
        font-size: 0.95rem;
        line-height: 1.5;
    }}
    @media (max-width: 900px) {{
        .minimal-grid {{ grid-template-columns: 1fr; gap: 60px; }}
    }}
    </style>
    '''
