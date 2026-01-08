from typing import Dict, Any
import random

from .variant_grid import render as render_grid
from .variant_circle_scroll import render as render_circle_scroll
from .variant_parallax_cards import render as render_parallax_cards


class EcommerceCategoriesTemplates:
    """E-commerce categories section"""
    
    VARIANTS = ["grid", "circle-scroll", "parallax-cards"]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None:
            variant = random.choice(cls.VARIANTS)
        
        dispatch = {
            "grid": render_grid,
            "circle-scroll": render_circle_scroll,
            "parallax-cards": render_parallax_cards
        }
        
        render_func = dispatch.get(variant)
        if render_func:
            return render_func(props, colors)
        
        return render_grid(props, colors)
