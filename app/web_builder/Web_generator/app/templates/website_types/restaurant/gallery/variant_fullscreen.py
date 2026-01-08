from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Fullscreen Showcase - Single fullscreen image sections"""
    title = props.get("sectionTitle", "Experience")
    
    primary = colors.get("primary", "#D4AF37")
    text = colors.get("text", "#FFFFFF")
    
    return f'''
    <section class="gallery-fullscreen" id="gallery">
        <div class="fullscreen-item">
            <img src="https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=1920" alt="">
            <div class="item-overlay">
                <h3>The Dining Experience</h3>
                <p>Elegant atmosphere for memorable moments</p>
            </div>
        </div>
        <div class="fullscreen-item">
            <img src="https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=1920" alt="">
            <div class="item-overlay">
                <h3>Culinary Art</h3>
                <p>Every dish is a masterpiece</p>
            </div>
        </div>
    </section>
    
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500&display=swap');
    
    .gallery-fullscreen {{
        display: flex;
        flex-direction: column;
    }}
    .fullscreen-item {{
        position: relative;
        height: 100vh;
        overflow: hidden;
    }}
    .fullscreen-item img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
    }}
    .item-overlay {{
        position: absolute;
        inset: 0;
        background: rgba(0,0,0,0.5);
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        padding: 40px;
    }}
    .item-overlay h3 {{
        font-family: 'Playfair Display', serif;
        font-size: clamp(3rem, 8vw, 5rem);
        color: {text};
        margin-bottom: 20px;
    }}
    .item-overlay p {{
        font-size: 1.2rem;
        color: {text}90;
        max-width: 500px;
    }}
    </style>
    '''
