from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """
    Aura Premium - Sophisticated hero with split layout, 
    elegant typography and premium coffee photography
    """
    title = props.get("title", "Crafted with Passion")
    subtitle = props.get("subtitle", "Where every cup tells a story")
    description = props.get("description", "Experience the art of coffee making in our cozy sanctuary.")
    cta = props.get("cta", "Explore Menu")
    cta_secondary = props.get("ctaSecondary", "Book a Table")
    
    # Use colors from user's selected palette - no hardcoded fallbacks
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    bg = colors.get("background")
    text = colors.get("text")
    accent = colors.get("accent")
    
    return f'''
    <section class="aura-hero" id="hero">
        <div class="hero-grid">
            <div class="hero-left">
                <div class="hero-content">
                    <div class="badge-elegant">
                        <span class="badge-icon">☕</span>
                        <span>Artisan Coffee House</span>
                    </div>
                    <h1 class="hero-title">{title}</h1>
                    <p class="hero-subtitle">{subtitle}</p>
                    <p class="hero-desc">{description}</p>
                    <div class="cta-group">
                        <a href="#menu" class="btn-primary-elegant">{cta}</a>
                        <a href="#contact" class="btn-outline-elegant">{cta_secondary}</a>
                    </div>
                    <div class="hero-stats">
                        <div class="stat-item">
                            <span class="stat-value">15+</span>
                            <span class="stat-label">Years Experience</span>
                        </div>
                        <div class="stat-divider"></div>
                        <div class="stat-item">
                            <span class="stat-value">50K+</span>
                            <span class="stat-label">Happy Customers</span>
                        </div>
                        <div class="stat-divider"></div>
                        <div class="stat-item">
                            <span class="stat-value">30+</span>
                            <span class="stat-label">Coffee Varieties</span>
                        </div>
                    </div>
                </div>
            </div>
            <div class="hero-right">
                <div class="image-container">
                    <div class="main-image">
                        <img src="https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=800" alt="Coffee">
                    </div>
                    <div class="floating-card card-1">
                        <span class="card-icon">🌟</span>
                        <div class="card-text">
                            <span class="card-title">4.9 Rating</span>
                            <span class="card-sub">500+ Reviews</span>
                        </div>
                    </div>
                    <div class="floating-card card-2">
                        <span class="card-icon">🏆</span>
                        <div class="card-text">
                            <span class="card-title">Award Winning</span>
                            <span class="card-sub">Best Cafe 2024</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="scroll-indicator">
            <div class="scroll-line"></div>
            <span>Scroll to explore</span>
        </div>
    </section>
    
    <style>
    .aura-hero {{
        min-height: 100vh;
        background: {bg};
        display: flex;
        flex-direction: column;
        justify-content: center;
        padding: 120px 60px 60px;
        position: relative;
        overflow: hidden;
    }}
    .hero-grid {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 80px;
        max-width: 1400px;
        margin: 0 auto;
        align-items: center;
    }}
    .hero-content {{ max-width: 560px; }}
    .badge-elegant {{
        display: inline-flex;
        align-items: center;
        gap: 10px;
        padding: 10px 20px;
        background: {primary}15;
        border-radius: 50px;
        font-size: 0.9rem;
        font-weight: 600;
        color: {primary};
        margin-bottom: 32px;
    }}
    .badge-icon {{ font-size: 1.1rem; }}
    .hero-title {{
        font-family: 'Playfair Display', serif;
        font-size: clamp(3rem, 5vw, 4.5rem);
        font-weight: 700;
        color: {text};
        line-height: 1.1;
        margin-bottom: 20px;
    }}
    .hero-subtitle {{
        font-size: 1.5rem;
        color: {primary};
        font-weight: 500;
        margin-bottom: 20px;
    }}
    .hero-desc {{
        font-size: 1.1rem;
        color: {secondary};
        line-height: 1.8;
        margin-bottom: 40px;
    }}
    .cta-group {{ display: flex; gap: 16px; margin-bottom: 50px; flex-wrap: wrap; }}
    .btn-primary-elegant {{
        padding: 16px 36px;
        background: {primary};
        color: #fff;
        border-radius: 50px;
        text-decoration: none;
        font-weight: 600;
        transition: all 0.3s;
        box-shadow: 0 10px 30px {primary}40;
    }}
    .btn-primary-elegant:hover {{ transform: translateY(-3px); box-shadow: 0 15px 40px {primary}50; }}
    .btn-outline-elegant {{
        padding: 16px 36px;
        background: transparent;
        color: {text};
        border: 2px solid {text}20;
        border-radius: 50px;
        text-decoration: none;
        font-weight: 600;
        transition: all 0.3s;
    }}
    .btn-outline-elegant:hover {{ border-color: {primary}; color: {primary}; }}
    .hero-stats {{ display: flex; align-items: center; gap: 30px; flex-wrap: wrap; }}
    .stat-item {{ text-align: center; }}
    .stat-value {{ display: block; font-size: 2rem; font-weight: 700; color: {text}; }}
    .stat-label {{ font-size: 0.85rem; color: #888; }}
    .stat-divider {{ width: 1px; height: 40px; background: #ddd; }}
    .hero-right {{ position: relative; }}
    .image-container {{ position: relative; }}
    .main-image {{
        width: 100%;
        aspect-ratio: 4/5;
        border-radius: 30px;
        overflow: hidden;
        box-shadow: 0 40px 80px rgba(0,0,0,0.15);
    }}
    .main-image img {{ width: 100%; height: 100%; object-fit: cover; }}
    .floating-card {{
        position: absolute;
        background: #fff;
        padding: 16px 24px;
        border-radius: 16px;
        display: flex;
        align-items: center;
        gap: 14px;
        box-shadow: 0 15px 40px rgba(0,0,0,0.1);
        animation: float 3s ease-in-out infinite;
    }}
    .card-1 {{ top: 20%; left: -60px; }}
    .card-2 {{ bottom: 15%; right: -40px; animation-delay: 1.5s; }}
    @keyframes float {{
        0%, 100% {{ transform: translateY(0); }}
        50% {{ transform: translateY(-10px); }}
    }}
    .card-icon {{ font-size: 2rem; }}
    .card-title {{ font-weight: 700; color: {text}; display: block; }}
    .card-sub {{ font-size: 0.8rem; color: #888; }}
    .scroll-indicator {{
        position: absolute;
        bottom: 40px;
        left: 50%;
        transform: translateX(-50%);
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 10px;
        color: #888;
        font-size: 0.85rem;
    }}
    .scroll-line {{
        width: 1px;
        height: 40px;
        background: linear-gradient(to bottom, {primary}, transparent);
        animation: scrollPulse 2s infinite;
    }}
    @keyframes scrollPulse {{
        0%, 100% {{ opacity: 0.3; }}
        50% {{ opacity: 1; }}
    }}
    @media (max-width: 1024px) {{
        .hero-grid {{ grid-template-columns: 1fr; gap: 60px; }}
        .aura-hero {{ padding: 100px 24px 60px; }}
        .floating-card {{ display: none; }}
    }}
    </style>
    '''
