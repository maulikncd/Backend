from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Parallax Scroll - Parallax scrolling sections"""
    title = props.get("sectionTitle", "Our Story")
    story = props.get("story", "A journey of passion and flavor")
    
    primary = colors.get("primary", "#E63946")
    bg = colors.get("background", "#FFFFFF")
    text = colors.get("text", "#1A1A1A")
    
    return f'''
    <section class="about-parallax" id="about">
        <div class="parallax-section sec-1">
            <div class="parallax-bg" style="background-image: url('https://images.unsplash.com/photo-1466978913421-dad2ebd01d17?w=1920')"></div>
            <div class="parallax-content">
                <span class="label">Our Story</span>
                <h2>{title}</h2>
            </div>
        </div>
        
        <div class="content-section">
            <div class="content-grid">
                <div class="content-text">
                    <p class="lead">{story}</p>
                    <p>What started as a small family kitchen has grown into one of the city's most beloved dining destinations. Our journey began with a simple belief: great food brings people together.</p>
                    <p>Today, we continue to honor that tradition while embracing innovation. Every dish tells a story, every meal creates a memory.</p>
                </div>
                <div class="content-image">
                    <img src="https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=600" alt="Food">
                </div>
            </div>
        </div>
        
        <div class="parallax-section sec-2">
            <div class="parallax-bg" style="background-image: url('https://images.unsplash.com/photo-1577219491135-ce391730fb2c?w=1920')"></div>
            <div class="parallax-content">
                <span class="label">Our Promise</span>
                <h3>Excellence in Every Bite</h3>
            </div>
        </div>
    </section>
    
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600&family=Source+Sans+Pro:wght@300;400;600&display=swap');
    
    .about-parallax {{
        background: {bg};
    }}
    .parallax-section {{
        height: 70vh;
        position: relative;
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
    }}
    .parallax-bg {{
        position: absolute;
        inset: -20%;
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    .parallax-section::after {{
        content: '';
        position: absolute;
        inset: 0;
        background: rgba(0,0,0,0.6);
    }}
    .parallax-content {{
        position: relative;
        z-index: 2;
        text-align: center;
        color: white;
    }}
    .parallax-content .label {{
        display: block;
        font-size: 0.85rem;
        letter-spacing: 4px;
        text-transform: uppercase;
        color: {primary};
        margin-bottom: 20px;
    }}
    .parallax-content h2 {{
        font-family: 'Playfair Display', serif;
        font-size: clamp(3rem, 8vw, 5rem);
        font-weight: 400;
    }}
    .parallax-content h3 {{
        font-family: 'Playfair Display', serif;
        font-size: clamp(2rem, 5vw, 3rem);
        font-weight: 400;
    }}
    .content-section {{
        padding: 100px 60px;
    }}
    .content-grid {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 80px;
        max-width: 1200px;
        margin: 0 auto;
        align-items: center;
    }}
    .content-text .lead {{
        font-family: 'Playfair Display', serif;
        font-size: 1.8rem;
        color: {text};
        line-height: 1.5;
        margin-bottom: 30px;
    }}
    .content-text p {{
        font-family: 'Source Sans Pro', sans-serif;
        font-size: 1.1rem;
        color: {text}90;
        line-height: 1.8;
        margin-bottom: 20px;
    }}
    .content-image img {{
        width: 100%;
        height: 500px;
        object-fit: cover;
        border-radius: 20px;
    }}
    @media (max-width: 968px) {{
        .content-section {{ padding: 80px 30px; }}
        .content-grid {{ grid-template-columns: 1fr; gap: 40px; }}
        .parallax-bg {{ background-attachment: scroll; }}
    }}
    </style>
    '''
