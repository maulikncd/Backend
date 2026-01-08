from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """
    Parallax Cards Categories - Large, immersive cards with parallax background effects.
    """
    categories = props.get("categories", ["Men", "Women", "Accessories"])
    # Ensure manageable count
    categories = categories[:3] 
    if len(categories) < 3:
        categories = ["Men", "Women", "Accessories"]
        
    images = [
        "https://images.unsplash.com/photo-1490578474895-699cd4e2cf59?w=1200",
        "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=1200",
        "https://images.unsplash.com/photo-1492707892479-7bc8d5a4ee93?w=1200"
    ]
    
    bg = colors.get("background", "#F2F2F2")
    
    cat_html = ""
    for idx, name in enumerate(categories):
        img = images[idx % len(images)]
        cat_html += f'''
        <div class="parallax-card">
            <div class="parallax-bg" style="background-image: url('{img}')"></div>
            <div class="card-content">
                <h2>{name}</h2>
                <a href="#{name.lower()}" class="btn-explore">Explore</a>
            </div>
        </div>
        '''

    return f'''
    <section class="parallax-categories" id="categories">
        {cat_html}
    </section>
    
    <style>
    .parallax-categories {{
        display: flex;
        flex-direction: column;
        background: {bg};
    }}
    
    .parallax-card {{
        position: relative;
        height: 60vh;
        overflow: hidden;
        display: flex;
        align-items: center;
        justify-content: center;
        /* Create pseudo-parallax via attachment fixed if desktop, but modern CSS uses perspective */
    }}
    
    .parallax-bg {{
        position: absolute;
        inset: 0;
        background-position: center;
        background-size: cover;
        background-attachment: fixed; /* Simple parallax */
        transition: transform 0.5s;
        filter: brightness(0.7);
    }}
    
    .parallax-card:hover .parallax-bg {{
        transform: scale(1.05);
        filter: brightness(0.5);
    }}
    
    .card-content {{
        position: relative;
        z-index: 2;
        text-align: center;
        color: white;
    }}
    
    .card-content h2 {{
        font-family: 'Playfair Display', serif;
        font-size: 5rem;
        margin-bottom: 20px;
        text-transform: uppercase;
        letter-spacing: 5px;
        opacity: 0;
        transform: translateY(30px);
        animation: fadeUp 1s forwards;
    }}
    
    .btn-explore {{
        display: inline-block;
        padding: 15px 40px;
        border: 1px solid white;
        color: white;
        text-transform: uppercase;
        text-decoration: none;
        letter-spacing: 2px;
        transition: all 0.3s;
        opacity: 0;
        transform: translateY(20px);
        animation: fadeUp 1s forwards 0.3s;
    }}
    
    .btn-explore:hover {{
        background: white;
        color: black;
    }}
    
    @keyframes fadeUp {{
        to {{ opacity: 1; transform: translateY(0); }}
    }}
    
    @media (max-width: 768px) {{
        .parallax-bg {{ background-attachment: scroll; }} /* Disable on mobile for performance */
        .card-content h2 {{ font-size: 3rem; }}
        .parallax-card {{ height: 50vh; }}
    }}
    </style>
    '''
