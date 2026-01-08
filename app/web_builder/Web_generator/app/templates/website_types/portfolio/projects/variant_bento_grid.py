from typing import Dict, Any, List

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """
    Bento Grid - Modern bento-box style project grid with
    varied card sizes and hover animations
    """
    title = props.get("sectionTitle", props.get("title", "Selected Works"))
    subtitle = props.get("subtitle", "A curated selection of my best projects")
    projects = props.get("projects", _get_default_projects())
    
    primary = colors.get("primary", "#6366F1")
    bg = colors.get("background", "#FFFFFF")
    text = colors.get("text", "#1F2937")
    
    # Generate project cards with varying sizes
    project_html = ""
    sizes = ["large", "medium", "medium", "small", "small", "medium"]
    
    for i, project in enumerate(projects[:6]):
        size = sizes[i] if i < len(sizes) else "medium"
        project_html += f'''
        <div class="project-card size-{size}" data-index="{i}">
            <div class="card-image">
                <img src="{project.get('image', f'https://images.unsplash.com/photo-155816779819{i}-a7c9a3?w=800')}" alt="{project.get('title', 'Project')}">
                <div class="card-overlay">
                    <a href="{project.get('url', '#')}" class="view-btn">View Project</a>
                </div>
            </div>
            <div class="card-content">
                <span class="project-category">{project.get('category', 'Web Design')}</span>
                <h3 class="project-title">{project.get('title', 'Project Title')}</h3>
                <p class="project-desc">{project.get('description', 'Project description goes here.')}</p>
            </div>
        </div>
        '''
    
    return f'''
    <section class="projects-section" id="projects">
        <div class="container">
            <div class="section-header">
                <span class="section-label">Portfolio</span>
                <h2 class="section-title">{title}</h2>
                <p class="section-subtitle">{subtitle}</p>
            </div>
            
            <div class="bento-grid">
                {project_html}
            </div>
            
            <div class="section-footer">
                <a href="#" class="view-all-btn">
                    View All Projects
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M5 12h14M12 5l7 7-7 7"/>
                    </svg>
                </a>
            </div>
        </div>
    </section>
    
    <style>
    .projects-section {{
        padding: 120px 0;
        background: {bg};
    }}
    .projects-section .container {{
        max-width: 1400px;
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
        max-width: 500px;
        margin: 0 auto;
    }}
    .bento-grid {{
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        grid-auto-rows: 300px;
        gap: 24px;
    }}
    .project-card {{
        border-radius: 24px;
        overflow: hidden;
        background: #f8fafc;
        display: flex;
        flex-direction: column;
        transition: transform 0.4s, box-shadow 0.4s;
        cursor: pointer;
    }}
    .project-card:hover {{
        transform: translateY(-8px);
        box-shadow: 0 30px 60px rgba(0,0,0,0.1);
    }}
    .size-large {{
        grid-column: span 2;
        grid-row: span 2;
    }}
    .size-medium {{
        grid-column: span 2;
    }}
    .size-small {{
        grid-column: span 1;
    }}
    .card-image {{
        flex: 1;
        position: relative;
        overflow: hidden;
    }}
    .card-image img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.5s;
    }}
    .project-card:hover .card-image img {{
        transform: scale(1.1);
    }}
    .card-overlay {{
        position: absolute;
        inset: 0;
        background: {primary}90;
        display: flex;
        align-items: center;
        justify-content: center;
        opacity: 0;
        transition: opacity 0.3s;
    }}
    .project-card:hover .card-overlay {{
        opacity: 1;
    }}
    .view-btn {{
        padding: 14px 28px;
        background: white;
        color: {primary};
        text-decoration: none;
        font-weight: 600;
        border-radius: 50px;
        transform: translateY(20px);
        transition: transform 0.3s;
    }}
    .project-card:hover .view-btn {{
        transform: translateY(0);
    }}
    .card-content {{
        padding: 24px;
    }}
    .project-category {{
        font-size: 0.8rem;
        color: {primary};
        text-transform: uppercase;
        letter-spacing: 1px;
        font-weight: 600;
    }}
    .project-title {{
        font-size: 1.3rem;
        font-weight: 700;
        color: {text};
        margin: 8px 0;
    }}
    .project-desc {{
        font-size: 0.95rem;
        color: {text}70;
        line-height: 1.6;
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
        overflow: hidden;
    }}
    .section-footer {{
        text-align: center;
        margin-top: 60px;
    }}
    .view-all-btn {{
        display: inline-flex;
        align-items: center;
        gap: 12px;
        padding: 18px 40px;
        background: {text};
        color: white;
        text-decoration: none;
        font-weight: 600;
        border-radius: 12px;
        transition: all 0.3s;
    }}
    .view-all-btn:hover {{
        background: {primary};
        transform: translateY(-2px);
    }}
    .view-all-btn svg {{
        transition: transform 0.3s;
    }}
    .view-all-btn:hover svg {{
        transform: translateX(5px);
    }}
    @media (max-width: 1024px) {{
        .bento-grid {{
            grid-template-columns: repeat(2, 1fr);
            grid-auto-rows: 280px;
        }}
        .size-large {{ grid-column: span 2; grid-row: span 1; }}
        .size-medium {{ grid-column: span 1; }}
    }}
    @media (max-width: 640px) {{
        .bento-grid {{
            grid-template-columns: 1fr;
            grid-auto-rows: 350px;
        }}
        .size-large, .size-medium, .size-small {{ grid-column: span 1; grid-row: span 1; }}
        .projects-section .container {{ padding: 0 20px; }}
    }}
    </style>
    '''


def _get_default_projects() -> List[Dict]:
    return [
        {"title": "E-Commerce Platform", "category": "Web Development", "description": "A modern e-commerce solution with seamless checkout experience", "image": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800"},
        {"title": "Finance Dashboard", "category": "UI/UX Design", "description": "Analytics dashboard for fintech startup", "image": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800"},
        {"title": "Mobile Banking App", "category": "Mobile App", "description": "Redesigning the mobile banking experience", "image": "https://images.unsplash.com/photo-1563986768609-322da13575f3?w=800"},
        {"title": "SaaS Landing Page", "category": "Web Design", "description": "High-converting landing page for B2B SaaS", "image": "https://images.unsplash.com/photo-1467232004584-a241de8bcf5d?w=800"},
        {"title": "Brand Identity", "category": "Branding", "description": "Complete brand identity for tech startup", "image": "https://images.unsplash.com/photo-1558655146-d09347e92766?w=800"},
        {"title": "Portfolio Website", "category": "Web Development", "description": "Personal portfolio with smooth animations", "image": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=800"},
    ]
