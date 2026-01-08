from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """
    Circular Scroll Categories - Instagram-story style layout for categories.
    Very modern and mobile-friendly.
    """
    categories = props.get("categories", ["New In", "Best Sellers", "Clothing", "Shoes", "Accessories", "Sale"])
    
    # Generate placeholder images if needed
    cat_data = []
    base_images = [
        "https://images.unsplash.com/photo-1548036328-c9fa89d128fa?w=200",
        "https://images.unsplash.com/photo-1491553895911-0055eca6402d?w=200",
        "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=200",
        "https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?w=200",
        "https://images.unsplash.com/photo-1523381210434-271e8be1f52b?w=200",
        "https://images.unsplash.com/photo-1515488042361-ee00e0ddd4e4?w=200"
    ]
    
    for idx, name in enumerate(categories):
        img = base_images[idx % len(base_images)]
        cat_data.append({"name": name, "image": img})
        
    bg = colors.get("background", "#FFFFFF")
    text = colors.get("text", "#000000")
    primary = colors.get("primary", "#000000")
    
    cat_html = ""
    for cat in cat_data:
        cat_html += f'''
        <div class="circle-cat">
            <div class="circle-ring">
                <img src="{cat.get("image")}" alt="{cat.get("name")}">
            </div>
            <span class="cat-name">{cat.get("name")}</span>
        </div>
        '''

    return f'''
    <section class="circle-categories" id="categories">
        <div class="container">
            <div class="circle-scroll">
                {cat_html}
            </div>
        </div>
    </section>
    
    <style>
    .circle-categories {{
        padding: 40px 0;
        background: {bg};
        border-bottom: 1px solid rgba(0,0,0,0.05);
    }}
    
    .container {{
        max-width: 1400px;
        margin: 0 auto;
        padding: 0 20px;
        overflow-x: auto;
        -webkit-overflow-scrolling: touch;
        scrollbar-width: none; /* Firefox */
    }}
    
    .container::-webkit-scrollbar {{
        display: none; 
    }}
    
    .circle-scroll {{
        display: flex;
        gap: 25px;
        justify-content: flex-start;
        min-width: max-content;
        padding: 10px;
    }}
    
    .circle-cat {{
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 10px;
        cursor: pointer;
        transition: transform 0.2s;
    }}
    
    .circle-cat:hover {{
        transform: translateY(-5px);
    }}
    
    .circle-ring {{
        width: 85px;
        height: 85px;
        border-radius: 50%;
        padding: 3px;
        border: 2px solid transparent;
        background: linear-gradient({bg}, {bg}), 
                    linear-gradient(45deg, #f09433 0%,#e6683c 25%,#dc2743 50%,#cc2366 75%,#bc1888 100%);
        background-clip: content-box, border-box;
        background-origin: border-box;
        /* Simulate Instagram ring logic somewhat or just use primary color */
        border: 2px solid {primary};
        display: flex;
        align-items: center;
        justify-content: center;
    }}

    .circle-ring img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        border-radius: 50%;
        border: 2px solid {bg};
    }}
    
    .cat-name {{
        font-family: 'Helvetica Neue', sans-serif;
        font-size: 0.85rem;
        font-weight: 500;
        color: {text};
        white-space: nowrap;
    }}
    </style>
    '''
