from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    title = props.get("title", "Fresh & Delicious")
    subtitle = props.get("subtitle", "Start your day with the perfect brew")
    description = props.get("description", "Artisan coffee and freshly baked goods made with love every single day.")
    cta = props.get("cta", "Explore Menu")
    image = props.get("image", "https://images.unsplash.com/photo-1509042239860-f550ce710b93?w=800")
    
    return f'''
    <section class="cafe-hero cafe-hero-split" id="hero">
        <div class="hero-left">
            <div class="hero-content">
                <div class="open-badge">
                    <span class="pulse"></span>
                    Open Now · 7AM - 9PM
                </div>
                <h1 class="hero-title">{title}</h1>
                <p class="hero-subtitle">{subtitle}</p>
                <p class="hero-description">{description}</p>
                <div class="hero-actions">
                    <a href="#menu" class="btn-primary">{cta}</a>
                    <div class="rating">
                        <span class="stars">★★★★★</span>
                        <span class="rating-text">4.9 · 200+ Reviews</span>
                    </div>
                </div>
            </div>
        </div>
        <div class="hero-right">
            <div class="image-frame">
                <img src="{image}" alt="Coffee">
                <div class="floating-card">
                    <span class="card-emoji">☕</span>
                    <div class="card-text">
                        <span class="card-title">Today's Special</span>
                        <span class="card-subtitle">Caramel Macchiato</span>
                    </div>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    .cafe-hero-split {{
        min-height: 100vh;
        display: grid;
        grid-template-columns: 1fr 1fr;
        background: {colors.get("background", "#FFF8F0")};
    }}
    .hero-left {{
        display: flex;
        align-items: center;
        padding: 80px 60px;
    }}
    .cafe-hero-split .hero-content {{
        max-width: 520px;
        animation: slideIn 0.8s ease-out;
    }}
    .open-badge {{
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 8px 16px;
        background: #22c55e15;
        color: #22c55e;
        border-radius: 50px;
        font-size: 0.85rem;
        font-weight: 500;
        margin-bottom: 24px;
    }}
    .pulse {{
        width: 8px;
        height: 8px;
        background: #22c55e;
        border-radius: 50%;
        animation: pulse 2s infinite;
    }}
    @keyframes pulse {{
        0%, 100% {{ opacity: 1; transform: scale(1); }}
        50% {{ opacity: 0.5; transform: scale(1.2); }}
    }}
    .cafe-hero-split .hero-title {{
        font-family: 'Playfair Display', Georgia, serif;
        font-size: clamp(2.5rem, 5vw, 4rem);
        color: {colors.get("text", "#2D2013")};
        font-weight: 700;
        line-height: 1.1;
        margin-bottom: 16px;
    }}
    .cafe-hero-split .hero-subtitle {{
        font-size: 1.25rem;
        color: {colors.get("primary", "#6F4E37")};
        font-weight: 500;
        margin-bottom: 16px;
    }}
    .cafe-hero-split .hero-description {{
        font-size: 1.05rem;
        color: {colors.get("text_muted", "#8B7355")};
        line-height: 1.7;
        margin-bottom: 32px;
    }}
    .hero-actions {{
        display: flex;
        align-items: center;
        gap: 24px;
        flex-wrap: wrap;
    }}
    .cafe-hero-split .btn-primary {{
        padding: 16px 32px;
        background: {colors.get("primary", "#6F4E37")};
        color: #fff;
        text-decoration: none;
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.3s ease;
    }}
    .cafe-hero-split .btn-primary:hover {{
        background: {colors.get("text", "#2D2013")};
        transform: translateY(-2px);
    }}
    .rating {{
        display: flex;
        flex-direction: column;
    }}
    .stars {{
        color: #f59e0b;
        font-size: 1.1rem;
    }}
    .rating-text {{
        font-size: 0.85rem;
        color: {colors.get("text_muted", "#8B7355")};
    }}
    .hero-right {{
        position: relative;
        overflow: hidden;
    }}
    .image-frame {{
        height: 100%;
        position: relative;
    }}
    .image-frame img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
    }}
    .floating-card {{
        position: absolute;
        bottom: 40px;
        left: -30px;
        background: #fff;
        padding: 16px 24px;
        border-radius: 16px;
        display: flex;
        align-items: center;
        gap: 12px;
        box-shadow: 0 20px 60px rgba(0,0,0,0.15);
        animation: float 3s ease-in-out infinite;
    }}
    .card-emoji {{
        font-size: 2rem;
    }}
    .card-title {{
        display: block;
        font-size: 0.8rem;
        color: {colors.get("text_muted", "#8B7355")};
    }}
    .card-subtitle {{
        display: block;
        font-weight: 600;
        color: {colors.get("text", "#2D2013")};
    }}
    @keyframes float {{
        0%, 100% {{ transform: translateY(0); }}
        50% {{ transform: translateY(-10px); }}
    }}
    @keyframes slideIn {{
        from {{ opacity: 0; transform: translateX(-30px); }}
        to {{ opacity: 1; transform: translateX(0); }}
    }}
    @media (max-width: 968px) {{
        .cafe-hero-split {{
            grid-template-columns: 1fr;
        }}
        .hero-right {{
            height: 50vh;
            order: -1;
        }}
        .hero-left {{
            padding: 40px 24px;
        }}
        .floating-card {{
            left: 20px;
            bottom: 20px;
        }}
    }}
    </style>
    '''
