from typing import Dict, Any, List

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """
    Categories View - Skills organized by category with
    clean tag-based display
    """
    title = props.get("sectionTitle", props.get("title", "What I Do"))
    skills = props.get("skills", _get_default_categorized_skills())
    
    primary = colors.get("primary", "#6366F1")
    bg = colors.get("background", "#FFFFFF")
    text = colors.get("text", "#1F2937")
    
    categories_html = ""
    for category, skill_list in skills.items():
        tags = "".join([f'<span class="skill-tag">{s}</span>' for s in skill_list])
        categories_html += f'''
        <div class="skill-category">
            <h3 class="category-title">{category}</h3>
            <div class="skill-tags">{tags}</div>
        </div>
        '''
    
    return f'''
    <section class="skills-categories" id="skills">
        <div class="container">
            <h2 class="section-title">{title}</h2>
            <div class="categories-grid">
                {categories_html}
            </div>
        </div>
    </section>
    
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=Inter:wght@400;500;600&display=swap');
    
    .skills-categories {{
        padding: 120px 0;
        background: {bg};
    }}
    .skills-categories .container {{
        max-width: 1000px;
        margin: 0 auto;
        padding: 0 40px;
    }}
    .section-title {{
        font-family: 'DM Serif Display', serif;
        font-size: 3rem;
        font-weight: 400;
        color: {text};
        margin-bottom: 60px;
    }}
    .categories-grid {{
        display: grid;
        gap: 50px;
    }}
    .skill-category {{
        padding-bottom: 50px;
        border-bottom: 1px solid {text}10;
    }}
    .skill-category:last-child {{
        border-bottom: none;
    }}
    .category-title {{
        font-size: 0.85rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 2px;
        color: {primary};
        margin-bottom: 24px;
    }}
    .skill-tags {{
        display: flex;
        flex-wrap: wrap;
        gap: 12px;
    }}
    .skill-tag {{
        padding: 12px 24px;
        background: {text}05;
        border: 1px solid {text}10;
        border-radius: 50px;
        font-size: 0.95rem;
        color: {text};
        transition: all 0.3s;
    }}
    .skill-tag:hover {{
        background: {primary}10;
        border-color: {primary}30;
        color: {primary};
    }}
    @media (max-width: 640px) {{
        .skills-categories .container {{ padding: 0 24px; }}
    }}
    </style>
    '''


def _get_default_categorized_skills() -> Dict[str, List[str]]:
    return {
        "Frontend Development": ["React", "Vue.js", "Next.js", "TypeScript", "Tailwind CSS", "SASS"],
        "Backend Development": ["Node.js", "Python", "FastAPI", "PostgreSQL", "MongoDB", "GraphQL"],
        "Design & Tools": ["Figma", "Adobe XD", "Photoshop", "Illustrator", "After Effects"],
        "Other": ["Git", "Docker", "AWS", "CI/CD", "Agile", "Leadership"]
    }
