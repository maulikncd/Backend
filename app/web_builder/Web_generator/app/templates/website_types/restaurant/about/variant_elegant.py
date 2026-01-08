from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """
    Elegant Story - Restaurant about section with chef story,
    history and philosophy
    """
    title = props.get("sectionTitle", props.get("title", "Our Story"))
    
    # Handle story - can be string or list of strings
    story_raw = props.get("story", props.get("description", "Founded in 1995, our restaurant has been serving exquisite cuisine for over two decades. Every dish tells a story of passion, tradition, and culinary excellence."))
    if isinstance(story_raw, list):
        # Join list items into paragraphs
        story = " ".join([str(s) for s in story_raw if s])
    else:
        story = str(story_raw)
    
    chef_name = props.get("chefName", "Chef Marco Rossi")
    chef_title = props.get("chefTitle", "Executive Chef")
    
    primary = colors.get("primary", "#C9A962")
    bg = colors.get("background", "#0A0A0A")
    
    # Smart text color - use white for dark backgrounds, dark for light
    text = colors.get("text_on_dark", colors.get("text", "#FFFFFF"))
    text_muted = f"{text}80"

    
    return f'''
    <section class="about-section" id="about">
        <div class="container">
            <div class="about-grid">
                <div class="about-images">
                    <div class="image-main">
                        <img src="https://images.unsplash.com/photo-1600565193348-f74bd3c7ccdf?w=600" alt="Restaurant Interior">
                    </div>
                    <div class="image-secondary">
                        <img src="https://images.unsplash.com/photo-1577219491135-ce391730fb2c?w=400" alt="Chef at work">
                    </div>
                    <div class="experience-badge">
                        <span class="exp-years">25+</span>
                        <span class="exp-text">Years of Excellence</span>
                    </div>
                </div>
                
                <div class="about-content">
                    <span class="section-label">About Us</span>
                    <h2 class="section-title">{title}</h2>
                    <p class="about-story">{story}</p>
                    
                    <div class="philosophy">
                        <div class="philosophy-item">
                            <span class="philosophy-icon">🍃</span>
                            <div>
                                <h4>Fresh Ingredients</h4>
                                <p>Locally sourced, seasonal produce</p>
                            </div>
                        </div>
                        <div class="philosophy-item">
                            <span class="philosophy-icon">👨‍🍳</span>
                            <div>
                                <h4>Expert Craftsmanship</h4>
                                <p>Decades of culinary experience</p>
                            </div>
                        </div>
                    </div>
                    
                    <div class="chef-info">
                        <img src="https://images.unsplash.com/photo-1583394293214-28ez1c79f3a9?w=100" alt="{chef_name}" class="chef-avatar">
                        <div>
                            <h4 class="chef-name">{chef_name}</h4>
                            <p class="chef-title">{chef_title}</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Lato:wght@400;500&display=swap');
    
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
        gap: 100px;
        align-items: center;
    }}
    .about-images {{
        position: relative;
    }}
    .image-main {{
        border-radius: 20px;
        overflow: hidden;
    }}
    .image-main img {{
        width: 100%;
        height: 500px;
        object-fit: cover;
    }}
    .image-secondary {{
        position: absolute;
        bottom: -40px;
        right: -40px;
        width: 250px;
        border-radius: 20px;
        overflow: hidden;
        border: 6px solid {bg};
    }}
    .image-secondary img {{
        width: 100%;
        height: 200px;
        object-fit: cover;
    }}
    .experience-badge {{
        position: absolute;
        top: 30px;
        left: -30px;
        background: {primary};
        padding: 24px 30px;
        border-radius: 16px;
        text-align: center;
    }}
    .exp-years {{
        display: block;
        font-family: 'Cormorant Garamond', serif;
        font-size: 3rem;
        font-weight: 700;
        color: #0A0A0A;
        line-height: 1;
    }}
    .exp-text {{
        font-size: 0.8rem;
        color: #0A0A0A;
        text-transform: uppercase;
        letter-spacing: 1px;
    }}
    .section-label {{
        display: inline-block;
        font-size: 0.85rem;
        color: {primary};
        text-transform: uppercase;
        letter-spacing: 4px;
        margin-bottom: 20px;
    }}
    .section-title {{
        font-family: 'Cormorant Garamond', serif;
        font-size: clamp(2.5rem, 4vw, 3.5rem);
        color: {text};
        margin-bottom: 24px;
    }}
    .about-story {{
        font-size: 1.15rem;
        color: {text}80;
        line-height: 1.9;
        margin-bottom: 40px;
    }}
    .philosophy {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 24px;
        margin-bottom: 40px;
    }}
    .philosophy-item {{
        display: flex;
        gap: 16px;
    }}
    .philosophy-icon {{
        font-size: 2rem;
    }}
    .philosophy-item h4 {{
        font-size: 1rem;
        color: {text};
        margin-bottom: 4px;
    }}
    .philosophy-item p {{
        font-size: 0.9rem;
        color: {text}60;
    }}
    .chef-info {{
        display: flex;
        align-items: center;
        gap: 16px;
        padding-top: 30px;
        border-top: 1px solid {text}15;
    }}
    .chef-avatar {{
        width: 60px;
        height: 60px;
        border-radius: 50%;
        object-fit: cover;
    }}
    .chef-name {{
        font-size: 1.1rem;
        color: {text};
        margin-bottom: 4px;
    }}
    .chef-title {{
        font-size: 0.9rem;
        color: {primary};
    }}
    @media (max-width: 1024px) {{
        .about-grid {{ grid-template-columns: 1fr; gap: 60px; }}
        .image-secondary {{ right: 20px; }}
        .experience-badge {{ left: 20px; }}
    }}
    </style>
    '''
