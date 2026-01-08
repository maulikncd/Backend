from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """
    Developer Spotlight - Bold split layout with animated code snippets,
    modern gradient accents and professional developer aesthetic
    """
    name = props.get("name", props.get("businessName", "Alex Developer"))
    title = props.get("title", "Full-Stack Developer")
    tagline = props.get("tagline", "Building Digital Experiences")
    description = props.get("description", "I craft beautiful, performant web applications with modern technologies. Passionate about clean code and great user experiences.")
    cta = props.get("cta", "View Projects")
    cta_secondary = props.get("ctaSecondary", "Contact Me")
    
    primary = colors.get("primary", "#6366F1")
    secondary = colors.get("secondary", "#EC4899")
    bg = colors.get("background", "#0F172A")
    text = colors.get("text", "#F8FAFC")
    
    return f'''
    <section class="dev-hero" id="hero">
        <div class="hero-bg-effects">
            <div class="gradient-orb orb-1"></div>
            <div class="gradient-orb orb-2"></div>
            <div class="grid-pattern"></div>
        </div>
        
        <div class="hero-container">
            <div class="hero-content">
                <div class="status-badge">
                    <span class="status-dot"></span>
                    <span>Available for Work</span>
                </div>
                
                <h1 class="hero-name">{name}</h1>
                <h2 class="hero-title">{title}</h2>
                <p class="hero-tagline">{tagline}</p>
                <p class="hero-desc">{description}</p>
                
                <div class="tech-stack">
                    <span class="tech-label">Tech Stack:</span>
                    <div class="tech-icons">
                        <span class="tech-pill">React</span>
                        <span class="tech-pill">Node.js</span>
                        <span class="tech-pill">Python</span>
                        <span class="tech-pill">TypeScript</span>
                    </div>
                </div>
                
                <div class="cta-group">
                    <a href="#projects" class="btn-primary">{cta}</a>
                    <a href="#contact" class="btn-outline">{cta_secondary}</a>
                </div>
                
                <div class="social-links">
                    <a href="#" class="social-link" aria-label="GitHub">
                        <svg viewBox="0 0 24 24" width="22" height="22"><path fill="currentColor" d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg>
                    </a>
                    <a href="#" class="social-link" aria-label="LinkedIn">
                        <svg viewBox="0 0 24 24" width="22" height="22"><path fill="currentColor" d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
                    </a>
                    <a href="#" class="social-link" aria-label="Twitter">
                        <svg viewBox="0 0 24 24" width="22" height="22"><path fill="currentColor" d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
                    </a>
                </div>
            </div>
            
            <div class="hero-visual">
                <div class="code-window">
                    <div class="window-header">
                        <span class="dot red"></span>
                        <span class="dot yellow"></span>
                        <span class="dot green"></span>
                        <span class="file-name">developer.tsx</span>
                    </div>
                    <div class="code-content">
                        <pre><code><span class="keyword">const</span> <span class="variable">Developer</span> = () => {{
  <span class="keyword">return</span> (
    <span class="tag">&lt;Profile&gt;</span>
      <span class="tag">&lt;Name&gt;</span>{name}<span class="tag">&lt;/Name&gt;</span>
      <span class="tag">&lt;Role&gt;</span>{title}<span class="tag">&lt;/Role&gt;</span>
      <span class="tag">&lt;Passion&gt;</span>Building<span class="tag">&lt;/Passion&gt;</span>
    <span class="tag">&lt;/Profile&gt;</span>
  );
}}</code></pre>
                    </div>
                </div>
                
                <div class="floating-stats">
                    <div class="stat-card">
                        <span class="stat-value">50+</span>
                        <span class="stat-label">Projects</span>
                    </div>
                    <div class="stat-card">
                        <span class="stat-value">5+</span>
                        <span class="stat-label">Years Exp</span>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="scroll-cta">
            <span>Scroll to explore</span>
            <div class="scroll-arrow"></div>
        </div>
    </section>
    
    <style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500&family=Inter:wght@400;500;600;700;800&display=swap');
    
    .dev-hero {{
        min-height: 100vh;
        background: {bg};
        position: relative;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 100px 40px 60px;
        overflow: hidden;
    }}
    .hero-bg-effects {{
        position: absolute;
        inset: 0;
        pointer-events: none;
    }}
    .gradient-orb {{
        position: absolute;
        border-radius: 50%;
        filter: blur(80px);
        opacity: 0.4;
    }}
    .orb-1 {{
        width: 600px;
        height: 600px;
        background: {primary};
        top: -200px;
        right: -100px;
    }}
    .orb-2 {{
        width: 400px;
        height: 400px;
        background: {secondary};
        bottom: -100px;
        left: -50px;
    }}
    .grid-pattern {{
        position: absolute;
        inset: 0;
        background-image: radial-gradient(circle, rgba(255,255,255,0.05) 1px, transparent 1px);
        background-size: 40px 40px;
    }}
    .hero-container {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 80px;
        max-width: 1400px;
        margin: 0 auto;
        align-items: center;
        position: relative;
        z-index: 1;
    }}
    .status-badge {{
        display: inline-flex;
        align-items: center;
        gap: 10px;
        padding: 10px 20px;
        background: rgba(34, 197, 94, 0.15);
        border: 1px solid rgba(34, 197, 94, 0.3);
        border-radius: 50px;
        color: #22C55E;
        font-size: 0.9rem;
        font-weight: 500;
        margin-bottom: 30px;
    }}
    .status-dot {{
        width: 10px;
        height: 10px;
        background: #22C55E;
        border-radius: 50%;
        animation: pulse 2s infinite;
    }}
    @keyframes pulse {{
        0%, 100% {{ opacity: 1; transform: scale(1); }}
        50% {{ opacity: 0.5; transform: scale(1.2); }}
    }}
    .hero-name {{
        font-family: 'Inter', sans-serif;
        font-size: clamp(3rem, 6vw, 5rem);
        font-weight: 800;
        background: linear-gradient(135deg, {text} 0%, {primary} 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        line-height: 1.1;
        margin-bottom: 12px;
    }}
    .hero-title {{
        font-size: 1.8rem;
        font-weight: 600;
        color: {primary};
        margin-bottom: 16px;
    }}
    .hero-tagline {{
        font-size: 1.3rem;
        color: rgba(255,255,255,0.7);
        margin-bottom: 20px;
    }}
    .hero-desc {{
        font-size: 1.1rem;
        color: rgba(255,255,255,0.5);
        line-height: 1.8;
        margin-bottom: 30px;
        max-width: 500px;
    }}
    .tech-stack {{
        margin-bottom: 40px;
    }}
    .tech-label {{
        display: block;
        font-size: 0.85rem;
        color: rgba(255,255,255,0.5);
        margin-bottom: 12px;
    }}
    .tech-icons {{
        display: flex;
        gap: 10px;
        flex-wrap: wrap;
    }}
    .tech-pill {{
        padding: 8px 16px;
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 6px;
        font-size: 0.9rem;
        color: rgba(255,255,255,0.7);
        font-family: 'JetBrains Mono', monospace;
    }}
    .cta-group {{
        display: flex;
        gap: 16px;
        margin-bottom: 40px;
        flex-wrap: wrap;
    }}
    .btn-primary {{
        padding: 16px 36px;
        background: linear-gradient(135deg, {primary}, {secondary});
        color: white;
        border-radius: 12px;
        text-decoration: none;
        font-weight: 600;
        transition: all 0.3s;
        box-shadow: 0 10px 40px {primary}40;
    }}
    .btn-primary:hover {{
        transform: translateY(-3px);
        box-shadow: 0 20px 50px {primary}50;
    }}
    .btn-outline {{
        padding: 16px 36px;
        background: transparent;
        color: {text};
        border: 2px solid rgba(255,255,255,0.2);
        border-radius: 12px;
        text-decoration: none;
        font-weight: 600;
        transition: all 0.3s;
    }}
    .btn-outline:hover {{
        border-color: {primary};
        color: {primary};
    }}
    .social-links {{
        display: flex;
        gap: 16px;
    }}
    .social-link {{
        width: 48px;
        height: 48px;
        display: flex;
        align-items: center;
        justify-content: center;
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 12px;
        color: rgba(255,255,255,0.7);
        transition: all 0.3s;
    }}
    .social-link:hover {{
        background: {primary};
        border-color: {primary};
        color: white;
        transform: translateY(-3px);
    }}
    .hero-visual {{
        position: relative;
    }}
    .code-window {{
        background: #1E293B;
        border-radius: 16px;
        overflow: hidden;
        box-shadow: 0 40px 80px rgba(0,0,0,0.4);
        border: 1px solid rgba(255,255,255,0.1);
    }}
    .window-header {{
        display: flex;
        align-items: center;
        gap: 8px;
        padding: 16px 20px;
        background: #0F172A;
        border-bottom: 1px solid rgba(255,255,255,0.05);
    }}
    .dot {{
        width: 12px;
        height: 12px;
        border-radius: 50%;
    }}
    .dot.red {{ background: #EF4444; }}
    .dot.yellow {{ background: #F59E0B; }}
    .dot.green {{ background: #22C55E; }}
    .file-name {{
        margin-left: auto;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.8rem;
        color: rgba(255,255,255,0.4);
    }}
    .code-content {{
        padding: 30px;
    }}
    .code-content pre {{
        margin: 0;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.95rem;
        line-height: 1.8;
    }}
    .keyword {{ color: #F472B6; }}
    .variable {{ color: #60A5FA; }}
    .tag {{ color: #34D399; }}
    .floating-stats {{
        position: absolute;
        bottom: -30px;
        left: -40px;
        display: flex;
        gap: 16px;
    }}
    .stat-card {{
        background: rgba(255,255,255,0.1);
        backdrop-filter: blur(10px);
        padding: 20px 30px;
        border-radius: 16px;
        text-align: center;
        border: 1px solid rgba(255,255,255,0.1);
    }}
    .stat-value {{
        display: block;
        font-size: 1.8rem;
        font-weight: 700;
        color: {text};
    }}
    .stat-label {{
        font-size: 0.85rem;
        color: rgba(255,255,255,0.5);
    }}
    .scroll-cta {{
        position: absolute;
        bottom: 40px;
        left: 50%;
        transform: translateX(-50%);
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 10px;
        color: rgba(255,255,255,0.4);
        font-size: 0.85rem;
    }}
    .scroll-arrow {{
        width: 20px;
        height: 20px;
        border-right: 2px solid rgba(255,255,255,0.4);
        border-bottom: 2px solid rgba(255,255,255,0.4);
        transform: rotate(45deg);
        animation: bounce 2s infinite;
    }}
    @keyframes bounce {{
        0%, 100% {{ transform: rotate(45deg) translateY(0); }}
        50% {{ transform: rotate(45deg) translateY(8px); }}
    }}
    @media (max-width: 1024px) {{
        .hero-container {{ grid-template-columns: 1fr; gap: 60px; text-align: center; }}
        .hero-content {{ display: flex; flex-direction: column; align-items: center; }}
        .cta-group {{ justify-content: center; }}
        .social-links {{ justify-content: center; }}
        .tech-icons {{ justify-content: center; }}
        .floating-stats {{ left: 50%; transform: translateX(-50%); bottom: -20px; }}
    }}
    @media (max-width: 640px) {{
        .dev-hero {{ padding: 100px 20px 80px; }}
        .floating-stats {{ display: none; }}
    }}
    </style>
    '''
