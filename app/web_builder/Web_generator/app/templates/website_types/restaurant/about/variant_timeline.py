from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Timeline Journey - Vertical timeline showing restaurant history"""
    title = props.get("sectionTitle", "Our Journey") 
    story = props.get("story", "A legacy of culinary excellence")
    
    primary = colors.get("primary", "#1E3A5F")
    bg = colors.get("background", "#FFFFFF")
    text = colors.get("text", "#1A1A1A")
    
    return f'''
    <section class="about-timeline" id="about">
        <div class="timeline-container">
            <div class="timeline-header">
                <span class="label">Our History</span>
                <h2 class="title">{title}</h2>
                <p class="subtitle">{story}</p>
            </div>
            
            <div class="timeline">
                <div class="timeline-item">
                    <div class="timeline-marker">
                        <span class="year">2010</span>
                    </div>
                    <div class="timeline-content">
                        <h3>The Beginning</h3>
                        <p>Started as a small family kitchen with a dream to share authentic recipes passed down through generations.</p>
                    </div>
                </div>
                
                <div class="timeline-item">
                    <div class="timeline-marker">
                        <span class="year">2015</span>
                    </div>
                    <div class="timeline-content">
                        <h3>First Recognition</h3>
                        <p>Awarded "Best New Restaurant" by Food & Wine magazine. Expanded our team with talented chefs from around the world.</p>
                    </div>
                </div>
                
                <div class="timeline-item">
                    <div class="timeline-marker">
                        <span class="year">2020</span>
                    </div>
                    <div class="timeline-content">
                        <h3>Michelin Star</h3>
                        <p>Received our first Michelin star, recognizing our commitment to culinary excellence and innovation.</p>
                    </div>
                </div>
                
                <div class="timeline-item">
                    <div class="timeline-marker">
                        <span class="year">Today</span>
                    </div>
                    <div class="timeline-content">
                        <h3>Continuing the Legacy</h3>
                        <p>Now serving over 500 guests weekly, we continue to push boundaries while honoring our roots.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Libre+Baskerville:wght@400;700&family=Source+Sans+Pro:wght@400;600&display=swap');
    
    .about-timeline {{
        padding: 120px 60px;
        background: {bg};
    }}
    .timeline-container {{
        max-width: 900px;
        margin: 0 auto;
    }}
    .timeline-header {{
        text-align: center;
        margin-bottom: 80px;
    }}
    .timeline-header .label {{
        display: inline-block;
        color: {primary};
        font-size: 0.85rem;
        letter-spacing: 3px;
        text-transform: uppercase;
        margin-bottom: 15px;
    }}
    .timeline-header .title {{
        font-family: 'Libre Baskerville', serif;
        font-size: clamp(2.5rem, 5vw, 4rem);
        color: {text};
        margin-bottom: 15px;
    }}
    .timeline-header .subtitle {{
        font-size: 1.15rem;
        color: {text}80;
        max-width: 600px;
        margin: 0 auto;
    }}
    .timeline {{
        position: relative;
        padding-left: 50px;
    }}
    .timeline::before {{
        content: '';
        position: absolute;
        left: 20px;
        top: 0;
        bottom: 0;
        width: 2px;
        background: linear-gradient(to bottom, {primary}, {primary}30);
    }}
    .timeline-item {{
        position: relative;
        margin-bottom: 60px;
        display: flex;
        gap: 40px;
    }}
    .timeline-item:last-child {{
        margin-bottom: 0;
    }}
    .timeline-marker {{
        position: absolute;
        left: -50px;
        width: 60px;
        display: flex;
        justify-content: center;
    }}
    .timeline-marker .year {{
        background: {primary};
        color: white;
        padding: 10px 15px;
        border-radius: 8px;
        font-size: 0.85rem;
        font-weight: 600;
        white-space: nowrap;
    }}
    .timeline-content {{
        background: {bg};
        padding: 30px;
        border-radius: 16px;
        border: 1px solid {text}10;
        box-shadow: 0 10px 40px rgba(0,0,0,0.05);
        flex: 1;
        margin-left: 30px;
    }}
    .timeline-content h3 {{
        font-family: 'Libre Baskerville', serif;
        font-size: 1.4rem;
        color: {text};
        margin-bottom: 12px;
    }}
    .timeline-content p {{
        font-family: 'Source Sans Pro', sans-serif;
        font-size: 1rem;
        color: {text}80;
        line-height: 1.7;
    }}
    @media (max-width: 768px) {{
        .about-timeline {{ padding: 80px 30px; }}
        .timeline {{ padding-left: 30px; }}
        .timeline::before {{ left: 10px; }}
        .timeline-marker {{ left: -30px; }}
        .timeline-marker .year {{ padding: 8px 12px; font-size: 0.75rem; }}
        .timeline-content {{ margin-left: 20px; padding: 20px; }}
    }}
    </style>
    '''
