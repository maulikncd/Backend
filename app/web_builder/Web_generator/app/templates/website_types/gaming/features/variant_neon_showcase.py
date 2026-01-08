from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Neon Showcase - Cyberpunk-style feature display with glowing elements"""
    title = props.get("title", "Platform Features")
    subtitle = props.get("subtitle", "Engineered for victory")
    
    # Dynamic colors from user's palette
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="gaming-features-neon" id="features">
        <div class="neon-grid-bg"></div>
        <div class="neon-container">
            <div class="neon-header">
                <div class="cyber-line"></div>
                <span class="cyber-label">// FEATURES.SYS</span>
                <h2>{title}</h2>
                <p>{subtitle}</p>
            </div>
            
            <div class="neon-features">
                <div class="neon-feature primary-feature">
                    <div class="feature-glow"></div>
                    <div class="feature-content">
                        <div class="feature-number">01</div>
                        <div class="feature-icon">⚡</div>
                        <h3>Ultra Performance</h3>
                        <p>Experience gaming without limits. Our infrastructure delivers consistent sub-10ms latency across all regions with 128-tick servers.</p>
                        <div class="feature-stats">
                            <div class="stat-item">
                                <span class="stat-val">10ms</span>
                                <span class="stat-lbl">Latency</span>
                            </div>
                            <div class="stat-item">
                                <span class="stat-val">128</span>
                                <span class="stat-lbl">Tick Rate</span>
                            </div>
                            <div class="stat-item">
                                <span class="stat-val">99.99%</span>
                                <span class="stat-lbl">Uptime</span>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="features-side">
                    <div class="neon-feature small">
                        <div class="feature-number">02</div>
                        <div class="feature-icon">🛡️</div>
                        <h4>Advanced Security</h4>
                        <p>AI-powered anti-cheat with real-time threat detection.</p>
                    </div>
                    
                    <div class="neon-feature small">
                        <div class="feature-number">03</div>
                        <div class="feature-icon">🎮</div>
                        <h4>Pro Analytics</h4>
                        <p>Detailed performance metrics and improvement insights.</p>
                    </div>
                    
                    <div class="neon-feature small">
                        <div class="feature-number">04</div>
                        <div class="feature-icon">🏆</div>
                        <h4>Tournaments</h4>
                        <p>Compete in daily events with real cash prizes.</p>
                    </div>
                    
                    <div class="neon-feature small">
                        <div class="feature-number">05</div>
                        <div class="feature-icon">👥</div>
                        <h4>Social Hub</h4>
                        <p>Connect, team up, and grow with the community.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    .gaming-features-neon {{
        padding: 140px 24px;
        background: {background};
        position: relative;
        overflow: hidden;
    }}
    .neon-grid-bg {{
        position: absolute;
        inset: 0;
        background-image: 
            linear-gradient({primary}08 1px, transparent 1px),
            linear-gradient(90deg, {primary}08 1px, transparent 1px);
        background-size: 80px 80px;
        mask-image: radial-gradient(ellipse at center, black 20%, transparent 70%);
        -webkit-mask-image: radial-gradient(ellipse at center, black 20%, transparent 70%);
    }}
    .neon-container {{
        max-width: 1200px;
        margin: 0 auto;
        position: relative;
        z-index: 2;
    }}
    .neon-header {{
        text-align: center;
        margin-bottom: 80px;
    }}
    .cyber-line {{
        width: 2px;
        height: 60px;
        background: linear-gradient(to bottom, transparent, {primary});
        margin: 0 auto 20px;
    }}
    .cyber-label {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.9rem;
        color: {primary};
        letter-spacing: 3px;
        display: block;
        margin-bottom: 20px;
    }}
    .neon-header h2 {{
        font-family: 'Orbitron', sans-serif;
        font-size: clamp(2.5rem, 5vw, 4rem);
        font-weight: 900;
        color: {text};
        margin-bottom: 16px;
        text-shadow: 0 0 60px {primary}30;
    }}
    .neon-header p {{
        font-size: 1.2rem;
        color: {secondary};
    }}
    .neon-features {{
        display: grid;
        grid-template-columns: 1.5fr 1fr;
        gap: 32px;
    }}
    .neon-feature {{
        background: linear-gradient(135deg, {text}05, transparent);
        border: 1px solid {primary}20;
        border-radius: 24px;
        padding: 48px;
        position: relative;
        overflow: hidden;
        transition: all 0.4s ease;
    }}
    .neon-feature:hover {{
        border-color: {primary}60;
        transform: translateY(-8px);
    }}
    .neon-feature.primary-feature {{
        grid-row: span 4;
    }}
    .neon-feature.small {{
        padding: 32px;
    }}
    .feature-glow {{
        position: absolute;
        bottom: -100px;
        right: -100px;
        width: 300px;
        height: 300px;
        background: {primary};
        filter: blur(120px);
        opacity: 0.15;
    }}
    .feature-content {{
        position: relative;
        z-index: 2;
    }}
    .feature-number {{
        font-family: 'Orbitron', sans-serif;
        font-size: 0.9rem;
        color: {primary}60;
        letter-spacing: 2px;
        margin-bottom: 16px;
    }}
    .feature-icon {{
        font-size: 3rem;
        margin-bottom: 24px;
    }}
    .neon-feature.small .feature-icon {{
        font-size: 2rem;
        margin-bottom: 16px;
    }}
    .neon-feature h3 {{
        font-size: 2rem;
        font-weight: 800;
        color: {text};
        margin-bottom: 16px;
    }}
    .neon-feature h4 {{
        font-size: 1.3rem;
        font-weight: 700;
        color: {text};
        margin-bottom: 8px;
    }}
    .neon-feature p {{
        color: {secondary};
        font-size: 1.1rem;
        line-height: 1.7;
    }}
    .neon-feature.small p {{
        font-size: 0.95rem;
    }}
    .feature-stats {{
        display: flex;
        gap: 40px;
        margin-top: 48px;
        padding-top: 32px;
        border-top: 1px solid {text}10;
    }}
    .stat-item {{
        text-align: center;
    }}
    .stat-val {{
        display: block;
        font-family: 'Orbitron', sans-serif;
        font-size: 2rem;
        font-weight: 900;
        color: {primary};
        text-shadow: 0 0 30px {primary}50;
        margin-bottom: 4px;
    }}
    .stat-lbl {{
        font-size: 0.8rem;
        color: {secondary};
        text-transform: uppercase;
        letter-spacing: 1px;
    }}
    .features-side {{
        display: flex;
        flex-direction: column;
        gap: 24px;
    }}
    @media (max-width: 900px) {{
        .neon-features {{ grid-template-columns: 1fr; }}
        .neon-feature.primary-feature {{ grid-row: span 1; }}
    }}
    </style>
    '''
