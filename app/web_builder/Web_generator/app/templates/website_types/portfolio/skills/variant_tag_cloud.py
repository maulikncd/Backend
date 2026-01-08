from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Tag Cloud - Skills as floating tags"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    skills = ["React", "Next.js", "Vue", "TypeScript", "Node.js", "Python", "Django", "PostgreSQL", "MongoDB", "Redis", "Docker", "AWS", "Git", "Figma", "UI/UX", "REST API", "GraphQL", "Testing"]
    
    tags_html = ""
    sizes = ["sm", "", "", "lg", "", "", "sm", "lg", "", ""]
    for i, s in enumerate(skills):
        size = sizes[i % len(sizes)]
        tags_html += f'<span class="tag-item {size}">{s}</span>'
    
    return f'''
    <section class="portfolio-skills-cloud" id="skills">
        <div class="cloud-container">
            <div class="cloud-header"><h2>Technologies I Work With</h2></div>
            <div class="tags-cloud">{tags_html}</div>
        </div>
    </section>
    
    <style>
    .portfolio-skills-cloud {{ padding: 120px 24px; background: {background}; }}
    .cloud-container {{ max-width: 900px; margin: 0 auto; text-align: center; }}
    .cloud-header {{ margin-bottom: 60px; }}
    .cloud-header h2 {{ font-size: clamp(2rem, 4vw, 3rem); font-weight: 800; color: {text}; }}
    .tags-cloud {{ display: flex; flex-wrap: wrap; justify-content: center; gap: 16px; }}
    .tag-item {{ padding: 14px 28px; background: {text}05; border: 1px solid {text}10; color: {text}; font-weight: 500; border-radius: 100px; transition: all 0.3s ease; cursor: default; }}
    .tag-item:hover {{ background: {primary}15; border-color: {primary}40; color: {primary}; transform: translateY(-4px); }}
    .tag-item.lg {{ font-size: 1.2rem; padding: 18px 36px; }}
    .tag-item.sm {{ font-size: 0.85rem; padding: 10px 20px; }}
    </style>
    '''
