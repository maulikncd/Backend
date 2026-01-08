from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    # Support blueprint's title and subtitle
    title = props.get("title", "Gallery")
    subtitle = props.get("subtitle", "")
    
    # Get images from blueprint
    raw_images = props.get("images", [])
    
    # Handle both string URLs and object formats
    images = []
    for img in raw_images:
        if isinstance(img, str):
            images.append(img)
        elif isinstance(img, dict):
            images.append(img.get("url", img.get("src", "")))
    
    # Fallback images if none provided
    if not images:
        images = [
            "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=800",
            "https://images.unsplash.com/photo-1509042239860-f550ce710b93?w=800",
            "https://images.unsplash.com/photo-1541167760496-162955ed8a9f?w=800",
            "https://images.unsplash.com/photo-1442512595331-e89e73853f31?w=800",
            "https://images.unsplash.com/photo-1453614512568-c4024d13c247?w=800",
            "https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?w=800"
        ]
    
    # Get categories from blueprint
    categories = props.get("categories", [])
    
    images_html = ""
    for i, img in enumerate(images):
        # Generate random image if URL seems invalid
        if "example.com" in img or not img.startswith("http"):
            img = f"https://source.unsplash.com/800x600/?cafe,coffee,food&sig={i}"
        
        images_html += f'''
        <div class="gallery-item animate-on-scroll">
            <img src="{img}" alt="Gallery Image {i+1}" loading="lazy">
            <div class="gallery-overlay">
                <span class="overlay-icon">+</span>
            </div>
        </div>
        '''
    
    return f'''
    <section class="cafe-gallery-masonry" id="gallery">
        <div class="gallery-info">
            <h2 class="gallery-title">{title}</h2>
            {f'<p class="gallery-subtitle">{subtitle}</p>' if subtitle else ''}
            <div class="gallery-line"></div>
        </div>
        <div class="gallery-grid">
            {images_html}
        </div>
    </section>
    
    <style>
    .cafe-gallery-masonry {{ padding: 100px 24px; background: #fff; }}
    .gallery-info {{ text-align: center; margin-bottom: 50px; }}
    .gallery-title {{ font-family: 'Playfair Display', serif; font-size: 2.5rem; margin-bottom: 12px; color: {colors.get("text", "#2D2013")}; }}
    .gallery-subtitle {{ color: {colors.get("text_muted", "#888")}; font-size: 1.1rem; margin-bottom: 20px; max-width: 600px; margin-left: auto; margin-right: auto; }}
    .gallery-line {{ width: 50px; height: 2px; background: {colors.get("primary", "#6F4E37")}; margin: 0 auto; }}
    .gallery-grid {{
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
        gap: 20px;
        max-width: 1200px;
        margin: 0 auto;
    }}
    .gallery-item {{
        position: relative;
        overflow: hidden;
        border-radius: 12px;
        aspect-ratio: 1;
    }}
    .gallery-item img {{ width: 100%; height: 100%; object-fit: cover; transition: transform 0.6s; }}
    .gallery-item:hover img {{ transform: scale(1.1); }}
    .gallery-overlay {{
        position: absolute;
        inset: 0;
        background: {colors.get("primary", "#6F4E37")}50;
        display: flex;
        align-items: center;
        justify-content: center;
        opacity: 0;
        transition: opacity 0.3s;
    }}
    .gallery-item:hover {{ cursor: pointer; }}
    .gallery-item:hover .gallery-overlay {{ opacity: 1; }}
    .overlay-icon {{ color: #fff; font-size: 2rem; border: 2px solid #fff; width: 50px; height: 50px; border-radius: 50%; display: flex; align-items: center; justify-content: center; }}
    </style>
    '''
