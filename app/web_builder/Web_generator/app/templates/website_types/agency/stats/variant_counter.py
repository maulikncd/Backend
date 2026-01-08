from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """
    Stats Counter - Animated counter section with key metrics
    """
    primary = colors.get("primary", "#2563EB")
    bg = colors.get("background", "#0F172A")
    text = colors.get("text", "#FFFFFF")
    
    return f'''
    <section class="stats-section" id="stats">
        <div class="container">
            <div class="stats-grid">
                <div class="stat-item">
                    <span class="stat-number" data-target="250">0</span>
                    <span class="stat-suffix">+</span>
                    <span class="stat-label">Projects Completed</span>
                </div>
                <div class="stat-item">
                    <span class="stat-number" data-target="50">0</span>
                    <span class="stat-suffix">+</span>
                    <span class="stat-label">Team Members</span>
                </div>
                <div class="stat-item">
                    <span class="stat-number" data-target="98">0</span>
                    <span class="stat-suffix">%</span>
                    <span class="stat-label">Client Satisfaction</span>
                </div>
                <div class="stat-item">
                    <span class="stat-number" data-target="15">0</span>
                    <span class="stat-suffix">+</span>
                    <span class="stat-label">Years Experience</span>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    .stats-section {{
        padding: 100px 0;
        background: {bg};
    }}
    .stats-section .container {{
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 40px;
    }}
    .stats-grid {{
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 40px;
    }}
    .stat-item {{
        text-align: center;
        padding: 40px 20px;
        background: rgba(255,255,255,0.02);
        border-radius: 20px;
        border: 1px solid rgba(255,255,255,0.05);
    }}
    .stat-number {{
        font-size: 4rem;
        font-weight: 800;
        color: {primary};
        line-height: 1;
    }}
    .stat-suffix {{
        font-size: 2rem;
        font-weight: 700;
        color: {primary};
    }}
    .stat-label {{
        display: block;
        margin-top: 16px;
        font-size: 1rem;
        color: {text}70;
    }}
    @media (max-width: 900px) {{
        .stats-grid {{ grid-template-columns: repeat(2, 1fr); }}
    }}
    @media (max-width: 500px) {{
        .stats-grid {{ grid-template-columns: 1fr; }}
    }}
    </style>
    
    <script>
    const observerOptions = {{
        threshold: 0.5
    }};
    
    const statsObserver = new IntersectionObserver((entries) => {{
        entries.forEach(entry => {{
            if (entry.isIntersecting) {{
                const numbers = entry.target.querySelectorAll('.stat-number');
                numbers.forEach(num => {{
                    const target = parseInt(num.dataset.target);
                    const duration = 2000;
                    const step = target / (duration / 16);
                    let current = 0;
                    
                    const counter = setInterval(() => {{
                        current += step;
                        if (current >= target) {{
                            num.textContent = target;
                            clearInterval(counter);
                        }} else {{
                            num.textContent = Math.floor(current);
                        }}
                    }}, 16);
                }});
                statsObserver.unobserve(entry.target);
            }}
        }});
    }}, observerOptions);
    
    document.querySelectorAll('.stats-section').forEach(section => {{
        statsObserver.observe(section);
    }});
    </script>
    '''
