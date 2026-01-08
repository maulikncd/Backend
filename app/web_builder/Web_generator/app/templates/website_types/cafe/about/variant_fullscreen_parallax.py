from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Fullscreen Parallax About - Immersive scrolling experience"""
    title = props.get("title", "Our Story")
    story = props.get("story", props.get("content", ""))[:400]
    
    primary = colors.get("primary", "#8B7355")
    
    return f'''
    <section class="about-parallax" id="about">
        <div class="parallax-bg" style="background-image: url('https://images.unsplash.com/photo-1445116572660-236099ec97a0?w=1920')"></div>
        <div class="parallax-overlay"></div>
        <div class="parallax-content">
            <span class="about-badge">Our Story</span>
            <h2>{title}</h2>
            <p>{story if story else "From humble beginnings to becoming a beloved community gathering place, our journey has been fueled by passion and dedication to the craft of coffee."}</p>
            <a href="#menu" class="explore-btn">Explore Our Menu</a>
        </div>
    </section>
    
    <style>
    .about-parallax {{ min-height: 100vh; position: relative; display: flex; align-items: center; justify-content: center; text-align: center; color: #fff; overflow: hidden; }}
    .parallax-bg {{ position: absolute; inset: -50px; background-size: cover; background-position: center; background-attachment: fixed; }}
    .parallax-overlay {{ position: absolute; inset: 0; background: linear-gradient(180deg, rgba(0,0,0,0.6) 0%, rgba(0,0,0,0.8) 100%); }}
    .parallax-content {{ position: relative; z-index: 2; max-width: 800px; padding: 40px; }}
    .about-badge {{ display: inline-block; padding: 10px 25px; border: 1px solid rgba(255,255,255,0.3); border-radius: 50px; font-size: 0.9rem; letter-spacing: 3px; text-transform: uppercase; margin-bottom: 30px; }}
    .about-parallax h2 {{ font-family: 'Playfair Display', serif; font-size: clamp(3rem, 6vw, 5rem); margin-bottom: 30px; font-weight: 400; }}
    .about-parallax p {{ font-size: 1.2rem; line-height: 1.9; color: rgba(255,255,255,0.85); margin-bottom: 40px; }}
    .explore-btn {{ display: inline-block; padding: 18px 50px; background: {primary}; color: #fff; text-decoration: none; border-radius: 50px; font-weight: 600; transition: 0.3s; }}
    .explore-btn:hover {{ transform: translateY(-3px); box-shadow: 0 20px 40px rgba(0,0,0,0.3); }}
    </style>
    '''
