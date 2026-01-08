from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Flash Sale - Countdown timer hero"""
    title = props.get("title", "Flash Sale")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="ecom-hero-flash" id="hero">
        <div class="flash-container">
            <div class="flash-content">
                <span class="sale-badge">⚡ Limited Time</span>
                <h1>Flash Sale<br/><span>Up to 70% Off</span></h1>
                <p>Don't miss out on our biggest sale of the year!</p>
                <div class="countdown">
                    <div class="time-block"><span class="num">02</span><span class="label">Days</span></div>
                    <div class="time-block"><span class="num">14</span><span class="label">Hours</span></div>
                    <div class="time-block"><span class="num">36</span><span class="label">Mins</span></div>
                    <div class="time-block"><span class="num">22</span><span class="label">Secs</span></div>
                </div>
                <a href="#products" class="shop-btn">Shop Now →</a>
            </div>
            <div class="flash-visual">
                <div class="circle-bg"></div>
                <div class="product-card"><span>70% OFF</span></div>
            </div>
        </div>
    </section>
    
    <style>
    .ecom-hero-flash {{ min-height: 100vh; background: linear-gradient(135deg, {primary}15, {background}); display: flex; align-items: center; padding: 80px 24px; }}
    .flash-container {{ max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: 1fr 1fr; gap: 60px; align-items: center; }}
    .sale-badge {{ display: inline-block; padding: 12px 28px; background: #ff3b3b; color: white; font-weight: 700; border-radius: 100px; margin-bottom: 24px; animation: pulse 2s infinite; }}
    @keyframes pulse {{ 0%, 100% {{ transform: scale(1); }} 50% {{ transform: scale(1.05); }} }}
    .flash-content h1 {{ font-size: clamp(3rem, 7vw, 5rem); font-weight: 900; color: {text}; line-height: 1.1; margin-bottom: 20px; }}
    .flash-content h1 span {{ color: {primary}; }}
    .flash-content p {{ color: {secondary}; font-size: 1.2rem; margin-bottom: 40px; }}
    .countdown {{ display: flex; gap: 16px; margin-bottom: 40px; }}
    .time-block {{ background: {text}08; border-radius: 16px; padding: 20px; text-align: center; min-width: 80px; }}
    .time-block .num {{ display: block; font-size: 2.5rem; font-weight: 900; color: {primary}; }}
    .time-block .label {{ color: {secondary}; font-size: 0.85rem; }}
    .shop-btn {{ display: inline-block; padding: 20px 48px; background: {primary}; color: {background}; text-decoration: none; font-weight: 700; font-size: 1.1rem; border-radius: 14px; transition: all 0.3s ease; }}
    .shop-btn:hover {{ transform: translateY(-4px); box-shadow: 0 25px 50px {primary}40; }}
    .flash-visual {{ position: relative; display: flex; justify-content: center; align-items: center; }}
    .circle-bg {{ width: 400px; height: 400px; background: {primary}20; border-radius: 50%; }}
    .product-card {{ position: absolute; width: 200px; height: 250px; background: {background}; border-radius: 20px; box-shadow: 0 30px 60px {primary}20; display: flex; align-items: center; justify-content: center; animation: float 3s ease-in-out infinite; }}
    .product-card span {{ font-size: 2rem; font-weight: 900; color: {primary}; }}
    @keyframes float {{ 0%, 100% {{ transform: translateY(0); }} 50% {{ transform: translateY(-20px); }} }}
    @media (max-width: 900px) {{ .flash-container {{ grid-template-columns: 1fr; text-align: center; }} .countdown {{ justify-content: center; }} .flash-visual {{ display: none; }} }}
    </style>
    '''
