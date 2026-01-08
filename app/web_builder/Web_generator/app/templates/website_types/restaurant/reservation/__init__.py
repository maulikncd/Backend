from typing import Dict, Any
import random

from .variant_form import render as render_form
from .variant_split_image import render as render_split_image
from .variant_centered_card import render as render_centered_card
from .variant_dark_elegant import render as render_dark_elegant


class RestaurantReservationTemplates:
    """Restaurant reservation section - 4 variants"""
    
    VARIANTS = [
        "form",
        "split-image",
        "centered-card",
        "dark-elegant"
    ]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None:
            variant = random.choice(cls.VARIANTS)
        
        dispatch = {
            "form": render_form,
            "split-image": render_split_image,
            "centered-card": render_centered_card,
            "dark-elegant": render_dark_elegant
        }
        
        render_func = dispatch.get(variant)
        if render_func:
            return render_func(props, colors)
        
        return render_form(props, colors)
