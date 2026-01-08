"""
Gallery Page Templates - Fully Functional with Lightbox
For all website types: Photos, Products, Portfolio, etc.
"""

from typing import Dict, Any, List


class GalleryPageTemplates:
    """Complete gallery page templates with working lightbox"""
    
    VARIANTS = ["masonry_lightbox", "grid_filter", "carousel_fullscreen", "minimal_clean"]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        variant = variant or "masonry_lightbox"
        images = props.get("images", props.get("gallery", cls._get_default_images(props.get("businessType", "general"))))
        
        if variant == "masonry_lightbox":
            return cls._render_masonry_lightbox(images, colors, props)
        elif variant == "grid_filter":
            return cls._render_grid_filter(images, colors, props)
        elif variant == "carousel_fullscreen":
            return cls._render_carousel_fullscreen(images, colors, props)
        else:
            return cls._render_masonry_lightbox(images, colors, props)
    
    @staticmethod
    def _get_default_images(business_type: str) -> List[Dict]:
        base_images = {
            "cafe": [
                {"url": "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=800", "caption": "Fresh Brewed Coffee", "category": "drinks"},
                {"url": "https://images.unsplash.com/photo-1509042239860-f550ce710b93?w=800", "caption": "Latte Art", "category": "drinks"},
                {"url": "https://images.unsplash.com/photo-1554118811-1e0d58224f24?w=800", "caption": "Cozy Interior", "category": "ambiance"},
                {"url": "https://images.unsplash.com/photo-1559305616-3f99cd43e353?w=800", "caption": "Fresh Pastries", "category": "food"},
                {"url": "https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?w=800", "caption": "Coffee Beans", "category": "drinks"},
                {"url": "https://images.unsplash.com/photo-1445116572660-236099ec97a0?w=800", "caption": "Cafe Vibes", "category": "ambiance"}
            ],
            "restaurant": [
                {"url": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=800", "caption": "Restaurant Interior", "category": "ambiance"},
                {"url": "https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=800", "caption": "Gourmet Dish", "category": "food"},
                {"url": "https://images.unsplash.com/photo-1559339352-11d035aa65de?w=800", "caption": "Fine Dining", "category": "food"},
                {"url": "https://images.unsplash.com/photo-1550966871-3ed3cdb5ed0c?w=800", "caption": "Chef at Work", "category": "team"},
                {"url": "https://images.unsplash.com/photo-1466978913421-dad2ebd01d17?w=800", "caption": "Bar Area", "category": "ambiance"},
                {"url": "https://images.unsplash.com/photo-1424847651672-bf20a4b0982b?w=800", "caption": "Dessert", "category": "food"}
            ],
            "gaming": [
                {"url": "https://images.unsplash.com/photo-1538481199705-c710c4e965fc?w=800", "caption": "Gaming Setup", "category": "setup"},
                {"url": "https://images.unsplash.com/photo-1542751371-adc38448a05e?w=800", "caption": "Esports Arena", "category": "events"},
                {"url": "https://images.unsplash.com/photo-1552820728-8b83bb6b2b0d?w=800", "caption": "Console Gaming", "category": "setup"},
                {"url": "https://images.unsplash.com/photo-1493711662062-fa541f7f3d24?w=800", "caption": "Game Night", "category": "events"},
                {"url": "https://images.unsplash.com/photo-1612287230202-1ff1d85d1bdf?w=800", "caption": "RGB Setup", "category": "setup"},
                {"url": "https://images.unsplash.com/photo-1511512578047-dfb367046420?w=800", "caption": "Game Art", "category": "art"}
            ],
            "portfolio": [
                {"url": "https://images.unsplash.com/photo-1558655146-d09347e92766?w=800", "caption": "Design Project", "category": "design"},
                {"url": "https://images.unsplash.com/photo-1581291518857-4e27b48ff24e?w=800", "caption": "Web Development", "category": "web"},
                {"url": "https://images.unsplash.com/photo-1561070791-2526d30994b5?w=800", "caption": "Branding Work", "category": "branding"},
                {"url": "https://images.unsplash.com/photo-1559028012-481c04fa702d?w=800", "caption": "UI/UX Project", "category": "design"},
                {"url": "https://images.unsplash.com/photo-1467232004584-a241de8bcf5d?w=800", "caption": "Mobile App", "category": "web"},
                {"url": "https://images.unsplash.com/photo-1572044162444-ad60f128bdea?w=800", "caption": "Photography", "category": "photography"}
            ]
        }
        return base_images.get(business_type.lower(), base_images["portfolio"])
    
    @classmethod
    def _render_masonry_lightbox(cls, images: List[Dict], colors: Dict[str, str], props: Dict) -> str:
        primary = colors.get("primary", "#6366f1")
        text = colors.get("text", "#1f2937")
        title = props.get("title", "Our Gallery")
        subtitle = props.get("subtitle", "Take a look at our work and atmosphere")
        
        items = ""
        for i, img in enumerate(images):
            url = img.get("url", img) if isinstance(img, dict) else img
            caption = img.get("caption", "") if isinstance(img, dict) else ""
            items += f'''
            <div class="gallery-item" onclick="openLightbox({i})">
                <img src="{url}" alt="{caption}" data-lightbox loading="lazy" />
                <div class="gallery-overlay">
                    <span class="gallery-caption">{caption}</span>
                    <span class="gallery-zoom">🔍</span>
                </div>
            </div>
            '''
        
        return f'''
        <section class="gallery-section" id="gallery">
            <div class="container">
                <div class="gallery-header">
                    <h2>{title}</h2>
                    <p>{subtitle}</p>
                </div>
                <div class="masonry-grid">{items}</div>
            </div>
        </section>
        
        <!-- Lightbox -->
        <div class="lightbox-overlay" id="lightbox">
            <button class="lightbox-close" onclick="closeLightbox()">&times;</button>
            <button class="lightbox-prev" onclick="navigateLightbox(-1)">&#10094;</button>
            <div class="lightbox-content">
                <img src="" alt="" id="lightboxImage" />
                <p class="lightbox-caption" id="lightboxCaption"></p>
            </div>
            <button class="lightbox-next" onclick="navigateLightbox(1)">&#10095;</button>
            <div class="lightbox-counter" id="lightboxCounter"></div>
        </div>
        
        <style>
        .gallery-section {{
            padding: 100px 0;
            background: #fafafa;
        }}
        .gallery-section .container {{
            max-width: 1400px;
            margin: 0 auto;
            padding: 0 24px;
        }}
        .gallery-header {{
            text-align: center;
            margin-bottom: 60px;
        }}
        .gallery-header h2 {{
            font-size: 2.5rem;
            color: {text};
            margin-bottom: 12px;
        }}
        .gallery-header p {{ color: #6b7280; font-size: 1.1rem; }}
        
        .masonry-grid {{
            column-count: 3;
            column-gap: 20px;
        }}
        .gallery-item {{
            break-inside: avoid;
            margin-bottom: 20px;
            border-radius: 16px;
            overflow: hidden;
            position: relative;
            cursor: pointer;
        }}
        .gallery-item img {{
            width: 100%;
            display: block;
            transition: transform 0.5s ease;
        }}
        .gallery-item:hover img {{ transform: scale(1.08); }}
        .gallery-overlay {{
            position: absolute;
            inset: 0;
            background: linear-gradient(to top, rgba(0,0,0,0.7) 0%, transparent 50%);
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
            padding: 20px;
            opacity: 0;
            transition: opacity 0.3s;
        }}
        .gallery-item:hover .gallery-overlay {{ opacity: 1; }}
        .gallery-caption {{
            color: white;
            font-weight: 500;
            font-size: 1rem;
        }}
        .gallery-zoom {{
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-size: 2rem;
            opacity: 0;
            transition: opacity 0.3s;
        }}
        .gallery-item:hover .gallery-zoom {{ opacity: 1; }}
        
        /* Lightbox */
        .lightbox-overlay {{
            display: none;
            position: fixed;
            inset: 0;
            background: rgba(0,0,0,0.95);
            z-index: 10000;
            justify-content: center;
            align-items: center;
        }}
        .lightbox-overlay.active {{ display: flex; }}
        .lightbox-content {{
            max-width: 90vw;
            max-height: 85vh;
            display: flex;
            flex-direction: column;
            align-items: center;
        }}
        #lightboxImage {{
            max-width: 100%;
            max-height: 80vh;
            object-fit: contain;
            border-radius: 8px;
        }}
        .lightbox-caption {{
            color: white;
            margin-top: 16px;
            font-size: 1.1rem;
            text-align: center;
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
            z-index: 10001;
            line-height: 1;
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
        .lightbox-prev:hover, .lightbox-next:hover {{ background: rgba(255,255,255,0.2); }}
        .lightbox-prev {{ left: 30px; }}
        .lightbox-next {{ right: 30px; }}
        .lightbox-counter {{
            position: absolute;
            bottom: 30px;
            color: white;
            font-size: 0.9rem;
        }}
        
        @media (max-width: 1024px) {{ .masonry-grid {{ column-count: 2; }} }}
        @media (max-width: 600px) {{
            .masonry-grid {{ column-count: 1; }}
            .lightbox-prev, .lightbox-next {{ display: none; }}
        }}
        </style>
        
        <script>
        const galleryImages = {[f'{{"url": "{img.get("url", img) if isinstance(img, dict) else img}", "caption": "{img.get("caption", "") if isinstance(img, dict) else ""}"}}' for img in images]};
        let currentIndex = 0;
        
        function openLightbox(index) {{
            currentIndex = index;
            updateLightbox();
            document.getElementById('lightbox').classList.add('active');
            document.body.style.overflow = 'hidden';
        }}
        
        function closeLightbox() {{
            document.getElementById('lightbox').classList.remove('active');
            document.body.style.overflow = '';
        }}
        
        function navigateLightbox(dir) {{
            currentIndex += dir;
            if (currentIndex < 0) currentIndex = galleryImages.length - 1;
            if (currentIndex >= galleryImages.length) currentIndex = 0;
            updateLightbox();
        }}
        
        function updateLightbox() {{
            const img = galleryImages[currentIndex];
            document.getElementById('lightboxImage').src = img.url;
            document.getElementById('lightboxCaption').textContent = img.caption;
            document.getElementById('lightboxCounter').textContent = `${{currentIndex + 1}} / ${{galleryImages.length}}`;
        }}
        
        // Keyboard navigation
        document.addEventListener('keydown', (e) => {{
            if (!document.getElementById('lightbox').classList.contains('active')) return;
            if (e.key === 'Escape') closeLightbox();
            if (e.key === 'ArrowLeft') navigateLightbox(-1);
            if (e.key === 'ArrowRight') navigateLightbox(1);
        }});
        
        // Click outside to close
        document.getElementById('lightbox').addEventListener('click', (e) => {{
            if (e.target.id === 'lightbox') closeLightbox();
        }});
        
        // Touch swipe
        let touchStartX = 0;
        document.getElementById('lightbox').addEventListener('touchstart', e => touchStartX = e.touches[0].clientX);
        document.getElementById('lightbox').addEventListener('touchend', e => {{
            const diff = touchStartX - e.changedTouches[0].clientX;
            if (Math.abs(diff) > 50) navigateLightbox(diff > 0 ? 1 : -1);
        }});
        </script>
        '''.replace("galleryImages = {", "galleryImages = [").replace("}}", "}]")
    
    @classmethod
    def _render_grid_filter(cls, images: List[Dict], colors: Dict[str, str], props: Dict) -> str:
        primary = colors.get("primary", "#6366f1")
        text = colors.get("text", "#1f2937")
        
        # Extract categories
        categories = set()
        for img in images:
            if isinstance(img, dict) and img.get("category"):
                categories.add(img.get("category"))
        
        # Filter buttons
        filters = '<button class="filter-btn active" onclick="filterGallery(\'all\')">All</button>'
        for cat in sorted(categories):
            filters += f'<button class="filter-btn" onclick="filterGallery(\'{cat}\')">{cat.capitalize()}</button>'
        
        # Gallery items
        items = ""
        for i, img in enumerate(images):
            url = img.get("url", img) if isinstance(img, dict) else img
            caption = img.get("caption", "") if isinstance(img, dict) else ""
            category = img.get("category", "all") if isinstance(img, dict) else "all"
            items += f'''
            <div class="filter-gallery-item" data-category="{category}">
                <img src="{url}" alt="{caption}" loading="lazy" data-lightbox />
                <div class="item-overlay"><span>{caption}</span></div>
            </div>
            '''
        
        return f'''
        <section class="gallery-filter-section" id="gallery">
            <div class="container">
                <h2>Gallery</h2>
                <div class="filter-buttons">{filters}</div>
                <div class="filter-grid">{items}</div>
            </div>
        </section>
        
        <style>
        .gallery-filter-section {{ padding: 80px 24px; }}
        .gallery-filter-section .container {{ max-width: 1200px; margin: 0 auto; }}
        .gallery-filter-section h2 {{ text-align: center; color: {text}; margin-bottom: 40px; }}
        .filter-buttons {{
            display: flex;
            justify-content: center;
            gap: 12px;
            margin-bottom: 40px;
            flex-wrap: wrap;
        }}
        .filter-btn {{
            padding: 10px 24px;
            background: #f3f4f6;
            border: none;
            border-radius: 50px;
            cursor: pointer;
            font-weight: 500;
            transition: all 0.3s;
            color: {text};
        }}
        .filter-btn:hover {{ background: #e5e7eb; }}
        .filter-btn.active {{ background: {primary}; color: white; }}
        .filter-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 20px;
        }}
        .filter-gallery-item {{
            position: relative;
            border-radius: 16px;
            overflow: hidden;
            aspect-ratio: 4/3;
            cursor: pointer;
            transition: transform 0.3s, opacity 0.3s;
        }}
        .filter-gallery-item.hidden {{
            display: none;
        }}
        .filter-gallery-item img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.5s;
        }}
        .filter-gallery-item:hover img {{ transform: scale(1.1); }}
        .item-overlay {{
            position: absolute;
            inset: 0;
            background: linear-gradient(to top, rgba(0,0,0,0.6), transparent);
            display: flex;
            align-items: flex-end;
            padding: 20px;
            opacity: 0;
            transition: opacity 0.3s;
        }}
        .filter-gallery-item:hover .item-overlay {{ opacity: 1; }}
        .item-overlay span {{ color: white; font-weight: 500; }}
        </style>
        
        <script>
        function filterGallery(category) {{
            // Update buttons
            document.querySelectorAll('.filter-btn').forEach(btn => {{
                btn.classList.toggle('active', btn.textContent.toLowerCase() === category || (category === 'all' && btn.textContent === 'All'));
            }});
            
            // Filter items
            document.querySelectorAll('.filter-gallery-item').forEach(item => {{
                if (category === 'all' || item.dataset.category === category) {{
                    item.classList.remove('hidden');
                    item.style.animation = 'fadeIn 0.3s ease forwards';
                }} else {{
                    item.classList.add('hidden');
                }}
            }});
        }}
        </script>
        '''
    
    @classmethod
    def _render_carousel_fullscreen(cls, images: List[Dict], colors: Dict[str, str], props: Dict) -> str:
        primary = colors.get("primary", "#6366f1")
        
        slides = ""
        dots = ""
        for i, img in enumerate(images):
            url = img.get("url", img) if isinstance(img, dict) else img
            caption = img.get("caption", "") if isinstance(img, dict) else ""
            active = "active" if i == 0 else ""
            slides += f'''
            <div class="carousel-slide {active}" data-slide="{i}">
                <img src="{url}" alt="{caption}" />
                <div class="slide-caption">{caption}</div>
            </div>
            '''
            dots += f'<button class="carousel-dot {active}" onclick="goToCarouselSlide({i})"></button>'
        
        return f'''
        <section class="gallery-carousel" id="gallery">
            <div class="carousel-container">
                <div class="carousel-slides">{slides}</div>
                <button class="carousel-nav prev" onclick="navigateCarousel(-1)">&#10094;</button>
                <button class="carousel-nav next" onclick="navigateCarousel(1)">&#10095;</button>
                <div class="carousel-dots">{dots}</div>
            </div>
        </section>
        
        <style>
        .gallery-carousel {{ background: #0a0a0a; }}
        .carousel-container {{
            position: relative;
            width: 100%;
            height: 100vh;
            overflow: hidden;
        }}
        .carousel-slide {{
            position: absolute;
            inset: 0;
            opacity: 0;
            transition: opacity 0.6s ease;
        }}
        .carousel-slide.active {{ opacity: 1; }}
        .carousel-slide img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
        }}
        .slide-caption {{
            position: absolute;
            bottom: 100px;
            left: 50%;
            transform: translateX(-50%);
            color: white;
            font-size: 1.5rem;
            font-weight: 600;
            text-shadow: 0 2px 10px rgba(0,0,0,0.5);
        }}
        .carousel-nav {{
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
            background: rgba(255,255,255,0.1);
            color: white;
            border: none;
            width: 60px;
            height: 60px;
            border-radius: 50%;
            font-size: 1.5rem;
            cursor: pointer;
            transition: background 0.3s;
        }}
        .carousel-nav:hover {{ background: rgba(255,255,255,0.2); }}
        .carousel-nav.prev {{ left: 30px; }}
        .carousel-nav.next {{ right: 30px; }}
        .carousel-dots {{
            position: absolute;
            bottom: 40px;
            left: 50%;
            transform: translateX(-50%);
            display: flex;
            gap: 12px;
        }}
        .carousel-dot {{
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background: rgba(255,255,255,0.4);
            border: none;
            cursor: pointer;
            transition: all 0.3s;
        }}
        .carousel-dot.active {{ background: {primary}; width: 36px; border-radius: 6px; }}
        </style>
        
        <script>
        let carouselIndex = 0;
        const totalCarouselSlides = {len(images)};
        
        function navigateCarousel(dir) {{
            carouselIndex += dir;
            if (carouselIndex < 0) carouselIndex = totalCarouselSlides - 1;
            if (carouselIndex >= totalCarouselSlides) carouselIndex = 0;
            updateCarousel();
        }}
        
        function goToCarouselSlide(idx) {{
            carouselIndex = idx;
            updateCarousel();
        }}
        
        function updateCarousel() {{
            document.querySelectorAll('.carousel-slide').forEach((s, i) => s.classList.toggle('active', i === carouselIndex));
            document.querySelectorAll('.carousel-dot').forEach((d, i) => d.classList.toggle('active', i === carouselIndex));
        }}
        
        // Auto-play
        setInterval(() => navigateCarousel(1), 5000);
        </script>
        '''
