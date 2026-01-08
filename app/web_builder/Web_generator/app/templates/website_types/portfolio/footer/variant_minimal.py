from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """
    Minimal Footer - Clean, simple footer with copyright and social links
    """
    name = props.get("name", props.get("businessName", "John Doe"))
    year = props.get("year", "2024")
    
    primary = colors.get("primary", "#6366F1")
    bg = colors.get("background", "#0F172A")
    text = colors.get("text", "#F8FAFC")
    
    return f'''
    <footer class="portfolio-footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-brand">
                    <span class="brand-name">{name}</span>
                    <p class="copyright">© {year} All rights reserved.</p>
                </div>
                
                <div class="footer-links">
                    <a href="#hero">Home</a>
                    <a href="#about">About</a>
                    <a href="#projects">Projects</a>
                    <a href="#contact">Contact</a>
                </div>
                
                <div class="footer-social">
                    <a href="#" aria-label="GitHub">
                        <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg>
                    </a>
                    <a href="#" aria-label="LinkedIn">
                        <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
                    </a>
                    <a href="#" aria-label="Twitter">
                        <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
                    </a>
                    <a href="#" aria-label="Dribbble">
                        <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor"><path d="M12 24C5.385 24 0 18.615 0 12S5.385 0 12 0s12 5.385 12 12-5.385 12-12 12zm10.12-10.358c-.35-.11-3.17-.953-6.384-.438 1.34 3.684 1.887 6.684 1.992 7.308a10.18 10.18 0 0 0 4.392-6.87zm-6.115 7.808c-.153-.9-.75-4.032-2.19-7.77l-.066.02c-5.79 2.015-7.86 6.025-8.04 6.4a10.161 10.161 0 0 0 6.29 2.166c1.42 0 2.77-.29 4.006-.816zm-11.62-2.58c.232-.4 3.045-5.055 8.332-6.765.133-.045.266-.085.4-.12-.26-.585-.54-1.167-.832-1.74C7.17 11.775 2.206 11.71 1.756 11.7l-.004.312c0 2.633.998 5.037 2.634 6.858zm-2.42-8.955c.46.008 4.683.026 9.477-1.248a65.473 65.473 0 0 0-3.8-5.928A10.172 10.172 0 0 0 1.965 9.915zM10.56 2.23a64.16 64.16 0 0 1 3.876 5.996c3.918-1.47 5.576-3.7 5.782-3.996A10.138 10.138 0 0 0 12 1.8c-.488 0-.97.036-1.44.106zm10.97 3.39c-.254.332-2.12 2.716-6.196 4.367.222.457.44.92.644 1.387.073.17.143.338.21.508 3.407-.43 6.794.26 7.13.335a10.045 10.045 0 0 0-1.788-6.597z"/></svg>
                    </a>
                </div>
            </div>
            
            <div class="back-to-top">
                <a href="#hero" class="top-btn" aria-label="Back to top">↑</a>
            </div>
        </div>
    </footer>
    
    <style>
    .portfolio-footer {{
        padding: 60px 0;
        background: {bg};
        border-top: 1px solid rgba(255,255,255,0.05);
    }}
    .portfolio-footer .container {{
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 40px;
    }}
    .footer-content {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 30px;
    }}
    .brand-name {{
        font-size: 1.3rem;
        font-weight: 700;
        color: {text};
        display: block;
        margin-bottom: 8px;
    }}
    .copyright {{
        font-size: 0.9rem;
        color: {text}50;
        margin: 0;
    }}
    .footer-links {{
        display: flex;
        gap: 30px;
    }}
    .footer-links a {{
        color: {text}60;
        text-decoration: none;
        font-size: 0.95rem;
        transition: color 0.3s;
    }}
    .footer-links a:hover {{
        color: {primary};
    }}
    .footer-social {{
        display: flex;
        gap: 16px;
    }}
    .footer-social a {{
        width: 44px;
        height: 44px;
        display: flex;
        align-items: center;
        justify-content: center;
        background: rgba(255,255,255,0.05);
        border-radius: 12px;
        color: {text}60;
        transition: all 0.3s;
    }}
    .footer-social a:hover {{
        background: {primary};
        color: white;
        transform: translateY(-3px);
    }}
    .back-to-top {{
        text-align: center;
        margin-top: 40px;
    }}
    .top-btn {{
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 50px;
        height: 50px;
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 50%;
        color: {text}60;
        text-decoration: none;
        font-size: 1.2rem;
        transition: all 0.3s;
    }}
    .top-btn:hover {{
        border-color: {primary};
        color: {primary};
        transform: translateY(-5px);
    }}
    @media (max-width: 768px) {{
        .footer-content {{ flex-direction: column; text-align: center; }}
        .portfolio-footer .container {{ padding: 0 24px; }}
    }}
    </style>
    '''
