from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Holographic Cards - Futuristic 3D holographic effect"""
    title = props.get("title", "The Future of Gaming")
    content = props.get("content", "Pioneering technology that redefines the gaming experience")
    
    # Dynamic colors from user's palette
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="gaming-about-holo" id="about">
        <div class="holo-container">
            <div class="holo-header">
                <div class="tech-line left"></div>
                <span class="tech-badge">// ABOUT.SYS</span>
                <div class="tech-line right"></div>
            </div>
            <h2 class="holo-title">{title}</h2>
            <p class="holo-subtitle">{content}</p>
            
            <div class="holo-grid">
                <div class="holo-card">
                    <div class="card-shine"></div>
                    <div class="card-border"></div>
                    <div class="card-content">
                        <div class="icon-hex">
                            <span>⚡</span>
                        </div>
                        <h3>Lightning Performance</h3>
                        <p>Advanced server architecture delivering sub-10ms latency worldwide.</p>
                        <div class="tech-specs">
                            <div class="spec">
                                <span class="spec-val">10ms</span>
                                <span class="spec-label">Latency</span>
                            </div>
                            <div class="spec">
                                <span class="spec-val">128</span>
                                <span class="spec-label">Tick Rate</span>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="holo-card">
                    <div class="card-shine"></div>
                    <div class="card-border"></div>
                    <div class="card-content">
                        <div class="icon-hex">
                            <span>🛡️</span>
                        </div>
                        <h3>Military-Grade Security</h3>
                        <p>Enterprise encryption and AI-powered anti-cheat systems.</p>
                        <div class="tech-specs">
                            <div class="spec">
                                <span class="spec-val">256bit</span>
                                <span class="spec-label">Encryption</span>
                            </div>
                            <div class="spec">
                                <span class="spec-val">AI</span>
                                <span class="spec-label">Anti-Cheat</span>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="holo-card">
                    <div class="card-shine"></div>
                    <div class="card-border"></div>
                    <div class="card-content">
                        <div class="icon-hex">
                            <span>🌐</span>
                        </div>
                        <h3>Global Infrastructure</h3>
                        <p>200+ edge servers ensuring optimal performance everywhere.</p>
                        <div class="tech-specs">
                            <div class="spec">
                                <span class="spec-val">200+</span>
                                <span class="spec-label">Servers</span>
                            </div>
                            <div class="spec">
                                <span class="spec-val">99.99%</span>
                                <span class="spec-label">Uptime</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="bottom-cta">
                <a href="#tech" class="cta-holo">
                    <span>Explore Technology</span>
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M5 12h14M12 5l7 7-7 7"/>
                    </svg>
                </a>
            </div>
        </div>
    </section>
    
    <style>
    .gaming-about-holo {{
        padding: 140px 24px;
        background: {background};
        position: relative;
        overflow: hidden;
    }}
    .gaming-about-holo::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 80%;
        height: 1px;
        background: linear-gradient(90deg, transparent, {primary}50, transparent);
    }}
    .holo-container {{
        max-width: 1200px;
        margin: 0 auto;
        text-align: center;
    }}
    .holo-header {{
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 24px;
        margin-bottom: 24px;
    }}
    .tech-line {{
        width: 100px;
        height: 1px;
        background: linear-gradient(90deg, transparent, {primary}60);
    }}
    .tech-line.right {{
        background: linear-gradient(90deg, {primary}60, transparent);
    }}
    .tech-badge {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.85rem;
        color: {primary};
        letter-spacing: 2px;
    }}
    .holo-title {{
        font-family: 'Orbitron', sans-serif;
        font-size: clamp(2.5rem, 5vw, 4rem);
        font-weight: 900;
        color: {text};
        margin-bottom: 20px;
        text-shadow: 0 0 60px {primary}20;
    }}
    .holo-subtitle {{
        font-size: 1.2rem;
        color: {secondary};
        max-width: 600px;
        margin: 0 auto 80px;
    }}
    .holo-grid {{
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 32px;
        margin-bottom: 60px;
    }}
    .holo-card {{
        position: relative;
        background: linear-gradient(135deg, {text}05, {text}02);
        border-radius: 24px;
        padding: 3px;
        overflow: hidden;
    }}
    .card-border {{
        position: absolute;
        inset: 0;
        border-radius: 24px;
        padding: 2px;
        background: linear-gradient(135deg, {primary}40, transparent, {secondary}40);
        -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
        mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
        -webkit-mask-composite: xor;
        mask-composite: exclude;
    }}
    .card-shine {{
        position: absolute;
        top: -100%;
        left: -100%;
        width: 200%;
        height: 200%;
        background: linear-gradient(
            135deg,
            transparent 40%,
            {primary}10 45%,
            {primary}20 50%,
            {primary}10 55%,
            transparent 60%
        );
        animation: shine 4s ease-in-out infinite;
    }}
    @keyframes shine {{
        0% {{ transform: translate(-30%, -30%) rotate(0deg); }}
        100% {{ transform: translate(30%, 30%) rotate(0deg); }}
    }}
    .card-content {{
        position: relative;
        z-index: 2;
        background: {background};
        border-radius: 22px;
        padding: 48px 32px;
    }}
    .icon-hex {{
        width: 80px;
        height: 80px;
        background: linear-gradient(135deg, {primary}20, {primary}05);
        clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 24px;
        font-size: 2rem;
    }}
    .holo-card h3 {{
        font-size: 1.4rem;
        font-weight: 800;
        color: {text};
        margin-bottom: 16px;
    }}
    .holo-card p {{
        color: {secondary};
        font-size: 1rem;
        line-height: 1.7;
        margin-bottom: 32px;
    }}
    .tech-specs {{
        display: flex;
        justify-content: center;
        gap: 40px;
        padding-top: 24px;
        border-top: 1px solid {text}10;
    }}
    .spec {{
        text-align: center;
    }}
    .spec-val {{
        display: block;
        font-family: 'Orbitron', sans-serif;
        font-size: 1.5rem;
        font-weight: 900;
        color: {primary};
        margin-bottom: 4px;
    }}
    .spec-label {{
        font-size: 0.75rem;
        color: {secondary};
        text-transform: uppercase;
        letter-spacing: 1px;
    }}
    .cta-holo {{
        display: inline-flex;
        align-items: center;
        gap: 12px;
        padding: 18px 40px;
        background: transparent;
        border: 2px solid {primary};
        color: {primary};
        font-weight: 700;
        font-size: 0.95rem;
        letter-spacing: 2px;
        text-transform: uppercase;
        text-decoration: none;
        border-radius: 8px;
        transition: all 0.3s ease;
    }}
    .cta-holo svg {{
        width: 20px;
        height: 20px;
        transition: transform 0.3s ease;
    }}
    .cta-holo:hover {{
        background: {primary};
        color: {background};
        box-shadow: 0 20px 60px {primary}30;
    }}
    .cta-holo:hover svg {{
        transform: translateX(4px);
    }}
    @media (max-width: 900px) {{
        .holo-grid {{ grid-template-columns: 1fr; }}
    }}
    </style>
    '''
