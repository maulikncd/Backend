from typing import Dict, Any, List

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """
    Minimal Cards - Clean, simple project cards with subtle hover effects
    and sophisticated typography
    """
    title = props.get("sectionTitle", props.get("title", "Work"))
    projects = props.get("projects", _get_default_projects())
    
    primary = colors.get("primary", "#0A0A0A")
    bg = colors.get("background", "#FAFAFA")
    text = colors.get("text", "#0A0A0A")
    accent = colors.get("secondary", "#6366F1")
    
    project_html = ""
    for i, project in enumerate(projects[:6]):
        project_html += f'''
        <a href="{project.get('url', '#')}" class="minimal-card">
            <div class="card-image-wrapper">
                <img src="{project.get('image', 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800')}" alt="{project.get('title', 'Project')}">
            </div>
            <div class="card-info">
                <div class="card-meta">
                    <span class="card-year">{project.get('year', '2024')}</span>
                    <span class="card-category">{project.get('category', 'Design')}</span>
                </div>
                <h3 class="card-title">{project.get('title', 'Project Title')}</h3>
                <span class="card-arrow">→</span>
            </div>
        </a>
        '''
    
    return f'''
    <section class="minimal-projects" id="projects">
        <div class="container">
            <div class="section-header">
                <h2>{title}</h2>
            </div>
            
            <div class="projects-grid">
                {project_html}
            </div>
        </div>
    </section>
    
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=Inter:wght@400;500;600&display=swap');
    
    .minimal-projects {{
        padding: 120px 0;
        background: {bg};
    }}
    .minimal-projects .container {{
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 40px;
    }}
    .section-header {{
        margin-bottom: 60px;
    }}
    .section-header h2 {{
        font-family: 'DM Serif Display', serif;
        font-size: 3rem;
        font-weight: 400;
        color: {text};
    }}
    .projects-grid {{
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 40px;
    }}
    .minimal-card {{
        text-decoration: none;
        display: block;
        transition: all 0.4s;
    }}
    .minimal-card:hover {{
        transform: translateY(-5px);
    }}
    .card-image-wrapper {{
        aspect-ratio: 4/3;
        overflow: hidden;
        margin-bottom: 24px;
    }}
    .card-image-wrapper img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        filter: grayscale(100%);
        transition: all 0.5s;
    }}
    .minimal-card:hover .card-image-wrapper img {{
        filter: grayscale(0%);
        transform: scale(1.05);
    }}
    .card-info {{
        display: flex;
        align-items: flex-start;
        gap: 20px;
    }}
    .card-meta {{
        display: flex;
        flex-direction: column;
        gap: 4px;
        min-width: 80px;
    }}
    .card-year {{
        font-size: 0.8rem;
        color: {text}50;
    }}
    .card-category {{
        font-size: 0.75rem;
        color: {accent};
        text-transform: uppercase;
        letter-spacing: 1px;
    }}
    .card-title {{
        flex: 1;
        font-family: 'DM Serif Display', serif;
        font-size: 1.5rem;
        font-weight: 400;
        color: {text};
        line-height: 1.3;
        margin: 0;
    }}
    .card-arrow {{
        font-size: 1.5rem;
        color: {text}30;
        transition: all 0.3s;
    }}
    .minimal-card:hover .card-arrow {{
        color: {accent};
        transform: translateX(5px);
    }}
    @media (max-width: 768px) {{
        .projects-grid {{ grid-template-columns: 1fr; }}
        .minimal-projects .container {{ padding: 0 24px; }}
    }}
    </style>
    '''


def _get_default_projects() -> List[Dict]:
    return [
        {"title": "E-Commerce Platform Redesign", "category": "Web Design", "year": "2024", "image": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800"},
        {"title": "Finance App UI Kit", "category": "Product Design", "year": "2024", "image": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800"},
        {"title": "Brand Identity System", "category": "Branding", "year": "2023", "image": "https://images.unsplash.com/photo-1558655146-d09347e92766?w=800"},
        {"title": "SaaS Dashboard", "category": "UI/UX", "year": "2023", "image": "https://images.unsplash.com/photo-1467232004584-a241de8bcf5d?w=800"},
        {"title": "Mobile Banking App", "category": "Mobile", "year": "2023", "image": "https://images.unsplash.com/photo-1563986768609-322da13575f3?w=800"},
        {"title": "NFT Marketplace", "category": "Web3", "year": "2023", "image": "https://images.unsplash.com/photo-1639762681057-408e52192e55?w=800"},
    ]
