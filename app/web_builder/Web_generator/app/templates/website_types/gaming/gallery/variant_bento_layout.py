from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Bento Gallery - Modern bento-style image layout"""
    title = props.get("title", "Media Gallery")
    subtitle = props.get("subtitle", "Explore our visual world")
    
    # Dynamic colors from user's palette
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="gaming-gallery-bento" id="gallery">
        <div class="bento-container">
            <div class="bento-header">
                <span class="section-badge">📸 Gallery</span>
                <h2>{title}</h2>
                <p>{subtitle}</p>
            </div>
            <div class="bento-layout">
                <div class="bento-item large">
                    <img src="https://images.unsplash.com/photo-1542751371-adc38448a05e?w=1200" alt="Featured">
                    <div class="item-overlay">
                        <span class="item-tag">Featured</span>
                        <h3>World Championship Arena</h3>
                    </div>
                </div>
                <div class="bento-item">
                    <img src="https://images.unsplash.com/photo-1538481199705-c710c4e965fc?w=600" alt="Setup">
                    <div class="item-overlay">
                        <h4>Pro Setup</h4>
                    </div>
                </div>
                <div class="bento-item">
                    <img src="https://images.unsplash.com/photo-1511512578047-dfb367046420?w=600" alt="Night">
                    <div class="item-overlay">
                        <h4>Night Session</h4>
                    </div>
                </div>
                <div class="bento-item tall">
                    <img src="https://images.unsplash.com/photo-1493711662062-fa541f7f069d?w=600" alt="Gear">
                    <div class="item-overlay">
                        <h4>Gaming Gear</h4>
                    </div>
                </div>
                <div class="bento-item wide">
                    <img src="https://images.unsplash.com/photo-1542751110-97427bbecf20?w=900" alt="Tournament">
                    <div class="item-overlay">
                        <h4>Tournament Highlights</h4>
                    </div>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    .gaming-gallery-bento {{
        padding: 140px 24px;
        background: {background};
    }}
    .bento-container {{
        max-width: 1200px;
        margin: 0 auto;
    }}
    .bento-header {{
        text-align: center;
        margin-bottom: 60px;
    }}
    .section-badge {{
        display: inline-block;
        padding: 10px 24px;
        background: {primary}15;
        color: {primary};
        font-weight: 700;
        font-size: 0.85rem;
        letter-spacing: 2px;
        border-radius: 100px;
        margin-bottom: 24px;
    }}
    .bento-header h2 {{
        font-family: 'Rajdhani', sans-serif;
        font-size: clamp(2.5rem, 5vw, 4rem);
        font-weight: 800;
        color: {text};
        margin-bottom: 16px;
    }}
    .bento-header p {{
        font-size: 1.2rem;
        color: {secondary};
    }}
    .bento-layout {{
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        grid-template-rows: repeat(3, 200px);
        gap: 20px;
    }}
    .bento-item {{
        position: relative;
        border-radius: 20px;
        overflow: hidden;
        cursor: pointer;
    }}
    .bento-item.large {{
        grid-column: span 2;
        grid-row: span 2;
    }}
    .bento-item.tall {{
        grid-row: span 2;
    }}
    .bento-item.wide {{
        grid-column: span 2;
    }}
    .bento-item img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
    }}
    .bento-item:hover img {{
        transform: scale(1.1);
    }}
    .item-overlay {{
        position: absolute;
        inset: 0;
        background: linear-gradient(to top, {background}CC, transparent 60%);
        padding: 24px;
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
        opacity: 0;
        transition: opacity 0.4s ease;
    }}
    .bento-item:hover .item-overlay {{
        opacity: 1;
    }}
    .item-tag {{
        display: inline-block;
        padding: 6px 14px;
        background: {primary};
        color: {background};
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        border-radius: 100px;
        margin-bottom: 12px;
        width: fit-content;
    }}
    .item-overlay h3 {{
        font-size: 1.8rem;
        font-weight: 800;
        color: {text};
    }}
    .item-overlay h4 {{
        font-size: 1.2rem;
        font-weight: 700;
        color: {text};
    }}
    @media (max-width: 900px) {{
        .bento-layout {{
            grid-template-columns: repeat(2, 1fr);
            grid-template-rows: auto;
        }}
        .bento-item.large,
        .bento-item.tall,
        .bento-item.wide {{
            grid-column: span 1;
            grid-row: span 1;
        }}
        .bento-item {{
            aspect-ratio: 4/3;
        }}
    }}
    </style>
    '''
