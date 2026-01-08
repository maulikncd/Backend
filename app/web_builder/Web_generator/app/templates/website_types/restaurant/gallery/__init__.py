from typing import Dict, Any
import random

from .variant_food_grid import render as render_food_grid
from .variant_masonry import render as render_masonry
from .variant_carousel import render as render_carousel
from .variant_lightbox_grid import render as render_lightbox_grid
from .variant_fullscreen import render as render_fullscreen


class RestaurantGalleryTemplates:
    """Restaurant gallery section - 5+ variants"""
    
    VARIANTS = [
        "food-grid",
        "masonry",
        "carousel",
        "lightbox-grid",
        "fullscreen"
    ]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None:
            variant = random.choice(cls.VARIANTS)
        
        dispatch = {
            "food-grid": render_food_grid,
            "masonry": render_masonry,
            "carousel": render_carousel,
            "lightbox-grid": render_lightbox_grid,
            "fullscreen": render_fullscreen
        }
        
        render_func = dispatch.get(variant)
        if render_func:
            return render_func(props, colors)
        
        return render_food_grid(props, colors)
