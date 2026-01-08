from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Split Image Features"""
    title = props.get("title", "Next-Gen Gaming")
    primary = colors.get("primary", "#FF4444")
    
    return f'''
    <section class="gaming-features-split" id="features"><div class="split-grid">
        <div class="split-img" style="background: url('https://images.unsplash.com/photo-1542751371-adc38448a05e?w=1000') center/cover"></div>
        <div class="split-content"><span class="tag">Features</span><h2>{title}</h2><ul class="feature-list">
            <li><span class="check">✓</span> Ray-tracing graphics</li>
            <li><span class="check">✓</span> 120 FPS support</li>
            <li><span class="check">✓</span> Haptic feedback</li>
            <li><span class="check">✓</span> Cloud saves</li>
        </ul><a href="#" class="cta-btn">Learn More</a></div>
    </div></section>
    <style>
    .gaming-features-split {{ min-height: 100vh; display: flex; }}
    .split-grid {{ display: grid; grid-template-columns: 1fr 1fr; width: 100%; }}
    .split-img {{ background-size: cover; }}
    .split-content {{ background: #0D0D15; padding: 80px 60px; display: flex; flex-direction: column; justify-content: center; color: #fff; }}
    .tag {{ color: {primary}; text-transform: uppercase; letter-spacing: 4px; font-size: 0.9rem; margin-bottom: 20px; }}
    .split-content h2 {{ font-size: 3rem; margin-bottom: 40px; }}
    .feature-list {{ list-style: none; margin-bottom: 40px; }}
    .feature-list li {{ padding: 15px 0; border-bottom: 1px solid #333; display: flex; align-items: center; gap: 15px; font-size: 1.1rem; }}
    .check {{ color: {primary}; font-weight: bold; }}
    .cta-btn {{ display: inline-block; padding: 18px 50px; background: {primary}; color: #fff; text-decoration: none; font-weight: 700; align-self: flex-start; transition: 0.3s; }}
    .cta-btn:hover {{ transform: scale(1.05); }}
    @media (max-width: 900px) {{ .split-grid {{ grid-template-columns: 1fr; }} .split-img {{ height: 300px; }} }}
    </style>
    '''
