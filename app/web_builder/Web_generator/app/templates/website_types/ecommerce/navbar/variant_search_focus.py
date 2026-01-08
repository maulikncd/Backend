from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Search Focus - Search bar centered"""
    brand = props.get("brand_name", "Shop")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <nav class="ecom-nav-search" id="navbar">
        <div class="nav-container">
            <a href="#" class="logo">{brand}</a>
            <div class="search-bar">
                <select class="cat-select"><option>All</option><option>Electronics</option><option>Fashion</option></select>
                <input type="text" placeholder="Search for products...">
                <button class="search-btn">Search</button>
            </div>
            <div class="nav-actions">
                <a href="#" class="action"><span class="icon">👤</span><span class="label">Account</span></a>
                <a href="#" class="action"><span class="icon">❤️</span><span class="label">Wishlist</span></a>
                <a href="#" class="action cart"><span class="icon">🛒</span><span class="label">Cart (3)</span></a>
            </div>
        </div>
    </nav>
    
    <style>
    .ecom-nav-search {{ position: fixed; top: 0; left: 0; right: 0; z-index: 1000; background: {background}; border-bottom: 1px solid {text}10; }}
    .nav-container {{ max-width: 1400px; margin: 0 auto; padding: 16px 24px; display: flex; align-items: center; gap: 40px; }}
    .logo {{ font-size: 1.8rem; font-weight: 900; color: {primary}; text-decoration: none; }}
    .search-bar {{ flex: 1; display: flex; background: {text}05; border-radius: 100px; overflow: hidden; border: 2px solid {primary}50; }}
    .cat-select {{ padding: 14px 20px; background: {text}08; border: none; color: {text}; font-weight: 500; cursor: pointer; }}
    .search-bar input {{ flex: 1; padding: 14px 20px; border: none; background: transparent; color: {text}; font-size: 1rem; }}
    .search-btn {{ padding: 14px 32px; background: {primary}; color: {background}; border: none; font-weight: 700; cursor: pointer; }}
    .nav-actions {{ display: flex; gap: 24px; }}
    .action {{ display: flex; flex-direction: column; align-items: center; text-decoration: none; color: {text}; }}
    .action .icon {{ font-size: 1.3rem; }}
    .action .label {{ font-size: 0.75rem; color: {secondary}; margin-top: 2px; }}
    .action.cart .label {{ color: {primary}; font-weight: 600; }}
    @media (max-width: 900px) {{ .cat-select, .action .label {{ display: none; }} .search-bar {{ flex: 1; }} }}
    </style>
    '''
