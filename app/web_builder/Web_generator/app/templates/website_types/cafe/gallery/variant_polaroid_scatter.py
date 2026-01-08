from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Polaroid Gallery - Scattered polaroid-style photos"""
    title = props.get("title", "Captured Moments")
    images = props.get("images", [])[:6]
    primary = colors.get("primary", "#8B7355")
    
    if not images:
        images = [f"https://source.unsplash.com/400x400/?cafe,coffee&sig={i}" for i in range(6)]
    
    captions = ["Coffee time", "Morning vibes", "Fresh pastries", "Our team", "Latte art", "Cozy corner"]
    images_html = ""
    rotations = [-5, 3, -2, 4, -3, 2]
    for i, img in enumerate(images):
        if isinstance(img, dict): img = img.get("url", "")
        if "example.com" in img: img = f"https://source.unsplash.com/400x400/?cafe&sig={i}"
        images_html += f'''<div class="polaroid" style="--rotation: {rotations[i % 6]}deg"><img src="{img}" alt="{captions[i % 6]}"><p>{captions[i % 6]}</p></div>'''
    
    return f'''
    <section class="gallery-polaroid" id="gallery">
        <h2>{title}</h2>
        <div class="polaroid-scatter">{images_html}</div>
    </section>
    <style>
    .gallery-polaroid {{ padding: 100px 24px; background: #FAF7F4; text-align: center; }}
    .gallery-polaroid h2 {{ font-family: 'Playfair Display', serif; font-size: 3rem; margin-bottom: 60px; }}
    .polaroid-scatter {{ display: flex; flex-wrap: wrap; justify-content: center; gap: 40px; max-width: 1100px; margin: 0 auto; }}
    .polaroid {{ background: #fff; padding: 15px 15px 50px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); transform: rotate(var(--rotation)); transition: 0.4s; }}
    .polaroid:hover {{ transform: rotate(0deg) scale(1.05); z-index: 10; box-shadow: 0 20px 50px rgba(0,0,0,0.15); }}
    .polaroid img {{ width: 250px; height: 250px; object-fit: cover; }}
    .polaroid p {{ font-family: 'Playfair Display', serif; font-style: italic; color: {primary}; margin-top: 15px; }}
    </style>
    '''
