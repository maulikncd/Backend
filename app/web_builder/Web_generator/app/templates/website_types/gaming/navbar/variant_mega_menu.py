from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Mega Menu - Full dropdown with categories"""
    brand = props.get("brand", "GameZone")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <nav class="gaming-nav-mega" id="navbar">
        <div class="nav-container">
            <a href="#" class="nav-brand">
                <span class="brand-icon">🎮</span>
                {brand}
            </a>
            <div class="nav-menu">
                <div class="nav-item has-mega">
                    <a href="#games">Games <span class="arrow">▾</span></a>
                    <div class="mega-dropdown">
                        <div class="mega-content">
                            <div class="mega-col">
                                <h4>Categories</h4>
                                <a href="#">Battle Royale</a>
                                <a href="#">FPS</a>
                                <a href="#">RPG</a>
                                <a href="#">Racing</a>
                            </div>
                            <div class="mega-col">
                                <h4>Popular</h4>
                                <a href="#">Cyber Warriors</a>
                                <a href="#">Speed Legends</a>
                                <a href="#">Shadow Quest</a>
                            </div>
                            <div class="mega-featured">
                                <img src="https://images.unsplash.com/photo-1542751371-adc38448a05e?w=400" alt="Featured">
                                <div class="featured-info">
                                    <span>New Release</span>
                                    <h5>Cyber Warriors 2</h5>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <a href="#tournaments" class="nav-item">Tournaments</a>
                <a href="#community" class="nav-item">Community</a>
                <a href="#store" class="nav-item">Store</a>
            </div>
            <div class="nav-actions">
                <button class="search-btn">🔍</button>
                <a href="#login">Login</a>
                <a href="#signup" class="btn-cta">Get Started</a>
            </div>
        </div>
    </nav>
    
    <style>
    .gaming-nav-mega {{
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 1000;
        background: {background};
        border-bottom: 1px solid {text}10;
    }}
    .nav-container {{
        max-width: 1400px;
        margin: 0 auto;
        padding: 0 40px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        height: 80px;
    }}
    .nav-brand {{
        display: flex;
        align-items: center;
        gap: 10px;
        font-family: 'Orbitron', sans-serif;
        font-size: 1.5rem;
        font-weight: 900;
        color: {text};
        text-decoration: none;
    }}
    .brand-icon {{
        font-size: 1.8rem;
    }}
    .nav-menu {{
        display: flex;
        align-items: center;
        gap: 8px;
    }}
    .nav-item {{
        position: relative;
    }}
    .nav-item > a, .nav-item {{
        color: {text};
        text-decoration: none;
        font-weight: 600;
        padding: 28px 20px;
        display: inline-block;
        transition: color 0.3s ease;
    }}
    .nav-item:hover > a, .nav-item:hover {{
        color: {primary};
    }}
    .arrow {{
        font-size: 0.8rem;
        margin-left: 4px;
    }}
    .mega-dropdown {{
        position: absolute;
        top: 100%;
        left: 50%;
        transform: translateX(-50%);
        background: {background};
        border: 1px solid {text}10;
        border-radius: 16px;
        padding: 32px;
        min-width: 600px;
        opacity: 0;
        visibility: hidden;
        transition: all 0.3s ease;
        box-shadow: 0 20px 60px {background};
    }}
    .nav-item.has-mega:hover .mega-dropdown {{
        opacity: 1;
        visibility: visible;
    }}
    .mega-content {{
        display: grid;
        grid-template-columns: 1fr 1fr 1.5fr;
        gap: 32px;
    }}
    .mega-col h4 {{
        color: {primary};
        font-weight: 700;
        margin-bottom: 16px;
        font-size: 0.9rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }}
    .mega-col a {{
        display: block;
        color: {secondary};
        text-decoration: none;
        padding: 8px 0;
        transition: color 0.3s ease;
    }}
    .mega-col a:hover {{
        color: {primary};
    }}
    .mega-featured {{
        position: relative;
        border-radius: 12px;
        overflow: hidden;
    }}
    .mega-featured img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
    }}
    .featured-info {{
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        padding: 16px;
        background: linear-gradient(to top, {background}, transparent);
    }}
    .featured-info span {{
        display: inline-block;
        padding: 4px 10px;
        background: {primary};
        color: {background};
        font-size: 0.7rem;
        font-weight: 700;
        border-radius: 100px;
        margin-bottom: 4px;
    }}
    .featured-info h5 {{
        color: {text};
        font-size: 1rem;
    }}
    .nav-actions {{
        display: flex;
        align-items: center;
        gap: 20px;
    }}
    .search-btn {{
        background: none;
        border: none;
        font-size: 1.2rem;
        cursor: pointer;
    }}
    .nav-actions a {{
        color: {text};
        text-decoration: none;
        font-weight: 600;
    }}
    .btn-cta {{
        padding: 12px 24px;
        background: {primary};
        color: {background} !important;
        border-radius: 8px;
        transition: all 0.3s ease;
    }}
    .btn-cta:hover {{
        transform: scale(1.05);
    }}
    @media (max-width: 1100px) {{
        .nav-menu, .search-btn {{ display: none; }}
    }}
    </style>
    '''
