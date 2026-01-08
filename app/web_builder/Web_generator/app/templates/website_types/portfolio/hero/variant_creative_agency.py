from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """
    Creative Agency - Bold asymmetric layout with large typography,
    video background option and creative professional aesthetic
    """
    name = props.get("name", props.get("businessName", "Creative Studio"))
    title = props.get("title", "Creative Director & Designer")
    tagline = props.get("tagline", "I Design. I Create. I Inspire.")
    cta = props.get("cta", "See My Work")
    
    primary = colors.get("primary", "#FF6B6B")
    secondary = colors.get("secondary", "#4ECDC4")
    bg = colors.get("background", "#1A1A2E")
    text = colors.get("text", "#FFFFFF")
    
    return f'''
    <section class="creative-hero" id="hero">
        <div class="hero-bg">
            <div class="bg-shape shape-1"></div>
            <div class="bg-shape shape-2"></div>
            <div class="noise-overlay"></div>
        </div>
        
        <div class="hero-content">
            <div class="intro-line">
                <span class="line"></span>
                <span class="intro-text">Hello, I'm</span>
            </div>
            
            <h1 class="hero-name">
                <span class="name-line">{name.split()[0] if ' ' in name else name}</span>
                <span class="name-line accent">{name.split()[1] if ' ' in name else ''}</span>
            </h1>
            
            <p class="hero-tagline">{tagline}</p>
            
            <div class="hero-meta">
                <span class="meta-item">{title}</span>
                <span class="meta-divider">•</span>
                <span class="meta-item">Based in NYC</span>
            </div>
            
            <div class="cta-wrapper">
                <a href="#projects" class="cta-btn">
                    <span>{cta}</span>
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M5 12h14M12 5l7 7-7 7"/>
                    </svg>
                </a>
                
                <div class="play-reel">
                    <button class="play-btn" aria-label="Play showreel">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                            <path d="M8 5v14l11-7z"/>
                        </svg>
                    </button>
                    <span>Watch Showreel</span>
                </div>
            </div>
        </div>
        
        <div class="side-info">
            <div class="scroll-indicator">
                <span>Scroll</span>
                <div class="scroll-line"></div>
            </div>
            
            <div class="hero-number">
                <span class="num">01</span>
                <span class="total">/06</span>
            </div>
        </div>
        
        <div class="floating-images">
            <div class="float-img img-1">
                <img src="https://images.unsplash.com/photo-1558655146-d09347e92766?w=400" alt="Project 1">
            </div>
            <div class="float-img img-2">
                <img src="https://images.unsplash.com/photo-1561070791-2526d30994b5?w=300" alt="Project 2">
            </div>
        </div>
    </section>
    
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&display=swap');
    
    .creative-hero {{
        min-height: 100vh;
        background: {bg};
        position: relative;
        display: flex;
        align-items: center;
        padding: 120px 80px;
        overflow: hidden;
    }}
    .hero-bg {{
        position: absolute;
        inset: 0;
    }}
    .bg-shape {{
        position: absolute;
        border-radius: 50%;
    }}
    .shape-1 {{
        width: 800px;
        height: 800px;
        background: linear-gradient(135deg, {primary}30, transparent);
        top: -400px;
        right: -300px;
        filter: blur(100px);
    }}
    .shape-2 {{
        width: 500px;
        height: 500px;
        background: linear-gradient(135deg, {secondary}20, transparent);
        bottom: -200px;
        left: -100px;
        filter: blur(80px);
    }}
    .noise-overlay {{
        position: absolute;
        inset: 0;
        background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E");
        opacity: 0.03;
    }}
    .hero-content {{
        position: relative;
        z-index: 2;
        max-width: 900px;
    }}
    .intro-line {{
        display: flex;
        align-items: center;
        gap: 20px;
        margin-bottom: 30px;
    }}
    .line {{
        width: 60px;
        height: 2px;
        background: {primary};
    }}
    .intro-text {{
        font-size: 1.1rem;
        color: rgba(255,255,255,0.6);
        text-transform: uppercase;
        letter-spacing: 3px;
    }}
    .hero-name {{
        font-family: 'Outfit', sans-serif;
        font-size: clamp(4rem, 12vw, 10rem);
        font-weight: 900;
        line-height: 0.95;
        margin-bottom: 30px;
    }}
    .name-line {{
        display: block;
        color: {text};
    }}
    .name-line.accent {{
        color: {primary};
        -webkit-text-stroke: 2px {primary};
        -webkit-text-fill-color: transparent;
    }}
    .hero-tagline {{
        font-size: 1.5rem;
        color: rgba(255,255,255,0.7);
        margin-bottom: 20px;
        max-width: 500px;
    }}
    .hero-meta {{
        display: flex;
        align-items: center;
        gap: 16px;
        margin-bottom: 50px;
        color: rgba(255,255,255,0.5);
        font-size: 0.95rem;
    }}
    .meta-divider {{
        color: {primary};
    }}
    .cta-wrapper {{
        display: flex;
        align-items: center;
        gap: 40px;
    }}
    .cta-btn {{
        display: inline-flex;
        align-items: center;
        gap: 14px;
        padding: 20px 40px;
        background: {primary};
        color: white;
        text-decoration: none;
        font-weight: 600;
        font-size: 1.1rem;
        border-radius: 60px;
        transition: all 0.4s;
    }}
    .cta-btn:hover {{
        transform: scale(1.05);
        box-shadow: 0 20px 50px {primary}50;
    }}
    .cta-btn svg {{
        transition: transform 0.3s;
    }}
    .cta-btn:hover svg {{
        transform: translateX(5px);
    }}
    .play-reel {{
        display: flex;
        align-items: center;
        gap: 16px;
        color: rgba(255,255,255,0.7);
        cursor: pointer;
        transition: color 0.3s;
    }}
    .play-reel:hover {{
        color: white;
    }}
    .play-btn {{
        width: 60px;
        height: 60px;
        background: transparent;
        border: 2px solid rgba(255,255,255,0.3);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        cursor: pointer;
        transition: all 0.3s;
    }}
    .play-btn:hover {{
        border-color: {primary};
        background: {primary};
    }}
    .side-info {{
        position: absolute;
        right: 60px;
        top: 50%;
        transform: translateY(-50%);
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 60px;
    }}
    .scroll-indicator {{
        writing-mode: vertical-rl;
        display: flex;
        align-items: center;
        gap: 20px;
        color: rgba(255,255,255,0.5);
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 2px;
    }}
    .scroll-line {{
        width: 1px;
        height: 80px;
        background: linear-gradient(to bottom, {primary}, transparent);
    }}
    .hero-number {{
        font-family: 'Outfit', sans-serif;
    }}
    .num {{
        font-size: 2.5rem;
        font-weight: 700;
        color: {primary};
    }}
    .total {{
        font-size: 1rem;
        color: rgba(255,255,255,0.4);
    }}
    .floating-images {{
        position: absolute;
        right: 15%;
        top: 55%;
        transform: translateY(-50%);
    }}
    .float-img {{
        position: absolute;
        border-radius: 20px;
        overflow: hidden;
        box-shadow: 0 30px 60px rgba(0,0,0,0.3);
    }}
    .float-img img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
    }}
    .img-1 {{
        width: 280px;
        height: 350px;
        transform: rotate(-5deg);
        animation: floatA 6s ease-in-out infinite;
    }}
    .img-2 {{
        width: 200px;
        height: 250px;
        top: 200px;
        left: 200px;
        transform: rotate(5deg);
        animation: floatB 6s ease-in-out infinite;
        animation-delay: 1s;
    }}
    @keyframes floatA {{
        0%, 100% {{ transform: rotate(-5deg) translateY(0); }}
        50% {{ transform: rotate(-5deg) translateY(-20px); }}
    }}
    @keyframes floatB {{
        0%, 100% {{ transform: rotate(5deg) translateY(0); }}
        50% {{ transform: rotate(5deg) translateY(-15px); }}
    }}
    @media (max-width: 1200px) {{
        .floating-images {{ display: none; }}
        .side-info {{ right: 30px; }}
    }}
    @media (max-width: 768px) {{
        .creative-hero {{ padding: 100px 24px; }}
        .side-info {{ display: none; }}
        .cta-wrapper {{ flex-direction: column; align-items: flex-start; gap: 24px; }}
        .play-reel span {{ display: none; }}
    }}
    </style>
    '''
