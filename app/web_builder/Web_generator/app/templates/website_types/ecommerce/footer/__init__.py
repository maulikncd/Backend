from typing import Dict, Any
import random

from .variant_full import render as render_full


class EcommerceFooterTemplates:
    """E-commerce footer section"""
    
    VARIANTS = ["full"]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None:
            variant = random.choice(cls.VARIANTS)
        
        dispatch = {
            "full": render_full
        }
        
        render_func = dispatch.get(variant)
        if render_func:
            return render_func(props, colors)
        
        return render_full(props, colors)
