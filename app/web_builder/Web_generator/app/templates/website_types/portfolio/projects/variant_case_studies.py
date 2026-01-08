from typing import Dict, Any, List

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """
    Case Studies - Detailed case study style with large images,
    project stats and comprehensive descriptions
    """
    title = props.get("sectionTitle", props.get("title", "Case Studies"))
    subtitle = props.get("subtitle", "Deep dives into selected projects")
    projects = props.get("projects", _get_default_projects())
    
    primary = colors.get("primary", "#6366F1")
    bg = colors.get("background", "#0F172A")
    text = colors.get("text", "#F8FAFC")
    
    project_html = ""
    for i, project in enumerate(projects[:3]):
        reverse = "reverse" if i % 2 == 1 else ""
        project_html += f'''
        <div class="case-study {reverse}">
            <div class="case-image">
                <img src="{project.get('image', 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=1000')}" alt="{project.get('title', 'Project')}">
                <div class="case-number">0{i+1}</div>
            </div>
            <div class="case-content">
                <span class="case-category">{project.get('category', 'Web Development')}</span>
                <h3 class="case-title">{project.get('title', 'Project Title')}</h3>
                <p class="case-desc">{project.get('description', 'Detailed project description showcasing the work done.')}</p>
                
                <div class="case-stats">
                    <div class="stat">
                        <span class="stat-value">{project.get('stat1_value', '+150%')}</span>
                        <span class="stat-label">{project.get('stat1_label', 'Conversion Rate')}</span>
                    </div>
                    <div class="stat">
                        <span class="stat-value">{project.get('stat2_value', '2x')}</span>
                        <span class="stat-label">{project.get('stat2_label', 'User Engagement')}</span>
                    </div>
                </div>
                
                <a href="{project.get('url', '#')}" class="case-link">
                    View Case Study
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M7 17L17 7M17 7H7M17 7V17"/>
                    </svg>
                </a>
            </div>
        </div>
        '''
    
    return f'''
    <section class="case-studies-section" id="projects">
        <div class="container">
            <div class="section-header">
                <h2 class="section-title">{title}</h2>
                <p class="section-subtitle">{subtitle}</p>
            </div>
            
            <div class="case-studies-list">
                {project_html}
            </div>
        </div>
    </section>
    
    <style>
    .case-studies-section {{
        padding: 120px 0;
        background: {bg};
    }}
    .case-studies-section .container {{
        max-width: 1400px;
        margin: 0 auto;
        padding: 0 40px;
    }}
    .section-header {{
        margin-bottom: 80px;
    }}
    .section-title {{
        font-size: clamp(2.5rem, 5vw, 4rem);
        font-weight: 700;
        color: {text};
        margin-bottom: 16px;
    }}
    .section-subtitle {{
        font-size: 1.2rem;
        color: {text}60;
    }}
    .case-studies-list {{
        display: flex;
        flex-direction: column;
        gap: 100px;
    }}
    .case-study {{
        display: grid;
        grid-template-columns: 1.2fr 1fr;
        gap: 80px;
        align-items: center;
    }}
    .case-study.reverse {{
        grid-template-columns: 1fr 1.2fr;
    }}
    .case-study.reverse .case-image {{
        order: 2;
    }}
    .case-image {{
        position: relative;
        border-radius: 24px;
        overflow: hidden;
    }}
    .case-image img {{
        width: 100%;
        height: 400px;
        object-fit: cover;
        transition: transform 0.5s;
    }}
    .case-study:hover .case-image img {{
        transform: scale(1.05);
    }}
    .case-number {{
        position: absolute;
        top: 30px;
        left: 30px;
        font-size: 4rem;
        font-weight: 800;
        color: white;
        opacity: 0.3;
        font-family: 'Inter', sans-serif;
    }}
    .case-content {{
        max-width: 500px;
    }}
    .case-study.reverse .case-content {{
        margin-left: auto;
    }}
    .case-category {{
        display: inline-block;
        padding: 8px 16px;
        background: {primary}20;
        color: {primary};
        border-radius: 50px;
        font-size: 0.8rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 20px;
    }}
    .case-title {{
        font-size: 2rem;
        font-weight: 700;
        color: {text};
        margin-bottom: 20px;
        line-height: 1.3;
    }}
    .case-desc {{
        font-size: 1.1rem;
        color: {text}70;
        line-height: 1.8;
        margin-bottom: 30px;
    }}
    .case-stats {{
        display: flex;
        gap: 40px;
        margin-bottom: 40px;
        padding: 30px;
        background: rgba(255,255,255,0.03);
        border-radius: 16px;
        border: 1px solid rgba(255,255,255,0.05);
    }}
    .stat-value {{
        display: block;
        font-size: 2rem;
        font-weight: 700;
        color: {primary};
    }}
    .stat-label {{
        font-size: 0.85rem;
        color: {text}50;
    }}
    .case-link {{
        display: inline-flex;
        align-items: center;
        gap: 10px;
        color: {text};
        text-decoration: none;
        font-weight: 600;
        padding: 16px 0;
        border-bottom: 2px solid {primary};
        transition: all 0.3s;
    }}
    .case-link:hover {{
        color: {primary};
        padding-left: 10px;
    }}
    .case-link svg {{
        transition: transform 0.3s;
    }}
    .case-link:hover svg {{
        transform: translate(5px, -5px);
    }}
    @media (max-width: 1024px) {{
        .case-study, .case-study.reverse {{
            grid-template-columns: 1fr;
            gap: 40px;
        }}
        .case-study.reverse .case-image {{ order: 0; }}
        .case-study.reverse .case-content {{ margin-left: 0; }}
    }}
    @media (max-width: 640px) {{
        .case-studies-section .container {{ padding: 0 20px; }}
        .case-stats {{ flex-direction: column; gap: 20px; }}
    }}
    </style>
    '''


def _get_default_projects() -> List[Dict]:
    return [
        {"title": "Revolutionizing E-Commerce Experience", "category": "Web Development", "description": "Led the complete redesign of a major e-commerce platform, resulting in significant improvements in user engagement and conversion rates.", "image": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=1000", "stat1_value": "+150%", "stat1_label": "Conversion Rate", "stat2_value": "2.5x", "stat2_label": "User Engagement"},
        {"title": "Finance Dashboard Redesign", "category": "UI/UX Design", "description": "Transformed complex financial data into an intuitive, accessible dashboard that empowers users to make informed decisions.", "image": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=1000", "stat1_value": "-40%", "stat1_label": "Support Tickets", "stat2_value": "+85%", "stat2_label": "Task Completion"},
        {"title": "Mobile Banking Revolution", "category": "Mobile App", "description": "Designed and developed a next-generation mobile banking app that prioritizes security and user experience.", "image": "https://images.unsplash.com/photo-1563986768609-322da13575f3?w=1000", "stat1_value": "4.8", "stat1_label": "App Store Rating", "stat2_value": "1M+", "stat2_label": "Downloads"},
    ]
