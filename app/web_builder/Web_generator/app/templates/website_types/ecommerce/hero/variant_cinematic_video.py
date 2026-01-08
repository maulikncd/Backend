from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """
    Cinematic Video Hero - Immersive full-screen video background with minimal
    overlay text and sophisticated glassmorphism controls.
    """
    tagline = props.get("tagline", "The Future of Fashion")
    description = props.get("description", "Immerse yourself in a world of uncompromising style and innovation.")
    cta = props.get("cta", "Watch Collection")
    
    primary = colors.get("primary", "#FFFFFF")
    text = colors.get("text", "#FFFFFF")
    
    # Using a high-quality fashion placeholder video
    video_poster = "https://images.unsplash.com/photo-1469334031218-e382a71b716b?w=1920"
    
    return f'''
    <section class="cinematic-hero" id="hero">
        <div class="video-container">
            <img src="{video_poster}" class="video-placeholder" alt="Background">
            <div class="video-overlay"></div>
        </div>
        
        <div class="content-layer">
            <div class="hero-brand">
                <span class="brand-line"></span>
                <span class="brand-text">CINEMATIC</span>
                <span class="brand-line"></span>
            </div>
            
            <h1 class="hero-title">
                <span class="reveal-text">{tagline}</span>
            </h1>
            
            <div class="hero-actions">
                <a href="#products" class="btn-glass">
                    <span class="btn-text">Shop Now</span>
                    <span class="btn-arrow">→</span>
                </a>
                <button class="btn-play">
                    <span class="play-icon">▶</span>
                    <span>{cta}</span>
                </button>
            </div>
            
            <div class="scroll-indicator">
                <span>Explore</span>
                <div class="scroll-track">
                    <div class="scroll-thumb"></div>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    .cinematic-hero {{
        height: 100vh;
        width: 100%;
        position: relative;
        overflow: hidden;
        background: #000;
        color: {text};
        display: flex;
        align-items: center;
        justify-content: center;
    }}
    
    .video-container {{
        position: absolute;
        inset: 0;
        z-index: 0;
    }}
    
    .video-placeholder {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        animation: slowZoom 20s infinite alternate;
    }}
    
    @keyframes slowZoom {{
        from {{ transform: scale(1); }}
        to {{ transform: scale(1.1); }}
    }}
    
    .video-overlay {{
        position: absolute;
        inset: 0;
        background: linear-gradient(
            to bottom,
            rgba(0,0,0,0.3),
            rgba(0,0,0,0.6)
        );
    }}
    
    .content-layer {{
        position: relative;
        z-index: 2;
        text-align: center;
        padding: 0 20px;
        max-width: 1200px;
    }}
    
    .hero-brand {{
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 15px;
        margin-bottom: 40px;
        opacity: 0;
        animation: fadeInDown 1s ease-out forwards 0.5s;
    }}
    
    .brand-line {{
        width: 40px;
        height: 1px;
        background: rgba(255,255,255,0.5);
    }}
    
    .brand-text {{
        font-family: 'Montserrat', sans-serif;
        font-size: 0.9rem;
        letter-spacing: 4px;
        text-transform: uppercase;
    }}
    
    .hero-title {{
        font-family: 'Didot', 'Playfair Display', serif;
        font-size: clamp(4rem, 8vw, 7rem);
        font-weight: 400;
        line-height: 1;
        margin-bottom: 50px;
        overflow: hidden;
    }}
    
    .reveal-text {{
        display: block;
        animation: revealText 1.5s cubic-bezier(0.77, 0, 0.175, 1) forwards;
        transform: translateY(100%);
    }}
    
    @keyframes revealText {{
        from {{ transform: translateY(100%); opacity: 0; }}
        to {{ transform: translateY(0); opacity: 1; }}
    }}
    
    .hero-actions {{
        display: flex;
        gap: 20px;
        justify-content: center;
        opacity: 0;
        animation: fadeInUp 1s ease-out forwards 1s;
    }}
    
    .btn-glass {{
        display: flex;
        align-items: center;
        gap: 10px;
        padding: 16px 40px;
        background: rgba(255,255,255,0.1);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.2);
        color: white;
        text-decoration: none;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-size: 0.8rem;
        transition: all 0.3s;
    }}
    
    .btn-glass:hover {{
        background: white;
        color: black;
    }}
    
    .btn-play {{
        display: flex;
        align-items: center;
        gap: 10px;
        background: transparent;
        border: none;
        color: white;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-size: 0.8rem;
        cursor: pointer;
        transition: opacity 0.3s;
    }}
    
    .btn-play:hover {{
        opacity: 0.8;
    }}
    
    .play-icon {{
        width: 40px;
        height: 40px;
        border: 1px solid rgba(255,255,255,0.3);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 0.8rem;
    }}
    
    .scroll-indicator {{
        position: absolute;
        bottom: 40px;
        left: 50%;
        transform: translateX(-50%);
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 15px;
        font-size: 0.7rem;
        text-transform: uppercase;
        letter-spacing: 3px;
        opacity: 0.7;
    }}
    
    .scroll-track {{
        width: 1px;
        height: 60px;
        background: rgba(255,255,255,0.2);
        position: relative;
        overflow: hidden;
    }}
    
    .scroll-thumb {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 50%;
        background: white;
        animation: scrollDown 2s infinite;
    }}
    
    @keyframes scrollDown {{
        0% {{ transform: translateY(-100%); }}
        100% {{ transform: translateY(200%); }}
    }}
    
    @keyframes fadeInDown {{
        from {{ opacity: 0; transform: translateY(-20px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}
    
    @keyframes fadeInUp {{
        from {{ opacity: 0; transform: translateY(20px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}
    </style>
    '''
