from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Split Showcase Gallery - Large hero image with thumbnails"""
    title = props.get("title", "Our Space")
    images = props.get("images", [])[:5]
    primary = colors.get("primary", "#8B7355")
    
    if not images:
        images = [f"https://source.unsplash.com/800x600/?cafe,interior&sig={i}" for i in range(5)]
    
    main_img = images[0] if images else "https://source.unsplash.com/1200x800/?cafe"
    if isinstance(main_img, dict): main_img = main_img.get("url", "")
    if "example.com" in main_img: main_img = "https://source.unsplash.com/1200x800/?cafe"
    
    thumbs_html = ""
    for i, img in enumerate(images[1:5]):
        if isinstance(img, dict): img = img.get("url", "")
        if "example.com" in img: img = f"https://source.unsplash.com/300x300/?cafe&sig={i}"
        thumbs_html += f'<div class="thumb" style="background-image: url(\'{img}\')"></div>'
    
    return f'''
    <section class="gallery-split-showcase" id="gallery">
        <div class="split-container">
            <div class="main-showcase" style="background-image: url('{main_img}')"><div class="showcase-label"><span>Featured</span><h3>{title}</h3></div></div>
            <div class="thumbs-grid">{thumbs_html}</div>
        </div>
    </section>
    <style>
    .gallery-split-showcase {{ padding: 100px 40px; background: #FAF7F4; }}
    .split-container {{ max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: 2fr 1fr; gap: 20px; }}
    .main-showcase {{ height: 600px; background-size: cover; background-position: center; border-radius: 20px; position: relative; overflow: hidden; }}
    .showcase-label {{ position: absolute; bottom: 0; left: 0; right: 0; padding: 40px; background: linear-gradient(to top, rgba(0,0,0,0.8), transparent); color: #fff; }}
    .showcase-label span {{ color: {primary}; text-transform: uppercase; letter-spacing: 3px; font-size: 0.8rem; }}
    .showcase-label h3 {{ font-family: 'Playfair Display', serif; font-size: 2.5rem; margin-top: 10px; }}
    .thumbs-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }}
    .thumb {{ background-size: cover; background-position: center; border-radius: 16px; transition: 0.3s; cursor: pointer; }}
    .thumb:hover {{ transform: scale(0.96); opacity: 0.8; }}
    @media (max-width: 900px) {{ .split-container {{ grid-template-columns: 1fr; }} .main-showcase {{ height: 400px; }} }}
    </style>
    '''
