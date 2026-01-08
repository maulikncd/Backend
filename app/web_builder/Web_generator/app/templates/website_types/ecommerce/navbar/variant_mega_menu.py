from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Mega Menu - Large dropdown menu"""
    brand = props.get("brand_name", "Shop")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <nav class="ecom-nav-mega" id="navbar">
        <div class="nav-container">
            <a href="#" class="logo">{brand}</a>
            <div class="nav-links">
                <div class="nav-item has-mega">
                    <a href="#">Categories ▾</a>
                    <div class="mega-menu">
                        <div class="mega-col"><h4>Electronics</h4><a href="#">Phones</a><a href="#">Laptops</a><a href="#">Tablets</a></div>
                        <div class="mega-col"><h4>Fashion</h4><a href="#">Men</a><a href="#">Women</a><a href="#">Kids</a></div>
                        <div class="mega-col"><h4>Home</h4><a href="#">Furniture</a><a href="#">Decor</a><a href="#">Kitchen</a></div>
                        <div class="mega-promo"><span>50% OFF</span><p>Flash Sale</p></div>
                    </div>
                </div>
                <a href="#products">New Arrivals</a>
                <a href="#deals">Deals</a>
                <a href="#about">About</a>
            </div>
            <div class="nav-actions">
                <input type="text" placeholder="Search products..." class="search-input">
                <a href="#" class="cart-btn">🛒 <span>3</span></a>
            </div>
        </div>
    </nav>
    
    <style>
    .ecom-nav-mega {{ position: fixed; top: 0; left: 0; right: 0; z-index: 1000; background: {background}; border-bottom: 1px solid {text}10; }}
    .nav-container {{ max-width: 1400px; margin: 0 auto; padding: 16px 24px; display: flex; align-items: center; gap: 40px; }}
    .logo {{ font-size: 1.5rem; font-weight: 800; color: {text}; text-decoration: none; }}
    .nav-links {{ display: flex; gap: 28px; flex: 1; }}
    .nav-item {{ position: relative; }}
    .nav-links a {{ color: {text}; text-decoration: none; font-weight: 500; }}
    .mega-menu {{ position: absolute; top: 100%; left: -100px; width: 600px; background: {background}; border-radius: 16px; box-shadow: 0 20px 50px rgba(0,0,0,0.15); padding: 32px; display: none; grid-template-columns: repeat(4, 1fr); gap: 24px; }}
    .nav-item:hover .mega-menu {{ display: grid; }}
    .mega-col h4 {{ font-size: 0.9rem; font-weight: 700; color: {primary}; margin-bottom: 12px; }}
    .mega-col a {{ display: block; color: {secondary}; padding: 6px 0; font-size: 0.9rem; }}
    .mega-col a:hover {{ color: {primary}; }}
    .mega-promo {{ background: {primary}; border-radius: 12px; padding: 20px; text-align: center; color: {background}; }}
    .mega-promo span {{ font-size: 1.5rem; font-weight: 900; display: block; }}
    .search-input {{ padding: 12px 20px; background: {text}05; border: 1px solid {text}10; border-radius: 100px; width: 250px; color: {text}; }}
    .cart-btn {{ position: relative; color: {text}; text-decoration: none; font-size: 1.3rem; }}
    .cart-btn span {{ position: absolute; top: -8px; right: -12px; background: {primary}; color: {background}; font-size: 0.7rem; font-weight: 700; padding: 2px 6px; border-radius: 100px; }}
    @media (max-width: 900px) {{ .nav-links, .search-input {{ display: none; }} }}
    </style>
    '''
