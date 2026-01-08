from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Coin Shop - Virtual currency store"""
    title = props.get("title", "Coin Shop")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    coins = [
        {"amount": "500", "price": "$4.99", "bonus": ""},
        {"amount": "1000", "price": "$9.99", "bonus": "+50"},
        {"amount": "2500", "price": "$19.99", "bonus": "+200"},
        {"amount": "5000", "price": "$39.99", "bonus": "+750"},
        {"amount": "10000", "price": "$74.99", "bonus": "+2000"},
        {"amount": "25000", "price": "$149.99", "bonus": "+7500"},
    ]
    
    cards_html = ""
    for i, c in enumerate(coins):
        popular = "popular" if i == 3 else ""
        bonus_html = f'<span class="bonus">+{c["bonus"]} Bonus</span>' if c["bonus"] else ""
        cards_html += f'''
        <div class="coin-card {popular}">
            {"<div class='popular-badge'>Best Value</div>" if popular else ""}
            <div class="coin-icon">🪙</div>
            <div class="coin-amount">{c['amount']}</div>
            {bonus_html}
            <div class="coin-price">{c['price']}</div>
            <button class="coin-btn">Buy</button>
        </div>
        '''
    
    return f'''
    <section class="gaming-store-coins" id="store">
        <div class="coins-container">
            <div class="coins-header">
                <span class="tag">🪙 Currency</span>
                <h2>{title}</h2>
                <p>Top up your game wallet</p>
            </div>
            <div class="coins-grid">
                {cards_html}
            </div>
        </div>
    </section>
    
    <style>
    .gaming-store-coins {{
        padding: 120px 24px;
        background: {background};
    }}
    .coins-container {{
        max-width: 1100px;
        margin: 0 auto;
    }}
    .coins-header {{
        text-align: center;
        margin-bottom: 60px;
    }}
    .tag {{
        display: inline-block;
        padding: 10px 24px;
        background: {primary}15;
        color: {primary};
        font-weight: 700;
        border-radius: 100px;
        margin-bottom: 20px;
    }}
    .coins-header h2 {{
        font-family: 'Rajdhani', sans-serif;
        font-size: clamp(2.5rem, 5vw, 4rem);
        font-weight: 800;
        color: {text};
        margin-bottom: 12px;
    }}
    .coins-header p {{
        color: {secondary};
        font-size: 1.2rem;
    }}
    .coins-grid {{
        display: grid;
        grid-template-columns: repeat(6, 1fr);
        gap: 16px;
    }}
    .coin-card {{
        background: {text}05;
        border: 1px solid {text}10;
        border-radius: 20px;
        padding: 24px 16px;
        text-align: center;
        transition: all 0.4s ease;
        position: relative;
    }}
    .coin-card:hover {{
        transform: translateY(-8px);
        border-color: {primary}40;
    }}
    .coin-card.popular {{
        background: linear-gradient(135deg, {primary}15, {primary}05);
        border-color: {primary};
        transform: scale(1.05);
    }}
    .coin-card.popular:hover {{
        transform: scale(1.05) translateY(-8px);
    }}
    .popular-badge {{
        position: absolute;
        top: -12px;
        left: 50%;
        transform: translateX(-50%);
        padding: 6px 16px;
        background: {primary};
        color: {background};
        font-size: 0.7rem;
        font-weight: 700;
        border-radius: 100px;
        white-space: nowrap;
    }}
    .coin-icon {{
        font-size: 2.5rem;
        margin-bottom: 12px;
    }}
    .coin-amount {{
        font-family: 'Orbitron', sans-serif;
        font-size: 1.8rem;
        font-weight: 900;
        color: {text};
        margin-bottom: 8px;
    }}
    .bonus {{
        display: inline-block;
        padding: 4px 10px;
        background: {primary}20;
        color: {primary};
        font-size: 0.75rem;
        font-weight: 700;
        border-radius: 100px;
        margin-bottom: 12px;
    }}
    .coin-price {{
        font-size: 1.2rem;
        font-weight: 700;
        color: {secondary};
        margin-bottom: 16px;
    }}
    .coin-btn {{
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
    .coin-btn:hover {{
        transform: scale(1.02);
    }}
    @media (max-width: 1000px) {{
        .coins-grid {{ grid-template-columns: repeat(3, 1fr); }}
    }}
    @media (max-width: 600px) {{
        .coins-grid {{ grid-template-columns: repeat(2, 1fr); }}
    }}
    </style>
    '''
