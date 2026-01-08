from typing import Dict, Any
import random

from .variant_food_grid import render as render_food_grid


class RestaurantGalleryTemplates:
    """Restaurant-specific gallery sections"""
    
    VARIANTS = ["food-grid"]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None:
            variant = random.choice(cls.VARIANTS)
        
        dispatch = {
            "food-grid": render_food_grid
        }
        
        render_func = dispatch.get(variant)
        if render_func:
            return render_func(props, colors)
        
        return render_food_grid(props, colors)
