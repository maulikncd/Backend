from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Video Background - Immersive video with overlaid content"""
    title = props.get("sectionTitle", "Our Philosophy")
    story = props.get("story", "We believe in the power of gathering around good food")
    mission = props.get("mission", "Creating memorable experiences one dish at a time")
    
    primary = colors.get("primary", "#D4AF37")
    text = colors.get("text", "#FFFFFF")
    
    return f'''
    <section class="about-video" id="about">
        <div class="video-wrapper">
            <video autoplay muted loop playsinline>
                <source src="https://assets.mixkit.co/videos/preview/mixkit-hands-of-a-woman-cooking-food-43790-large.mp4" type="video/mp4">
            </video>
            <div class="video-overlay"></div>
        </div>
        
        <div class="about-content">
            <div class="content-inner">
                <span class="section-label">About Us</span>
                <h2 class="section-title">{title}</h2>
                <div class="content-divider"></div>
                <p class="story-text">{story}</p>
                <p class="mission-quote">"{mission}"</p>
                
                <div class="values-row">
                    <div class="value-item">
                        <div class="value-icon">🌱</div>
                        <h4>Farm Fresh</h4>
                        <p>Locally sourced ingredients</p>
                    </div>
                    <div class="value-item">
                        <div class="value-icon">👨‍🍳</div>
                        <h4>Artisan Craft</h4>
                        <p>Handcrafted with passion</p>
                    </div>
                    <div class="value-item">
                        <div class="value-icon">❤️</div>
                        <h4>Made with Love</h4>
                        <p>Every dish tells a story</p>
                    </div>
                </div>
                
                <a href="#menu" class="btn-explore">Explore Menu</a>
            </div>
        </div>
    </section>
    
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600&family=Poppins:wght@300;400;500&display=swap');
    
    .about-video {{
        min-height: 100vh;
        position: relative;
        display: flex;
        align-items: center;
        justify-content: center;
    }}
    .video-wrapper {{
        position: absolute;
        inset: 0;
    }}
    .video-wrapper video {{
        width: 100%;
        height: 100%;
        object-fit: cover;
    }}
    .video-overlay {{
        position: absolute;
        inset: 0;
        background: linear-gradient(135deg, rgba(0,0,0,0.85) 0%, rgba(0,0,0,0.6) 100%);
    }}
    .about-content {{
        position: relative;
        z-index: 2;
        text-align: center;
        max-width: 900px;
        padding: 60px 40px;
    }}
    .content-inner {{
        background: rgba(255,255,255,0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 30px;
        padding: 60px;
    }}
    .section-label {{
        color: {primary};
        font-size: 0.85rem;
        letter-spacing: 4px;
        text-transform: uppercase;
        display: block;
        margin-bottom: 20px;
    }}
    .section-title {{
        font-family: 'Playfair Display', serif;
        font-size: clamp(2.5rem, 6vw, 4rem);
        color: {text};
        margin-bottom: 25px;
    }}
    .content-divider {{
        width: 80px;
        height: 2px;
        background: {primary};
        margin: 0 auto 30px;
    }}
    .story-text {{
        font-family: 'Poppins', sans-serif;
        font-size: 1.2rem;
        color: {text}CC;
        line-height: 1.8;
        margin-bottom: 25px;
        max-width: 700px;
        margin-left: auto;
        margin-right: auto;
    }}
    .mission-quote {{
        font-family: 'Playfair Display', serif;
        font-size: 1.4rem;
        color: {primary};
        font-style: italic;
        margin-bottom: 50px;
    }}
    .values-row {{
        display: flex;
        justify-content: center;
        gap: 60px;
        margin-bottom: 50px;
        flex-wrap: wrap;
    }}
    .value-item {{
        text-align: center;
    }}
    .value-icon {{
        font-size: 2.5rem;
        margin-bottom: 15px;
    }}
    .value-item h4 {{
        color: {text};
        font-size: 1.1rem;
        margin-bottom: 8px;
    }}
    .value-item p {{
        color: {text}80;
        font-size: 0.9rem;
    }}
    .btn-explore {{
        display: inline-block;
        padding: 18px 50px;
        background: {primary};
        color: #0A0A0A;
        text-decoration: none;
        font-weight: 600;
        letter-spacing: 1px;
        transition: all 0.3s;
    }}
    .btn-explore:hover {{
        transform: translateY(-3px);
        box-shadow: 0 15px 40px {primary}50;
    }}
    @media (max-width: 768px) {{
        .content-inner {{ padding: 40px 25px; }}
        .values-row {{ gap: 30px; }}
    }}
    </style>
    '''
