from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Booking Style - Calendar booking style"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="portfolio-contact-booking" id="contact">
        <div class="booking-container">
            <div class="booking-content">
                <span class="tag">Let's Chat</span>
                <h2>Book a Call</h2>
                <p>Schedule a 30-minute discovery call to discuss your project.</p>
                <ul class="benefits">
                    <li>✓ Free consultation</li>
                    <li>✓ No obligation</li>
                    <li>✓ Project scoping</li>
                </ul>
            </div>
            <div class="booking-form">
                <div class="time-slots">
                    <span class="slot-label">Available This Week</span>
                    <button class="slot">Mon 10:00 AM</button>
                    <button class="slot">Tue 2:00 PM</button>
                    <button class="slot active">Wed 11:00 AM</button>
                    <button class="slot">Thu 3:00 PM</button>
                </div>
                <div class="form-group"><label>Your Email</label><input type="email" placeholder="your@email.com"></div>
                <button class="book-btn">Schedule Call →</button>
            </div>
        </div>
    </section>
    
    <style>
    .portfolio-contact-booking {{ padding: 120px 24px; background: {background}; }}
    .booking-container {{ max-width: 1000px; margin: 0 auto; display: grid; grid-template-columns: 1fr 1fr; gap: 60px; align-items: center; }}
    .tag {{ display: inline-block; padding: 10px 24px; background: {primary}15; color: {primary}; font-weight: 600; border-radius: 100px; margin-bottom: 20px; }}
    .booking-content h2 {{ font-size: clamp(2.5rem, 5vw, 4rem); font-weight: 800; color: {text}; margin-bottom: 16px; }}
    .booking-content p {{ color: {secondary}; font-size: 1.1rem; margin-bottom: 32px; }}
    .benefits {{ list-style: none; padding: 0; }}
    .benefits li {{ color: {text}; padding: 10px 0; font-weight: 500; }}
    .booking-form {{ background: {text}05; border-radius: 24px; padding: 32px; }}
    .time-slots {{ margin-bottom: 24px; }}
    .slot-label {{ display: block; color: {secondary}; font-size: 0.9rem; margin-bottom: 12px; }}
    .slot {{ padding: 12px 16px; background: {text}08; border: 1px solid {text}10; color: {text}; border-radius: 10px; margin: 4px; cursor: pointer; transition: all 0.3s ease; }}
    .slot:hover, .slot.active {{ background: {primary}15; border-color: {primary}; color: {primary}; }}
    .form-group {{ margin-bottom: 20px; }}
    .form-group label {{ display: block; color: {text}; font-weight: 600; margin-bottom: 8px; }}
    .form-group input {{ width: 100%; padding: 16px; background: {background}; border: 1px solid {text}15; border-radius: 12px; color: {text}; font-size: 1rem; }}
    .book-btn {{ width: 100%; padding: 18px; background: {primary}; color: {background}; border: none; font-weight: 700; font-size: 1.1rem; border-radius: 12px; cursor: pointer; transition: all 0.3s ease; }}
    .book-btn:hover {{ transform: translateY(-4px); box-shadow: 0 20px 40px {primary}40; }}
    @media (max-width: 900px) {{ .booking-container {{ grid-template-columns: 1fr; }} }}
    </style>
    '''
