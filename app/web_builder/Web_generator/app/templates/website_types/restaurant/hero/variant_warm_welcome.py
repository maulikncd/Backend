from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """
    Warm Welcome - Cozy, inviting hero with warm tones
    and friendly atmosphere
    """
    name = props.get("name", props.get("businessName", "The Hearth"))
    tagline = props.get("tagline", "Home Away From Home")
    description = props.get("description", "Where every meal feels like a warm embrace")
    cta = props.get("cta", "Join Us Tonight")
    
    primary = colors.get("primary", "#C17F59")
    bg = colors.get("background", "#FDF8F3")
    text = colors.get("text", "#3D2C1E")
    
    return f'''
    <section class="hero-warm" id="hero">
        <div class="warm-bg">
            <img src="https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=1920" alt="Restaurant Interior">
            <div class="warm-overlay"></div>
        </div>
        
        <div class="hero-wrapper">
            <div class="hero-card">
                <div class="card-decoration">
                    <svg viewBox="0 0 100 20" class="flourish">
                        <path d="M0,10 Q25,0 50,10 T100,10" fill="none" stroke="currentColor" stroke-width="1"/>
                    </svg>
                </div>
                
                <span class="welcome-text">Welcome to</span>
                <h1 class="hero-title">{name}</h1>
                <p class="hero-tagline">{tagline}</p>
                <div class="divider-ornate">
                    <span>✦</span>
                </div>
                <p class="hero-desc">{description}</p>
                
                <div class="cta-section">
                    <a href="#reservation" class="btn-warm">{cta}</a>
                    <div class="phone-info">
                        <span class="phone-label">Call for reservations</span>
                        <span class="phone-number">(555) 123-4567</span>
                    </div>
                </div>
            </div>
            
            <div class="hero-features">
                <div class="feature">
                    <span class="feature-icon">🍷</span>
                    <span class="feature-text">Award-Winning Wine List</span>
                </div>
                <div class="feature">
                    <span class="feature-icon">👨‍🍳</span>
                    <span class="feature-text">Chef's Tasting Menu</span>
                </div>
                <div class="feature">
                    <span class="feature-icon">🌿</span>
                    <span class="feature-text">Farm-to-Table Fresh</span>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600&family=Lora:wght@400;500&display=swap');
    
    .hero-warm {{
        min-height: 100vh;
        position: relative;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 40px;
    }}
    .warm-bg {{
        position: absolute;
        inset: 0;
    }}
    .warm-bg img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
    }}
    .warm-overlay {{
        position: absolute;
        inset: 0;
        background: linear-gradient(
            135deg,
            rgba(61,44,30,0.85) 0%,
            rgba(61,44,30,0.7) 50%,
            rgba(61,44,30,0.8) 100%
        );
    }}
    .hero-wrapper {{
        position: relative;
        z-index: 2;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 60px;
        max-width: 800px;
    }}
    .hero-card {{
        background: {bg};
        padding: 60px 80px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 30px 80px rgba(0,0,0,0.3);
    }}
    .card-decoration {{
        margin-bottom: 20px;
    }}
    .flourish {{
        width: 100px;
        height: 20px;
        color: {primary};
    }}
    .welcome-text {{
        display: block;
        font-family: 'Lora', serif;
        font-size: 1rem;
        color: {primary};
        letter-spacing: 3px;
        text-transform: uppercase;
        margin-bottom: 10px;
    }}
    .hero-title {{
        font-family: 'Playfair Display', serif;
        font-size: clamp(3rem, 8vw, 5rem);
        font-weight: 500;
        color: {text};
        margin-bottom: 15px;
    }}
    .hero-tagline {{
        font-family: 'Lora', serif;
        font-size: 1.3rem;
        color: {text}90;
        font-style: italic;
        margin-bottom: 20px;
    }}
    .divider-ornate {{
        color: {primary};
        font-size: 1.2rem;
        margin-bottom: 20px;
    }}
    .hero-desc {{
        font-family: 'Lora', serif;
        font-size: 1.1rem;
        color: {text}80;
        line-height: 1.8;
        margin-bottom: 40px;
        max-width: 500px;
        margin-left: auto;
        margin-right: auto;
    }}
    .cta-section {{
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 25px;
    }}
    .btn-warm {{
        padding: 18px 50px;
        background: {primary};
        color: white;
        text-decoration: none;
        border-radius: 50px;
        font-size: 0.95rem;
        font-weight: 500;
        letter-spacing: 1px;
        transition: all 0.3s;
    }}
    .btn-warm:hover {{
        transform: translateY(-3px);
        box-shadow: 0 15px 40px {primary}50;
    }}
    .phone-info {{
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 5px;
    }}
    .phone-label {{
        font-size: 0.8rem;
        color: {text}60;
    }}
    .phone-number {{
        font-family: 'Playfair Display', serif;
        font-size: 1.1rem;
        color: {primary};
    }}
    .hero-features {{
        display: flex;
        gap: 50px;
        flex-wrap: wrap;
        justify-content: center;
    }}
    .feature {{
        display: flex;
        align-items: center;
        gap: 12px;
        color: white;
        font-size: 0.95rem;
    }}
    .feature-icon {{
        font-size: 1.3rem;
    }}
    @media (max-width: 768px) {{
        .hero-card {{ padding: 40px 30px; }}
        .hero-features {{ flex-direction: column; gap: 20px; }}
    }}
    </style>
    '''
