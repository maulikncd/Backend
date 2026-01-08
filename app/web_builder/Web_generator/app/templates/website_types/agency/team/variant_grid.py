from typing import Dict, Any, List

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """
    Team Grid - Professional team section with photos and roles
    """
    title = props.get("sectionTitle", props.get("title", "Meet Our Team"))
    subtitle = props.get("subtitle", "The talented people behind our success")
    team = props.get("team", _get_default_team())
    
    primary = colors.get("primary", "#2563EB")
    bg = colors.get("background", "#FFFFFF")
    text = colors.get("text", "#0F172A")
    
    team_html = ""
    for member in team[:6]:
        team_html += f'''
        <div class="team-card">
            <div class="member-image">
                <img src="{member.get('image', 'https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=400')}" alt="{member.get('name', 'Team Member')}">
                <div class="member-social">
                    <a href="#" aria-label="LinkedIn">in</a>
                    <a href="#" aria-label="Twitter">𝕏</a>
                </div>
            </div>
            <div class="member-info">
                <h3 class="member-name">{member.get('name', 'John Doe')}</h3>
                <p class="member-role">{member.get('role', 'Team Member')}</p>
            </div>
        </div>
        '''
    
    return f'''
    <section class="team-section" id="team">
        <div class="container">
            <div class="section-header">
                <span class="section-label">Our Team</span>
                <h2 class="section-title">{title}</h2>
                <p class="section-subtitle">{subtitle}</p>
            </div>
            
            <div class="team-grid">
                {team_html}
            </div>
        </div>
    </section>
    
    <style>
    .team-section {{
        padding: 120px 0;
        background: {bg};
    }}
    .team-section .container {{
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 40px;
    }}
    .section-header {{
        text-align: center;
        margin-bottom: 60px;
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
        font-size: clamp(2.5rem, 5vw, 3rem);
        font-weight: 700;
        color: {text};
        margin-bottom: 16px;
    }}
    .section-subtitle {{
        font-size: 1.1rem;
        color: {text}70;
    }}
    .team-grid {{
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 40px;
    }}
    .team-card {{
        text-align: center;
    }}
    .member-image {{
        position: relative;
        margin-bottom: 24px;
        border-radius: 20px;
        overflow: hidden;
    }}
    .member-image img {{
        width: 100%;
        height: 350px;
        object-fit: cover;
        transition: transform 0.5s;
    }}
    .team-card:hover .member-image img {{
        transform: scale(1.05);
    }}
    .member-social {{
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        padding: 20px;
        background: linear-gradient(to top, rgba(0,0,0,0.8), transparent);
        display: flex;
        justify-content: center;
        gap: 12px;
        transform: translateY(100%);
        transition: transform 0.3s;
    }}
    .team-card:hover .member-social {{
        transform: translateY(0);
    }}
    .member-social a {{
        width: 40px;
        height: 40px;
        display: flex;
        align-items: center;
        justify-content: center;
        background: white;
        border-radius: 50%;
        color: {text};
        text-decoration: none;
        font-weight: 600;
        transition: all 0.3s;
    }}
    .member-social a:hover {{
        background: {primary};
        color: white;
    }}
    .member-name {{
        font-size: 1.3rem;
        font-weight: 700;
        color: {text};
        margin-bottom: 6px;
    }}
    .member-role {{
        font-size: 0.95rem;
        color: {primary};
    }}
    @media (max-width: 900px) {{
        .team-grid {{ grid-template-columns: repeat(2, 1fr); }}
    }}
    @media (max-width: 600px) {{
        .team-grid {{ grid-template-columns: 1fr; }}
    }}
    </style>
    '''


def _get_default_team() -> List[Dict]:
    return [
        {"name": "Sarah Johnson", "role": "CEO & Founder", "image": "https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=400"},
        {"name": "Michael Chen", "role": "Creative Director", "image": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400"},
        {"name": "Emily Davis", "role": "Lead Designer", "image": "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=400"},
        {"name": "David Kim", "role": "Tech Lead", "image": "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=400"},
        {"name": "Lisa Wang", "role": "Project Manager", "image": "https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=400"},
        {"name": "James Wilson", "role": "Marketing Head", "image": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=400"},
    ]
