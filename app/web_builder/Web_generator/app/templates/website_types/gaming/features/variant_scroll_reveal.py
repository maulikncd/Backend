from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Scroll Reveal - Features that reveal on scroll with staggered animations"""
    title = props.get("title", "Why Gamers Choose Us")
    subtitle = props.get("subtitle", "Features that make the difference")
    
    # Dynamic colors from user's palette
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="gaming-features-scroll" id="features">
        <div class="scroll-container">
            <div class="scroll-header">
                <div class="badge-row">
                    <span class="badge">✨ Premium Features</span>
                </div>
                <h2>{title}</h2>
                <p>{subtitle}</p>
            </div>
            
            <div class="scroll-features">
                <div class="feature-row">
                    <div class="feature-visual">
                        <div class="visual-wrapper">
                            <div class="icon-display">⚡</div>
                            <div class="visual-ring"></div>
                        </div>
                    </div>
                    <div class="feature-text">
                        <span class="feature-num">01</span>
                        <h3>Blazing Fast Performance</h3>
                        <p>Our globally distributed infrastructure ensures sub-10ms latency for players worldwide. Experience gaming without lag, stutter, or delays.</p>
                        <ul class="feature-list">
                            <li>128-tick server rate</li>
                            <li>200+ edge locations</li>
                            <li>99.99% uptime guarantee</li>
                        </ul>
                    </div>
                </div>
                
                <div class="feature-row reverse">
                    <div class="feature-visual">
                        <div class="visual-wrapper">
                            <div class="icon-display">🛡️</div>
                            <div class="visual-ring"></div>
                        </div>
                    </div>
                    <div class="feature-text">
                        <span class="feature-num">02</span>
                        <h3>Military-Grade Security</h3>
                        <p>Play with confidence knowing our AI-powered anti-cheat system and enterprise-level encryption protect every match.</p>
                        <ul class="feature-list">
                            <li>Real-time threat detection</li>
                            <li>256-bit encryption</li>
                            <li>Verified player rankings</li>
                        </ul>
                    </div>
                </div>
                
                <div class="feature-row">
                    <div class="feature-visual">
                        <div class="visual-wrapper">
                            <div class="icon-display">🏆</div>
                            <div class="visual-ring"></div>
                        </div>
                    </div>
                    <div class="feature-text">
                        <span class="feature-num">03</span>
                        <h3>Competitive Ecosystem</h3>
                        <p>From casual matches to million-dollar tournaments, we provide the complete competitive gaming experience.</p>
                        <ul class="feature-list">
                            <li>Daily tournaments</li>
                            <li>$10M+ prize pool</li>
                            <li>Pro league pathways</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    .gaming-features-scroll {{
        padding: 140px 24px;
        background: {background};
    }}
    .scroll-container {{
        max-width: 1100px;
        margin: 0 auto;
    }}
    .scroll-header {{
        text-align: center;
        margin-bottom: 100px;
    }}
    .badge-row {{
        margin-bottom: 24px;
    }}
    .badge {{
        display: inline-block;
        padding: 10px 24px;
        background: {primary}15;
        color: {primary};
        font-weight: 700;
        font-size: 0.85rem;
        letter-spacing: 2px;
        border-radius: 100px;
    }}
    .scroll-header h2 {{
        font-family: 'Rajdhani', sans-serif;
        font-size: clamp(2.5rem, 5vw, 4rem);
        font-weight: 800;
        color: {text};
        margin-bottom: 16px;
    }}
    .scroll-header p {{
        font-size: 1.2rem;
        color: {secondary};
    }}
    .scroll-features {{
        display: flex;
        flex-direction: column;
        gap: 120px;
    }}
    .feature-row {{
        display: grid;
        grid-template-columns: 1fr 1.5fr;
        gap: 80px;
        align-items: center;
    }}
    .feature-row.reverse {{
        grid-template-columns: 1.5fr 1fr;
    }}
    .feature-row.reverse .feature-visual {{
        order: 2;
    }}
    .feature-visual {{
        display: flex;
        justify-content: center;
    }}
    .visual-wrapper {{
        position: relative;
        width: 250px;
        height: 250px;
    }}
    .icon-display {{
        width: 100%;
        height: 100%;
        background: linear-gradient(135deg, {primary}20, {primary}05);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 5rem;
        position: relative;
        z-index: 2;
        box-shadow: 0 0 80px {primary}30;
    }}
    .visual-ring {{
        position: absolute;
        inset: -20px;
        border: 2px dashed {primary}30;
        border-radius: 50%;
        animation: spin 30s linear infinite;
    }}
    @keyframes spin {{
        from {{ transform: rotate(0deg); }}
        to {{ transform: rotate(360deg); }}
    }}
    .feature-text {{
        padding: 20px 0;
    }}
    .feature-num {{
        font-family: 'Orbitron', sans-serif;
        font-size: 0.9rem;
        color: {primary};
        letter-spacing: 3px;
        display: block;
        margin-bottom: 16px;
    }}
    .feature-text h3 {{
        font-size: 2rem;
        font-weight: 800;
        color: {text};
        margin-bottom: 20px;
    }}
    .feature-text p {{
        color: {secondary};
        font-size: 1.1rem;
        line-height: 1.8;
        margin-bottom: 32px;
    }}
    .feature-list {{
        list-style: none;
        padding: 0;
        margin: 0;
    }}
    .feature-list li {{
        display: flex;
        align-items: center;
        gap: 12px;
        color: {text};
        font-size: 1rem;
        padding: 12px 0;
        border-bottom: 1px solid {text}08;
    }}
    .feature-list li::before {{
        content: '✓';
        color: {primary};
        font-weight: 700;
    }}
    @media (max-width: 900px) {{
        .feature-row, .feature-row.reverse {{
            grid-template-columns: 1fr;
            gap: 40px;
        }}
        .feature-row.reverse .feature-visual {{
            order: 0;
        }}
        .visual-wrapper {{
            width: 180px;
            height: 180px;
        }}
        .icon-display {{
            font-size: 3.5rem;
        }}
        .scroll-features {{
            gap: 80px;
        }}
    }}
    </style>
    '''
