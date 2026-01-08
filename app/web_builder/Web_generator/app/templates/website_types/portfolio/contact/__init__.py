from typing import Dict, Any
import random

from .variant_modern_split import render as render_modern_split


class PortfolioContactTemplates:
    """Portfolio contact section"""
    
    VARIANTS = ["modern-split"]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None:
            variant = random.choice(cls.VARIANTS)
        
        dispatch = {
            "modern-split": render_modern_split
        }
        
        render_func = dispatch.get(variant)
        if render_func:
            return render_func(props, colors)
        
        return render_modern_split(props, colors)
