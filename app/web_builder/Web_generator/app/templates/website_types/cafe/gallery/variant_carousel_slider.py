from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Carousel Gallery - Full-width sliding gallery"""
    title = props.get("title", "Gallery")
    images = props.get("images", [])[:6]
    primary = colors.get("primary", "#8B7355")
    
    if not images:
        images = [f"https://source.unsplash.com/1200x600/?cafe,coffee&sig={i}" for i in range(6)]
    
    slides_html = ""
    dots_html = ""
    for i, img in enumerate(images):
        if isinstance(img, dict): img = img.get("url", "")
        if "example.com" in img: img = f"https://source.unsplash.com/1200x600/?cafe&sig={i}"
        active = "active" if i == 0 else ""
        slides_html += f'<div class="carousel-slide {active}" style="background-image: url(\'{img}\')"></div>'
        dots_html += f'<span class="dot {active}"></span>'
    
    return f'''
    <section class="gallery-carousel" id="gallery">
        <div class="carousel-wrapper">
            <h2>{title}</h2>
            <div class="carousel-track">{slides_html}</div>
            <div class="carousel-nav"><button class="nav-prev">←</button><button class="nav-next">→</button></div>
            <div class="carousel-dots">{dots_html}</div>
        </div>
    </section>
    <style>
    .gallery-carousel {{ padding: 100px 0; background: #0D0D0D; }}
    .carousel-wrapper {{ max-width: 1400px; margin: 0 auto; padding: 0 40px; }}
    .gallery-carousel h2 {{ font-family: 'Playfair Display', serif; font-size: 3rem; color: #fff; text-align: center; margin-bottom: 50px; }}
    .carousel-track {{ position: relative; height: 500px; border-radius: 20px; overflow: hidden; }}
    .carousel-slide {{ position: absolute; inset: 0; background-size: cover; background-position: center; opacity: 0; transition: opacity 0.5s; }}
    .carousel-slide.active {{ opacity: 1; }}
    .carousel-nav {{ display: flex; justify-content: space-between; position: absolute; top: 50%; left: 20px; right: 20px; transform: translateY(-50%); pointer-events: none; }}
    .nav-prev, .nav-next {{ width: 50px; height: 50px; border: 2px solid #fff; background: transparent; color: #fff; border-radius: 50%; font-size: 1.2rem; cursor: pointer; pointer-events: all; transition: 0.3s; }}
    .nav-prev:hover, .nav-next:hover {{ background: {primary}; border-color: {primary}; }}
    .carousel-dots {{ display: flex; justify-content: center; gap: 10px; margin-top: 30px; }}
    .dot {{ width: 10px; height: 10px; border-radius: 50%; background: #fff3; transition: 0.3s; }}
    .dot.active {{ background: {primary}; width: 30px; border-radius: 5px; }}
    </style>
    '''
