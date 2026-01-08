from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    # Support blueprint's title and subtitle
    title = props.get("title", "Captured Moments")
    subtitle = props.get("subtitle", "A glimpse into our daily brewing and baking.")
    
    # Get images from blueprint
    raw_images = props.get("images", [])
    
    # Handle both string URLs and object formats
    images = []
    for img in raw_images:
        if isinstance(img, str):
            images.append(img)
        elif isinstance(img, dict):
            images.append(img.get("url", img.get("src", "")))
    
    # Fallback images if none or invalid
    default_images = [
        "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=800",
        "https://images.unsplash.com/photo-1509042239860-f550ce710b93?w=800",
        "https://images.unsplash.com/photo-1541167760496-162955ed8a9f?w=800",
        "https://images.unsplash.com/photo-1442512595331-e89e73853f31?w=800"
    ]
    
    # Process images - replace invalid ones
    processed_images = []
    for i, img in enumerate(images[:4] if images else default_images):
        if "example.com" in img or not img.startswith("http"):
            processed_images.append(f"https://source.unsplash.com/800x600/?cafe,coffee&sig={i}")
        else:
            processed_images.append(img)
    
    # Ensure we have at least 4 images
    while len(processed_images) < 4:
        processed_images.append(default_images[len(processed_images) % len(default_images)])
    
    return f'''
    <section class="cafe-gallery-interlock" id="gallery">
        <div class="interlock-container">
            <div class="interlock-grid">
                <div class="grid-item item-1"><img src="{processed_images[0]}" alt="Gallery" loading="lazy"></div>
                <div class="grid-item item-2"><img src="{processed_images[1]}" alt="Gallery" loading="lazy"></div>
                <div class="grid-item item-3">
                    <div class="info-box">
                        <h3>{title}</h3>
                        <p>{subtitle}</p>
                    </div>
                </div>
                <div class="grid-item item-4"><img src="{processed_images[2]}" alt="Gallery" loading="lazy"></div>
                <div class="grid-item item-5"><img src="{processed_images[3]}" alt="Gallery" loading="lazy"></div>
            </div>
        </div>
    </section>
    
    <style>
    .cafe-gallery-interlock {{ padding: 120px 24px; background: {colors.get("background", "#FFF8F0")}; }}
    .interlock-container {{ max-width: 1100px; margin: 0 auto; }}
    .interlock-grid {{
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        grid-template-rows: repeat(2, 300px);
        gap: 20px;
    }}
    .grid-item {{ border-radius: 20px; overflow: hidden; }}
    .grid-item img {{ width: 100%; height: 100%; object-fit: cover; transition: 0.5s; }}
    .grid-item:hover img {{ transform: scale(1.05); }}
    .item-1 {{ grid-column: 1 / 3; grid-row: 1; }}
    .item-2 {{ grid-column: 3; grid-row: 1; }}
    .item-3 {{ grid-column: 4; grid-row: 1 / 3; background: {colors.get("primary", "#6F4E37")}; color: #fff; padding: 40px; display: flex; align-items: flex-end; }}
    .item-4 {{ grid-column: 1; grid-row: 2; }}
    .item-5 {{ grid-column: 2 / 4; grid-row: 2; }}
    .info-box h3 {{ font-family: 'Playfair Display', serif; font-size: 2rem; margin-bottom: 20px; }}
    .info-box p {{ font-size: 1rem; opacity: 0.9; line-height: 1.6; }}
    @media (max-width: 900px) {{
        .interlock-grid {{ grid-template-columns: 1fr 1fr; grid-template-rows: auto; }}
        .item-1, .item-2, .item-3, .item-4, .item-5 {{ grid-column: span 1; grid-row: auto; height: 300px; }}
        .item-3 {{ grid-column: span 2; }}
    }}
    </style>
    '''
