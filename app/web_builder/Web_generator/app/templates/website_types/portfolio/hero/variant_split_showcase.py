from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """
    Split Showcase - Clean split layout with large image and text,
    professional and modern aesthetic
    """
    name = props.get("name", props.get("businessName", "Emma Designer"))
    title = props.get("title", "Product Designer")
    tagline = props.get("tagline", "Creating meaningful digital products")
    description = props.get("description", "I help startups and enterprises design user-centered products that make a difference.")
    cta = props.get("cta", "See Projects")
    
    primary = colors.get("primary", "#2563EB")
    bg = colors.get("background", "#FFFFFF")
    text = colors.get("text", "#1F2937")
    
    return f'''
    <section class="split-hero" id="hero">
        <div class="hero-left">
            <div class="content-wrapper">
                <div class="label-badge">
                    <span>Portfolio</span>
                </div>
                
                <h1 class="hero-name">{name}</h1>
                <h2 class="hero-title">{title}</h2>
                
                <p class="hero-desc">{description}</p>
                
                <div class="action-row">
                    <a href="#projects" class="btn-solid">{cta}</a>
                    <a href="#contact" class="btn-link">Let's Talk →</a>
                </div>
                
                <div class="clients-section">
                    <span class="clients-label">Trusted by</span>
                    <div class="client-logos">
                        <span class="logo-placeholder">Google</span>
                        <span class="logo-placeholder">Meta</span>
                        <span class="logo-placeholder">Apple</span>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="hero-right">
            <div class="image-wrapper">
                <img src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=800" alt="{name}">
                <div class="image-overlay"></div>
            </div>
            
            <div class="experience-badge">
                <span class="exp-number">10+</span>
                <span class="exp-text">Years of<br>Experience</span>
            </div>
        </div>
    </section>
    
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=DM+Serif+Display&display=swap');
    
    .split-hero {{
        min-height: 100vh;
        display: grid;
        grid-template-columns: 1fr 1fr;
        background: {bg};
    }}
    .hero-left {{
        display: flex;
        align-items: center;
        padding: 120px 80px 80px;
    }}
    .content-wrapper {{
        max-width: 520px;
    }}
    .label-badge {{
        display: inline-block;
        padding: 8px 20px;
        background: {primary}10;
        color: {primary};
        border-radius: 50px;
        font-size: 0.85rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 30px;
    }}
    .hero-name {{
        font-family: 'DM Serif Display', serif;
        font-size: clamp(3rem, 5vw, 4.5rem);
        font-weight: 400;
        color: {text};
        line-height: 1.1;
        margin-bottom: 12px;
    }}
    .hero-title {{
        font-family: 'DM Sans', sans-serif;
        font-size: 1.4rem;
        font-weight: 500;
        color: {primary};
        margin-bottom: 30px;
    }}
    .hero-desc {{
        font-size: 1.1rem;
        color: {text}90;
        line-height: 1.8;
        margin-bottom: 40px;
    }}
    .action-row {{
        display: flex;
        align-items: center;
        gap: 30px;
        margin-bottom: 60px;
        flex-wrap: wrap;
    }}
    .btn-solid {{
        padding: 18px 36px;
        background: {primary};
        color: white;
        text-decoration: none;
        font-weight: 600;
        border-radius: 12px;
        transition: all 0.3s;
    }}
    .btn-solid:hover {{
        transform: translateY(-2px);
        box-shadow: 0 15px 40px {primary}30;
    }}
    .btn-link {{
        color: {text};
        text-decoration: none;
        font-weight: 600;
        transition: color 0.3s;
    }}
    .btn-link:hover {{
        color: {primary};
    }}
    .clients-section {{
        padding-top: 30px;
        border-top: 1px solid #eee;
    }}
    .clients-label {{
        display: block;
        font-size: 0.8rem;
        color: {text}60;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 16px;
    }}
    .client-logos {{
        display: flex;
        gap: 30px;
    }}
    .logo-placeholder {{
        font-size: 0.95rem;
        font-weight: 600;
        color: {text}40;
    }}
    .hero-right {{
        position: relative;
        overflow: hidden;
    }}
    .image-wrapper {{
        height: 100%;
        position: relative;
    }}
    .image-wrapper img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
    }}
    .image-overlay {{
        position: absolute;
        inset: 0;
        background: linear-gradient(135deg, {primary}20, transparent);
    }}
    .experience-badge {{
        position: absolute;
        bottom: 60px;
        left: -40px;
        background: white;
        padding: 30px 40px;
        border-radius: 20px;
        box-shadow: 0 20px 50px rgba(0,0,0,0.1);
        display: flex;
        align-items: center;
        gap: 16px;
    }}
    .exp-number {{
        font-size: 3rem;
        font-weight: 700;
        color: {primary};
    }}
    .exp-text {{
        font-size: 0.9rem;
        color: {text}80;
        line-height: 1.4;
    }}
    @media (max-width: 1024px) {{
        .split-hero {{ grid-template-columns: 1fr; }}
        .hero-left {{ padding: 120px 40px 60px; text-align: center; }}
        .content-wrapper {{ max-width: 100%; }}
        .action-row {{ justify-content: center; }}
        .clients-section {{ text-align: center; }}
        .client-logos {{ justify-content: center; }}
        .hero-right {{ height: 60vh; }}
        .experience-badge {{ left: 50%; transform: translateX(-50%); bottom: 40px; }}
    }}
    @media (max-width: 640px) {{
        .hero-left {{ padding: 100px 24px 40px; }}
        .experience-badge {{ display: none; }}
    }}
    </style>
    '''
