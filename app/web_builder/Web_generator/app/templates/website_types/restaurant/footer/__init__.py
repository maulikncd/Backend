from typing import Dict, Any
import random

from .variant_elegant import render as render_elegant


class RestaurantFooterTemplates:
    """Restaurant footer section"""
    
    VARIANTS = ["elegant"]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None:
            variant = random.choice(cls.VARIANTS)
        
        dispatch = {
            "elegant": render_elegant
        }
        
        render_func = dispatch.get(variant)
        if render_func:
            return render_func(props, colors)
        
        return render_elegant(props, colors)
