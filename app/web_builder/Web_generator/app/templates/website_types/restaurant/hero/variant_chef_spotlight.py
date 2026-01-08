from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """
    Chef Spotlight - Hero focused on the chef/team with signature dish
    """
    name = props.get("name", props.get("businessName", "Chef's Table"))
    tagline = props.get("tagline", "Culinary Artistry")
    description = props.get("description", "Led by award-winning Chef Mario")
    cta = props.get("cta", "Book The Experience")
    
    primary = colors.get("primary", "#1E3A5F")
    bg = colors.get("background", "#F5F1EB")
    text = colors.get("text", "#1A1A1A")
    
    return f'''
    <section class="hero-chef" id="hero">
        <div class="chef-grid">
            <div class="chef-image">
                <img src="https://images.unsplash.com/photo-1556910103-1c02745aae4d?w=800" alt="Chef">
                <div class="image-accent"></div>
            </div>
            
            <div class="chef-content">
                <span class="award-badge">★ Michelin Star Restaurant</span>
                <h1 class="hero-title">{name}</h1>
                <p class="hero-tagline">{tagline}</p>
                <p class="hero-desc">{description}</p>
                
                <blockquote class="chef-quote">
                    "Cooking is not just about ingredients. It's about creating memories that last forever."
                    <cite>— Chef Mario Rosetti</cite>
                </blockquote>
                
                <div class="hero-actions">
                    <a href="#reservation" class="btn-primary">{cta}</a>
                    <a href="#menu" class="btn-outline">View Menu</a>
                </div>
            </div>
            
            <div class="dish-showcase">
                <img src="https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=600" alt="Signature Dish">
                <div class="dish-info">
                    <span class="dish-label">Signature</span>
                    <span class="dish-name">Truffle Risotto</span>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&family=Source+Sans+Pro:wght@300;400;600&display=swap');
    
    .hero-chef {{
        min-height: 100vh;
        background: {bg};
        padding: 80px;
        display: flex;
        align-items: center;
    }}
    .chef-grid {{
        display: grid;
        grid-template-columns: 1fr 1.2fr 0.8fr;
        gap: 60px;
        align-items: center;
        max-width: 1400px;
        margin: 0 auto;
    }}
    .chef-image {{
        position: relative;
    }}
    .chef-image img {{
        width: 100%;
        height: auto;
        border-radius: 200px 200px 20px 20px;
        object-fit: cover;
    }}
    .image-accent {{
        position: absolute;
        top: 20px;
        left: -20px;
        right: 20px;
        bottom: -20px;
        border: 3px solid {primary}30;
        border-radius: 200px 200px 20px 20px;
        z-index: -1;
    }}
    .chef-content {{
        padding: 40px 0;
    }}
    .award-badge {{
        display: inline-block;
        padding: 12px 25px;
        background: {primary};
        color: white;
        font-size: 0.8rem;
        letter-spacing: 2px;
        border-radius: 50px;
        margin-bottom: 30px;
    }}
    .hero-title {{
        font-family: 'Libre Baskerville', serif;
        font-size: clamp(3rem, 6vw, 4.5rem);
        color: {text};
        margin-bottom: 15px;
        line-height: 1.2;
    }}
    .hero-tagline {{
        font-family: 'Libre Baskerville', serif;
        font-size: 1.4rem;
        color: {primary};
        font-style: italic;
        margin-bottom: 15px;
    }}
    .hero-desc {{
        font-family: 'Source Sans Pro', sans-serif;
        font-size: 1.1rem;
        color: {text}80;
        margin-bottom: 30px;
    }}
    .chef-quote {{
        font-family: 'Libre Baskerville', serif;
        font-size: 1.1rem;
        color: {text}90;
        font-style: italic;
        padding: 25px 30px;
        border-left: 4px solid {primary};
        background: white;
        margin-bottom: 40px;
    }}
    .chef-quote cite {{
        display: block;
        margin-top: 15px;
        font-size: 0.9rem;
        color: {primary};
        font-style: normal;
    }}
    .hero-actions {{
        display: flex;
        gap: 20px;
        flex-wrap: wrap;
    }}
    .btn-primary {{
        padding: 18px 40px;
        background: {primary};
        color: white;
        text-decoration: none;
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.3s;
    }}
    .btn-primary:hover {{
        transform: translateY(-3px);
        box-shadow: 0 15px 40px {primary}40;
    }}
    .btn-outline {{
        padding: 18px 40px;
        background: transparent;
        border: 2px solid {primary};
        color: {primary};
        text-decoration: none;
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.3s;
    }}
    .btn-outline:hover {{
        background: {primary}10;
    }}
    .dish-showcase {{
        position: relative;
    }}
    .dish-showcase img {{
        width: 100%;
        height: 500px;
        object-fit: cover;
        border-radius: 20px;
    }}
    .dish-info {{
        position: absolute;
        bottom: 30px;
        left: 30px;
        right: 30px;
        padding: 20px;
        background: white;
        border-radius: 12px;
        text-align: center;
    }}
    .dish-label {{
        display: block;
        font-size: 0.75rem;
        color: {primary};
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 5px;
    }}
    .dish-name {{
        font-family: 'Libre Baskerville', serif;
        font-size: 1.2rem;
        color: {text};
    }}
    @media (max-width: 1100px) {{
        .chef-grid {{ grid-template-columns: 1fr 1fr; }}
        .dish-showcase {{ grid-column: span 2; }}
        .dish-showcase img {{ height: 300px; }}
    }}
    @media (max-width: 768px) {{
        .hero-chef {{ padding: 60px 30px; }}
        .chef-grid {{ grid-template-columns: 1fr; }}
        .dish-showcase {{ grid-column: auto; }}
    }}
    </style>
    '''
