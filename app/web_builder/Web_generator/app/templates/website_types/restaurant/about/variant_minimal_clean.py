from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Minimal Clean - Ultra clean minimal design"""
    title = props.get("sectionTitle", "About")
    story = props.get("story", "Simple ingredients, extraordinary results")
    
    primary = colors.get("primary", "#1A1A1A")
    bg = colors.get("background", "#FFFFFF")
    text = colors.get("text", "#1A1A1A")
    
    return f'''
    <section class="about-minimal" id="about">
        <div class="minimal-grid">
            <div class="minimal-left">
                <h2>{title}</h2>
            </div>
            <div class="minimal-right">
                <p class="lead">{story}</p>
                <p class="body">We believe that great food starts with exceptional ingredients. Our kitchen sources the freshest produce from local farmers, sustainable fisheries, and artisan suppliers.</p>
                <p class="body">Every dish is crafted with care, precision, and a deep respect for culinary traditions while embracing modern techniques.</p>
                <a href="#menu" class="minimal-link">See our menu</a>
            </div>
        </div>
    </section>
    
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant:wght@400;500&family=Karla:wght@400;500&display=swap');
    
    .about-minimal {{
        padding: 150px 80px;
        background: {bg};
    }}
    .minimal-grid {{
        display: grid;
        grid-template-columns: 1fr 1.5fr;
        gap: 100px;
        max-width: 1200px;
        margin: 0 auto;
    }}
    .minimal-left h2 {{
        font-family: 'Cormorant', serif;
        font-size: 5rem;
        font-weight: 400;
        color: {text};
        position: sticky;
        top: 150px;
    }}
    .minimal-right {{
        padding-top: 20px;
    }}
    .minimal-right .lead {{
        font-family: 'Cormorant', serif;
        font-size: 2rem;
        color: {text};
        line-height: 1.5;
        margin-bottom: 40px;
    }}
    .minimal-right .body {{
        font-family: 'Karla', sans-serif;
        font-size: 1.1rem;
        color: {text}90;
        line-height: 1.9;
        margin-bottom: 25px;
    }}
    .minimal-link {{
        display: inline-block;
        margin-top: 30px;
        color: {text};
        text-decoration: none;
        font-family: 'Karla', sans-serif;
        font-size: 1rem;
        padding-bottom: 5px;
        border-bottom: 2px solid {text};
        transition: all 0.3s;
    }}
    .minimal-link:hover {{
        border-color: {primary};
        color: {primary};
    }}
    @media (max-width: 968px) {{
        .about-minimal {{ padding: 100px 40px; }}
        .minimal-grid {{ grid-template-columns: 1fr; gap: 40px; }}
        .minimal-left h2 {{ font-size: 3rem; position: static; }}
    }}
    </style>
    '''
