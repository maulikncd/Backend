from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Dark Premium - Dark luxury style"""
    brand = props.get("brand_name", "Shop")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <nav class="ecom-nav-dark" id="navbar">
        <div class="nav-container">
            <a href="#" class="logo">{brand}</a>
            <div class="nav-links">
                <a href="#products">Collection</a>
                <a href="#categories">Categories</a>
                <a href="#about">About</a>
                <a href="#contact">Contact</a>
            </div>
            <div class="nav-actions">
                <a href="#" class="icon-link">🔍</a>
                <a href="#" class="icon-link">👤</a>
                <a href="#" class="cart-link">Cart (3)</a>
            </div>
        </div>
    </nav>
    
    <style>
    .ecom-nav-dark {{ position: fixed; top: 0; left: 0; right: 0; z-index: 1000; background: {text}; }}
    .nav-container {{ max-width: 1400px; margin: 0 auto; padding: 20px 40px; display: flex; justify-content: space-between; align-items: center; }}
    .logo {{ font-size: 1.5rem; font-weight: 800; color: {background}; text-decoration: none; letter-spacing: 2px; text-transform: uppercase; }}
    .nav-links {{ display: flex; gap: 40px; }}
    .nav-links a {{ color: {background}80; text-decoration: none; font-weight: 500; font-size: 0.9rem; letter-spacing: 1px; transition: color 0.3s ease; }}
    .nav-links a:hover {{ color: {background}; }}
    .nav-actions {{ display: flex; align-items: center; gap: 24px; }}
    .icon-link {{ color: {background}80; text-decoration: none; font-size: 1.2rem; }}
    .cart-link {{ color: {primary}; text-decoration: none; font-weight: 600; font-size: 0.9rem; letter-spacing: 1px; }}
    @media (max-width: 768px) {{ .nav-links {{ display: none; }} }}
    </style>
    '''
