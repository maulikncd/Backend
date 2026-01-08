from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Flash Sale - Limited time offers with countdown"""
    title = props.get("title", "Flash Sale")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    products = [
        {"name": "Battle Pass", "old": "$29.99", "new": "$14.99", "img": "https://images.unsplash.com/photo-1593305841991-05c297ba4575?w=400", "discount": "50%"},
        {"name": "Coin Pack", "old": "$49.99", "new": "$29.99", "img": "https://images.unsplash.com/photo-1493711662062-fa541f7f069d?w=400", "discount": "40%"},
        {"name": "Skin Bundle", "old": "$24.99", "new": "$12.99", "img": "https://images.unsplash.com/photo-1612287230202-1ff1d85d1bdf?w=400", "discount": "48%"},
        {"name": "Starter Kit", "old": "$19.99", "new": "$9.99", "img": "https://images.unsplash.com/photo-1538481199705-c710c4e965fc?w=400", "discount": "50%"},
    ]
    
    cards_html = ""
    for p in products:
        cards_html += f'''
        <div class="flash-card">
            <div class="discount-badge">-{p['discount']}</div>
            <img src="{p['img']}" alt="{p['name']}">
            <h3>{p['name']}</h3>
            <div class="flash-pricing">
                <span class="old">{p['old']}</span>
                <span class="new">{p['new']}</span>
            </div>
            <button class="flash-btn">Buy Now</button>
        </div>
        '''
    
    return f'''
    <section class="gaming-store-flash" id="store">
        <div class="flash-container">
            <div class="flash-header">
                <div class="flash-title">
                    <span class="flash-icon">⚡</span>
                    <h2>{title}</h2>
                </div>
                <div class="countdown">
                    <span class="label">Ends in:</span>
                    <div class="timer">
                        <div class="time-block"><span class="num">02</span><span class="unit">Hours</span></div>
                        <span class="sep">:</span>
                        <div class="time-block"><span class="num">45</span><span class="unit">Min</span></div>
                        <span class="sep">:</span>
                        <div class="time-block"><span class="num">30</span><span class="unit">Sec</span></div>
                    </div>
                </div>
            </div>
            <div class="flash-grid">
                {cards_html}
            </div>
        </div>
    </section>
    
    <style>
    .gaming-store-flash {{
        padding: 120px 24px;
        background: linear-gradient(135deg, {primary}10, {background});
    }}
    .flash-container {{
        max-width: 1200px;
        margin: 0 auto;
    }}
    .flash-header {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 48px;
        flex-wrap: wrap;
        gap: 24px;
    }}
    .flash-title {{
        display: flex;
        align-items: center;
        gap: 16px;
    }}
    .flash-icon {{
        font-size: 3rem;
    }}
    .flash-title h2 {{
        font-family: 'Rajdhani', sans-serif;
        font-size: 2.5rem;
        font-weight: 800;
        color: {text};
    }}
    .countdown {{
        display: flex;
        align-items: center;
        gap: 16px;
    }}
    .label {{
        color: {secondary};
        font-weight: 600;
    }}
    .timer {{
        display: flex;
        align-items: center;
        gap: 8px;
    }}
    .time-block {{
        background: {primary};
        color: {background};
        padding: 12px 16px;
        border-radius: 10px;
        text-align: center;
    }}
    .num {{
        display: block;
        font-size: 1.8rem;
        font-weight: 900;
    }}
    .unit {{
        font-size: 0.7rem;
        text-transform: uppercase;
    }}
    .sep {{
        color: {primary};
        font-size: 1.5rem;
        font-weight: 700;
    }}
    .flash-grid {{
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 24px;
    }}
    .flash-card {{
        background: {background};
        border-radius: 20px;
        padding: 20px;
        position: relative;
        text-align: center;
        transition: all 0.4s ease;
        border: 1px solid {text}10;
    }}
    .flash-card:hover {{
        transform: translateY(-8px);
        box-shadow: 0 30px 60px {primary}20;
    }}
    .discount-badge {{
        position: absolute;
        top: 16px;
        left: 16px;
        padding: 6px 12px;
        background: #ff3b3b;
        color: white;
        font-weight: 800;
        font-size: 0.9rem;
        border-radius: 8px;
    }}
    .flash-card img {{
        width: 100%;
        aspect-ratio: 1;
        object-fit: cover;
        border-radius: 12px;
        margin-bottom: 16px;
    }}
    .flash-card h3 {{
        font-size: 1.1rem;
        font-weight: 700;
        color: {text};
        margin-bottom: 12px;
    }}
    .flash-pricing {{
        display: flex;
        justify-content: center;
        gap: 12px;
        margin-bottom: 16px;
    }}
    .old {{
        color: {secondary};
        text-decoration: line-through;
    }}
    .new {{
        color: {primary};
        font-weight: 900;
        font-size: 1.3rem;
    }}
    .flash-btn {{
        width: 100%;
        padding: 12px;
        background: {primary};
        color: {background};
        border: none;
        font-weight: 700;
        border-radius: 10px;
        cursor: pointer;
        transition: all 0.3s ease;
    }}
    .flash-btn:hover {{
        transform: scale(1.02);
    }}
    @media (max-width: 1000px) {{
        .flash-grid {{ grid-template-columns: repeat(2, 1fr); }}
    }}
    @media (max-width: 600px) {{
        .flash-grid {{ grid-template-columns: 1fr; }}
    }}
    </style>
    '''
