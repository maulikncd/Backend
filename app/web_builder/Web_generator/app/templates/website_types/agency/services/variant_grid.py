from typing import Dict, Any, List

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """
    Services Grid - Professional services display with icons,
    descriptions and hover effects
    """
    title = props.get("sectionTitle", props.get("title", "What We Do"))
    subtitle = props.get("subtitle", "Full-spectrum digital services to help your business grow")
    services = props.get("services", _get_default_services())
    
    primary = colors.get("primary", "#2563EB")
    bg = colors.get("background", "#F8FAFC")
    text = colors.get("text", "#0F172A")
    
    services_html = ""
    for i, service in enumerate(services[:6]):
        services_html += f'''
        <div class="service-card">
            <div class="service-icon">{service.get('icon', '💡')}</div>
            <span class="service-number">0{i+1}</span>
            <h3 class="service-title">{service.get('name', 'Service')}</h3>
            <p class="service-desc">{service.get('description', 'Professional service description')}</p>
            <a href="#" class="service-link">Learn More →</a>
        </div>
        '''
    
    return f'''
    <section class="services-section" id="services">
        <div class="container">
            <div class="section-header">
                <span class="section-label">Services</span>
                <h2 class="section-title">{title}</h2>
                <p class="section-subtitle">{subtitle}</p>
            </div>
            
            <div class="services-grid">
                {services_html}
            </div>
        </div>
    </section>
    
    <style>
    .services-section {{
        padding: 120px 0;
        background: {bg};
    }}
    .services-section .container {{
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 40px;
    }}
    .section-header {{
        text-align: center;
        margin-bottom: 80px;
    }}
    .section-label {{
        display: inline-block;
        padding: 8px 20px;
        background: {primary}10;
        color: {primary};
        border-radius: 50px;
        font-size: 0.85rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 20px;
    }}
    .section-title {{
        font-size: clamp(2.5rem, 5vw, 3.5rem);
        font-weight: 700;
        color: {text};
        margin-bottom: 16px;
    }}
    .section-subtitle {{
        font-size: 1.2rem;
        color: {text}70;
        max-width: 600px;
        margin: 0 auto;
    }}
    .services-grid {{
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 30px;
    }}
    .service-card {{
        background: white;
        padding: 40px;
        border-radius: 20px;
        position: relative;
        transition: all 0.4s;
        border: 1px solid transparent;
    }}
    .service-card:hover {{
        border-color: {primary}30;
        transform: translateY(-10px);
        box-shadow: 0 30px 60px rgba(0,0,0,0.08);
    }}
    .service-icon {{
        font-size: 3rem;
        margin-bottom: 20px;
    }}
    .service-number {{
        position: absolute;
        top: 30px;
        right: 30px;
        font-size: 0.8rem;
        font-weight: 700;
        color: {text}20;
    }}
    .service-title {{
        font-size: 1.4rem;
        font-weight: 700;
        color: {text};
        margin-bottom: 16px;
    }}
    .service-desc {{
        font-size: 1rem;
        color: {text}70;
        line-height: 1.7;
        margin-bottom: 24px;
    }}
    .service-link {{
        color: {primary};
        text-decoration: none;
        font-weight: 600;
        font-size: 0.95rem;
        transition: all 0.3s;
    }}
    .service-link:hover {{
        padding-left: 10px;
    }}
    @media (max-width: 1024px) {{
        .services-grid {{ grid-template-columns: repeat(2, 1fr); }}
    }}
    @media (max-width: 640px) {{
        .services-grid {{ grid-template-columns: 1fr; }}
        .services-section .container {{ padding: 0 24px; }}
    }}
    </style>
    '''


def _get_default_services() -> List[Dict]:
    return [
        {"name": "Brand Strategy", "icon": "🎯", "description": "We help define your brand's vision, mission, and positioning to stand out in the market."},
        {"name": "Web Development", "icon": "💻", "description": "Custom web solutions built with modern technologies for optimal performance."},
        {"name": "UI/UX Design", "icon": "🎨", "description": "User-centered design that creates intuitive and engaging digital experiences."},
        {"name": "Digital Marketing", "icon": "📈", "description": "Data-driven marketing strategies to grow your online presence and reach."},
        {"name": "Mobile Apps", "icon": "📱", "description": "Native and cross-platform mobile applications for iOS and Android."},
        {"name": "Analytics & SEO", "icon": "🔍", "description": "Optimize your digital presence with data insights and search visibility."},
    ]
