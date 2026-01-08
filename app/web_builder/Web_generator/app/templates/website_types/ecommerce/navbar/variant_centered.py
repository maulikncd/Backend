from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Centered Logo - Logo in center"""
    brand = props.get("brand_name", "Shop")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <nav class="ecom-nav-centered" id="navbar">
        <div class="nav-container">
            <div class="nav-left">
                <a href="#products">Shop</a>
                <a href="#categories">Categories</a>
                <a href="#deals">Deals</a>
            </div>
            <a href="#" class="logo">{brand}</a>
            <div class="nav-right">
                <a href="#">Search</a>
                <a href="#">Account</a>
                <a href="#" class="cart">Cart (3)</a>
            </div>
        </div>
    </nav>
    
    <style>
    .ecom-nav-centered {{ position: fixed; top: 0; left: 0; right: 0; z-index: 1000; background: {background}; border-bottom: 1px solid {text}10; }}
    .nav-container {{ max-width: 1200px; margin: 0 auto; padding: 24px; display: grid; grid-template-columns: 1fr auto 1fr; align-items: center; }}
    .logo {{ font-size: 2rem; font-weight: 900; color: {text}; text-decoration: none; text-align: center; letter-spacing: 4px; text-transform: uppercase; }}
    .nav-left, .nav-right {{ display: flex; gap: 32px; }}
    .nav-left {{ justify-content: flex-start; }}
    .nav-right {{ justify-content: flex-end; }}
    .nav-left a, .nav-right a {{ color: {text}; text-decoration: none; font-weight: 500; font-size: 0.9rem; transition: color 0.3s ease; }}
    .nav-left a:hover, .nav-right a:hover {{ color: {primary}; }}
    .cart {{ color: {primary} !important; font-weight: 600; }}
    @media (max-width: 768px) {{ .nav-left, .nav-right {{ display: none; }} .nav-container {{ grid-template-columns: 1fr; justify-items: center; }} }}
    </style>
    '''
