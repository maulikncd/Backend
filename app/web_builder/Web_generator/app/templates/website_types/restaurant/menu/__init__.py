from typing import Dict, Any
import random

from .variant_elegant_cards import render as render_elegant_cards


class RestaurantMenuTemplates:
    """Restaurant menu section"""
    
    VARIANTS = ["elegant-cards"]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None:
            variant = random.choice(cls.VARIANTS)
        
        dispatch = {
            "elegant-cards": render_elegant_cards
        }
        
        render_func = dispatch.get(variant)
        if render_func:
            return render_func(props, colors)
        
        return render_elegant_cards(props, colors)
