from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Minimal Nav - Clean minimal navbar"""
    brand = props.get("brand_name", "Shop")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <nav class="ecom-nav-minimal" id="navbar">
        <div class="nav-container">
            <a href="#" class="logo">{brand}</a>
            <div class="nav-center">
                <a href="#products">Shop</a>
                <a href="#categories">Categories</a>
                <a href="#about">About</a>
            </div>
            <div class="nav-right">
                <a href="#" class="icon-btn">🔍</a>
                <a href="#" class="icon-btn">👤</a>
                <a href="#" class="icon-btn cart">🛒<span>3</span></a>
            </div>
        </div>
    </nav>
    
    <style>
    .ecom-nav-minimal {{ position: fixed; top: 0; left: 0; right: 0; z-index: 1000; background: {background}; }}
    .nav-container {{ max-width: 1200px; margin: 0 auto; padding: 20px 24px; display: flex; justify-content: space-between; align-items: center; }}
    .logo {{ font-size: 1.8rem; font-weight: 900; color: {text}; text-decoration: none; letter-spacing: -1px; }}
    .nav-center {{ display: flex; gap: 40px; }}
    .nav-center a {{ color: {text}; text-decoration: none; font-weight: 500; font-size: 0.95rem; transition: color 0.3s ease; }}
    .nav-center a:hover {{ color: {primary}; }}
    .nav-right {{ display: flex; gap: 20px; }}
    .icon-btn {{ color: {text}; text-decoration: none; font-size: 1.2rem; position: relative; }}
    .icon-btn.cart span {{ position: absolute; top: -6px; right: -10px; background: {primary}; color: {background}; font-size: 0.65rem; font-weight: 700; padding: 2px 5px; border-radius: 100px; }}
    @media (max-width: 768px) {{ .nav-center {{ display: none; }} }}
    </style>
    '''
