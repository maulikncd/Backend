from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Registration - Tournament signup form"""
    title = props.get("title", "Register Your Team")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="gaming-tournament-register" id="tournaments">
        <div class="register-container">
            <div class="register-info">
                <span class="tag">🏆 World Championship 2024</span>
                <h2>{title}</h2>
                <p>Join the biggest gaming event of the year. $1M prize pool awaits!</p>
                <div class="event-details">
                    <div class="detail"><span>📅</span><label>Dec 15-20, 2024</label></div>
                    <div class="detail"><span>👥</span><label>64 Teams</label></div>
                    <div class="detail"><span>💰</span><label>$1M Prize Pool</label></div>
                </div>
            </div>
            <div class="register-form">
                <h3>Team Registration</h3>
                <div class="form-group"><label>Team Name</label><input type="text" placeholder="Enter team name"></div>
                <div class="form-group"><label>Captain Email</label><input type="email" placeholder="captain@team.com"></div>
                <div class="form-group"><label>Region</label><select><option>North America</option><option>Europe</option><option>Asia</option></select></div>
                <button class="submit-btn">Register Now</button>
                <p class="form-note">Registration closes Dec 10, 2024</p>
            </div>
        </div>
    </section>
    
    <style>
    .gaming-tournament-register {{ padding: 120px 24px; background: {background}; }}
    .register-container {{ max-width: 1100px; margin: 0 auto; display: grid; grid-template-columns: 1fr 1fr; gap: 60px; align-items: center; }}
    .tag {{ display: inline-block; padding: 10px 24px; background: {primary}15; color: {primary}; font-weight: 700; border-radius: 100px; margin-bottom: 20px; }}
    .register-info h2 {{ font-family: 'Rajdhani', sans-serif; font-size: 3rem; font-weight: 800; color: {text}; margin-bottom: 16px; }}
    .register-info p {{ color: {secondary}; font-size: 1.2rem; line-height: 1.7; margin-bottom: 32px; }}
    .event-details {{ display: flex; flex-direction: column; gap: 16px; }}
    .detail {{ display: flex; align-items: center; gap: 12px; }}
    .detail span {{ font-size: 1.5rem; }}
    .detail label {{ color: {text}; font-weight: 600; }}
    .register-form {{ background: {text}05; border-radius: 24px; padding: 40px; }}
    .register-form h3 {{ font-size: 1.5rem; font-weight: 700; color: {text}; margin-bottom: 24px; text-align: center; }}
    .form-group {{ margin-bottom: 20px; }}
    .form-group label {{ display: block; color: {secondary}; margin-bottom: 8px; font-weight: 600; }}
    .form-group input, .form-group select {{ width: 100%; padding: 14px 16px; background: {background}; border: 1px solid {text}15; border-radius: 10px; color: {text}; font-size: 1rem; }}
    .submit-btn {{ width: 100%; padding: 16px; background: {primary}; color: {background}; border: none; font-weight: 700; font-size: 1rem; border-radius: 12px; cursor: pointer; transition: all 0.3s ease; margin-top: 8px; }}
    .submit-btn:hover {{ transform: scale(1.02); box-shadow: 0 15px 40px {primary}40; }}
    .form-note {{ text-align: center; color: {secondary}; font-size: 0.9rem; margin-top: 16px; }}
    @media (max-width: 900px) {{ .register-container {{ grid-template-columns: 1fr; }} }}
    </style>
    '''
