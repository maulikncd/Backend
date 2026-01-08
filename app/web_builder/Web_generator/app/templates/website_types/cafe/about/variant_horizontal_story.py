from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Horizontal Scroll About - Cinematic scrolling story"""
    title = props.get("title", "Our Journey")
    milestones = props.get("milestones", [])
    
    primary = colors.get("primary", "#8B7355")
    text = colors.get("text", "#2D2013")
    
    if not milestones:
        milestones = [
            {"year": "2020", "title": "The Beginning", "description": "Our cafe was born from a shared love of exceptional coffee"},
            {"year": "2021", "title": "Growing Together", "description": "We expanded our menu and welcomed new team members"},
            {"year": "2022", "title": "Community Hub", "description": "Became a beloved gathering place for locals"},
            {"year": "2023", "title": "Recognition", "description": "Awarded best cafe in the neighborhood"},
            {"year": "2024", "title": "Innovation", "description": "Launched our signature seasonal menu"}
        ]
    
    slides_html = ""
    images = [
        "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=800",
        "https://images.unsplash.com/photo-1445116572660-236099ec97a0?w=800",
        "https://images.unsplash.com/photo-1442512595331-e89e73853f31?w=800",
        "https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?w=800",
        "https://images.unsplash.com/photo-1559496417-e7f25cb247f3?w=800"
    ]
    for i, ms in enumerate(milestones[:5]):
        slides_html += f'''
        <div class="story-slide">
            <div class="slide-image" style="background-image: url('{images[i % len(images)]}')"></div>
            <div class="slide-content">
                <span class="slide-year">{ms.get("year", "")}</span>
                <h3>{ms.get("title", "")}</h3>
                <p>{ms.get("description", "")[:100]}</p>
            </div>
        </div>
        '''
    
    return f'''
    <section class="about-hscroll" id="about">
        <div class="hscroll-header">
            <h2>{title}</h2>
            <p>Scroll horizontally to explore our story →</p>
        </div>
        <div class="hscroll-track">
            {slides_html}
        </div>
    </section>
    
    <style>
    .about-hscroll {{ padding: 100px 0; background: #0D0D0D; color: #fff; overflow: hidden; }}
    .hscroll-header {{ max-width: 1200px; margin: 0 auto 60px; padding: 0 40px; }}
    .hscroll-header h2 {{ font-family: 'Playfair Display', serif; font-size: 3.5rem; margin-bottom: 10px; }}
    .hscroll-header p {{ color: rgba(255,255,255,0.5); font-size: 1rem; }}
    .hscroll-track {{ display: flex; gap: 40px; padding: 0 40px; overflow-x: auto; scroll-behavior: smooth; scrollbar-width: none; }}
    .hscroll-track::-webkit-scrollbar {{ display: none; }}
    .story-slide {{ flex: 0 0 500px; position: relative; border-radius: 20px; overflow: hidden; height: 500px; }}
    .slide-image {{ position: absolute; inset: 0; background-size: cover; background-position: center; }}
    .slide-content {{ position: absolute; inset: 0; background: linear-gradient(to top, rgba(0,0,0,0.9), transparent); padding: 40px; display: flex; flex-direction: column; justify-content: flex-end; }}
    .slide-year {{ display: inline-block; padding: 8px 20px; background: {primary}; border-radius: 50px; font-weight: 600; font-size: 0.9rem; margin-bottom: 16px; align-self: flex-start; }}
    .slide-content h3 {{ font-family: 'Playfair Display', serif; font-size: 2rem; margin-bottom: 12px; }}
    .slide-content p {{ color: rgba(255,255,255,0.7); line-height: 1.6; }}
    </style>
    '''
