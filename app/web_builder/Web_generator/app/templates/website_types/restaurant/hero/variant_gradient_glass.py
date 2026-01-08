from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """
    Gradient Glass - Modern glassmorphism with gradient background
    """
    name = props.get("name", props.get("businessName", "Fusion"))
    tagline = props.get("tagline", "Modern Gastronomy")
    description = props.get("description", "Where tradition meets innovation")
    cta = props.get("cta", "Reserve Now")
    
    primary = colors.get("primary", "#7C3AED")
    secondary = colors.get("secondary", "#EC4899")
    text = colors.get("text", "#FFFFFF")
    
    return f'''
    <section class="hero-glass" id="hero">
        <div class="gradient-bg">
            <div class="gradient-orb orb-1"></div>
            <div class="gradient-orb orb-2"></div>
            <div class="gradient-orb orb-3"></div>
        </div>
        
        <div class="glass-container">
            <div class="glass-card main-card">
                <div class="card-glow"></div>
                <span class="badge">🌟 New Opening</span>
                <h1 class="hero-title">{name}</h1>
                <p class="hero-tagline">{tagline}</p>
                <p class="hero-desc">{description}</p>
                
                <div class="action-row">
                    <a href="#reservation" class="btn-glow">{cta}</a>
                    <div class="rating-pill">
                        <span class="stars">★★★★★</span>
                        <span class="count">4.9 (500+)</span>
                    </div>
                </div>
            </div>
            
            <div class="side-cards">
                <div class="glass-card small-card">
                    <img src="https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=400" alt="Pizza">
                    <div class="card-overlay">
                        <span class="dish-name">Truffle Pizza</span>
                        <span class="dish-price">$32</span>
                    </div>
                </div>
                <div class="glass-card small-card">
                    <img src="https://images.unsplash.com/photo-1540189549336-e6e99c3679fe?w=400" alt="Salad">
                    <div class="card-overlay">
                        <span class="dish-name">Garden Fresh</span>
                        <span class="dish-price">$18</span>
                    </div>
                </div>
                <div class="glass-card small-card">
                    <img src="https://images.unsplash.com/photo-1544025162-d76694265947?w=400" alt="Steak">
                    <div class="card-overlay">
                        <span class="dish-name">Wagyu Steak</span>
                        <span class="dish-price">$85</span>
                    </div>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&display=swap');
    
    .hero-glass {{
        min-height: 100vh;
        position: relative;
        overflow: hidden;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 40px;
    }}
    .gradient-bg {{
        position: absolute;
        inset: 0;
        background: #0F0F1A;
    }}
    .gradient-orb {{
        position: absolute;
        border-radius: 50%;
        filter: blur(100px);
        opacity: 0.6;
    }}
    .orb-1 {{
        width: 600px;
        height: 600px;
        background: {primary};
        top: -20%;
        left: -10%;
        animation: float1 15s infinite;
    }}
    .orb-2 {{
        width: 500px;
        height: 500px;
        background: {secondary};
        bottom: -20%;
        right: -10%;
        animation: float2 18s infinite;
    }}
    .orb-3 {{
        width: 400px;
        height: 400px;
        background: linear-gradient({primary}, {secondary});
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        animation: pulse 10s infinite;
    }}
    @keyframes float1 {{
        0%, 100% {{ transform: translate(0, 0); }}
        50% {{ transform: translate(50px, 30px); }}
    }}
    @keyframes float2 {{
        0%, 100% {{ transform: translate(0, 0); }}
        50% {{ transform: translate(-40px, -20px); }}
    }}
    @keyframes pulse {{
        0%, 100% {{ transform: translate(-50%, -50%) scale(1); opacity: 0.4; }}
        50% {{ transform: translate(-50%, -50%) scale(1.2); opacity: 0.6; }}
    }}
    .glass-container {{
        position: relative;
        z-index: 2;
        display: grid;
        grid-template-columns: 1.5fr 1fr;
        gap: 40px;
        max-width: 1200px;
        align-items: center;
    }}
    .glass-card {{
        background: rgba(255,255,255,0.1);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255,255,255,0.15);
        border-radius: 30px;
        overflow: hidden;
    }}
    .main-card {{
        padding: 60px;
        position: relative;
    }}
    .card-glow {{
        position: absolute;
        top: -50%;
        right: -50%;
        width: 100%;
        height: 100%;
        background: linear-gradient(45deg, {primary}20, transparent);
        pointer-events: none;
    }}
    .badge {{
        display: inline-block;
        padding: 10px 20px;
        background: linear-gradient(90deg, {primary}, {secondary});
        color: white;
        font-size: 0.85rem;
        border-radius: 50px;
        margin-bottom: 30px;
    }}
    .hero-title {{
        font-family: 'Space Grotesk', sans-serif;
        font-size: clamp(3rem, 8vw, 5rem);
        font-weight: 700;
        color: {text};
        margin-bottom: 15px;
        background: linear-gradient(90deg, {text}, {primary});
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }}
    .hero-tagline {{
        font-size: 1.4rem;
        color: {text}90;
        margin-bottom: 15px;
    }}
    .hero-desc {{
        font-size: 1.1rem;
        color: {text}70;
        margin-bottom: 40px;
        line-height: 1.7;
    }}
    .action-row {{
        display: flex;
        align-items: center;
        gap: 30px;
        flex-wrap: wrap;
    }}
    .btn-glow {{
        padding: 18px 45px;
        background: linear-gradient(90deg, {primary}, {secondary});
        color: white;
        text-decoration: none;
        border-radius: 12px;
        font-weight: 600;
        transition: all 0.3s;
        box-shadow: 0 10px 40px {primary}50;
    }}
    .btn-glow:hover {{
        transform: translateY(-3px);
        box-shadow: 0 20px 50px {primary}60;
    }}
    .rating-pill {{
        display: flex;
        flex-direction: column;
        gap: 5px;
    }}
    .stars {{
        color: #FFD700;
        font-size: 1.1rem;
    }}
    .count {{
        color: {text}70;
        font-size: 0.85rem;
    }}
    .side-cards {{
        display: flex;
        flex-direction: column;
        gap: 20px;
    }}
    .small-card {{
        position: relative;
        height: 150px;
    }}
    .small-card img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
    }}
    .card-overlay {{
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        padding: 15px 20px;
        background: linear-gradient(transparent, rgba(0,0,0,0.8));
        display: flex;
        justify-content: space-between;
        align-items: center;
    }}
    .dish-name {{
        color: white;
        font-weight: 500;
    }}
    .dish-price {{
        color: {primary};
        font-weight: 600;
    }}
    @media (max-width: 968px) {{
        .glass-container {{ grid-template-columns: 1fr; }}
        .side-cards {{ flex-direction: row; }}
        .small-card {{ flex: 1; height: 200px; }}
    }}
    @media (max-width: 600px) {{
        .side-cards {{ flex-direction: column; }}
    }}
    </style>
    '''
