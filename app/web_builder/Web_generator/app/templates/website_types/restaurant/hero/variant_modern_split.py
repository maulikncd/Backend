from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """
    Modern Split - Contemporary split-screen hero with
    animated elements and bold typography
    """
    name = props.get("name", props.get("businessName", "The Kitchen"))
    tagline = props.get("tagline", "Modern Culinary Art")
    description = props.get("description", "Where innovation meets tradition")
    cta = props.get("cta", "Book Now")
    
    primary = colors.get("primary", "#E63946")
    bg = colors.get("background", "#1A1A1A")
    text = colors.get("text", "#FFFFFF")
    
    return f'''
    <section class="hero-split" id="hero">
        <div class="split-left">
            <div class="left-content">
                <span class="location-badge">📍 Downtown NYC</span>
                <h1 class="hero-title">{name}</h1>
                <p class="hero-tagline">{tagline}</p>
                <p class="hero-desc">{description}</p>
                
                <div class="hero-actions">
                    <a href="#reservation" class="btn-primary">{cta}</a>
                    <a href="#menu" class="btn-ghost">Explore Menu →</a>
                </div>
                
                <div class="awards">
                    <div class="award">
                        <span class="award-icon">⭐</span>
                        <span>Michelin Star 2024</span>
                    </div>
                    <div class="award">
                        <span class="award-icon">🏆</span>
                        <span>Best Fine Dining</span>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="split-right">
            <div class="image-stack">
                <img src="https://images.unsplash.com/photo-1544025162-d76694265947?w=800" alt="Dish 1" class="stack-img img-1">
                <img src="https://images.unsplash.com/photo-1540189549336-e6e99c3679fe?w=600" alt="Dish 2" class="stack-img img-2">
                <img src="https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=500" alt="Dish 3" class="stack-img img-3">
            </div>
            <div class="floating-card">
                <div class="rating">4.9</div>
                <div class="reviews">2000+ Reviews</div>
            </div>
        </div>
    </section>
    
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    
    .hero-split {{
        min-height: 100vh;
        display: grid;
        grid-template-columns: 1fr 1fr;
        background: {bg};
    }}
    .split-left {{
        display: flex;
        align-items: center;
        padding: 80px;
    }}
    .left-content {{
        max-width: 550px;
    }}
    .location-badge {{
        display: inline-block;
        padding: 10px 20px;
        background: {primary}20;
        color: {primary};
        border-radius: 50px;
        font-size: 0.9rem;
        margin-bottom: 30px;
    }}
    .hero-title {{
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-size: clamp(3rem, 6vw, 5rem);
        font-weight: 800;
        color: {text};
        line-height: 1.1;
        margin-bottom: 20px;
    }}
    .hero-tagline {{
        font-size: 1.5rem;
        color: {primary};
        margin-bottom: 15px;
        font-weight: 500;
    }}
    .hero-desc {{
        font-size: 1.1rem;
        color: {text}99;
        line-height: 1.8;
        margin-bottom: 40px;
    }}
    .hero-actions {{
        display: flex;
        gap: 20px;
        margin-bottom: 50px;
        flex-wrap: wrap;
    }}
    .btn-primary {{
        padding: 18px 40px;
        background: {primary};
        color: white;
        text-decoration: none;
        border-radius: 12px;
        font-weight: 600;
        transition: all 0.3s;
    }}
    .btn-primary:hover {{
        transform: translateY(-3px);
        box-shadow: 0 15px 40px {primary}50;
    }}
    .btn-ghost {{
        padding: 18px 40px;
        color: {text};
        text-decoration: none;
        font-weight: 600;
        transition: color 0.3s;
    }}
    .btn-ghost:hover {{ color: {primary}; }}
    .awards {{
        display: flex;
        gap: 30px;
    }}
    .award {{
        display: flex;
        align-items: center;
        gap: 10px;
        color: {text}80;
        font-size: 0.9rem;
    }}
    .award-icon {{ font-size: 1.2rem; }}
    .split-right {{
        position: relative;
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
    }}
    .image-stack {{
        position: relative;
        width: 100%;
        height: 100%;
    }}
    .stack-img {{
        position: absolute;
        border-radius: 20px;
        object-fit: cover;
        box-shadow: 0 30px 60px rgba(0,0,0,0.3);
    }}
    .img-1 {{ width: 70%; height: 60%; top: 20%; left: 10%; z-index: 3; }}
    .img-2 {{ width: 45%; height: 40%; top: 5%; right: 5%; z-index: 2; }}
    .img-3 {{ width: 40%; height: 35%; bottom: 10%; right: 15%; z-index: 1; }}
    .floating-card {{
        position: absolute;
        bottom: 15%;
        left: 10%;
        background: white;
        padding: 20px 30px;
        border-radius: 16px;
        box-shadow: 0 20px 50px rgba(0,0,0,0.2);
        z-index: 10;
    }}
    .rating {{
        font-size: 2rem;
        font-weight: 800;
        color: {primary};
    }}
    .reviews {{
        font-size: 0.85rem;
        color: #666;
    }}
    @media (max-width: 968px) {{
        .hero-split {{ grid-template-columns: 1fr; }}
        .split-left {{ padding: 60px 30px; }}
        .split-right {{ min-height: 50vh; }}
    }}
    </style>
    '''
