from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Glass Style - Glassmorphism navbar"""
    brand = props.get("brand_name", "Shop")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <nav class="ecom-nav-glass" id="navbar">
        <div class="nav-container">
            <a href="#" class="logo">{brand}</a>
            <div class="nav-links">
                <a href="#products">Products</a>
                <a href="#categories">Categories</a>
                <a href="#deals">Deals</a>
            </div>
            <div class="nav-actions">
                <button class="search-toggle">🔍</button>
                <a href="#" class="cart-btn"><span class="cart-icon">🛒</span><span class="cart-count">3</span></a>
            </div>
        </div>
    </nav>
    
    <style>
    .ecom-nav-glass {{ position: fixed; top: 20px; left: 50%; transform: translateX(-50%); z-index: 1000; width: 90%; max-width: 1200px; }}
    .nav-container {{ background: {background}80; backdrop-filter: blur(20px); border: 1px solid {text}10; border-radius: 100px; padding: 16px 32px; display: flex; justify-content: space-between; align-items: center; }}
    .logo {{ font-size: 1.5rem; font-weight: 800; color: {text}; text-decoration: none; }}
    .nav-links {{ display: flex; gap: 32px; }}
    .nav-links a {{ color: {text}; text-decoration: none; font-weight: 500; transition: color 0.3s ease; }}
    .nav-links a:hover {{ color: {primary}; }}
    .nav-actions {{ display: flex; align-items: center; gap: 16px; }}
    .search-toggle {{ background: {text}08; border: none; width: 44px; height: 44px; border-radius: 50%; font-size: 1.1rem; cursor: pointer; }}
    .cart-btn {{ position: relative; background: {primary}; color: {background}; padding: 12px 24px; border-radius: 100px; text-decoration: none; font-weight: 600; display: flex; align-items: center; gap: 8px; }}
    .cart-count {{ background: {background}; color: {primary}; padding: 2px 8px; border-radius: 100px; font-size: 0.8rem; }}
    @media (max-width: 768px) {{ .nav-links {{ display: none; }} }}
    </style>
    '''
