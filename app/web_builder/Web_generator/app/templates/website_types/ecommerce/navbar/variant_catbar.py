from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Categories Bar - With category strip"""
    brand = props.get("brand_name", "Shop")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <nav class="ecom-nav-catbar" id="navbar">
        <div class="main-bar">
            <a href="#" class="logo">{brand}</a>
            <div class="search-box">
                <input type="text" placeholder="Search products...">
                <button>🔍</button>
            </div>
            <div class="nav-actions">
                <a href="#">👤 Account</a>
                <a href="#" class="cart">🛒 Cart (3)</a>
            </div>
        </div>
        <div class="cat-bar">
            <a href="#">Electronics</a>
            <a href="#">Fashion</a>
            <a href="#">Home & Garden</a>
            <a href="#">Sports</a>
            <a href="#">Beauty</a>
            <a href="#" class="deals">🔥 Deals</a>
        </div>
    </nav>
    
    <style>
    .ecom-nav-catbar {{ position: fixed; top: 0; left: 0; right: 0; z-index: 1000; background: {background}; }}
    .main-bar {{ max-width: 1400px; margin: 0 auto; padding: 16px 24px; display: flex; align-items: center; gap: 40px; }}
    .logo {{ font-size: 1.8rem; font-weight: 900; color: {primary}; text-decoration: none; }}
    .search-box {{ flex: 1; display: flex; max-width: 500px; }}
    .search-box input {{ flex: 1; padding: 12px 20px; border: 2px solid {text}15; border-right: none; border-radius: 8px 0 0 8px; color: {text}; }}
    .search-box button {{ padding: 12px 20px; background: {primary}; border: none; border-radius: 0 8px 8px 0; cursor: pointer; }}
    .nav-actions {{ display: flex; gap: 24px; }}
    .nav-actions a {{ color: {text}; text-decoration: none; font-weight: 500; }}
    .cart {{ color: {primary} !important; }}
    .cat-bar {{ background: {text}05; border-top: 1px solid {text}10; padding: 12px 24px; display: flex; justify-content: center; gap: 40px; }}
    .cat-bar a {{ color: {secondary}; text-decoration: none; font-weight: 500; font-size: 0.9rem; transition: color 0.3s ease; }}
    .cat-bar a:hover {{ color: {primary}; }}
    .deals {{ color: {primary} !important; }}
    @media (max-width: 900px) {{ .search-box {{ display: none; }} .cat-bar {{ overflow-x: auto; justify-content: flex-start; gap: 24px; }} }}
    </style>
    '''
