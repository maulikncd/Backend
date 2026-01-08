from typing import Dict, Any
import random

from .variant_form import render as render_form


class RestaurantReservationTemplates:
    """Restaurant reservation section"""
    
    VARIANTS = ["form"]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None:
            variant = random.choice(cls.VARIANTS)
        
        dispatch = {
            "form": render_form
        }
        
        render_func = dispatch.get(variant)
        if render_func:
            return render_func(props, colors)
        
        return render_form(props, colors)
