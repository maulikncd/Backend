from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Video Background About - Motion-rich experience"""
    title = props.get("title", "Our Passion")
    story = props.get("story", props.get("content", ""))[:300]
    
    primary = colors.get("primary", "#8B7355")
    
    return f'''
    <section class="about-video-bg" id="about">
        <div class="video-container">
            <video autoplay muted loop playsinline>
                <source src="https://assets.mixkit.co/videos/preview/mixkit-making-a-latte-coffee-17470-large.mp4" type="video/mp4">
            </video>
            <div class="video-overlay"></div>
        </div>
        <div class="video-content">
            <div class="content-box">
                <span class="pre-title">About Us</span>
                <h2>{title}</h2>
                <p>{story if story else "Every cup we serve is a testament to our commitment to quality, sustainability, and the art of coffee making."}</p>
                <div class="content-stats">
                    <div class="v-stat"><span>Est.</span><strong>2020</strong></div>
                    <div class="v-stat"><span>Cups</span><strong>500K+</strong></div>
                    <div class="v-stat"><span>Team</span><strong>25+</strong></div>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    .about-video-bg {{ min-height: 100vh; position: relative; display: flex; align-items: center; }}
    .video-container {{ position: absolute; inset: 0; overflow: hidden; }}
    .video-container video {{ width: 100%; height: 100%; object-fit: cover; }}
    .video-overlay {{ position: absolute; inset: 0; background: linear-gradient(90deg, rgba(0,0,0,0.85) 0%, rgba(0,0,0,0.4) 100%); }}
    .video-content {{ position: relative; z-index: 2; width: 100%; max-width: 600px; padding: 60px; color: #fff; }}
    .content-box {{ }}
    .pre-title {{ display: block; text-transform: uppercase; letter-spacing: 4px; font-size: 0.85rem; color: {primary}; margin-bottom: 20px; }}
    .about-video-bg h2 {{ font-family: 'Playfair Display', serif; font-size: 4rem; margin-bottom: 30px; line-height: 1.1; }}
    .about-video-bg p {{ font-size: 1.2rem; line-height: 1.8; color: rgba(255,255,255,0.8); margin-bottom: 50px; }}
    .content-stats {{ display: flex; gap: 50px; }}
    .v-stat {{ text-align: left; }}
    .v-stat span {{ display: block; font-size: 0.85rem; color: rgba(255,255,255,0.5); text-transform: uppercase; letter-spacing: 2px; margin-bottom: 5px; }}
    .v-stat strong {{ font-size: 2rem; color: {primary}; }}
    @media (max-width: 768px) {{ .video-content {{ padding: 40px 24px; }} }}
    </style>
    '''
