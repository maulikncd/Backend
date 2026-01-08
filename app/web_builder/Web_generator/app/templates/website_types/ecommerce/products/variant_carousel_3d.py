from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """
    3D Carousel Products - A visually stunning horizontal scroll with 3D perspective
    cards that rotate as you scroll.
    """
    products = props.get("products", [])
    # Fallback data
    if not products:
        products = [
            {"name": "Abstract Lamp", "price": "$120", "image": "https://images.unsplash.com/photo-1507473888900-52e1ad1459ee?w=500"},
            {"name": "Modern Chair", "price": "$299", "image": "https://images.unsplash.com/photo-1503602642458-232111445b1b?w=500"},
            {"name": "Ceramic Vase", "price": "$89", "image": "https://images.unsplash.com/photo-1578500494198-246f612d3e3d?w=500"},
            {"name": "Wood Table", "price": "$450", "image": "https://images.unsplash.com/photo-1533090481720-856c6e3c1fdc?w=500"},
            {"name": "Desk Lamp", "price": "$120", "image": "https://images.unsplash.com/photo-1534349762913-961f777f3a29?w=500"},
        ] * 2

    bg = colors.get("background", "#FFFFFF")
    text = colors.get("text", "#111111")
    
    product_cards = ""
    for prod in products:
        product_cards += f'''
        <div class="carousel-item">
            <div class="card-3d">
                <div class="img-box">
                    <img src="{prod.get("image")}" alt="{prod.get("name")}">
                </div>
                <div class="info-box">
                    <h3>{prod.get("name")}</h3>
                    <span>{prod.get("price")}</span>
                </div>
            </div>
        </div>
        '''
        
    return f'''
    <section class="carousel-products-3d" id="products">
        <div class="container-fluid">
            <h2 class="section-title">Trending Now</h2>
            <div class="carousel-track">
                {product_cards}
            </div>
        </div>
    </section>
    
    <style>
    .carousel-products-3d {{
        padding: 100px 0;
        background: {bg};
        overflow: hidden;
        perspective: 1000px;
    }}
    
    .section-title {{
        text-align: center;
        font-family: 'Playfair Display', serif;
        font-size: 3rem;
        margin-bottom: 60px;
        color: {text};
    }}
    
    .carousel-track {{
        display: flex;
        gap: 40px;
        padding: 40px 100px;
        width: max-content;
        animation: scrollHorizontal 40s linear infinite;
    }}
    
    .carousel-track:hover {{
        animation-play-state: paused;
    }}
    
    .carousel-item {{
        width: 300px;
        flex-shrink: 0;
        transform-style: preserve-3d;
        transition: transform 0.3s;
    }}
    
    .carousel-item:hover {{
        transform: scale(1.1) rotateY(10deg);
        z-index: 10;
    }}
    
    .card-3d {{
        position: relative;
        border-radius: 20px;
        overflow: hidden;
        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        background: white;
    }}
    
    .img-box {{
        height: 400px;
        overflow: hidden;
    }}
    
    .img-box img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
    }}
    
    .info-box {{
        padding: 20px;
        text-align: center;
        background: white;
    }}
    
    .info-box h3 {{
        margin: 0;
        font-size: 1.2rem;
        color: #333;
    }}
    
    .info-box span {{
        display: block;
        margin-top: 5px;
        color: #666;
        font-weight: 600;
    }}
    
    @keyframes scrollHorizontal {{
        0% {{ transform: translateX(0); }}
        100% {{ transform: translateX(-50%); }}
    }}
    </style>
    '''
