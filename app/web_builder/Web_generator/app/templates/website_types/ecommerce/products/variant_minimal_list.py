from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """
    Minimal Interactive List - A sophisticated list view where hovering over a name
    reveals the product image in a fixed position. Very high-end editorial feel.
    """
    products = props.get("products", [])
    if not products:
        products = [
            {"name": "Midnight Velvet Sofa", "price": "$1200", "image": "https://images.unsplash.com/photo-1555041469-a586c61ea9bc?w=600"},
            {"name": "Marble Coffee Table", "price": "$850", "image": "https://images.unsplash.com/photo-1533090481720-856c6e3c1fdc?w=600"},
            {"name": "Industrial Floor Lamp", "price": "$320", "image": "https://images.unsplash.com/photo-1507473888900-52e1ad1459ee?w=600"},
            {"name": "Abstract Wall Art", "price": "$410", "image": "https://images.unsplash.com/photo-1582562124811-ba36d418e0a1?w=600"},
        ]

    bg = colors.get("background", "#FFFFFF")
    text = colors.get("text", "#000000")
    
    list_items = ""
    # Inject images hiddenly or use JS to swap source. 
    # For pure HTML/CSS hover, we can structure it carefully.
    
    script = f"""
    <script>
    function showPreview(url) {{
        const preview = document.getElementById('product-preview-img');
        preview.src = url;
        preview.style.opacity = 1;
        preview.style.transform = 'scale(1)';
    }}
    function hidePreview() {{
        // Optional: clear or hide
        // const preview = document.getElementById('product-preview-img');
        // preview.style.opacity = 0;
    }}
    </script>
    """
    
    for prod in products:
        img_url = prod.get("image")
        list_items += f'''
        <div class="product-row" onmouseenter="showPreview('{img_url}')">
            <div class="row-left">
                <span class="row-index">0{products.index(prod) + 1}</span>
                <h3 class="row-title">{prod.get("name")}</h3>
            </div>
            <div class="row-right">
                <span class="row-price">{prod.get("price")}</span>
                <span class="row-arrow">→</span>
            </div>
        </div>
        '''
        
    # Initial image
    initial_img = products[0].get("image") if products else ""

    return f'''
    <section class="minimal-list" id="products">
        <div class="container-split">
            <div class="list-side">
                <div class="list-header">
                    <h2>Selected Works</h2>
                    <p>Design Collection 2026</p>
                </div>
                <div class="product-list">
                    {list_items}
                </div>
            </div>
            <div class="preview-side">
                <div class="preview-frame">
                    <img id="product-preview-img" src="{initial_img}" alt="Preview">
                </div>
            </div>
        </div>
        {script}
    </section>
    
    <style>
    .minimal-list {{
        padding: 0;
        background: {bg};
        color: {text};
        min-height: 100vh;
        display: flex;
        align-items: center;
    }}
    
    .container-split {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        width: 100%;
        max-width: 1600px;
        margin: 0 auto;
        padding: 40px;
        gap: 60px;
    }}
    
    .list-header {{
        margin-bottom: 60px;
        border-bottom: 2px solid {text};
        padding-bottom: 20px;
    }}
    
    .list-header h2 {{
        font-family: 'Helvetica Neue', sans-serif;
        font-size: 3rem;
        font-weight: 700;
        margin: 0 0 10px;
        text-transform: uppercase;
    }}
    
    .product-row {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 30px 0;
        border-bottom: 1px solid rgba(0,0,0,0.1);
        cursor: pointer;
        transition: padding 0.3s;
    }}
    
    .product-row:hover {{
        padding-left: 20px;
        border-bottom-color: {text};
    }}
    
    .row-left {{
        display: flex;
        align-items: baseline;
        gap: 30px;
    }}
    
    .row-index {{
        font-family: 'Courier New', monospace;
        font-size: 0.9rem;
        color: #999;
    }}
    
    .row-title {{
        font-size: 1.8rem;
        font-weight: 400;
        margin: 0;
    }}
    
    .row-right {{
        display: flex;
        align-items: center;
        gap: 20px;
        font-family: 'Courier New', monospace;
    }}
    
    .row-arrow {{
        opacity: 0;
        transform: translateX(-10px);
        transition: all 0.3s;
    }}
    
    .product-row:hover .row-arrow {{
        opacity: 1;
        transform: translateX(0);
    }}
    
    .preview-side {{
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
    }}
    
    .preview-frame {{
        width: 100%;
        height: 600px;
        position: sticky;
        top: 100px;
    }}
    
    .preview-frame img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        opacity: 1;
        transition: opacity 0.5s ease;
        border-radius: 4px;
        filter: brightness(0.9);
    }}
    
    @media (max-width: 900px) {{
        .container-split {{ grid-template-columns: 1fr; }}
        .preview-side {{ display: none; }}
    }}
    </style>
    '''
