from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Sidebar Toggle - Mobile-first sidebar"""
    brand = props.get("brand_name", "Shop")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <nav class="ecom-nav-sidebar" id="navbar">
        <div class="nav-container">
            <button class="menu-toggle">☰</button>
            <a href="#" class="logo">{brand}</a>
            <div class="nav-right">
                <a href="#" class="icon">🔍</a>
                <a href="#" class="cart-icon">🛒<span>3</span></a>
            </div>
        </div>
    </nav>
    
    <style>
    .ecom-nav-sidebar {{ position: fixed; top: 0; left: 0; right: 0; z-index: 1000; background: {background}; border-bottom: 1px solid {text}10; }}
    .nav-container {{ max-width: 1400px; margin: 0 auto; padding: 16px 24px; display: flex; justify-content: space-between; align-items: center; }}
    .menu-toggle {{ background: none; border: none; font-size: 1.5rem; cursor: pointer; color: {text}; }}
    .logo {{ font-size: 1.5rem; font-weight: 800; color: {text}; text-decoration: none; position: absolute; left: 50%; transform: translateX(-50%); }}
    .nav-right {{ display: flex; gap: 16px; }}
    .icon {{ color: {text}; text-decoration: none; font-size: 1.2rem; }}
    .cart-icon {{ position: relative; color: {text}; text-decoration: none; font-size: 1.3rem; }}
    .cart-icon span {{ position: absolute; top: -6px; right: -10px; background: {primary}; color: {background}; font-size: 0.65rem; font-weight: 700; padding: 2px 6px; border-radius: 100px; }}
    </style>
    '''
