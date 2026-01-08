from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """
    Rustic Bistro - Warm, casual hero with friendly vibes
    and emphasis on food imagery
    """
    name = props.get("name", props.get("businessName", "The Hungry Fork"))
    tagline = props.get("tagline", "Home-style Comfort Food")
    description = props.get("description", "Fresh ingredients, family recipes, unforgettable flavors")
    cta = props.get("cta", "Order Now")
    
    primary = colors.get("primary", "#D97706")
    secondary = colors.get("secondary", "#DC2626")
    bg = colors.get("background", "#FFFBEB")
    text = colors.get("text", "#1C1917")
    
    return f'''
    <section class="bistro-hero" id="hero">
        <div class="hero-bg-pattern"></div>
        
        <div class="hero-container">
            <div class="hero-text">
                <div class="hero-badge">
                    <span>🍴</span>
                    <span>Family Owned Since 1978</span>
                </div>
                
                <h1 class="hero-name">{name}</h1>
                <p class="hero-tagline">{tagline}</p>
                <p class="hero-desc">{description}</p>
                
                <div class="cta-group">
                    <a href="#menu" class="btn-primary">{cta}</a>
                    <a href="#about" class="btn-secondary">Our Story</a>
                </div>
                
                <div class="quick-info">
                    <div class="info-badge">
                        <span class="badge-icon">⭐</span>
                        <span class="badge-text">4.9 Rating</span>
                    </div>
                    <div class="info-badge">
                        <span class="badge-icon">🚚</span>
                        <span class="badge-text">Free Delivery</span>
                    </div>
                    <div class="info-badge">
                        <span class="badge-icon">⏰</span>
                        <span class="badge-text">Open Now</span>
                    </div>
                </div>
            </div>
            
            <div class="hero-image">
                <div class="image-stack">
                    <img src="https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=600" alt="Dish 1" class="main-dish">
                    <div class="floating-card">
                        <span class="card-icon">🔥</span>
                        <span class="card-text">Today's Special</span>
                    </div>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Poppins:wght@400;500;600;700&display=swap');
    
    .bistro-hero {{
        min-height: 100vh;
        background: {bg};
        position: relative;
        display: flex;
        align-items: center;
        padding: 120px 60px;
        overflow: hidden;
    }}
    .hero-bg-pattern {{
        position: absolute;
        inset: 0;
        background: radial-gradient(circle at 10% 20%, {primary}10 0%, transparent 40%),
                    radial-gradient(circle at 90% 80%, {secondary}10 0%, transparent 40%);
    }}
    .hero-container {{
        max-width: 1400px;
        margin: 0 auto;
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 80px;
        align-items: center;
        position: relative;
        z-index: 1;
    }}
    .hero-badge {{
        display: inline-flex;
        align-items: center;
        gap: 10px;
        padding: 10px 20px;
        background: {primary}15;
        border-radius: 50px;
        font-size: 0.9rem;
        color: {primary};
        font-weight: 600;
        margin-bottom: 24px;
    }}
    .hero-name {{
        font-family: 'Playfair Display', serif;
        font-size: clamp(3rem, 6vw, 5rem);
        color: {text};
        line-height: 1.1;
        margin-bottom: 16px;
    }}
    .hero-tagline {{
        font-size: 1.5rem;
        color: {primary};
        font-weight: 500;
        margin-bottom: 16px;
    }}
    .hero-desc {{
        font-size: 1.1rem;
        color: {text}90;
        line-height: 1.8;
        margin-bottom: 40px;
        max-width: 500px;
    }}
    .cta-group {{
        display: flex;
        gap: 16px;
        margin-bottom: 50px;
        flex-wrap: wrap;
    }}
    .btn-primary {{
        padding: 18px 40px;
        background: {primary};
        color: white;
        text-decoration: none;
        font-weight: 600;
        border-radius: 50px;
        transition: all 0.3s;
        box-shadow: 0 10px 30px {primary}40;
    }}
    .btn-primary:hover {{
        transform: translateY(-3px);
        box-shadow: 0 15px 40px {primary}50;
    }}
    .btn-secondary {{
        padding: 18px 40px;
        background: transparent;
        border: 2px solid {text}30;
        color: {text};
        text-decoration: none;
        font-weight: 600;
        border-radius: 50px;
        transition: all 0.3s;
    }}
    .btn-secondary:hover {{
        border-color: {primary};
        color: {primary};
    }}
    .quick-info {{
        display: flex;
        gap: 20px;
        flex-wrap: wrap;
    }}
    .info-badge {{
        display: flex;
        align-items: center;
        gap: 8px;
        padding: 10px 16px;
        background: white;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        font-size: 0.9rem;
        color: {text};
    }}
    .hero-image {{
        position: relative;
    }}
    .image-stack {{
        position: relative;
    }}
    .main-dish {{
        width: 100%;
        border-radius: 40px;
        box-shadow: 0 40px 80px rgba(0,0,0,0.15);
    }}
    .floating-card {{
        position: absolute;
        bottom: 40px;
        left: -40px;
        background: white;
        padding: 16px 24px;
        border-radius: 16px;
        display: flex;
        align-items: center;
        gap: 12px;
        box-shadow: 0 15px 40px rgba(0,0,0,0.1);
        animation: float 3s ease-in-out infinite;
    }}
    @keyframes float {{
        0%, 100% {{ transform: translateY(0); }}
        50% {{ transform: translateY(-10px); }}
    }}
    .card-icon {{ font-size: 1.5rem; }}
    .card-text {{ font-weight: 600; color: {text}; }}
    @media (max-width: 1024px) {{
        .hero-container {{ grid-template-columns: 1fr; gap: 60px; }}
        .bistro-hero {{ padding: 120px 40px; }}
    }}
    @media (max-width: 640px) {{
        .bistro-hero {{ padding: 100px 24px; }}
        .floating-card {{ display: none; }}
    }}
    </style>
    '''
