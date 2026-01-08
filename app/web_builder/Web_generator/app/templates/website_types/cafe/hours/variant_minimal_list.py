from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    title = props.get("title", "Opening Hours")
    hours = props.get("hours", [
        {"day": "Monday - Friday", "time": "7:00 AM - 8:00 PM"},
        {"day": "Saturday", "time": "8:00 AM - 9:00 PM"},
        {"day": "Sunday", "time": "9:00 AM - 6:00 PM"}
    ])
    
    hours_html = "".join([f'''
        <div class="hours-row">
            <span class="day">{h["day"]}</span>
            <div class="dots"></div>
            <span class="time">{h["time"]}</span>
        </div>
    ''' for h in hours])
    
    return f'''
    <section class="cafe-hours" id="hours">
        <div class="hours-container">
            <div class="hours-card">
                <h2 class="hours-title">{title}</h2>
                <div class="hours-list">
                    {hours_html}
                </div>
                <div class="hours-note">
                    <p>* Holiday hours may vary. Follow us on IG for updates.</p>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    .cafe-hours {{ padding: 100px 24px; background: #fff; }}
    .hours-container {{ max-width: 600px; margin: 0 auto; }}
    .hours-card {{
        padding: 60px;
        background: {colors.get("background", "#FFF8F0")};
        border-radius: 30px;
        text-align: center;
        border: 1px solid {colors.get("primary", "#6F4E37")}20;
    }}
    .hours-title {{ font-family: 'Playfair Display', serif; font-size: 2.5rem; margin-bottom: 40px; color: {colors.get("text", "#2D2013")}; }}
    .hours-list {{ display: flex; flex-direction: column; gap: 20px; margin-bottom: 40px; }}
    .hours-row {{ display: flex; align-items: baseline; gap: 12px; }}
    .day {{ font-weight: 600; font-size: 1.1rem; color: {colors.get("text", "#2D2013")}; white-space: nowrap; }}
    .dots {{ flex: 1; border-bottom: 2px dotted {colors.get("primary", "#6F4E37")}30; }}
    .time {{ font-weight: 500; color: {colors.get("primary", "#6F4E37")}; }}
    .hours-note {{ font-size: 0.85rem; color: {colors.get("text_muted", "#8B7355")}; font-style: italic; }}
    </style>
    '''
