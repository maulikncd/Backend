from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    title = props.get("title", "Game Media")
    images = props.get("images", [
        "https://images.unsplash.com/photo-1542751371-adc38448a05e?w=800",
        "https://images.unsplash.com/photo-1511512578047-dfb367046420?w=800",
        "https://images.unsplash.com/photo-1552820728-8b83bb6b773f?w=800",
        "https://images.unsplash.com/photo-1538481199705-c710c4e965fc?w=800",
        "https://images.unsplash.com/photo-1542751110-97427bbecf20?w=800",
        "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=800"
    ])
    
    primary = colors.get("primary", "#00FF88")
    bg = colors.get("background", "#050505")
    
    # Build gallery items separately
    gallery_items = ""
    for img in images:
        gallery_items += f'''
            <div class="gallery-item animate-on-scroll">
                <img src="{img}" alt="Gaming Capture">
                <div class="gallery-overlay">
                    <span class="view-icon">👁️</span>
                    <span class="play-icon">▶</span>
                </div>
            </div>
        '''
    
    return f'''
    <section class="gaming-gallery gaming-gallery-wall" id="gallery">
        <div class="container-fluid">
            <div class="gallery-header text-center">
                <h2 class="section-title">{title}</h2>
                <div class="header-line"></div>
            </div>
            <div class="gallery-grid">
                {gallery_items}
            </div>
        </div>
    </section>
    
    <style>
    .gaming-gallery-wall {{
        padding: 100px 0;
        background: {bg};
    }}
    .gallery-header {{ margin-bottom: 60px; }}
    .header-line {{ width: 100px; height: 3px; background: {primary}; margin: 20px auto; }}
    .gallery-grid {{
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(400px, 1fr));
        gap: 10px;
    }}
    .gallery-item {{
        height: 300px;
        position: relative;
        overflow: hidden;
        cursor: pointer;
    }}
    .gallery-item img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: 0.7s;
        filter: grayscale(0.5) brightness(0.8);
    }}
    .gallery-item:hover img {{
        transform: scale(1.1);
        filter: grayscale(0) brightness(1);
    }}
    .gallery-overlay {{
        position: absolute;
        inset: 0;
        background: rgba(0, 255, 136, 0.2);
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 20px;
        opacity: 0;
        transition: 0.3s;
    }}
    .gallery-item:hover .gallery-overlay {{ opacity: 1; }}
    .view-icon, .play-icon {{
        width: 60px;
        height: 60px;
        background: #fff;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.5rem;
        color: #000;
        transform: translateY(20px);
        transition: 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .gallery-item:hover .view-icon, .gallery-item:hover .play-icon {{
        transform: translateY(0);
    }}
    .play-icon {{ transition-delay: 0.1s; }}
    @media (max-width: 768px) {{ .gallery-grid {{ grid-template-columns: 1fr; }} }}
    </style>
    '''
