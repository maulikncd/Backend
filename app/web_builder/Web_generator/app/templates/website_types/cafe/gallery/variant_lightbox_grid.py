from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Lightbox Gallery - Click to expand with modal effect"""
    title = props.get("title", "Photo Gallery")
    images = props.get("images", [])[:8]
    
    primary = colors.get("primary", "#8B7355")
    text = colors.get("text", "#2D2013")
    
    if not images:
        images = [f"https://source.unsplash.com/600x600/?cafe,coffee&sig={i}" for i in range(8)]
    
    images_html = ""
    for i, img in enumerate(images):
        if isinstance(img, dict): img = img.get("url", "")
        if "example.com" in img: img = f"https://source.unsplash.com/600x600/?cafe&sig={i}"
        images_html += f'<div class="lightbox-item" style="background-image: url(\'{img}\')"><div class="item-hover"><span>View</span></div></div>'
    
    return f'''
    <section class="gallery-lightbox" id="gallery">
        <div class="gallery-header"><h2>{title}</h2><div class="header-line"></div></div>
        <div class="lightbox-grid">{images_html}</div>
    </section>
    <style>
    .gallery-lightbox {{ padding: 100px 24px; background: #fff; }}
    .gallery-header {{ text-align: center; margin-bottom: 60px; }}
    .gallery-header h2 {{ font-family: 'Playfair Display', serif; font-size: 3rem; color: {text}; }}
    .header-line {{ width: 60px; height: 2px; background: {primary}; margin: 20px auto; }}
    .lightbox-grid {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 15px; max-width: 1200px; margin: 0 auto; }}
    .lightbox-item {{ aspect-ratio: 1; background-size: cover; background-position: center; border-radius: 12px; position: relative; cursor: pointer; overflow: hidden; }}
    .item-hover {{ position: absolute; inset: 0; background: {primary}90; display: flex; align-items: center; justify-content: center; opacity: 0; transition: 0.3s; }}
    .lightbox-item:hover .item-hover {{ opacity: 1; }}
    .item-hover span {{ color: #fff; font-weight: 600; border: 2px solid #fff; padding: 10px 25px; border-radius: 50px; }}
    @media (max-width: 768px) {{ .lightbox-grid {{ grid-template-columns: repeat(2, 1fr); }} }}
    </style>
    '''
