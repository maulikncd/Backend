from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """
    Agency About - Company story with mission and vision
    """
    title = props.get("sectionTitle", props.get("title", "About Us"))
    story = props.get("story", props.get("description", "We're a team of passionate creators, strategists, and technologists helping brands succeed in the digital age."))
    mission = props.get("mission", "To empower businesses with innovative digital solutions that drive growth and create lasting impact.")
    
    primary = colors.get("primary", "#2563EB")
    bg = colors.get("background", "#F8FAFC")
    text = colors.get("text", "#0F172A")
    
    return f'''
    <section class="about-section" id="about">
        <div class="container">
            <div class="about-grid">
                <div class="about-content">
                    <span class="section-label">About Us</span>
                    <h2 class="section-title">{title}</h2>
                    <p class="about-story">{story}</p>
                    
                    <div class="mission-box">
                        <h4>Our Mission</h4>
                        <p>{mission}</p>
                    </div>
                    
                    <a href="#contact" class="cta-btn">Work With Us</a>
                </div>
                
                <div class="about-visual">
                    <div class="image-grid">
                        <img src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=600" alt="Team" class="img-main">
                        <img src="https://images.unsplash.com/photo-1552664730-d307ca884978?w=400" alt="Meeting" class="img-secondary">
                    </div>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    .about-section {{
        padding: 120px 0;
        background: {bg};
    }}
    .about-section .container {{
        max-width: 1300px;
        margin: 0 auto;
        padding: 0 40px;
    }}
    .about-grid {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 80px;
        align-items: center;
    }}
    .section-label {{
        display: inline-block;
        padding: 8px 20px;
        background: {primary}10;
        color: {primary};
        border-radius: 50px;
        font-size: 0.85rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 20px;
    }}
    .section-title {{
        font-size: clamp(2.5rem, 5vw, 3.5rem);
        font-weight: 700;
        color: {text};
        margin-bottom: 24px;
    }}
    .about-story {{
        font-size: 1.15rem;
        color: {text}80;
        line-height: 1.9;
        margin-bottom: 40px;
    }}
    .mission-box {{
        padding: 30px;
        background: white;
        border-left: 4px solid {primary};
        border-radius: 0 12px 12px 0;
        margin-bottom: 40px;
    }}
    .mission-box h4 {{
        font-size: 1rem;
        color: {primary};
        margin-bottom: 10px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }}
    .mission-box p {{
        font-size: 1rem;
        color: {text}80;
        line-height: 1.7;
    }}
    .cta-btn {{
        display: inline-block;
        padding: 16px 36px;
        background: {primary};
        color: white;
        text-decoration: none;
        font-weight: 600;
        border-radius: 12px;
        transition: all 0.3s;
    }}
    .cta-btn:hover {{
        transform: translateY(-2px);
        box-shadow: 0 10px 30px {primary}30;
    }}
    .image-grid {{
        position: relative;
    }}
    .img-main {{
        width: 100%;
        border-radius: 20px;
        box-shadow: 0 20px 50px rgba(0,0,0,0.1);
    }}
    .img-secondary {{
        position: absolute;
        bottom: -40px;
        left: -40px;
        width: 200px;
        border-radius: 16px;
        border: 6px solid {bg};
        box-shadow: 0 15px 40px rgba(0,0,0,0.15);
    }}
    @media (max-width: 1024px) {{
        .about-grid {{ grid-template-columns: 1fr; gap: 60px; }}
        .img-secondary {{ left: 20px; }}
    }}
    </style>
    '''
