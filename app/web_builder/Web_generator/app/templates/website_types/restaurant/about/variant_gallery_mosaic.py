from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Gallery Mosaic - Image-heavy mosaic layout"""
    title = props.get("sectionTitle", "Our World")
    story = props.get("story", "Experience the atmosphere")
    
    primary = colors.get("primary", "#8B7355")
    bg = colors.get("background", "#0A0A0A")
    text = colors.get("text", "#FFFFFF")
    
    return f'''
    <section class="about-mosaic" id="about">
        <div class="mosaic-header">
            <span class="label">About Us</span>
            <h2>{title}</h2>
            <p>{story}</p>
        </div>
        
        <div class="mosaic-grid">
            <div class="mosaic-item item-1">
                <img src="https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=800" alt="Interior">
                <div class="item-overlay">
                    <span>The Ambiance</span>
                </div>
            </div>
            <div class="mosaic-item item-2">
                <img src="https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=600" alt="Dish">
                <div class="item-overlay">
                    <span>The Cuisine</span>
                </div>
            </div>
            <div class="mosaic-item item-3">
                <img src="https://images.unsplash.com/photo-1577219491135-ce391730fb2c?w=600" alt="Chef">
                <div class="item-overlay">
                    <span>The Team</span>
                </div>
            </div>
            <div class="mosaic-item item-4">
                <img src="https://images.unsplash.com/photo-1466978913421-dad2ebd01d17?w=800" alt="Bar">
                <div class="item-overlay">
                    <span>The Experience</span>
                </div>
            </div>
        </div>
        
        <div class="mosaic-footer">
            <a href="#reservation" class="btn-mosaic">Book Your Table</a>
        </div>
    </section>
    
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500&family=Lato:wght@300;400&display=swap');
    
    .about-mosaic {{
        padding: 120px 60px;
        background: {bg};
    }}
    .mosaic-header {{
        text-align: center;
        margin-bottom: 60px;
    }}
    .mosaic-header .label {{
        color: {primary};
        font-size: 0.85rem;
        letter-spacing: 3px;
        text-transform: uppercase;
        display: block;
        margin-bottom: 15px;
    }}
    .mosaic-header h2 {{
        font-family: 'Playfair Display', serif;
        font-size: clamp(2.5rem, 5vw, 4rem);
        color: {text};
        margin-bottom: 15px;
    }}
    .mosaic-header p {{
        color: {text}80;
        font-size: 1.1rem;
    }}
    .mosaic-grid {{
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        grid-template-rows: repeat(2, 300px);
        gap: 20px;
        max-width: 1400px;
        margin: 0 auto;
    }}
    .mosaic-item {{
        position: relative;
        overflow: hidden;
        border-radius: 15px;
    }}
    .mosaic-item img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.5s;
    }}
    .mosaic-item:hover img {{
        transform: scale(1.08);
    }}
    .item-overlay {{
        position: absolute;
        inset: 0;
        background: linear-gradient(to top, rgba(0,0,0,0.8) 0%, transparent 60%);
        display: flex;
        align-items: flex-end;
        padding: 25px;
        opacity: 0;
        transition: opacity 0.4s;
    }}
    .mosaic-item:hover .item-overlay {{
        opacity: 1;
    }}
    .item-overlay span {{
        color: {text};
        font-family: 'Playfair Display', serif;
        font-size: 1.3rem;
    }}
    .item-1 {{ grid-column: span 2; }}
    .item-4 {{ grid-column: span 2; }}
    .mosaic-footer {{
        text-align: center;
        margin-top: 60px;
    }}
    .btn-mosaic {{
        display: inline-block;
        padding: 18px 50px;
        background: {primary};
        color: white;
        text-decoration: none;
        border-radius: 50px;
        font-weight: 500;
        transition: all 0.3s;
    }}
    .btn-mosaic:hover {{
        transform: translateY(-3px);
        box-shadow: 0 15px 40px {primary}40;
    }}
    @media (max-width: 968px) {{
        .about-mosaic {{ padding: 80px 30px; }}
        .mosaic-grid {{ grid-template-columns: 1fr 1fr; }}
        .item-1, .item-4 {{ grid-column: span 2; }}
    }}
    @media (max-width: 600px) {{
        .mosaic-grid {{ grid-template-columns: 1fr; grid-template-rows: auto; }}
        .item-1, .item-4 {{ grid-column: auto; }}
        .mosaic-item {{ height: 250px; }}
    }}
    </style>
    '''
