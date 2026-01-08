from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Season Pass - Pass tiers showcase"""
    title = props.get("title", "Season 5 Pass")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="gaming-store-pass" id="store">
        <div class="pass-container">
            <div class="pass-header">
                <span class="tag">🏆 Season 5</span>
                <h2>{title}</h2>
                <p>100+ Rewards • Exclusive Skins • Premium Content</p>
            </div>
            <div class="pass-tiers">
                <div class="pass-tier free">
                    <h3>Free Track</h3>
                    <div class="tier-rewards">
                        <div class="reward-item">🎮 5 Free Skins</div>
                        <div class="reward-item">🪙 500 Coins</div>
                        <div class="reward-item">🎨 10 Sprays</div>
                    </div>
                    <div class="tier-price">FREE</div>
                </div>
                <div class="pass-tier premium">
                    <h3>Premium Pass</h3>
                    <div class="tier-rewards">
                        <div class="reward-item">🎮 50+ Exclusive Skins</div>
                        <div class="reward-item">🪙 5000 Coins</div>
                        <div class="reward-item">✨ Instant 25 Levels</div>
                    </div>
                    <div class="tier-price">$19.99</div>
                    <a href="#" class="btn-pass">Get Pass</a>
                </div>
                <div class="pass-tier ultimate">
                    <h3>Ultimate Pass</h3>
                    <div class="tier-rewards">
                        <div class="reward-item">✅ All Premium</div>
                        <div class="reward-item">⚡ Instant 50 Levels</div>
                        <div class="reward-item">👑 Exclusive Title</div>
                    </div>
                    <div class="tier-price">$49.99</div>
                    <a href="#" class="btn-pass">Get Ultimate</a>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    .gaming-store-pass {{ padding: 120px 24px; background: {background}; }}
    .pass-container {{ max-width: 1100px; margin: 0 auto; }}
    .pass-header {{ text-align: center; margin-bottom: 60px; }}
    .tag {{ display: inline-block; padding: 10px 24px; background: {primary}15; color: {primary}; font-weight: 700; border-radius: 100px; margin-bottom: 20px; }}
    .pass-header h2 {{ font-family: 'Rajdhani', sans-serif; font-size: 3rem; font-weight: 800; color: {text}; margin-bottom: 12px; }}
    .pass-header p {{ color: {secondary}; }}
    .pass-tiers {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; }}
    .pass-tier {{ background: {text}05; border: 1px solid {text}10; border-radius: 24px; padding: 32px; text-align: center; }}
    .pass-tier.premium {{ background: linear-gradient(135deg, {primary}15, {primary}05); border-color: {primary}50; transform: translateY(-20px); }}
    .pass-tier h3 {{ font-size: 1.5rem; font-weight: 800; color: {text}; margin-bottom: 24px; }}
    .tier-rewards {{ text-align: left; margin-bottom: 24px; }}
    .reward-item {{ padding: 12px 0; border-bottom: 1px solid {text}08; color: {text}; }}
    .tier-price {{ font-size: 2.5rem; font-weight: 900; color: {primary}; margin-bottom: 24px; }}
    .btn-pass {{ display: block; padding: 16px; background: {primary}; color: {background}; text-decoration: none; font-weight: 700; border-radius: 12px; transition: all 0.3s ease; }}
    .btn-pass:hover {{ transform: scale(1.02); box-shadow: 0 15px 40px {primary}40; }}
    @media (max-width: 900px) {{ .pass-tiers {{ grid-template-columns: 1fr; max-width: 400px; margin: 0 auto; }} .pass-tier.premium {{ transform: none; }} }}
    </style>
    '''
