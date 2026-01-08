from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Location Based - With map/location"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="portfolio-contact-location" id="contact">
        <div class="location-container">
            <div class="map-section">
                <div class="map-placeholder">📍 San Francisco, CA</div>
            </div>
            <div class="contact-section">
                <h2>Let's Meet</h2>
                <p>Based in San Francisco, available for meetings worldwide.</p>
                <div class="contact-details">
                    <div class="detail"><span class="label">Email</span><a href="mailto:hello@example.com">hello@example.com</a></div>
                    <div class="detail"><span class="label">Phone</span><a href="tel:+1234567890">+1 (234) 567-890</a></div>
                    <div class="detail"><span class="label">Office</span><span>123 Main St, SF, CA 94102</span></div>
                </div>
                <a href="mailto:hello@example.com" class="btn">Get in Touch →</a>
            </div>
        </div>
    </section>
    
    <style>
    .portfolio-contact-location {{ padding: 120px 24px; background: {background}; }}
    .location-container {{ max-width: 1100px; margin: 0 auto; display: grid; grid-template-columns: 1fr 1fr; gap: 60px; align-items: center; }}
    .map-section {{ aspect-ratio: 4/3; background: {text}05; border-radius: 24px; display: flex; align-items: center; justify-content: center; }}
    .map-placeholder {{ font-size: 2rem; color: {primary}; font-weight: 600; }}
    .contact-section h2 {{ font-size: clamp(2.5rem, 5vw, 4rem); font-weight: 800; color: {text}; margin-bottom: 16px; }}
    .contact-section p {{ color: {secondary}; font-size: 1.1rem; margin-bottom: 40px; }}
    .contact-details {{ margin-bottom: 40px; }}
    .detail {{ padding: 16px 0; border-bottom: 1px solid {text}10; }}
    .label {{ display: block; color: {secondary}; font-size: 0.9rem; margin-bottom: 4px; }}
    .detail a, .detail span {{ color: {text}; font-weight: 600; text-decoration: none; }}
    .detail a:hover {{ color: {primary}; }}
    .btn {{ display: inline-block; padding: 18px 40px; background: {primary}; color: {background}; text-decoration: none; font-weight: 700; border-radius: 12px; transition: all 0.3s ease; }}
    .btn:hover {{ transform: translateY(-4px); box-shadow: 0 20px 40px {primary}40; }}
    @media (max-width: 900px) {{ .location-container {{ grid-template-columns: 1fr; }} }}
    </style>
    '''
