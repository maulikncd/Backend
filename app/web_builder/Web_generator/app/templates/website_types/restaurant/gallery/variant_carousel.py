from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Carousel Slider - Full-width image carousel"""
    title = props.get("sectionTitle", "Our Atmosphere")
    
    primary = colors.get("primary", "#E63946")
    bg = colors.get("background", "#FFFFFF")
    text = colors.get("text", "#1A1A1A")
    
    images = [
        "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=1200",
        "https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=1200",
        "https://images.unsplash.com/photo-1466978913421-dad2ebd01d17?w=1200",
    ]
    
    slides_html = ""
    dots_html = ""
    for i, img in enumerate(images):
        active = "active" if i == 0 else ""
        slides_html += f'''
        <div class="carousel-slide {active}">
            <img src="{img}" alt="Slide {i+1}">
        </div>
        '''
        dots_html += f'<button class="dot {active}" data-slide="{i}"></button>'
    
    return f'''
    <section class="gallery-carousel" id="gallery">
        <div class="carousel-header">
            <h2>{title}</h2>
        </div>
        
        <div class="carousel-wrapper">
            <div class="carousel-track">
                {slides_html}
            </div>
            
            <button class="carousel-btn prev">←</button>
            <button class="carousel-btn next">→</button>
            
            <div class="carousel-dots">
                {dots_html}
            </div>
        </div>
    </section>
    
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500&display=swap');
    
    .gallery-carousel {{
        padding: 80px 0;
        background: {bg};
    }}
    .carousel-header {{
        text-align: center;
        margin-bottom: 50px;
    }}
    .carousel-header h2 {{
        font-family: 'Playfair Display', serif;
        font-size: clamp(2.5rem, 5vw, 4rem);
        color: {text};
    }}
    .carousel-wrapper {{
        position: relative;
        max-width: 1400px;
        margin: 0 auto;
        overflow: hidden;
    }}
    .carousel-track {{
        display: flex;
        transition: transform 0.5s ease;
    }}
    .carousel-slide {{
        min-width: 100%;
        display: none;
    }}
    .carousel-slide.active {{
        display: block;
    }}
    .carousel-slide img {{
        width: 100%;
        height: 600px;
        object-fit: cover;
    }}
    .carousel-btn {{
        position: absolute;
        top: 50%;
        transform: translateY(-50%);
        width: 60px;
        height: 60px;
        background: white;
        border: none;
        border-radius: 50%;
        font-size: 1.5rem;
        cursor: pointer;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        transition: all 0.3s;
        z-index: 10;
    }}
    .carousel-btn:hover {{
        background: {primary};
        color: white;
    }}
    .carousel-btn.prev {{ left: 30px; }}
    .carousel-btn.next {{ right: 30px; }}
    .carousel-dots {{
        position: absolute;
        bottom: 30px;
        left: 50%;
        transform: translateX(-50%);
        display: flex;
        gap: 12px;
    }}
    .dot {{
        width: 12px;
        height: 12px;
        border-radius: 50%;
        border: 2px solid white;
        background: transparent;
        cursor: pointer;
        transition: all 0.3s;
    }}
    .dot.active {{
        background: white;
    }}
    @media (max-width: 768px) {{
        .carousel-slide img {{ height: 400px; }}
        .carousel-btn {{ width: 45px; height: 45px; font-size: 1.2rem; }}
    }}
    </style>
    
    <script>
    (function() {{
        const slides = document.querySelectorAll('.carousel-slide');
        const dots = document.querySelectorAll('.dot');
        let current = 0;
        
        function showSlide(n) {{
            slides.forEach(s => s.classList.remove('active'));
            dots.forEach(d => d.classList.remove('active'));
            current = (n + slides.length) % slides.length;
            slides[current].classList.add('active');
            dots[current].classList.add('active');
        }}
        
        document.querySelector('.prev')?.addEventListener('click', () => showSlide(current - 1));
        document.querySelector('.next')?.addEventListener('click', () => showSlide(current + 1));
        dots.forEach((dot, i) => dot.addEventListener('click', () => showSlide(i)));
    }})();
    </script>
    '''
