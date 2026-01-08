from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """
    Aura Premium Gallery - Fullscreen lightbox style with 
    hover reveals and masonry layout
    """
    title = props.get("title", "Gallery")
    subtitle = props.get("subtitle", "Moments captured in our cafe")
    
    raw_images = props.get("images", [])
    
    # Process images
    images = []
    for img in raw_images:
        if isinstance(img, str):
            images.append(img)
        elif isinstance(img, dict):
            images.append(img.get("url", img.get("src", "")))
    
    # Default images
    if not images or len(images) < 6:
        images = [
            "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=800",
            "https://images.unsplash.com/photo-1509042239860-f550ce710b93?w=800",
            "https://images.unsplash.com/photo-1447933601403-0c6688de566e?w=800",
            "https://images.unsplash.com/photo-1493857671505-72967e2e2760?w=800",
            "https://images.unsplash.com/photo-1559496417-e7f25cb247f3?w=800",
            "https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?w=800"
        ]
    
    primary = colors.get("primary", "#8B7355")
    text = colors.get("text", "#2D2013")
    
    # Process images for display
    for i, img in enumerate(images):
        if "example.com" in img or not img.startswith("http"):
            images[i] = f"https://source.unsplash.com/800x600/?cafe,coffee&sig={i}"
    
    gallery_html = ""
    sizes = ["large", "small", "small", "tall", "small", "large"]
    for i, img in enumerate(images[:6]):
        size_class = sizes[i % len(sizes)]
        gallery_html += f'''
        <div class="gallery-item {size_class} animate-on-scroll">
            <img src="{img}" alt="Gallery {i+1}" loading="lazy">
            <div class="item-overlay">
                <span class="zoom-icon">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <circle cx="11" cy="11" r="8"></circle>
                        <path d="m21 21-4.35-4.35"></path>
                        <path d="M11 8v6"></path>
                        <path d="M8 11h6"></path>
                    </svg>
                </span>
            </div>
        </div>
        '''
    
    return f'''
    <section class="aura-gallery" id="gallery">
        <div class="gallery-header">
            <span class="section-badge">Gallery</span>
            <h2 class="section-title">{title}</h2>
            <p class="section-subtitle">{subtitle}</p>
        </div>
        <div class="gallery-masonry">
            {gallery_html}
        </div>
    </section>
    
    <style>
    .aura-gallery {{
        padding: 120px 40px;
        background: #fff;
    }}
    .gallery-header {{
        text-align: center;
        margin-bottom: 60px;
    }}
    .aura-gallery .section-badge {{
        display: inline-block;
        padding: 8px 20px;
        background: {primary}15;
        color: {primary};
        border-radius: 50px;
        font-size: 0.85rem;
        font-weight: 600;
        margin-bottom: 20px;
    }}
    .aura-gallery .section-title {{
        font-family: 'Playfair Display', serif;
        font-size: clamp(2.5rem, 4vw, 3.5rem);
        color: {text};
        margin-bottom: 16px;
    }}
    .aura-gallery .section-subtitle {{
        color: #888;
        font-size: 1.1rem;
    }}
    .gallery-masonry {{
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        grid-auto-rows: 200px;
        gap: 20px;
        max-width: 1400px;
        margin: 0 auto;
    }}
    .gallery-item {{
        position: relative;
        border-radius: 16px;
        overflow: hidden;
        cursor: pointer;
    }}
    .gallery-item.large {{ grid-column: span 2; grid-row: span 2; }}
    .gallery-item.tall {{ grid-row: span 2; }}
    .gallery-item.small {{ }}
    .gallery-item img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.6s;
    }}
    .gallery-item:hover img {{ transform: scale(1.1); }}
    .item-overlay {{
        position: absolute;
        inset: 0;
        background: {primary}80;
        display: flex;
        align-items: center;
        justify-content: center;
        opacity: 0;
        transition: opacity 0.3s;
    }}
    .gallery-item:hover .item-overlay {{ opacity: 1; }}
    .zoom-icon {{
        width: 60px;
        height: 60px;
        background: #fff;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: {primary};
        transform: scale(0.8);
        transition: transform 0.3s;
    }}
    .gallery-item:hover .zoom-icon {{ transform: scale(1); }}
    @media (max-width: 1024px) {{
        .gallery-masonry {{ grid-template-columns: repeat(2, 1fr); }}
        .gallery-item.large {{ grid-column: span 2; }}
    }}
    @media (max-width: 600px) {{
        .gallery-masonry {{ grid-template-columns: 1fr; }}
        .gallery-item.large, .gallery-item.tall {{ grid-column: span 1; grid-row: span 1; }}
    }}
    </style>
    '''
