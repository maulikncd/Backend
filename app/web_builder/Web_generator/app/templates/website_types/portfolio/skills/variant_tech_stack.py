from typing import Dict, Any, List

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """
    Tech Stack Grid - Modern grid display of skills with icons,
    proficiency bars, and category grouping
    """
    title = props.get("sectionTitle", props.get("title", "Skills & Expertise"))
    subtitle = props.get("subtitle", "Technologies I work with")
    skills = props.get("skills", _get_default_skills())
    
    primary = colors.get("primary", "#6366F1")
    bg = colors.get("background", "#0F172A")
    text = colors.get("text", "#F8FAFC")
    
    skills_html = ""
    for skill in skills:
        proficiency = skill.get("level", 90)
        skills_html += f'''
        <div class="skill-card">
            <div class="skill-icon">{skill.get('icon', '💻')}</div>
            <h3 class="skill-name">{skill.get('name', 'Skill')}</h3>
            <div class="skill-bar">
                <div class="skill-progress" style="width: {proficiency}%"></div>
            </div>
            <span class="skill-percent">{proficiency}%</span>
        </div>
        '''
    
    return f'''
    <section class="skills-section" id="skills">
        <div class="container">
            <div class="section-header">
                <span class="section-label">Expertise</span>
                <h2 class="section-title">{title}</h2>
                <p class="section-subtitle">{subtitle}</p>
            </div>
            
            <div class="skills-grid">
                {skills_html}
            </div>
            
            <div class="experience-stats">
                <div class="exp-stat">
                    <span class="exp-number">8+</span>
                    <span class="exp-label">Years Experience</span>
                </div>
                <div class="exp-stat">
                    <span class="exp-number">100+</span>
                    <span class="exp-label">Projects Completed</span>
                </div>
                <div class="exp-stat">
                    <span class="exp-number">50+</span>
                    <span class="exp-label">Happy Clients</span>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    .skills-section {{
        padding: 120px 0;
        background: {bg};
    }}
    .skills-section .container {{
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
        background: {primary}20;
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
        color: {text}60;
    }}
    .skills-grid {{
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 24px;
        margin-bottom: 80px;
    }}
    .skill-card {{
        background: rgba(255,255,255,0.03);
        border: 1px solid rgba(255,255,255,0.05);
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        transition: all 0.3s;
    }}
    .skill-card:hover {{
        background: rgba(255,255,255,0.06);
        transform: translateY(-5px);
        border-color: {primary}50;
    }}
    .skill-icon {{
        font-size: 3rem;
        margin-bottom: 16px;
    }}
    .skill-name {{
        font-size: 1.1rem;
        font-weight: 600;
        color: {text};
        margin-bottom: 16px;
    }}
    .skill-bar {{
        height: 6px;
        background: rgba(255,255,255,0.1);
        border-radius: 3px;
        overflow: hidden;
        margin-bottom: 10px;
    }}
    .skill-progress {{
        height: 100%;
        background: linear-gradient(90deg, {primary}, {colors.get('secondary', '#EC4899')});
        border-radius: 3px;
        transition: width 1s ease-out;
    }}
    .skill-percent {{
        font-size: 0.85rem;
        color: {text}50;
    }}
    .experience-stats {{
        display: flex;
        justify-content: center;
        gap: 80px;
        padding: 60px;
        background: rgba(255,255,255,0.02);
        border-radius: 24px;
        border: 1px solid rgba(255,255,255,0.05);
    }}
    .exp-stat {{
        text-align: center;
    }}
    .exp-number {{
        display: block;
        font-size: 3.5rem;
        font-weight: 700;
        color: {primary};
        line-height: 1;
        margin-bottom: 10px;
    }}
    .exp-label {{
        font-size: 0.95rem;
        color: {text}60;
    }}
    @media (max-width: 1024px) {{
        .skills-grid {{ grid-template-columns: repeat(3, 1fr); }}
    }}
    @media (max-width: 768px) {{
        .skills-grid {{ grid-template-columns: repeat(2, 1fr); }}
        .experience-stats {{ flex-direction: column; gap: 40px; padding: 40px; }}
    }}
    @media (max-width: 480px) {{
        .skills-section .container {{ padding: 0 20px; }}
    }}
    </style>
    '''


def _get_default_skills() -> List[Dict]:
    return [
        {"name": "React", "icon": "⚛️", "level": 95},
        {"name": "TypeScript", "icon": "📘", "level": 90},
        {"name": "Node.js", "icon": "🟢", "level": 88},
        {"name": "Python", "icon": "🐍", "level": 85},
        {"name": "Figma", "icon": "🎨", "level": 92},
        {"name": "Next.js", "icon": "▲", "level": 90},
        {"name": "PostgreSQL", "icon": "🐘", "level": 82},
        {"name": "AWS", "icon": "☁️", "level": 78},
    ]
