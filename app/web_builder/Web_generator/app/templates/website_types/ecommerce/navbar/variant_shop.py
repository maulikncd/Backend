from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Shop Nav - Standard ecommerce navbar"""
    brand = props.get("brand_name", "Shop")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <nav class="ecom-nav-shop" id="navbar">
        <div class="nav-container">
            <a href="#" class="logo">{brand}</a>
            <div class="nav-links">
                <a href="#products">Products</a>
                <a href="#categories">Categories</a>
                <a href="#deals">Deals</a>
                <a href="#about">About</a>
            </div>
            <div class="nav-actions">
                <button class="search-btn">🔍</button>
                <a href="#" class="cart-btn">🛒 <span class="count">3</span></a>
                <a href="#" class="account-btn">Account</a>
            </div>
        </div>
    </nav>
    
    <style>
    .ecom-nav-shop {{ position: fixed; top: 0; left: 0; right: 0; z-index: 1000; background: {background}E6; backdrop-filter: blur(20px); border-bottom: 1px solid {text}10; }}
    .nav-container {{ max-width: 1400px; margin: 0 auto; padding: 16px 24px; display: flex; justify-content: space-between; align-items: center; }}
    .logo {{ font-size: 1.5rem; font-weight: 800; color: {text}; text-decoration: none; }}
    .nav-links {{ display: flex; gap: 32px; }}
    .nav-links a {{ color: {secondary}; text-decoration: none; font-weight: 500; transition: color 0.3s ease; }}
    .nav-links a:hover {{ color: {primary}; }}
    .nav-actions {{ display: flex; align-items: center; gap: 20px; }}
    .search-btn {{ background: none; border: none; font-size: 1.2rem; cursor: pointer; }}
    .cart-btn {{ position: relative; color: {text}; text-decoration: none; font-size: 1.3rem; }}
    .count {{ position: absolute; top: -8px; right: -12px; background: {primary}; color: {background}; font-size: 0.7rem; font-weight: 700; padding: 2px 6px; border-radius: 100px; }}
    .account-btn {{ padding: 10px 24px; background: {primary}; color: {background}; text-decoration: none; font-weight: 600; border-radius: 100px; }}
    @media (max-width: 768px) {{ .nav-links {{ display: none; }} }}
    </style>
    '''
