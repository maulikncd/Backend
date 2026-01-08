from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Social Focus Footer"""
    logo = props.get("logo", "Cafe")
    primary = colors.get("primary", "#8B7355")
    
    return f'''
    <footer class="footer-social-focus"><div class="social-container"><h3>Follow Our Journey</h3><p>@{logo.lower().replace(" ", "")}</p><div class="social-icons"><a href="#" class="social-icon"><svg fill="currentColor" viewBox="0 0 24 24"><path d="M22 12c0-5.523-4.477-10-10-10S2 6.477 2 12c0 4.991 3.657 9.128 8.438 9.878v-6.987h-2.54V12h2.54V9.797c0-2.506 1.492-3.89 3.777-3.89 1.094 0 2.238.195 2.238.195v2.46h-1.26c-1.243 0-1.63.771-1.63 1.562V12h2.773l-.443 2.89h-2.33v6.988C18.343 21.128 22 16.991 22 12z"/></svg></a><a href="#" class="social-icon"><svg fill="currentColor" viewBox="0 0 24 24"><path d="M12.315 2c2.43 0 2.784.013 3.808.06 1.064.049 1.791.218 2.427.465a4.902 4.902 0 011.772 1.153 4.902 4.902 0 011.153 1.772c.247.636.416 1.363.465 2.427.048 1.067.06 1.407.06 4.123v.08c0 2.643-.012 2.987-.06 4.043-.049 1.064-.218 1.791-.465 2.427a4.902 4.902 0 01-1.153 1.772 4.902 4.902 0 01-1.772 1.153c-.636.247-1.363.416-2.427.465-1.067.048-1.407.06-4.123.06h-.08c-2.643 0-2.987-.012-4.043-.06-1.064-.049-1.791-.218-2.427-.465a4.902 4.902 0 01-1.772-1.153 4.902 4.902 0 01-1.153-1.772c-.247-.636-.416-1.363-.465-2.427-.047-1.024-.06-1.379-.06-3.808v-.63c0-2.43.013-2.784.06-3.808.049-1.064.218-1.791.465-2.427a4.902 4.902 0 011.153-1.772A4.902 4.902 0 015.45 2.525c.636-.247 1.363-.416 2.427-.465C8.901 2.013 9.256 2 11.685 2h.63z"/></svg></a><a href="#" class="social-icon"><svg fill="currentColor" viewBox="0 0 24 24"><path d="M8.29 20.251c7.547 0 11.675-6.253 11.675-11.675 0-.178 0-.355-.012-.53A8.348 8.348 0 0022 5.92a8.19 8.19 0 01-2.357.646 4.118 4.118 0 001.804-2.27 8.224 8.224 0 01-2.605.996 4.107 4.107 0 00-6.993 3.743 11.65 11.65 0 01-8.457-4.287 4.106 4.106 0 001.27 5.477A4.072 4.072 0 012.8 9.713v.052a4.105 4.105 0 003.292 4.022 4.095 4.095 0 01-1.853.07 4.108 4.108 0 003.834 2.85A8.233 8.233 0 012 18.407a11.616 11.616 0 006.29 1.84"/></svg></a><a href="#" class="social-icon"><svg fill="currentColor" viewBox="0 0 24 24"><path d="M19.615 3.184c-3.604-.246-11.631-.245-15.23 0-3.897.266-4.356 2.62-4.385 8.816.029 6.185.484 8.549 4.385 8.816 3.6.245 11.626.246 15.23 0 3.897-.266 4.356-2.62 4.385-8.816-.029-6.185-.484-8.549-4.385-8.816zm-10.615 12.816v-8l8 3.993-8 4.007z"/></svg></a></div><div class="footer-bottom"><span>{logo}</span><span>© 2025</span></div></div></footer>
    <style>
    .footer-social-focus {{ background: #0D0D0D; padding: 100px 24px 40px; text-align: center; color: #fff; }}
    .social-container h3 {{ font-family: 'Playfair Display', serif; font-size: 2.5rem; margin-bottom: 10px; }}
    .social-container > p {{ color: {primary}; font-size: 1.2rem; margin-bottom: 40px; }}
    .social-icons {{ display: flex; justify-content: center; gap: 20px; margin-bottom: 60px; }}
    .social-icon {{ width: 60px; height: 60px; border: 1px solid #333; border-radius: 50%; display: flex; align-items: center; justify-content: center; transition: 0.3s; }}
    .social-icon svg {{ width: 24px; height: 24px; fill: #fff; }}
    .social-icon:hover {{ border-color: {primary}; background: {primary}; }}
    .footer-bottom {{ display: flex; justify-content: center; gap: 40px; color: #666; font-size: 0.9rem; }}
    </style>
    '''
