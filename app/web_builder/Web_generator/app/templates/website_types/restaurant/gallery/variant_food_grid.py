"""
Restaurant Gallery - Food Photography Grid
Shows restaurant interior, food, and ambiance photos
"""
from typing import Dict, Any, List

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """
    Food Photography Grid - Restaurant gallery with food and ambiance photos
    """
    title = props.get("title", props.get("sectionTitle", "Our Gallery"))
    subtitle = props.get("subtitle", "Experience the ambiance and flavors")
    
    # Get images from props or use restaurant-specific defaults
    images = props.get("images", props.get("gallery", []))
    if not images or (isinstance(images, list) and len(images) == 0):
        images = [
            {"url": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=800", "caption": "Restaurant Interior", "category": "ambiance"},
            {"url": "https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=800", "caption": "Gourmet Dish", "category": "food"},
            {"url": "https://images.unsplash.com/photo-1559339352-11d035aa65de?w=800", "caption": "Fine Dining", "category": "food"},
            {"url": "https://images.unsplash.com/photo-1550966871-3ed3cdb5ed0c?w=800", "caption": "Chef at Work", "category": "team"},
            {"url": "https://images.unsplash.com/photo-1466978913421-dad2ebd01d17?w=800", "caption": "Bar Area", "category": "ambiance"},
            {"url": "https://images.unsplash.com/photo-1424847651672-bf20a4b0982b?w=800", "caption": "Dessert", "category": "food"}
        ]
    
    # Handle if images is a list of strings (URLs only)
    processed_images = []
    for img in images:
        if isinstance(img, str):
            processed_images.append({"url": img, "caption": "", "category": "food"})
        elif isinstance(img, dict):
            processed_images.append(img)
    
    if not processed_images:
        processed_images = images
    
    primary = colors.get("primary", "#C9A962")
    bg = colors.get("background", "#0A0A0A")
    text = colors.get("text_on_dark", colors.get("text", "#FFFFFF"))
    
    # Build gallery items
    items_html = ""
    for i, img in enumerate(processed_images[:9]):  # Limit to 9 images
        url = img.get("url", "") if isinstance(img, dict) else str(img)
        caption = img.get("caption", "") if isinstance(img, dict) else ""
        
        # Vary sizes for visual interest
        size_class = "large" if i == 0 or i == 4 else ""
        
        items_html += f'''
        <div class="gallery-item {size_class}" onclick="openGalleryLightbox({i})">
            <img src="{url}" alt="{caption}" loading="lazy">
            <div class="item-overlay">
                <span class="caption">{caption}</span>
                <span class="zoom-icon">+</span>
            </div>
        </div>
        '''
    
    return f'''
    <section class="restaurant-gallery" id="gallery">
        <div class="container">
            <div class="gallery-header">
                <span class="section-label">Gallery</span>
                <h2 class="section-title">{title}</h2>
                <p class="section-subtitle">{subtitle}</p>
            </div>
            
            <div class="gallery-grid">
                {items_html}
            </div>
        </div>
        
        <!-- Lightbox -->
        <div class="gallery-lightbox" id="galleryLightbox">
            <button class="lightbox-close" onclick="closeGalleryLightbox()">&times;</button>
            <button class="lightbox-prev" onclick="navGallery(-1)">&#10094;</button>
            <div class="lightbox-content">
                <img src="" alt="" id="galleryLightboxImg">
                <p class="lightbox-caption" id="galleryLightboxCaption"></p>
            </div>
            <button class="lightbox-next" onclick="navGallery(1)">&#10095;</button>
        </div>
    </section>
    
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Lato:wght@400;500&display=swap');
    
    .restaurant-gallery {{
        padding: 120px 0;
        background: {bg};
    }}
    .restaurant-gallery .container {{
        max-width: 1400px;
        margin: 0 auto;
        padding: 0 40px;
    }}
    .gallery-header {{
        text-align: center;
        margin-bottom: 60px;
    }}
    .section-label {{
        display: inline-block;
        font-size: 0.85rem;
        color: {primary};
        text-transform: uppercase;
        letter-spacing: 4px;
        margin-bottom: 20px;
    }}
    .section-title {{
        font-family: 'Cormorant Garamond', serif;
        font-size: clamp(2.5rem, 5vw, 4rem);
        color: {text};
        margin-bottom: 16px;
    }}
    .section-subtitle {{
        font-size: 1.1rem;
        color: {text}80;
    }}
    .gallery-grid {{
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 20px;
    }}
    .gallery-item {{
        position: relative;
        border-radius: 16px;
        overflow: hidden;
        aspect-ratio: 4/3;
        cursor: pointer;
    }}
    .gallery-item.large {{
        grid-row: span 2;
        aspect-ratio: auto;
    }}
    .gallery-item img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.5s ease;
    }}
    .gallery-item:hover img {{
        transform: scale(1.1);
    }}
    .item-overlay {{
        position: absolute;
        inset: 0;
        background: linear-gradient(to top, rgba(0,0,0,0.8) 0%, transparent 60%);
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
        padding: 24px;
        opacity: 0;
        transition: opacity 0.3s;
    }}
    .gallery-item:hover .item-overlay {{
        opacity: 1;
    }}
    .item-overlay .caption {{
        color: white;
        font-size: 1.1rem;
        font-weight: 500;
    }}
    .item-overlay .zoom-icon {{
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 50px;
        height: 50px;
        background: {primary};
        color: #0A0A0A;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 2rem;
        opacity: 0;
        transition: opacity 0.3s;
    }}
    .gallery-item:hover .zoom-icon {{
        opacity: 1;
    }}
    
    /* Lightbox */
    .gallery-lightbox {{
        display: none;
        position: fixed;
        inset: 0;
        background: rgba(0,0,0,0.95);
        z-index: 10000;
        justify-content: center;
        align-items: center;
    }}
    .gallery-lightbox.active {{
        display: flex;
    }}
    .lightbox-content {{
        max-width: 90vw;
        max-height: 85vh;
        text-align: center;
    }}
    #galleryLightboxImg {{
        max-width: 100%;
        max-height: 80vh;
        object-fit: contain;
        border-radius: 8px;
    }}
    .lightbox-caption {{
        color: white;
        margin-top: 16px;
        font-size: 1.2rem;
    }}
    .lightbox-close {{
        position: absolute;
        top: 20px;
        right: 30px;
        font-size: 3rem;
        color: white;
        background: none;
        border: none;
        cursor: pointer;
    }}
    .lightbox-prev, .lightbox-next {{
        position: absolute;
        top: 50%;
        transform: translateY(-50%);
        font-size: 2.5rem;
        color: white;
        background: rgba(255,255,255,0.1);
        border: none;
        width: 60px;
        height: 60px;
        border-radius: 50%;
        cursor: pointer;
        transition: background 0.3s;
    }}
    .lightbox-prev:hover, .lightbox-next:hover {{
        background: {primary};
        color: #0A0A0A;
    }}
    .lightbox-prev {{ left: 30px; }}
    .lightbox-next {{ right: 30px; }}
    
    @media (max-width: 1024px) {{
        .gallery-grid {{ grid-template-columns: repeat(2, 1fr); }}
        .gallery-item.large {{ grid-row: span 1; aspect-ratio: 4/3; }}
    }}
    @media (max-width: 640px) {{
        .gallery-grid {{ grid-template-columns: 1fr; }}
    }}
    </style>
    
    <script>
    const galleryImgs = {[f'{{"url": "{img.get("url", img) if isinstance(img, dict) else img}", "caption": "{img.get("caption", "") if isinstance(img, dict) else ""}"}}' for img in processed_images]};
    let galleryIdx = 0;
    
    function openGalleryLightbox(idx) {{
        galleryIdx = idx;
        updateGalleryLightbox();
        document.getElementById('galleryLightbox').classList.add('active');
        document.body.style.overflow = 'hidden';
    }}
    
    function closeGalleryLightbox() {{
        document.getElementById('galleryLightbox').classList.remove('active');
        document.body.style.overflow = '';
    }}
    
    function navGallery(dir) {{
        galleryIdx += dir;
        if (galleryIdx < 0) galleryIdx = galleryImgs.length - 1;
        if (galleryIdx >= galleryImgs.length) galleryIdx = 0;
        updateGalleryLightbox();
    }}
    
    function updateGalleryLightbox() {{
        const img = galleryImgs[galleryIdx];
        document.getElementById('galleryLightboxImg').src = img.url;
        document.getElementById('galleryLightboxCaption').textContent = img.caption;
    }}
    
    document.addEventListener('keydown', (e) => {{
        if (!document.getElementById('galleryLightbox').classList.contains('active')) return;
        if (e.key === 'Escape') closeGalleryLightbox();
        if (e.key === 'ArrowLeft') navGallery(-1);
        if (e.key === 'ArrowRight') navGallery(1);
    }});
    </script>
    '''.replace("galleryImgs = {", "galleryImgs = [").replace("}]", "}]")
