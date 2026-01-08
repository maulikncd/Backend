from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Two Row - Double row navbar"""
    brand = props.get("brand_name", "Shop")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <nav class="ecom-nav-tworow" id="navbar">
        <div class="top-bar">
            <span>Free shipping on orders over $50! 🚚</span>
            <div class="top-links"><a href="#">Help</a><a href="#">Track Order</a><a href="#">Sign In</a></div>
        </div>
        <div class="main-nav">
            <a href="#" class="logo">{brand}</a>
            <div class="nav-links">
                <a href="#products">New Arrivals</a>
                <a href="#categories">Categories</a>
                <a href="#deals">Sale</a>
                <a href="#about">About</a>
            </div>
            <div class="nav-actions">
                <a href="#">🔍</a>
                <a href="#">❤️</a>
                <a href="#" class="cart">🛒 <span>3</span></a>
            </div>
        </div>
    </nav>
    
    <style>
    .ecom-nav-tworow {{ position: fixed; top: 0; left: 0; right: 0; z-index: 1000; }}
    .top-bar {{ background: {primary}; color: {background}; padding: 10px 24px; display: flex; justify-content: space-between; align-items: center; font-size: 0.85rem; }}
    .top-links {{ display: flex; gap: 20px; }}
    .top-links a {{ color: {background}; text-decoration: none; opacity: 0.9; }}
    .main-nav {{ background: {background}; padding: 16px 24px; display: flex; justify-content: space-between; align-items: center; max-width: 1400px; margin: 0 auto; }}
    .logo {{ font-size: 1.8rem; font-weight: 900; color: {text}; text-decoration: none; }}
    .nav-links {{ display: flex; gap: 32px; }}
    .nav-links a {{ color: {text}; text-decoration: none; font-weight: 500; }}
    .nav-links a:hover {{ color: {primary}; }}
    .nav-actions {{ display: flex; gap: 20px; }}
    .nav-actions a {{ color: {text}; text-decoration: none; font-size: 1.3rem; }}
    .cart {{ position: relative; }}
    .cart span {{ position: absolute; top: -6px; right: -10px; background: {primary}; color: {background}; font-size: 0.65rem; font-weight: 700; padding: 2px 6px; border-radius: 100px; }}
    @media (max-width: 768px) {{ .nav-links, .top-links {{ display: none; }} }}
    </style>
    '''
