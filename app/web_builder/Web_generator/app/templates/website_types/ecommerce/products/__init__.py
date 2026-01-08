from typing import Dict, Any
import random

from .variant_grid import render as render_grid
from .variant_aura_products import render as render_aura_products
from .variant_carousel_3d import render as render_carousel_3d
from .variant_masonry_wall import render as render_masonry_wall
from .variant_minimal_list import render as render_minimal_list


class EcommerceProductsTemplates:
    """E-commerce products section"""
    
    VARIANTS = [
        "grid", 
        "aura-products", 
        "carousel-3d", 
        "masonry-wall", 
        "minimal-list"
    ]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None:
            variant = random.choice(cls.VARIANTS)
        
        dispatch = {
            "grid": render_grid,
            "aura-products": render_aura_products,
            "carousel-3d": render_carousel_3d,
            "masonry-wall": render_masonry_wall,
            "minimal-list": render_minimal_list
        }
        
        render_func = dispatch.get(variant)
        if render_func:
            return render_func(props, colors)
        
        return render_grid(props, colors)
