from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Team Cards - Focus on chef and team members"""
    title = props.get("sectionTitle", "Meet Our Team")
    story = props.get("story", "The passionate people behind your dining experience")
    
    primary = colors.get("primary", "#2D3436")
    bg = colors.get("background", "#F8F9FA")
    text = colors.get("text", "#1A1A1A")
    
    return f'''
    <section class="about-team" id="about">
        <div class="team-container">
            <div class="team-header">
                <span class="eyebrow">Our Team</span>
                <h2 class="title">{title}</h2>
                <p class="subtitle">{story}</p>
            </div>
            
            <div class="team-grid">
                <div class="team-card featured">
                    <div class="card-image">
                        <img src="https://images.unsplash.com/photo-1577219491135-ce391730fb2c?w=600" alt="Head Chef">
                    </div>
                    <div class="card-content">
                        <span class="role">Executive Chef</span>
                        <h3 class="name">Marco Rosetti</h3>
                        <p class="bio">With over 20 years of experience in Michelin-starred kitchens across Europe, Chef Marco brings his passion for perfection to every dish.</p>
                        <div class="social">
                            <a href="#">Instagram</a>
                        </div>
                    </div>
                </div>
                
                <div class="team-card">
                    <div class="card-image">
                        <img src="https://images.unsplash.com/photo-1583394293214-28ez64e7de74?w=400" alt="Sous Chef">
                    </div>
                    <div class="card-content">
                        <span class="role">Sous Chef</span>
                        <h3 class="name">Sofia Chen</h3>
                        <p class="bio">Specializing in fusion cuisine, Sofia adds innovative twists to classic dishes.</p>
                    </div>
                </div>
                
                <div class="team-card">
                    <div class="card-image">
                        <img src="https://images.unsplash.com/photo-1566554273541-37a9ca77b91f?w=400" alt="Pastry Chef">
                    </div>
                    <div class="card-content">
                        <span class="role">Pastry Chef</span>
                        <h3 class="name">Elena Dubois</h3>
                        <p class="bio">Creating sweet masterpieces that are almost too beautiful to eat.</p>
                    </div>
                </div>
                
                <div class="team-card">
                    <div class="card-image">
                        <img src="https://images.unsplash.com/photo-1560250097-0b93528c311a?w=400" alt="Sommelier">
                    </div>
                    <div class="card-content">
                        <span class="role">Head Sommelier</span>
                        <h3 class="name">James Miller</h3>
                        <p class="bio">Curating the perfect wine pairing for every course.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600&family=Lato:wght@400;500&display=swap');
    
    .about-team {{
        padding: 120px 60px;
        background: {bg};
    }}
    .team-container {{
        max-width: 1300px;
        margin: 0 auto;
    }}
    .team-header {{
        text-align: center;
        margin-bottom: 70px;
    }}
    .team-header .eyebrow {{
        color: {primary};
        font-size: 0.85rem;
        letter-spacing: 3px;
        text-transform: uppercase;
        margin-bottom: 15px;
        display: block;
    }}
    .team-header .title {{
        font-family: 'Cormorant Garamond', serif;
        font-size: clamp(2.5rem, 5vw, 3.5rem);
        color: {text};
        margin-bottom: 15px;
    }}
    .team-header .subtitle {{
        font-size: 1.1rem;
        color: {text}80;
        max-width: 600px;
        margin: 0 auto;
    }}
    .team-grid {{
        display: grid;
        grid-template-columns: 1.5fr 1fr 1fr 1fr;
        gap: 30px;
    }}
    .team-card {{
        background: white;
        border-radius: 20px;
        overflow: hidden;
        transition: all 0.3s;
        box-shadow: 0 10px 40px rgba(0,0,0,0.05);
    }}
    .team-card:hover {{
        transform: translateY(-10px);
        box-shadow: 0 20px 50px rgba(0,0,0,0.1);
    }}
    .team-card.featured {{
        grid-row: span 2;
    }}
    .team-card.featured .card-image {{
        height: 350px;
    }}
    .card-image {{
        height: 200px;
        overflow: hidden;
    }}
    .card-image img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.4s;
    }}
    .team-card:hover .card-image img {{
        transform: scale(1.05);
    }}
    .card-content {{
        padding: 25px;
    }}
    .card-content .role {{
        color: {primary};
        font-size: 0.8rem;
        letter-spacing: 2px;
        text-transform: uppercase;
    }}
    .card-content .name {{
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.5rem;
        color: {text};
        margin: 8px 0 12px;
    }}
    .card-content .bio {{
        font-size: 0.95rem;
        color: {text}80;
        line-height: 1.6;
    }}
    .social {{
        margin-top: 15px;
    }}
    .social a {{
        color: {primary};
        text-decoration: none;
        font-size: 0.85rem;
        font-weight: 500;
    }}
    @media (max-width: 1100px) {{
        .team-grid {{ grid-template-columns: 1fr 1fr; }}
        .team-card.featured {{ grid-row: auto; }}
    }}
    @media (max-width: 768px) {{
        .about-team {{ padding: 80px 30px; }}
        .team-grid {{ grid-template-columns: 1fr; }}
    }}
    </style>
    '''
