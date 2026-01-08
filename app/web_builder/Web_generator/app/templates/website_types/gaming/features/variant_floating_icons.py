from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Floating Icons - 3D floating elements with depth effect"""
    title = props.get("title", "Next-Gen Features")
    subtitle = props.get("subtitle", "Built for the future of gaming")
    
    # Dynamic colors from user's palette
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="gaming-features-floating" id="features">
        <div class="floating-orbs">
            <div class="orb orb-1"></div>
            <div class="orb orb-2"></div>
            <div class="orb orb-3"></div>
        </div>
        <div class="floating-container">
            <div class="floating-header">
                <h2>{title}</h2>
                <p>{subtitle}</p>
            </div>
            
            <div class="floating-showcase">
                <div class="center-graphic">
                    <div class="hex-core">
                        <span>🎮</span>
                    </div>
                    <div class="core-rings">
                        <div class="ring ring-1"></div>
                        <div class="ring ring-2"></div>
                        <div class="ring ring-3"></div>
                    </div>
                </div>
                
                <div class="feature-orbit feature-1">
                    <div class="orbit-card">
                        <div class="card-icon">⚡</div>
                        <h4>10ms Latency</h4>
                        <p>Lightning-fast response</p>
                    </div>
                </div>
                
                <div class="feature-orbit feature-2">
                    <div class="orbit-card">
                        <div class="card-icon">🛡️</div>
                        <h4>AI Anti-Cheat</h4>
                        <p>Smart protection</p>
                    </div>
                </div>
                
                <div class="feature-orbit feature-3">
                    <div class="orbit-card">
                        <div class="card-icon">🌐</div>
                        <h4>200+ Servers</h4>
                        <p>Global coverage</p>
                    </div>
                </div>
                
                <div class="feature-orbit feature-4">
                    <div class="orbit-card">
                        <div class="card-icon">🏆</div>
                        <h4>$10M Prizes</h4>
                        <p>Real rewards</p>
                    </div>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    .gaming-features-floating {{
        padding: 140px 24px;
        background: {background};
        position: relative;
        overflow: hidden;
        min-height: 100vh;
    }}
    .floating-orbs {{
        position: absolute;
        inset: 0;
        pointer-events: none;
    }}
    .orb {{
        position: absolute;
        border-radius: 50%;
        filter: blur(100px);
        opacity: 0.3;
    }}
    .orb-1 {{
        width: 500px;
        height: 500px;
        background: {primary};
        top: -200px;
        left: -200px;
        animation: floatOrb 20s ease-in-out infinite;
    }}
    .orb-2 {{
        width: 400px;
        height: 400px;
        background: {secondary};
        bottom: -100px;
        right: -100px;
        animation: floatOrb 25s ease-in-out infinite reverse;
    }}
    .orb-3 {{
        width: 300px;
        height: 300px;
        background: {primary};
        top: 50%;
        left: 30%;
        animation: floatOrb 15s ease-in-out infinite;
    }}
    @keyframes floatOrb {{
        0%, 100% {{ transform: translate(0, 0); }}
        50% {{ transform: translate(50px, -50px); }}
    }}
    .floating-container {{
        max-width: 1200px;
        margin: 0 auto;
        position: relative;
        z-index: 2;
    }}
    .floating-header {{
        text-align: center;
        margin-bottom: 80px;
    }}
    .floating-header h2 {{
        font-family: 'Orbitron', sans-serif;
        font-size: clamp(2.5rem, 5vw, 4rem);
        font-weight: 900;
        color: {text};
        margin-bottom: 16px;
        text-shadow: 0 0 60px {primary}30;
    }}
    .floating-header p {{
        font-size: 1.2rem;
        color: {secondary};
    }}
    .floating-showcase {{
        position: relative;
        height: 600px;
        display: flex;
        align-items: center;
        justify-content: center;
    }}
    .center-graphic {{
        position: relative;
        width: 200px;
        height: 200px;
    }}
    .hex-core {{
        width: 100%;
        height: 100%;
        background: linear-gradient(135deg, {primary}30, {primary}10);
        clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 4rem;
        position: relative;
        z-index: 3;
        animation: pulse-core 3s ease-in-out infinite;
    }}
    @keyframes pulse-core {{
        0%, 100% {{ transform: scale(1); }}
        50% {{ transform: scale(1.05); }}
    }}
    .core-rings {{
        position: absolute;
        inset: -50px;
    }}
    .ring {{
        position: absolute;
        inset: 0;
        border: 2px solid {primary}30;
        border-radius: 50%;
        animation: spin-ring linear infinite;
    }}
    .ring-1 {{ animation-duration: 20s; }}
    .ring-2 {{ inset: -30px; animation-duration: 30s; animation-direction: reverse; }}
    .ring-3 {{ inset: -60px; animation-duration: 40s; border-style: dashed; }}
    @keyframes spin-ring {{
        from {{ transform: rotate(0deg); }}
        to {{ transform: rotate(360deg); }}
    }}
    .feature-orbit {{
        position: absolute;
        animation: float-card 6s ease-in-out infinite;
    }}
    .feature-1 {{ top: 5%; left: 10%; animation-delay: 0s; }}
    .feature-2 {{ top: 10%; right: 10%; animation-delay: -1.5s; }}
    .feature-3 {{ bottom: 10%; left: 15%; animation-delay: -3s; }}
    .feature-4 {{ bottom: 15%; right: 15%; animation-delay: -4.5s; }}
    @keyframes float-card {{
        0%, 100% {{ transform: translateY(0) rotate(0deg); }}
        50% {{ transform: translateY(-20px) rotate(2deg); }}
    }}
    .orbit-card {{
        background: linear-gradient(135deg, {text}10, {text}05);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid {text}15;
        border-radius: 20px;
        padding: 32px;
        text-align: center;
        min-width: 180px;
        transition: all 0.4s ease;
    }}
    .orbit-card:hover {{
        border-color: {primary}50;
        transform: scale(1.1);
        box-shadow: 0 30px 60px {primary}20;
    }}
    .card-icon {{
        font-size: 2.5rem;
        margin-bottom: 16px;
    }}
    .orbit-card h4 {{
        font-size: 1.1rem;
        font-weight: 800;
        color: {text};
        margin-bottom: 8px;
    }}
    .orbit-card p {{
        font-size: 0.85rem;
        color: {secondary};
    }}
    @media (max-width: 900px) {{
        .floating-showcase {{ height: auto; flex-direction: column; gap: 24px; padding: 60px 0; }}
        .feature-orbit {{ position: relative; top: auto !important; left: auto !important; right: auto !important; bottom: auto !important; }}
        .center-graphic {{ margin-bottom: 40px; }}
    }}
    </style>
    '''
