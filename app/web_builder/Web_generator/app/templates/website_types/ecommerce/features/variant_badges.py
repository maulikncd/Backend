from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """
    Shop Features - Trust badges and shipping info section
    """
    primary = colors.get("primary", "#000000")
    bg = colors.get("background", "#FFFFFF")
    text = colors.get("text", "#111111")
    
    return f'''
    <section class="features-section" id="features">
        <div class="container">
            <div class="features-grid">
                <div class="feature-card">
                    <div class="feature-icon">🚚</div>
                    <h3 class="feature-title">Free Shipping</h3>
                    <p class="feature-desc">Free shipping on all orders over $50</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">↩️</div>
                    <h3 class="feature-title">Easy Returns</h3>
                    <p class="feature-desc">30-day hassle-free return policy</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">🔒</div>
                    <h3 class="feature-title">Secure Checkout</h3>
                    <p class="feature-desc">100% secure payment processing</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">💬</div>
                    <h3 class="feature-title">24/7 Support</h3>
                    <p class="feature-desc">Round-the-clock customer service</p>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    .features-section {{
        padding: 80px 0;
        background: {bg};
        border-top: 1px solid {text}08;
        border-bottom: 1px solid {text}08;
    }}
    .features-section .container {{
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 40px;
    }}
    .features-grid {{
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 40px;
    }}
    .feature-card {{
        text-align: center;
        padding: 30px 20px;
    }}
    .feature-icon {{
        font-size: 3rem;
        margin-bottom: 20px;
    }}
    .feature-title {{
        font-size: 1.1rem;
        font-weight: 700;
        color: {text};
        margin-bottom: 10px;
    }}
    .feature-desc {{
        font-size: 0.95rem;
        color: {text}60;
        line-height: 1.6;
    }}
    @media (max-width: 900px) {{
        .features-grid {{ grid-template-columns: repeat(2, 1fr); }}
    }}
    @media (max-width: 500px) {{
        .features-grid {{ grid-template-columns: 1fr; }}
    }}
    </style>
    '''
