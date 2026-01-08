"""
Testimonials/Reviews Section Templates
Fully functional with carousel, ratings, and animations
"""

from typing import Dict, Any, List


class TestimonialsTemplates:
    """Premium testimonial section templates"""
    
    VARIANTS = [
        "carousel_modern",
        "grid_cards", 
        "masonry_style",
        "minimal_quotes",
        "video_testimonials"
    ]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        variant = variant or "carousel_modern"
        testimonials = props.get("testimonials", cls._get_default_testimonials())
        
        if variant == "carousel_modern":
            return cls._render_carousel_modern(testimonials, colors, props)
        elif variant == "grid_cards":
            return cls._render_grid_cards(testimonials, colors, props)
        elif variant == "masonry_style":
            return cls._render_masonry(testimonials, colors, props)
        elif variant == "minimal_quotes":
            return cls._render_minimal_quotes(testimonials, colors, props)
        else:
            return cls._render_carousel_modern(testimonials, colors, props)
    
    @staticmethod
    def _get_default_testimonials() -> List[Dict]:
        return [
            {
                "name": "Sarah Johnson",
                "role": "CEO, TechStart",
                "image": "https://randomuser.me/api/portraits/women/44.jpg",
                "rating": 5,
                "text": "Absolutely amazing experience! The quality exceeded all my expectations. Highly recommend to everyone."
            },
            {
                "name": "Michael Chen",
                "role": "Designer",
                "image": "https://randomuser.me/api/portraits/men/32.jpg",
                "rating": 5,
                "text": "Professional service from start to finish. They truly understand what customers need."
            },
            {
                "name": "Emily Rodriguez",
                "role": "Marketing Director",
                "image": "https://randomuser.me/api/portraits/women/68.jpg",
                "rating": 5,
                "text": "Best decision we ever made. The team is responsive, creative, and delivers outstanding results."
            }
        ]
    
    @classmethod
    def _render_carousel_modern(cls, testimonials: List[Dict], colors: Dict[str, str], props: Dict) -> str:
        primary = colors.get("primary", "#6366f1")
        bg = colors.get("background", "#ffffff")
        text_color = colors.get("text", "#1f2937")
        title = props.get("title", "What Our Customers Say")
        subtitle = props.get("subtitle", "Don't just take our word for it")
        
        slides = ""
        dots = ""
        for i, t in enumerate(testimonials):
            active = "active" if i == 0 else ""
            stars = "★" * t.get("rating", 5) + "☆" * (5 - t.get("rating", 5))
            slides += f'''
            <div class="testimonial-slide {active}" data-slide="{i}">
                <div class="testimonial-card">
                    <div class="quote-icon">"</div>
                    <div class="stars">{stars}</div>
                    <p class="testimonial-text">{t.get("text", "")}</p>
                    <div class="testimonial-author">
                        <img src="{t.get("image", "https://via.placeholder.com/60")}" alt="{t.get("name", "Customer")}" class="author-image" />
                        <div class="author-info">
                            <h4 class="author-name">{t.get("name", "Customer")}</h4>
                            <span class="author-role">{t.get("role", "")}</span>
                        </div>
                    </div>
                </div>
            </div>
            '''
            dots += f'<button class="carousel-dot {active}" onclick="goToSlide({i})" data-dot="{i}"></button>'
        
        return f'''
        <section class="testimonials-section" id="testimonials">
            <div class="container">
                <div class="section-header">
                    <h2 class="section-title">{title}</h2>
                    <p class="section-subtitle">{subtitle}</p>
                </div>
                
                <div class="testimonials-carousel" id="testimonialsCarousel">
                    <button class="carousel-btn prev" onclick="changeSlide(-1)">
                        <svg viewBox="0 0 24 24" width="24" height="24"><path d="M15 18l-6-6 6-6" stroke="currentColor" stroke-width="2" fill="none"/></svg>
                    </button>
                    
                    <div class="carousel-track">
                        {slides}
                    </div>
                    
                    <button class="carousel-btn next" onclick="changeSlide(1)">
                        <svg viewBox="0 0 24 24" width="24" height="24"><path d="M9 6l6 6-6 6" stroke="currentColor" stroke-width="2" fill="none"/></svg>
                    </button>
                </div>
                
                <div class="carousel-dots">{dots}</div>
            </div>
        </section>
        
        <style>
        .testimonials-section {{
            padding: 100px 0;
            background: linear-gradient(135deg, {bg} 0%, {primary}08 100%);
        }}
        .testimonials-section .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 24px;
        }}
        .section-header {{
            text-align: center;
            margin-bottom: 60px;
        }}
        .section-title {{
            font-size: clamp(2rem, 4vw, 3rem);
            font-weight: 700;
            color: {text_color};
            margin-bottom: 16px;
        }}
        .section-subtitle {{
            font-size: 1.2rem;
            color: #6b7280;
        }}
        .testimonials-carousel {{
            position: relative;
            max-width: 800px;
            margin: 0 auto;
        }}
        .carousel-track {{
            overflow: hidden;
            position: relative;
        }}
        .testimonial-slide {{
            display: none;
            animation: fadeIn 0.5s ease;
        }}
        .testimonial-slide.active {{ display: block; }}
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(20px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        .testimonial-card {{
            background: white;
            padding: 50px;
            border-radius: 24px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.08);
            text-align: center;
            position: relative;
        }}
        .quote-icon {{
            font-size: 6rem;
            color: {primary}20;
            line-height: 0.5;
            position: absolute;
            top: 20px;
            left: 30px;
            font-family: Georgia, serif;
        }}
        .stars {{
            color: #fbbf24;
            font-size: 1.5rem;
            margin-bottom: 24px;
            letter-spacing: 4px;
        }}
        .testimonial-text {{
            font-size: 1.25rem;
            line-height: 1.8;
            color: {text_color};
            margin-bottom: 32px;
            font-style: italic;
        }}
        .testimonial-author {{
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 16px;
        }}
        .author-image {{
            width: 60px;
            height: 60px;
            border-radius: 50%;
            object-fit: cover;
            border: 3px solid {primary}30;
        }}
        .author-info {{ text-align: left; }}
        .author-name {{
            font-weight: 700;
            color: {text_color};
            margin: 0;
        }}
        .author-role {{
            color: #6b7280;
            font-size: 0.9rem;
        }}
        .carousel-btn {{
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
            width: 50px;
            height: 50px;
            border-radius: 50%;
            background: white;
            border: 2px solid #e5e7eb;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.3s;
            z-index: 10;
            color: {text_color};
        }}
        .carousel-btn:hover {{
            background: {primary};
            border-color: {primary};
            color: white;
        }}
        .carousel-btn.prev {{ left: -70px; }}
        .carousel-btn.next {{ right: -70px; }}
        .carousel-dots {{
            display: flex;
            justify-content: center;
            gap: 12px;
            margin-top: 40px;
        }}
        .carousel-dot {{
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background: #e5e7eb;
            border: none;
            cursor: pointer;
            transition: all 0.3s;
        }}
        .carousel-dot.active {{
            background: {primary};
            width: 36px;
            border-radius: 6px;
        }}
        @media (max-width: 900px) {{
            .carousel-btn {{ display: none; }}
            .testimonial-card {{ padding: 30px 20px; }}
        }}
        </style>
        
        <script>
        let currentSlide = 0;
        const totalSlides = {len(testimonials)};
        
        function changeSlide(direction) {{
            currentSlide += direction;
            if (currentSlide < 0) currentSlide = totalSlides - 1;
            if (currentSlide >= totalSlides) currentSlide = 0;
            updateCarousel();
        }}
        
        function goToSlide(index) {{
            currentSlide = index;
            updateCarousel();
        }}
        
        function updateCarousel() {{
            document.querySelectorAll('.testimonial-slide').forEach((slide, i) => {{
                slide.classList.toggle('active', i === currentSlide);
            }});
            document.querySelectorAll('.carousel-dot').forEach((dot, i) => {{
                dot.classList.toggle('active', i === currentSlide);
            }});
        }}
        
        // Auto-play
        setInterval(() => changeSlide(1), 5000);
        
        // Touch/Swipe support
        let touchStartX = 0;
        const carousel = document.getElementById('testimonialsCarousel');
        if (carousel) {{
            carousel.addEventListener('touchstart', e => touchStartX = e.touches[0].clientX);
            carousel.addEventListener('touchend', e => {{
                const diff = touchStartX - e.changedTouches[0].clientX;
                if (Math.abs(diff) > 50) changeSlide(diff > 0 ? 1 : -1);
            }});
        }}
        </script>
        '''
    
    @classmethod
    def _render_grid_cards(cls, testimonials: List[Dict], colors: Dict[str, str], props: Dict) -> str:
        primary = colors.get("primary", "#6366f1")
        text_color = colors.get("text", "#1f2937")
        title = props.get("title", "Customer Reviews")
        
        cards = ""
        for t in testimonials:
            stars = "★" * t.get("rating", 5) + "☆" * (5 - t.get("rating", 5))
            cards += f'''
            <div class="review-card">
                <div class="review-header">
                    <img src="{t.get("image", "https://via.placeholder.com/50")}" alt="{t.get("name", "")}" />
                    <div>
                        <h4>{t.get("name", "Customer")}</h4>
                        <span>{t.get("role", "")}</span>
                    </div>
                    <div class="rating">{stars}</div>
                </div>
                <p class="review-text">{t.get("text", "")}</p>
            </div>
            '''
        
        return f'''
        <section class="reviews-section" id="reviews">
            <div class="container">
                <h2 class="reviews-title">{title}</h2>
                <div class="reviews-grid">{cards}</div>
            </div>
        </section>
        
        <style>
        .reviews-section {{ padding: 80px 0; background: #f9fafb; }}
        .reviews-section .container {{ max-width: 1200px; margin: 0 auto; padding: 0 24px; }}
        .reviews-title {{ text-align: center; font-size: 2.5rem; color: {text_color}; margin-bottom: 50px; }}
        .reviews-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 24px; }}
        .review-card {{
            background: white;
            padding: 28px;
            border-radius: 16px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.06);
            transition: transform 0.3s, box-shadow 0.3s;
        }}
        .review-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 12px 40px rgba(0,0,0,0.1);
        }}
        .review-header {{
            display: flex;
            align-items: center;
            gap: 14px;
            margin-bottom: 20px;
        }}
        .review-header img {{
            width: 50px;
            height: 50px;
            border-radius: 50%;
            object-fit: cover;
        }}
        .review-header h4 {{ margin: 0; color: {text_color}; font-size: 1rem; }}
        .review-header span {{ color: #6b7280; font-size: 0.85rem; }}
        .rating {{ margin-left: auto; color: #fbbf24; font-size: 1rem; }}
        .review-text {{ color: #4b5563; line-height: 1.7; margin: 0; }}
        </style>
        '''
    
    @classmethod
    def _render_masonry(cls, testimonials: List[Dict], colors: Dict[str, str], props: Dict) -> str:
        primary = colors.get("primary", "#6366f1")
        text_color = colors.get("text", "#1f2937")
        
        cards = ""
        for t in testimonials:
            stars = "★" * t.get("rating", 5)
            cards += f'''
            <div class="masonry-card">
                <div class="stars">{stars}</div>
                <p>"{t.get("text", "")}"</p>
                <div class="author">
                    <img src="{t.get("image", "")}" alt="" />
                    <div>
                        <strong>{t.get("name", "")}</strong>
                        <span>{t.get("role", "")}</span>
                    </div>
                </div>
            </div>
            '''
        
        return f'''
        <section class="masonry-testimonials" id="testimonials">
            <div class="masonry-grid">{cards}</div>
        </section>
        
        <style>
        .masonry-testimonials {{ padding: 80px 24px; background: #fafafa; }}
        .masonry-grid {{
            column-count: 3;
            column-gap: 24px;
            max-width: 1200px;
            margin: 0 auto;
        }}
        .masonry-card {{
            break-inside: avoid;
            background: white;
            padding: 30px;
            border-radius: 16px;
            margin-bottom: 24px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        }}
        .masonry-card .stars {{ color: #fbbf24; margin-bottom: 16px; }}
        .masonry-card p {{ color: {text_color}; line-height: 1.7; margin-bottom: 20px; }}
        .masonry-card .author {{ display: flex; align-items: center; gap: 12px; }}
        .masonry-card .author img {{ width: 45px; height: 45px; border-radius: 50%; }}
        .masonry-card .author strong {{ display: block; color: {text_color}; }}
        .masonry-card .author span {{ color: #6b7280; font-size: 0.85rem; }}
        @media (max-width: 900px) {{ .masonry-grid {{ column-count: 2; }} }}
        @media (max-width: 600px) {{ .masonry-grid {{ column-count: 1; }} }}
        </style>
        '''
    
    @classmethod
    def _render_minimal_quotes(cls, testimonials: List[Dict], colors: Dict[str, str], props: Dict) -> str:
        primary = colors.get("primary", "#6366f1")
        
        quotes = ""
        for t in testimonials:
            quotes += f'''
            <div class="quote-item">
                <blockquote>"{t.get("text", "")}"</blockquote>
                <cite>— {t.get("name", "")}, <span>{t.get("role", "")}</span></cite>
            </div>
            '''
        
        return f'''
        <section class="minimal-quotes" id="testimonials">
            {quotes}
        </section>
        
        <style>
        .minimal-quotes {{
            max-width: 800px;
            margin: 0 auto;
            padding: 100px 24px;
        }}
        .quote-item {{
            text-align: center;
            padding: 60px 0;
            border-bottom: 1px solid #e5e7eb;
        }}
        .quote-item:last-child {{ border-bottom: none; }}
        .quote-item blockquote {{
            font-size: 1.5rem;
            font-style: italic;
            color: #374151;
            line-height: 1.8;
            margin: 0 0 24px;
        }}
        .quote-item cite {{
            color: {primary};
            font-style: normal;
            font-weight: 600;
        }}
        .quote-item cite span {{ color: #6b7280; font-weight: 400; }}
        </style>
        '''
