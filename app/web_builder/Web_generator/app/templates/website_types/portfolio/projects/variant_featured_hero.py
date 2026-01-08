from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Featured Hero - Large featured project with thumbnails"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="portfolio-projects-featured" id="projects">
        <div class="featured-container">
            <div class="projects-header">
                <span class="tag">Work</span>
                <h2>Featured Projects</h2>
            </div>
            <div class="featured-layout">
                <div class="main-project">
                    <div class="project-image"><div class="placeholder">Featured Project</div></div>
                    <div class="project-info">
                        <span class="category">Web Application</span>
                        <h3>E-Commerce Platform</h3>
                        <p>A full-stack e-commerce solution with payment integration and admin dashboard.</p>
                        <div class="tech-tags">
                            <span>React</span><span>Node.js</span><span>MongoDB</span>
                        </div>
                        <a href="#" class="view-btn">View Project →</a>
                    </div>
                </div>
                <div class="side-projects">
                    <div class="side-project">
                        <div class="side-image"><div class="placeholder-sm">P1</div></div>
                        <h4>Portfolio Builder</h4>
                    </div>
                    <div class="side-project">
                        <div class="side-image"><div class="placeholder-sm">P2</div></div>
                        <h4>Task Manager App</h4>
                    </div>
                    <div class="side-project">
                        <div class="side-image"><div class="placeholder-sm">P3</div></div>
                        <h4>Analytics Dashboard</h4>
                    </div>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    .portfolio-projects-featured {{ padding: 120px 24px; background: {background}; }}
    .featured-container {{ max-width: 1200px; margin: 0 auto; }}
    .projects-header {{ text-align: center; margin-bottom: 60px; }}
    .tag {{ display: inline-block; padding: 10px 24px; background: {primary}15; color: {primary}; font-weight: 600; border-radius: 100px; margin-bottom: 20px; }}
    .projects-header h2 {{ font-size: clamp(2.5rem, 5vw, 4rem); font-weight: 800; color: {text}; }}
    .featured-layout {{ display: grid; grid-template-columns: 2fr 1fr; gap: 40px; }}
    .main-project {{ background: {text}05; border-radius: 24px; overflow: hidden; }}
    .project-image {{ aspect-ratio: 16/10; }}
    .placeholder {{ width: 100%; height: 100%; background: linear-gradient(135deg, {primary}20, {primary}05); display: flex; align-items: center; justify-content: center; font-weight: 600; color: {primary}; font-size: 1.5rem; }}
    .project-info {{ padding: 32px; }}
    .category {{ display: inline-block; padding: 5px 14px; background: {primary}20; color: {primary}; font-size: 0.8rem; font-weight: 600; border-radius: 100px; margin-bottom: 12px; }}
    .project-info h3 {{ font-size: 1.8rem; font-weight: 700; color: {text}; margin-bottom: 12px; }}
    .project-info p {{ color: {secondary}; line-height: 1.7; margin-bottom: 20px; }}
    .tech-tags {{ display: flex; gap: 10px; margin-bottom: 24px; }}
    .tech-tags span {{ padding: 6px 14px; background: {text}08; color: {text}; font-size: 0.85rem; border-radius: 100px; }}
    .view-btn {{ color: {primary}; text-decoration: none; font-weight: 700; }}
    .side-projects {{ display: flex; flex-direction: column; gap: 20px; }}
    .side-project {{ background: {text}05; border-radius: 16px; padding: 16px; display: flex; gap: 16px; align-items: center; transition: all 0.3s ease; cursor: pointer; }}
    .side-project:hover {{ background: {primary}10; }}
    .side-image {{ width: 80px; height: 60px; flex-shrink: 0; }}
    .placeholder-sm {{ width: 100%; height: 100%; background: {primary}20; border-radius: 8px; display: flex; align-items: center; justify-content: center; color: {primary}; font-weight: 700; }}
    .side-project h4 {{ font-size: 1rem; font-weight: 600; color: {text}; }}
    @media (max-width: 900px) {{ .featured-layout {{ grid-template-columns: 1fr; }} }}
    </style>
    '''
