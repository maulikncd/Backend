from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    logo = props.get("logo", "GAMER_ZONE")
    
    return f'''
    <footer class="gaming-footer gaming-footer-cyber" id="footer">
        <div class="footer-top">
            <div class="footer-container">
                <div class="footer-brand">
                    <h2 class="footer-logo">{logo}</h2>
                    <p class="brand-bio">The ultimate destination for competitive gaming and pro esports content.</p>
                    <div class="social-links">
                        <a href="#" class="social-icon">Tw</a>
                        <a href="#" class="social-icon">Yt</a>
                        <a href="#" class="social-icon">Dc</a>
                        <a href="#" class="social-icon">Ig</a>
                    </div>
                </div>
                <div class="footer-nav">
                    <div class="footer-col">
                        <h4>Explore</h4>
                        <a href="#games">Games</a>
                        <a href="#tournaments">Tournaments</a>
                        <a href="#shop">Shop</a>
                    </div>
                    <div class="footer-col">
                        <h4>Support</h4>
                        <a href="#faq">FAQ</a>
                        <a href="#contact">Contact</a>
                        <a href="#privacy">Privacy Policy</a>
                    </div>
                </div>
                <div class="footer-news">
                    <h4>Join the list</h4>
                    <p>Get pro tips and tournament updates.</p>
                    <form class="news-form">
                        <input type="email" placeholder="Email Address">
                        <button type="submit">JOIN</button>
                    </form>
                </div>
            </div>
        </div>
        <div class="footer-bottom">
            <div class="footer-container">
                <p>&copy; 2024 {logo}. All rights reserved.</p>
                <div class="bottom-links">
                    <a href="#">Terms</a>
                    <a href="#">Sitemap</a>
                </div>
            </div>
        </div>
    </footer>
    
    <style>
    .gaming-footer-cyber {{
        background: #050505;
        color: #888;
        padding-top: 80px;
        position: relative;
        border-top: 1px solid rgba(255,255,255,0.05);
    }}
    .footer-container {{
        max-width: 1300px;
        margin: 0 auto;
        padding: 0 40px;
        display: grid;
        grid-template-columns: 1.5fr 2fr 1.5fr;
        gap: 60px;
    }}
    .footer-logo {{
        font-family: 'Rajdhani', sans-serif;
        font-size: 2rem;
        color: #fff;
        margin-bottom: 20px;
    }}
    .brand-bio {{ line-height: 1.6; margin-bottom: 30px; }}
    .social-links {{ display: flex; gap: 15px; }}
    .social-icon {{
        width: 40px;
        height: 40px;
        background: rgba(255,255,255,0.05);
        display: flex;
        align-items: center;
        justify-content: center;
        color: #fff;
        text-decoration: none;
        border-radius: 4px;
        transition: 0.3s;
    }}
    .social-icon:hover {{ background: {colors.get("primary", "#00FF88")}; color: #000; }}
    .footer-nav {{ display: flex; gap: 60px; }}
    .footer-col h4 {{ color: #fff; margin-bottom: 25px; text-transform: uppercase; letter-spacing: 2px; }}
    .footer-col a {{ display: block; color: inherit; text-decoration: none; margin-bottom: 12px; transition: 0.3s; }}
    .footer-col a:hover {{ color: {colors.get("primary", "#00FF88")}; padding-left: 5px; }}
    .footer-news h4 {{ color: #fff; margin-bottom: 20px; }}
    .news-form {{ display: flex; gap: 10px; margin-top: 20px; }}
    .news-form input {{
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.1);
        padding: 12px;
        color: #fff;
        flex: 1;
    }}
    .news-form button {{
        background: {colors.get("primary", "#00FF88")};
        color: #000;
        border: none;
        padding: 0 25px;
        font-weight: 800;
        cursor: pointer;
    }}
    .footer-bottom {{
        margin-top: 80px;
        padding: 30px 0;
        border-top: 1px solid rgba(255,255,255,0.05);
    }}
    .footer-bottom .footer-container {{ display: flex; justify-content: space-between; grid-template-columns: none; }}
    .bottom-links {{ display: flex; gap: 30px; }}
    .bottom-links a {{ color: inherit; text-decoration: none; }}
    @media (max-width: 1024px) {{ .footer-container {{ grid-template-columns: 1fr; gap: 40px; }} }}
    </style>
    '''
