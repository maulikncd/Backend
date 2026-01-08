from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Comparison Table - Feature comparison with competitors"""
    title = props.get("title", "The Complete Package")
    subtitle = props.get("subtitle", "See how we compare")
    
    # Dynamic colors from user's palette
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="gaming-features-compare" id="features">
        <div class="compare-container">
            <div class="compare-header">
                <span class="header-tag">⚔️ Comparison</span>
                <h2>{title}</h2>
                <p>{subtitle}</p>
            </div>
            
            <div class="compare-table">
                <div class="table-header">
                    <div class="header-cell feature-col">Features</div>
                    <div class="header-cell us-col highlight">
                        <span class="recommended">Recommended</span>
                        <span class="brand">Our Platform</span>
                    </div>
                    <div class="header-cell other-col">Others</div>
                </div>
                
                <div class="table-row">
                    <div class="row-cell feature-col">
                        <span class="feature-name">Server Latency</span>
                    </div>
                    <div class="row-cell us-col highlight">
                        <span class="value best">10ms</span>
                    </div>
                    <div class="row-cell other-col">
                        <span class="value">50ms+</span>
                    </div>
                </div>
                
                <div class="table-row">
                    <div class="row-cell feature-col">
                        <span class="feature-name">Tick Rate</span>
                    </div>
                    <div class="row-cell us-col highlight">
                        <span class="value best">128 tick</span>
                    </div>
                    <div class="row-cell other-col">
                        <span class="value">64 tick</span>
                    </div>
                </div>
                
                <div class="table-row">
                    <div class="row-cell feature-col">
                        <span class="feature-name">Anti-Cheat System</span>
                    </div>
                    <div class="row-cell us-col highlight">
                        <span class="value best">AI-Powered</span>
                    </div>
                    <div class="row-cell other-col">
                        <span class="value">Basic</span>
                    </div>
                </div>
                
                <div class="table-row">
                    <div class="row-cell feature-col">
                        <span class="feature-name">Tournament Prizes</span>
                    </div>
                    <div class="row-cell us-col highlight">
                        <span class="value best">$10M+</span>
                    </div>
                    <div class="row-cell other-col">
                        <span class="value">$100K</span>
                    </div>
                </div>
                
                <div class="table-row">
                    <div class="row-cell feature-col">
                        <span class="feature-name">Global Servers</span>
                    </div>
                    <div class="row-cell us-col highlight">
                        <span class="value best">200+</span>
                    </div>
                    <div class="row-cell other-col">
                        <span class="value">50</span>
                    </div>
                </div>
                
                <div class="table-row">
                    <div class="row-cell feature-col">
                        <span class="feature-name">Pro Analytics</span>
                    </div>
                    <div class="row-cell us-col highlight">
                        <span class="check">✓</span>
                    </div>
                    <div class="row-cell other-col">
                        <span class="cross">✗</span>
                    </div>
                </div>
                
                <div class="table-row">
                    <div class="row-cell feature-col">
                        <span class="feature-name">24/7 Support</span>
                    </div>
                    <div class="row-cell us-col highlight">
                        <span class="check">✓</span>
                    </div>
                    <div class="row-cell other-col">
                        <span class="cross">✗</span>
                    </div>
                </div>
                
                <div class="table-footer">
                    <div class="footer-cell feature-col"></div>
                    <div class="footer-cell us-col highlight">
                        <a href="#start" class="btn-compare">Get Started Free</a>
                    </div>
                    <div class="footer-cell other-col"></div>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    .gaming-features-compare {{
        padding: 140px 24px;
        background: {background};
    }}
    .compare-container {{
        max-width: 1000px;
        margin: 0 auto;
    }}
    .compare-header {{
        text-align: center;
        margin-bottom: 60px;
    }}
    .header-tag {{
        display: inline-block;
        padding: 10px 24px;
        background: {primary}15;
        color: {primary};
        font-weight: 700;
        font-size: 0.85rem;
        letter-spacing: 2px;
        border-radius: 100px;
        margin-bottom: 24px;
    }}
    .compare-header h2 {{
        font-family: 'Rajdhani', sans-serif;
        font-size: clamp(2.5rem, 5vw, 4rem);
        font-weight: 800;
        color: {text};
        margin-bottom: 16px;
    }}
    .compare-header p {{
        font-size: 1.2rem;
        color: {secondary};
    }}
    .compare-table {{
        background: {text}03;
        border: 1px solid {text}08;
        border-radius: 24px;
        overflow: hidden;
    }}
    .table-header, .table-row, .table-footer {{
        display: grid;
        grid-template-columns: 1.5fr 1fr 1fr;
    }}
    .table-header {{
        background: {text}05;
        border-bottom: 1px solid {text}08;
    }}
    .header-cell {{
        padding: 24px 32px;
        font-weight: 700;
        color: {secondary};
        text-transform: uppercase;
        font-size: 0.85rem;
        letter-spacing: 1px;
    }}
    .header-cell.highlight {{
        background: linear-gradient(135deg, {primary}15, {primary}05);
        color: {text};
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 8px;
    }}
    .recommended {{
        display: inline-block;
        padding: 4px 12px;
        background: {primary};
        color: {background};
        font-size: 0.7rem;
        font-weight: 800;
        border-radius: 100px;
        letter-spacing: 1px;
    }}
    .brand {{
        font-size: 1rem;
        font-weight: 800;
        color: {primary};
    }}
    .table-row {{
        border-bottom: 1px solid {text}06;
    }}
    .row-cell {{
        padding: 20px 32px;
        display: flex;
        align-items: center;
    }}
    .row-cell.highlight {{
        background: {primary}05;
        justify-content: center;
    }}
    .other-col {{
        justify-content: center;
    }}
    .feature-name {{
        color: {text};
        font-weight: 600;
    }}
    .value {{
        color: {secondary};
    }}
    .value.best {{
        color: {primary};
        font-weight: 800;
        font-size: 1.1rem;
    }}
    .check {{
        width: 32px;
        height: 32px;
        background: {primary}20;
        color: {primary};
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 700;
    }}
    .cross {{
        width: 32px;
        height: 32px;
        background: {secondary}20;
        color: {secondary};
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 700;
    }}
    .table-footer {{
        padding: 8px 0;
    }}
    .footer-cell {{
        padding: 20px 32px;
        display: flex;
        justify-content: center;
    }}
    .footer-cell.highlight {{
        background: {primary}05;
    }}
    .btn-compare {{
        display: inline-block;
        padding: 16px 40px;
        background: {primary};
        color: {background};
        font-weight: 700;
        text-decoration: none;
        border-radius: 12px;
        transition: all 0.3s ease;
    }}
    .btn-compare:hover {{
        transform: scale(1.05);
        box-shadow: 0 20px 40px {primary}40;
    }}
    @media (max-width: 768px) {{
        .table-header, .table-row, .table-footer {{
            grid-template-columns: 1.2fr 1fr 0.8fr;
        }}
        .header-cell, .row-cell, .footer-cell {{
            padding: 16px;
        }}
        .recommended {{ display: none; }}
    }}
    </style>
    '''
