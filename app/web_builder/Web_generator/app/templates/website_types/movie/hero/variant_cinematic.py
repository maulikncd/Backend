from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """
    Movie Theater Hero - Cinematic hero with dark theme and movie posters
    """
    title = props.get("title", props.get("businessName", "Cinema Paradise"))
    tagline = props.get("tagline", "Experience Movies Like Never Before")
    
    primary = colors.get("primary", "#E50914")
    secondary = colors.get("secondary", "#FFD700")
    bg = colors.get("background", "#0A0A0A")
    text = colors.get("text", "#FFFFFF")
    
    return f'''
    <section class="movie-hero" id="home">
        <div class="hero-background">
            <div class="poster-grid">
                <img src="https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?w=400" alt="Movie 1">
                <img src="https://images.unsplash.com/photo-1536440136628-849c177e76a1?w=400" alt="Movie 2">
                <img src="https://images.unsplash.com/photo-1440404653325-ab127d49abc1?w=400" alt="Movie 3">
            </div>
            <div class="hero-overlay"></div>
        </div>
        
        <div class="hero-content">
            <div class="container">
                <h1 class="hero-title">{title}</h1>
                <p class="hero-tagline">{tagline}</p>
                <div class="hero-cta">
                    <a href="#showtimes" class="btn-primary">View Showtimes</a>
                    <a href="#movies" class="btn-secondary">Now Showing</a>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    .movie-hero {{
        min-height: 100vh;
        position: relative;
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
    }}
    .hero-background {{
        position: absolute;
        inset: 0;
    }}
    .poster-grid {{
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        height: 100%;
        opacity: 0.3;
    }}
    .poster-grid img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
    }}
    .hero-overlay {{
        position: absolute;
        inset: 0;
        background: linear-gradient(to top, {bg}, transparent 40%, {bg}80);
    }}
    .hero-content {{
        position: relative;
        z-index: 10;
        text-align: center;
        padding: 40px;
    }}
    .hero-title {{
        font-size: clamp(3rem, 8vw, 6rem);
        font-weight: 800;
        color: {text};
        text-transform: uppercase;
        letter-spacing: 8px;
        margin-bottom: 20px;
    }}
    .hero-tagline {{
        font-size: 1.5rem;
        color: {text}80;
        margin-bottom: 40px;
    }}
    .hero-cta {{
        display: flex;
        gap: 20px;
        justify-content: center;
        flex-wrap: wrap;
    }}
    .btn-primary {{
        padding: 18px 48px;
        background: {primary};
        color: white;
        text-decoration: none;
        font-weight: 700;
        border-radius: 8px;
        text-transform: uppercase;
        letter-spacing: 2px;
        transition: all 0.3s;
    }}
    .btn-primary:hover {{
        transform: scale(1.05);
        box-shadow: 0 10px 30px {primary}50;
    }}
    .btn-secondary {{
        padding: 18px 48px;
        background: transparent;
        color: {text};
        text-decoration: none;
        font-weight: 600;
        border: 2px solid {text}30;
        border-radius: 8px;
        text-transform: uppercase;
        letter-spacing: 2px;
        transition: all 0.3s;
    }}
    .btn-secondary:hover {{
        border-color: {secondary};
        color: {secondary};
    }}
    </style>
    '''
