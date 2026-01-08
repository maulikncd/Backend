from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Cards Grid - Feature cards layout"""
    title = props.get("sectionTitle", "Why Choose Us")
    story = props.get("story", "Experience dining excellence")
    
    primary = colors.get("primary", "#2D3436")
    bg = colors.get("background", "#F5F5F5")
    text = colors.get("text", "#1A1A1A")
    
    return f'''
    <section class="about-cards" id="about">
        <div class="cards-container">
            <div class="cards-header">
                <span class="label">About Us</span>
                <h2>{title}</h2>
                <p>{story}</p>
            </div>
            
            <div class="cards-grid">
                <div class="feature-card">
                    <div class="card-icon">🌿</div>
                    <h3>Fresh Ingredients</h3>
                    <p>We source the finest local and seasonal ingredients from trusted farmers and suppliers.</p>
                </div>
                <div class="feature-card">
                    <div class="card-icon">👨‍🍳</div>
                    <h3>Expert Chefs</h3>
                    <p>Our team of award-winning chefs brings decades of culinary experience to every dish.</p>
                </div>
                <div class="feature-card">
                    <div class="card-icon">🍷</div>
                    <h3>Fine Wine Selection</h3>
                    <p>Curated wine list featuring exceptional vintages from around the world.</p>
                </div>
                <div class="feature-card">
                    <div class="card-icon">✨</div>
                    <h3>Elegant Atmosphere</h3>
                    <p>Sophisticated ambiance perfect for romantic dinners and special celebrations.</p>
                </div>
                <div class="feature-card">
                    <div class="card-icon">🎯</div>
                    <h3>Personalized Service</h3>
                    <p>Attentive staff dedicated to making every visit memorable.</p>
                </div>
                <div class="feature-card">
                    <div class="card-icon">🏆</div>
                    <h3>Award Winning</h3>
                    <p>Recognized by Michelin and top culinary publications worldwide.</p>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500&family=Inter:wght@400;500&display=swap');
    
    .about-cards {{
        padding: 120px 60px;
        background: {bg};
    }}
    .cards-container {{
        max-width: 1200px;
        margin: 0 auto;
    }}
    .cards-header {{
        text-align: center;
        margin-bottom: 70px;
    }}
    .cards-header .label {{
        color: {primary};
        font-size: 0.85rem;
        letter-spacing: 3px;
        text-transform: uppercase;
        display: block;
        margin-bottom: 15px;
    }}
    .cards-header h2 {{
        font-family: 'Playfair Display', serif;
        font-size: clamp(2.5rem, 5vw, 3.5rem);
        color: {text};
        margin-bottom: 15px;
    }}
    .cards-header p {{
        color: {text}80;
        font-size: 1.1rem;
        max-width: 600px;
        margin: 0 auto;
    }}
    .cards-grid {{
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 30px;
    }}
    .feature-card {{
        background: white;
        padding: 40px;
        border-radius: 20px;
        text-align: center;
        transition: all 0.3s;
        box-shadow: 0 10px 40px rgba(0,0,0,0.05);
    }}
    .feature-card:hover {{
        transform: translateY(-10px);
        box-shadow: 0 20px 50px rgba(0,0,0,0.1);
    }}
    .card-icon {{
        font-size: 3rem;
        margin-bottom: 25px;
    }}
    .feature-card h3 {{
        font-family: 'Playfair Display', serif;
        font-size: 1.4rem;
        color: {text};
        margin-bottom: 15px;
    }}
    .feature-card p {{
        font-family: 'Inter', sans-serif;
        font-size: 0.95rem;
        color: {text}80;
        line-height: 1.7;
    }}
    @media (max-width: 968px) {{
        .cards-grid {{ grid-template-columns: repeat(2, 1fr); }}
    }}
    @media (max-width: 600px) {{
        .about-cards {{ padding: 80px 30px; }}
        .cards-grid {{ grid-template-columns: 1fr; }}
    }}
    </style>
    '''
