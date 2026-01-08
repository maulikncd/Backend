from typing import Dict, Any, List

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """
    Story Timeline - About section with personal story,
    timeline of experience, and achievements
    """
    title = props.get("sectionTitle", props.get("title", "About Me"))
    bio = props.get("bio", props.get("description", "I'm a passionate developer with years of experience building digital products. I love turning complex problems into simple, beautiful solutions."))
    name = props.get("name", props.get("businessName", "John Doe"))
    
    primary = colors.get("primary", "#6366F1")
    bg = colors.get("background", "#FFFFFF")
    text = colors.get("text", "#1F2937")
    
    return f'''
    <section class="about-section" id="about">
        <div class="container">
            <div class="about-grid">
                <div class="about-image">
                    <div class="image-wrapper">
                        <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=600" alt="{name}">
                    </div>
                    <div class="image-decoration"></div>
                </div>
                
                <div class="about-content">
                    <span class="section-label">About</span>
                    <h2 class="section-title">{title}</h2>
                    <p class="about-bio">{bio}</p>
                    
                    <div class="timeline">
                        <div class="timeline-item">
                            <span class="timeline-year">2020 - Present</span>
                            <h4 class="timeline-title">Senior Developer @ Tech Corp</h4>
                            <p class="timeline-desc">Leading frontend development for enterprise applications</p>
                        </div>
                        <div class="timeline-item">
                            <span class="timeline-year">2018 - 2020</span>
                            <h4 class="timeline-title">Full Stack Developer @ Startup</h4>
                            <p class="timeline-desc">Built multiple products from scratch</p>
                        </div>
                        <div class="timeline-item">
                            <span class="timeline-year">2016 - 2018</span>
                            <h4 class="timeline-title">Junior Developer @ Agency</h4>
                            <p class="timeline-desc">Started my professional journey</p>
                        </div>
                    </div>
                    
                    <a href="#contact" class="contact-btn">Get in Touch</a>
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
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 40px;
    }}
    .about-grid {{
        display: grid;
        grid-template-columns: 1fr 1.2fr;
        gap: 80px;
        align-items: center;
    }}
    .about-image {{
        position: relative;
    }}
    .image-wrapper {{
        position: relative;
        z-index: 1;
    }}
    .image-wrapper img {{
        width: 100%;
        border-radius: 24px;
        aspect-ratio: 4/5;
        object-fit: cover;
    }}
    .image-decoration {{
        position: absolute;
        top: 30px;
        left: 30px;
        right: -30px;
        bottom: -30px;
        border: 2px solid {primary};
        border-radius: 24px;
        z-index: 0;
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
        font-size: clamp(2rem, 4vw, 3rem);
        font-weight: 700;
        color: {text};
        margin-bottom: 24px;
    }}
    .about-bio {{
        font-size: 1.15rem;
        color: {text}80;
        line-height: 1.9;
        margin-bottom: 40px;
    }}
    .timeline {{
        margin-bottom: 40px;
        padding-left: 30px;
        border-left: 2px solid {primary}30;
    }}
    .timeline-item {{
        position: relative;
        padding-bottom: 30px;
    }}
    .timeline-item:last-child {{
        padding-bottom: 0;
    }}
    .timeline-item::before {{
        content: '';
        position: absolute;
        left: -37px;
        top: 4px;
        width: 12px;
        height: 12px;
        background: {primary};
        border-radius: 50%;
    }}
    .timeline-year {{
        font-size: 0.8rem;
        color: {primary};
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
    }}
    .timeline-title {{
        font-size: 1.1rem;
        font-weight: 600;
        color: {text};
        margin: 8px 0 4px;
    }}
    .timeline-desc {{
        font-size: 0.95rem;
        color: {text}60;
    }}
    .contact-btn {{
        display: inline-block;
        padding: 16px 36px;
        background: {primary};
        color: white;
        text-decoration: none;
        font-weight: 600;
        border-radius: 12px;
        transition: all 0.3s;
    }}
    .contact-btn:hover {{
        transform: translateY(-2px);
        box-shadow: 0 15px 40px {primary}30;
    }}
    @media (max-width: 1024px) {{
        .about-grid {{ grid-template-columns: 1fr; gap: 60px; }}
        .image-decoration {{ display: none; }}
    }}
    @media (max-width: 640px) {{
        .about-section .container {{ padding: 0 24px; }}
    }}
    </style>
    '''
