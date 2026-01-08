from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Pricing Tiers - Plan comparison layout"""
    title = props.get("title", "Choose Your Plan")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="gaming-store-pricing" id="store">
        <div class="pricing-container">
            <div class="pricing-header">
                <span class="tag">💎 Premium</span>
                <h2>{title}</h2>
                <p>Upgrade your gaming experience</p>
            </div>
            <div class="pricing-grid">
                <div class="pricing-card">
                    <h3>Basic</h3>
                    <div class="price">
                        <span class="amount">Free</span>
                    </div>
                    <ul class="features">
                        <li>✓ Access to free games</li>
                        <li>✓ Basic matchmaking</li>
                        <li>✓ Community forums</li>
                        <li class="disabled">✗ Premium skins</li>
                        <li class="disabled">✗ Priority servers</li>
                    </ul>
                    <a href="#" class="btn-tier">Get Started</a>
                </div>
                <div class="pricing-card featured">
                    <div class="recommended">Most Popular</div>
                    <h3>Pro</h3>
                    <div class="price">
                        <span class="amount">$9.99</span>
                        <span class="period">/month</span>
                    </div>
                    <ul class="features">
                        <li>✓ All free features</li>
                        <li>✓ Priority matchmaking</li>
                        <li>✓ Exclusive skins</li>
                        <li>✓ Premium servers</li>
                        <li>✓ Monthly rewards</li>
                    </ul>
                    <a href="#" class="btn-tier primary">Subscribe Now</a>
                </div>
                <div class="pricing-card">
                    <h3>Ultimate</h3>
                    <div class="price">
                        <span class="amount">$24.99</span>
                        <span class="period">/month</span>
                    </div>
                    <ul class="features">
                        <li>✓ All Pro features</li>
                        <li>✓ Early access content</li>
                        <li>✓ Exclusive tournaments</li>
                        <li>✓ Personal coach session</li>
                        <li>✓ VIP support</li>
                    </ul>
                    <a href="#" class="btn-tier">Go Ultimate</a>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    .gaming-store-pricing {{
        padding: 120px 24px;
        background: {background};
    }}
    .pricing-container {{
        max-width: 1100px;
        margin: 0 auto;
    }}
    .pricing-header {{
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
    .pricing-header h2 {{
        font-family: 'Rajdhani', sans-serif;
        font-size: clamp(2.5rem, 5vw, 4rem);
        font-weight: 800;
        color: {text};
        margin-bottom: 12px;
    }}
    .pricing-header p {{
        color: {secondary};
        font-size: 1.2rem;
    }}
    .pricing-grid {{
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 32px;
        align-items: start;
    }}
    .pricing-card {{
        background: {text}05;
        border: 1px solid {text}10;
        border-radius: 24px;
        padding: 40px;
        text-align: center;
        position: relative;
        transition: all 0.4s ease;
    }}
    .pricing-card:hover {{
        transform: translateY(-8px);
    }}
    .pricing-card.featured {{
        background: linear-gradient(135deg, {primary}15, {primary}05);
        border-color: {primary}40;
        transform: scale(1.05);
    }}
    .pricing-card.featured:hover {{
        transform: scale(1.05) translateY(-8px);
    }}
    .recommended {{
        position: absolute;
        top: -14px;
        left: 50%;
        transform: translateX(-50%);
        padding: 8px 24px;
        background: {primary};
        color: {background};
        font-weight: 700;
        font-size: 0.85rem;
        border-radius: 100px;
    }}
    .pricing-card h3 {{
        font-size: 1.5rem;
        font-weight: 700;
        color: {text};
        margin-bottom: 24px;
    }}
    .price {{
        margin-bottom: 32px;
    }}
    .amount {{
        font-size: 3rem;
        font-weight: 900;
        color: {text};
    }}
    .period {{
        color: {secondary};
    }}
    .features {{
        list-style: none;
        padding: 0;
        margin: 0 0 32px;
        text-align: left;
    }}
    .features li {{
        padding: 12px 0;
        border-bottom: 1px solid {text}08;
        color: {text};
    }}
    .features li.disabled {{
        color: {secondary};
        opacity: 0.5;
    }}
    .btn-tier {{
        display: block;
        padding: 16px;
        background: {text}10;
        color: {text};
        text-decoration: none;
        font-weight: 700;
        border-radius: 12px;
        transition: all 0.3s ease;
    }}
    .btn-tier:hover {{
        background: {primary}20;
    }}
    .btn-tier.primary {{
        background: {primary};
        color: {background};
    }}
    .btn-tier.primary:hover {{
        transform: scale(1.02);
        box-shadow: 0 10px 30px {primary}40;
    }}
    @media (max-width: 900px) {{
        .pricing-grid {{ grid-template-columns: 1fr; max-width: 400px; margin: 0 auto; }}
        .pricing-card.featured {{ transform: none; }}
    }}
    </style>
    '''
