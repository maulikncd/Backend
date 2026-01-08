from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Quote Centered - Large quote with image background"""
    title = props.get("sectionTitle", "Our Philosophy")
    story = props.get("story", "Food is not just eating energy. It's an experience.")
    mission = props.get("mission", "We create moments that become memories")
    
    primary = colors.get("primary", "#D4AF37")
    text = colors.get("text", "#FFFFFF")
    
    return f'''
    <section class="about-quote" id="about">
        <div class="quote-bg">
            <img src="https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1920" alt="Restaurant">
            <div class="bg-overlay"></div>
        </div>
        
        <div class="quote-content">
            <span class="section-label">Our Philosophy</span>
            <blockquote class="main-quote">{story}</blockquote>
            <p class="quote-author">— Chef Marco Rosetti</p>
            <div class="quote-divider"></div>
            <p class="mission">{mission}</p>
            <a href="#reservation" class="btn-quote">Reserve a Table</a>
        </div>
    </section>
    
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400&family=Montserrat:wght@300;400;500&display=swap');
    
    .about-quote {{
        min-height: 100vh;
        position: relative;
        display: flex;
        align-items: center;
        justify-content: center;
    }}
    .quote-bg {{
        position: absolute;
        inset: 0;
    }}
    .quote-bg img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
    }}
    .bg-overlay {{
        position: absolute;
        inset: 0;
        background: rgba(0,0,0,0.75);
    }}
    .quote-content {{
        position: relative;
        z-index: 2;
        text-align: center;
        max-width: 900px;
        padding: 60px 40px;
    }}
    .section-label {{
        color: {primary};
        font-size: 0.85rem;
        letter-spacing: 4px;
        text-transform: uppercase;
        display: block;
        margin-bottom: 40px;
    }}
    .main-quote {{
        font-family: 'Cormorant Garamond', serif;
        font-size: clamp(2rem, 5vw, 3.5rem);
        font-style: italic;
        color: {text};
        line-height: 1.5;
        margin-bottom: 30px;
        position: relative;
    }}
    .main-quote::before {{
        content: '"';
        position: absolute;
        top: -40px;
        left: 50%;
        transform: translateX(-50%);
        font-size: 6rem;
        color: {primary}30;
        font-family: serif;
    }}
    .quote-author {{
        color: {primary};
        font-size: 1.1rem;
        letter-spacing: 2px;
        margin-bottom: 40px;
    }}
    .quote-divider {{
        width: 60px;
        height: 2px;
        background: {primary};
        margin: 0 auto 40px;
    }}
    .mission {{
        font-family: 'Montserrat', sans-serif;
        font-size: 1.2rem;
        color: {text}90;
        margin-bottom: 50px;
    }}
    .btn-quote {{
        display: inline-block;
        padding: 20px 60px;
        background: transparent;
        border: 1px solid {primary};
        color: {primary};
        text-decoration: none;
        font-size: 0.9rem;
        letter-spacing: 2px;
        text-transform: uppercase;
        transition: all 0.4s;
    }}
    .btn-quote:hover {{
        background: {primary};
        color: #0A0A0A;
    }}
    @media (max-width: 768px) {{
        .quote-content {{ padding: 40px 25px; }}
    }}
    </style>
    '''
