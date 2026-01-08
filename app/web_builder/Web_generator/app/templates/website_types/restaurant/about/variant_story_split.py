from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Story Split - Split layout with storytelling focus"""
    title = props.get("sectionTitle", "Our Story")
    story = props.get("story", "Founded with a passion for authentic flavors")
    mission = props.get("mission", "To bring people together through exceptional food")
    
    primary = colors.get("primary", "#C17F59")
    bg = colors.get("background", "#FDFBF7")
    text = colors.get("text", "#2D2013")
    
    return f'''
    <section class="about-story" id="about">
        <div class="story-grid">
            <div class="story-images">
                <div class="image-main">
                    <img src="https://images.unsplash.com/photo-1466978913421-dad2ebd01d17?w=800" alt="Restaurant">
                </div>
                <div class="image-accent">
                    <img src="https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=400" alt="Dish">
                </div>
                <div class="year-badge">Est. 2010</div>
            </div>
            
            <div class="story-content">
                <span class="section-label">About Us</span>
                <h2 class="section-title">{title}</h2>
                <div class="story-divider"></div>
                <p class="story-text">{story}</p>
                <p class="mission-text">"{mission}"</p>
                
                <div class="stats-row">
                    <div class="stat-item">
                        <span class="stat-num">15</span>
                        <span class="stat-label">Years of Excellence</span>
                    </div>
                    <div class="stat-item">
                        <span class="stat-num">50K+</span>
                        <span class="stat-label">Happy Guests</span>
                    </div>
                </div>
                
                <a href="#menu" class="btn-story">Explore Our Menu</a>
            </div>
        </div>
    </section>
    
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600&family=Lora:wght@400;500&display=swap');
    
    .about-story {{
        padding: 120px 60px;
        background: {bg};
    }}
    .story-grid {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 80px;
        max-width: 1300px;
        margin: 0 auto;
        align-items: center;
    }}
    .story-images {{
        position: relative;
    }}
    .image-main img {{
        width: 100%;
        height: 500px;
        object-fit: cover;
        border-radius: 20px;
    }}
    .image-accent {{
        position: absolute;
        bottom: -40px;
        right: -40px;
        width: 200px;
        height: 200px;
        border-radius: 20px;
        overflow: hidden;
        border: 6px solid {bg};
        box-shadow: 0 20px 50px rgba(0,0,0,0.1);
    }}
    .image-accent img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
    }}
    .year-badge {{
        position: absolute;
        top: 30px;
        left: 30px;
        padding: 15px 30px;
        background: {primary};
        color: white;
        font-size: 0.9rem;
        letter-spacing: 2px;
        border-radius: 50px;
    }}
    .story-content {{
        padding: 20px 0;
    }}
    .section-label {{
        display: inline-block;
        color: {primary};
        font-size: 0.85rem;
        letter-spacing: 3px;
        text-transform: uppercase;
        margin-bottom: 15px;
    }}
    .section-title {{
        font-family: 'Playfair Display', serif;
        font-size: clamp(2.5rem, 5vw, 4rem);
        color: {text};
        margin-bottom: 20px;
    }}
    .story-divider {{
        width: 60px;
        height: 3px;
        background: {primary};
        margin-bottom: 30px;
    }}
    .story-text {{
        font-family: 'Lora', serif;
        font-size: 1.15rem;
        color: {text}CC;
        line-height: 1.9;
        margin-bottom: 25px;
    }}
    .mission-text {{
        font-family: 'Playfair Display', serif;
        font-size: 1.3rem;
        color: {primary};
        font-style: italic;
        padding-left: 25px;
        border-left: 3px solid {primary}50;
        margin-bottom: 40px;
    }}
    .stats-row {{
        display: flex;
        gap: 50px;
        margin-bottom: 40px;
    }}
    .stat-item {{
        display: flex;
        flex-direction: column;
        gap: 5px;
    }}
    .stat-num {{
        font-family: 'Playfair Display', serif;
        font-size: 2.5rem;
        color: {primary};
        font-weight: 600;
    }}
    .stat-label {{
        font-size: 0.9rem;
        color: {text}80;
    }}
    .btn-story {{
        display: inline-block;
        padding: 18px 45px;
        background: {primary};
        color: white;
        text-decoration: none;
        border-radius: 50px;
        font-weight: 500;
        transition: all 0.3s;
    }}
    .btn-story:hover {{
        transform: translateY(-3px);
        box-shadow: 0 15px 40px {primary}40;
    }}
    @media (max-width: 968px) {{
        .about-story {{ padding: 80px 30px; }}
        .story-grid {{ grid-template-columns: 1fr; gap: 60px; }}
        .image-accent {{ right: 20px; bottom: -30px; }}
    }}
    </style>
    '''
