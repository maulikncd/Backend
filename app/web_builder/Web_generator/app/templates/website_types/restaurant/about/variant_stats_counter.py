from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Stats Counter - Big numbers with counter animation"""
    title = props.get("sectionTitle", "By The Numbers")
    story = props.get("story", "Our achievements speak for themselves")
    
    primary = colors.get("primary", "#C9A962")
    bg = colors.get("background", "#0A0A0A")
    text = colors.get("text", "#FFFFFF")
    
    return f'''
    <section class="about-stats" id="about">
        <div class="stats-container">
            <div class="stats-header">
                <span class="label">About Us</span>
                <h2 class="title">{title}</h2>
                <p class="subtitle">{story}</p>
            </div>
            
            <div class="stats-grid">
                <div class="stat-card">
                    <div class="stat-number" data-count="15">15+</div>
                    <div class="stat-label">Years of Excellence</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number" data-count="50000">50K+</div>
                    <div class="stat-label">Happy Guests</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number" data-count="120">120+</div>
                    <div class="stat-label">Signature Dishes</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number" data-count="25">25+</div>
                    <div class="stat-label">Awards Won</div>
                </div>
            </div>
            
            <div class="about-story">
                <div class="story-content">
                    <h3>Our Story</h3>
                    <p>Founded in 2010, we've grown from a small family kitchen to one of the city's most beloved dining destinations. Our commitment to quality, authenticity, and exceptional service remains unchanged.</p>
                    <a href="#menu" class="link-arrow">View Our Menu →</a>
                </div>
                <div class="story-image">
                    <img src="https://images.unsplash.com/photo-1466978913421-dad2ebd01d17?w=600" alt="Restaurant">
                </div>
            </div>
        </div>
    </section>
    
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600&family=Lato:wght@300;400&display=swap');
    
    .about-stats {{
        padding: 120px 60px;
        background: {bg};
    }}
    .stats-container {{
        max-width: 1200px;
        margin: 0 auto;
    }}
    .stats-header {{
        text-align: center;
        margin-bottom: 70px;
    }}
    .stats-header .label {{
        color: {primary};
        font-size: 0.85rem;
        letter-spacing: 3px;
        text-transform: uppercase;
        display: block;
        margin-bottom: 15px;
    }}
    .stats-header .title {{
        font-family: 'Playfair Display', serif;
        font-size: clamp(2.5rem, 5vw, 4rem);
        color: {text};
        margin-bottom: 15px;
    }}
    .stats-header .subtitle {{
        color: {text}80;
        font-size: 1.1rem;
    }}
    .stats-grid {{
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 30px;
        margin-bottom: 80px;
    }}
    .stat-card {{
        text-align: center;
        padding: 40px 20px;
        background: rgba(255,255,255,0.03);
        border: 1px solid {text}10;
        border-radius: 20px;
        transition: all 0.3s;
    }}
    .stat-card:hover {{
        background: rgba(255,255,255,0.06);
        transform: translateY(-5px);
    }}
    .stat-number {{
        font-family: 'Playfair Display', serif;
        font-size: 4rem;
        font-weight: 600;
        color: {primary};
        margin-bottom: 10px;
    }}
    .stat-label {{
        color: {text}80;
        font-size: 0.95rem;
        letter-spacing: 1px;
    }}
    .about-story {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 60px;
        align-items: center;
    }}
    .story-content h3 {{
        font-family: 'Playfair Display', serif;
        font-size: 2rem;
        color: {text};
        margin-bottom: 20px;
    }}
    .story-content p {{
        color: {text}90;
        line-height: 1.8;
        margin-bottom: 25px;
    }}
    .link-arrow {{
        color: {primary};
        text-decoration: none;
        font-weight: 500;
        transition: all 0.3s;
    }}
    .link-arrow:hover {{ letter-spacing: 2px; }}
    .story-image img {{
        width: 100%;
        height: 400px;
        object-fit: cover;
        border-radius: 20px;
    }}
    @media (max-width: 968px) {{
        .stats-grid {{ grid-template-columns: repeat(2, 1fr); }}
        .about-story {{ grid-template-columns: 1fr; }}
    }}
    @media (max-width: 600px) {{
        .about-stats {{ padding: 80px 30px; }}
        .stats-grid {{ grid-template-columns: 1fr; }}
    }}
    </style>
    '''
