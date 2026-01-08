from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """
    Aura Premium - High-end, dark-themed e-commerce hero with glassmorphism,
    glowing gradients, and sophisticated typography.
    """
    name = props.get("name", props.get("businessName", "AURA"))
    tagline = props.get("tagline", "Redefining Luxury")
    description = props.get("description", "Experience the pinnacle of craftsmanship and design. Our exclusive collection awaits.")
    cta = props.get("cta", "Explore Collection")
    
    # Force a dark/premium palette if specific colors aren't provided
    primary = colors.get("primary", "#D4AF37") # Gold/Metallic
    secondary = colors.get("secondary", "#A8A8A8") # Silver
    bg = colors.get("background", "#0F0F0F") # Deep Black
    text = colors.get("text", "#FFFFFF")
    accent = "#7B2CBF" # Deep Purple accent for aura effect
    
    return f'''
    <section class="aura-hero" id="hero">
        <div class="aura-bg">
            <div class="aura-orb orb-1"></div>
            <div class="aura-orb orb-2"></div>
            <div class="grid-overlay"></div>
        </div>
        
        <div class="container">
            <div class="hero-layout">
                <div class="hero-text-content">
                    <span class="brand-tag">
                        <span class="tag-line"></span>
                        PREMIUM COLLECTION
                    </span>
                    
                    <h1 class="hero-heading">
                        {tagline}
                        <span class="heading-accent">.</span>
                    </h1>
                    
                    <p class="hero-sub">{description}</p>
                    
                    <div class="cta-wrapper">
                        <a href="#products" class="btn-aura-primary">
                            <span>{cta}</span>
                            <div class="btn-glow"></div>
                        </a>
                        <a href="#about" class="btn-aura-secondary">
                            <span>Our Story</span>
                        </a>
                    </div>
                    
                    <div class="stat-row">
                        <div class="stat-item">
                            <span class="stat-val">50k+</span>
                            <span class="stat-label">Exclusive Members</span>
                        </div>
                        <div class="stat-separator"></div>
                        <div class="stat-item">
                            <span class="stat-val">100+</span>
                            <span class="stat-label">Global Brands</span>
                        </div>
                    </div>
                </div>
                
                <div class="hero-visual">
                    <div class="glass-card main-card">
                        <div class="card-content">
                            <span class="card-badge">New Arrival</span>
                            <img src="https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=600" alt="Premium Product" class="product-img">
                            <div class="card-info">
                                <h3>Limitless Edition</h3>
                                <p>Starting at $299</p>
                            </div>
                        </div>
                    </div>
                    
                    <div class="glass-card float-card card-1">
                        <img src="https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=200" alt="Accessory">
                    </div>
                    
                    <div class="glass-card float-card card-2">
                        <img src="https://images.unsplash.com/photo-1572635196237-14b3f281503f?w=200" alt="Accessory">
                    </div>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;700&family=Playfair+Display:ital,wght@0,400;0,700;1,400&display=swap');
    
    .aura-hero {{
        min-height: 100vh;
        background-color: {bg};
        color: {text};
        position: relative;
        overflow: hidden;
        display: flex;
        align-items: center;
        font-family: 'Outfit', sans-serif;
    }}
    
    .aura-bg {{
        position: absolute;
        inset: 0;
        z-index: 0;
    }}
    
    .grid-overlay {{
        position: absolute;
        inset: 0;
        background-image: linear-gradient(rgba(255, 255, 255, 0.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255, 255, 255, 0.03) 1px, transparent 1px);
        background-size: 50px 50px;
        opacity: 0.5;
    }}
    
    .aura-orb {{
        position: absolute;
        border-radius: 50%;
        filter: blur(80px);
        opacity: 0.4;
        animation: floatOrb 10s infinite ease-in-out alternate;
    }}
    
    .orb-1 {{
        width: 500px;
        height: 500px;
        background: {primary};
        top: -100px;
        right: -100px;
        animation-delay: -2s;
    }}
    
    .orb-2 {{
        width: 400px;
        height: 400px;
        background: {accent};
        bottom: -50px;
        left: -100px;
    }}
    
    @keyframes floatOrb {{
        0% {{ transform: translate(0, 0) scale(1); }}
        100% {{ transform: translate(30px, 50px) scale(1.1); }}
    }}
    
    .container {{
        max-width: 1400px;
        margin: 0 auto;
        padding: 0 40px;
        position: relative;
        z-index: 1;
        width: 100%;
    }}
    
    .hero-layout {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 80px;
        align-items: center;
    }}
    
    .brand-tag {{
        display: inline-flex;
        align-items: center;
        gap: 12px;
        font-size: 0.9rem;
        letter-spacing: 4px;
        text-transform: uppercase;
        color: {primary};
        margin-bottom: 30px;
        font-weight: 500;
    }}
    
    .tag-line {{
        width: 40px;
        height: 1px;
        background: {primary};
    }}
    
    .hero-heading {{
        font-family: 'Playfair Display', serif;
        font-size: clamp(3.5rem, 6vw, 5.5rem);
        line-height: 1.1;
        margin-bottom: 30px;
        background: linear-gradient(135deg, {text} 0%, rgba(255,255,255,0.7) 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }}
    
    .heading-accent {{
        color: {primary};
        -webkit-text-fill-color: {primary};
    }}
    
    .hero-sub {{
        font-size: 1.2rem;
        color: rgba(255, 255, 255, 0.7);
        line-height: 1.8;
        margin-bottom: 50px;
        max-width: 500px;
        font-weight: 300;
    }}
    
    .cta-wrapper {{
        display: flex;
        gap: 20px;
        margin-bottom: 60px;
    }}
    
    .btn-aura-primary {{
        position: relative;
        padding: 16px 40px;
        background: transparent;
        border: 1px solid rgba(255, 255, 255, 0.2);
        color: white;
        text-decoration: none;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-size: 0.9rem;
        overflow: hidden;
        transition: all 0.3s;
        backdrop-filter: blur(5px);
    }}
    
    .btn-aura-primary::before {{
        content: '';
        position: absolute;
        inset: 0;
        background: {primary};
        transform: translateX(-100%);
        transition: transform 0.3s ease;
        z-index: -1;
    }}
    
    .btn-aura-primary:hover {{
        border-color: {primary};
    }}
    
    .btn-aura-primary:hover::before {{
        transform: translateX(0);
    }}
    
    .btn-aura-primary span {{
        position: relative;
        z-index: 1;
    }}
    
    .btn-aura-secondary {{
        padding: 16px 40px;
        color: white;
        text-decoration: none;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-size: 0.9rem;
        position: relative;
    }}
    
    .btn-aura-secondary::after {{
        content: '';
        position: absolute;
        bottom: 10px;
        left: 40px;
        right: 40px;
        height: 1px;
        background: rgba(255, 255, 255, 0.3);
        transition: all 0.3s;
    }}
    
    .btn-aura-secondary:hover::after {{
        background: {primary};
        left: 20px;
        right: 20px;
    }}
    
    .stat-row {{
        display: flex;
        align-items: center;
        gap: 30px;
        padding-top: 30px;
        border-top: 1px solid rgba(255, 255, 255, 0.1);
    }}
    
    .stat-item {{
        display: flex;
        flex-direction: column;
    }}
    
    .stat-val {{
        font-size: 1.5rem;
        font-weight: 700;
        color: {text};
        font-family: 'Playfair Display', serif;
    }}
    
    .stat-label {{
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        color: rgba(255, 255, 255, 0.5);
    }}
    
    .stat-separator {{
        width: 1px;
        height: 40px;
        background: rgba(255, 255, 255, 0.1);
    }}
    
    .hero-visual {{
        position: relative;
        height: 600px;
        display: flex;
        align-items: center;
        justify-content: center;
    }}
    
    .glass-card {{
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
    }}
    
    .main-card {{
        width: 100%;
        max-width: 450px;
        padding: 20px;
        position: relative;
        z-index: 2;
        transform: perspective(1000px) rotateY(-5deg);
        transition: transform 0.5s ease;
    }}
    
    .main-card:hover {{
        transform: perspective(1000px) rotateY(0deg);
    }}
    
    .card-content {{
        position: relative;
        border-radius: 12px;
        overflow: hidden;
    }}
    
    .card-badge {{
        position: absolute;
        top: 15px;
        left: 15px;
        background: {primary};
        color: black;
        padding: 6px 16px;
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        z-index: 10;
    }}
    
    .product-img {{
        width: 100%;
        height: 500px;
        object-fit: cover;
        transition: transform 0.7s ease;
    }}
    
    .main-card:hover .product-img {{
        transform: scale(1.05);
    }}
    
    .card-info {{
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        padding: 20px;
        background: linear-gradient(to top, rgba(0,0,0,0.9), transparent);
    }}
    
    .card-info h3 {{
        font-family: 'Playfair Display', serif;
        font-size: 1.5rem;
        margin-bottom: 5px;
    }}
    
    .card-info p {{
        color: {primary};
        font-weight: 500;
    }}
    
    .float-card {{
        padding: 10px;
        position: absolute;
        z-index: 1;
        width: 140px;
        height: 140px;
        display: flex;
        align-items: center;
        justify-content: center;
        animation: floatY 6s infinite ease-in-out;
    }}
    
    .float-card img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        border-radius: 10px;
    }}
    
    .card-1 {{
        top: 50px;
        right: 0;
        animation-delay: -1s;
    }}
    
    .card-2 {{
        bottom: 50px;
        left: 0;
        animation-delay: -3s;
    }}
    
    @keyframes floatY {{
        0%, 100% {{ transform: translateY(0); }}
        50% {{ transform: translateY(-20px); }}
    }}
    
    @media (max-width: 1024px) {{
        .hero-layout {{
            grid-template-columns: 1fr;
            text-align: center;
        }}
        
        .hero-text-content {{
            display: flex;
            flex-direction: column;
            align-items: center;
        }}
        
        .stat-row {{
            width: 100%;
            justify-content: center;
        }}
        
        .hero-visual {{
            height: 500px;
        }}
    }}
    
    @media (max-width: 640px) {{
        .hero-heading {{
            font-size: 3rem;
        }}
        
        .float-card {{
            display: none;
        }}
    }}
    </style>
    '''
